#! /bin/bash

if [[ "$#" -ne 1 ]]; then
    echo Deploy the passed commit to prod.
    echo
    echo "Usage: $0 <commit>"
    exit 2
fi

project_dir=$(dirname "$0")
short_hash=$(git rev-parse --short "$1")

"./$project_dir/build.sh" "$short_hash"

# TODO I should probably make this a standard path. /var/www/sites?
site_root=/usr/local/nginx/sites/www.nateeag.com

# Make sure the base directories exist.
commands="\
mkdir -p \"$site_root/builds\" \
mkdir -p \"$site_root/releases\" \
"

# SSH commands rely on setup in my personal SSH config.
ssh -t www.nateeag.com "$commands"

# Could use sticky bit to set group server-side? For moment, relies on later
# sudo command to get perms right...
# TODO Use a faster deployment mechanism.
# A straightforward hack could be to recursively copy the previous deployment's
# directory to the new one's path, so rsync only needs to synchronize the
# changes since the last deployment.
rsync -azv "$project_dir/build/$short_hash/" \
      www.nateeag.com:"$site_root/builds/$short_hash"

# Do the atomic symlink rename dance. The key is making the temporary link then
# moving it, per this blog post:
#
# http://blog.moertel.com/posts/2005-08-22-how-to-change-symlinks-atomically.html
#
# GRIPE I don't like using sudo here, but I don't want my webserver to have
# write access to a static site's docroot. Is there a better way?
#
# TODO For a site that mattered, deployment would be two-phase:
#
#   * Bring up a test instance of the site on some IP-limited domain name
#   * Once smoke tests are run against the test instance, a human pulls the
#     trigger  on moving the prod symlink.
commands="\
sudo chown -R www-data:deployers \"$site_root/builds/$short_hash\"
ln -s \"$site_root/builds/$short_hash/\" \"$site_root/releases/prod-tmp\" &&\
    mv -Tf \"$site_root/releases/prod-tmp\" \"$site_root/releases/prod\"
"
ssh -t www.nateeag.com "$commands"

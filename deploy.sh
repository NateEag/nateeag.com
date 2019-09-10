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

# TODO Use Heredoc for embedded scripts?
# The nest of escaping is hard to cope with in the current form.
#
# Something like https://stackoverflow.com/a/7363641/1128957 is probably the
# best answer. I mean, yeah, Ansible, but this is much simpler for my use case
# (completely static sites).

# Make sure the base directories exist, and copy the previous build into the
# new build's planned location. This makes deployments a whole lot faster,
# since for most deployments, relatively little changes, so rsync doesn't have
# much work to do.
#
# It is, of course, possible to speed things up in much the same way by keeping
# the git repository on the server, pushing to it, and performing builds
# server-side.
#
# However, that means installing more dependencies on the server.
#
# When you want to avoid that, something like this approach is useful.
#
# FIXME Automate provisioning. For the current setup to work, siteroot owner
# needs to be the SSH user, the site group owner needs to be www-data, and it
# needs to have the setgid bit set.
#
# FIXME We should skip the recursive copy when the builds/ folder is empty.
commands="\
mkdir -p \"$site_root/builds\" && \
last_build_dir=\$(ls -1tc \"$site_root/builds\" | head -1) &&
mkdir -p \"$site_root/releases\" &&
cp -rp \"$site_root/builds/\$last_build_dir\" \"$site_root/builds/$short_hash\"
"

# SSH commands rely on setup in my personal SSH config.
ssh -t www.nateeag.com "$commands"

# Could use sticky bit to set group server-side? For moment, relies on later
# sudo command to get perms right...
#
# Because we copy the previous release to save time, we delete extraneous
# files, so no outdated files are hanging around in the docroot after the
# sync.
rsync -rltzv --delete \
      --chmod=ugo=rwX \
      "$project_dir/build/$short_hash/" \
      www.nateeag.com:"$site_root/builds/$short_hash"

# Do the atomic symlink rename dance. The key is making the temporary link then
# moving it, per this blog post:
#
# http://blog.moertel.com/posts/2005-08-22-how-to-change-symlinks-atomically.html
#
# TODO For a site that mattered, deployment would be two-phase:
#
#   * Bring up a test instance of the site on some IP-limited domain name
#   * Once smoke tests are run against the test instance, a human pulls the
#     trigger on moving the prod symlink.
#
# The chmods make sure the web user can actually read the files and that not
# every user can, as the default umask doesn't give the group access to them.
#
# TODO Figure out how to get rsync to just set permissions as if I were working
# interactively on the remote server.
commands="\
chmod -R o-rwx \"$site_root/builds/$short_hash\" &&
chmod -R g+rxs \"$site_root/builds/$short_hash\" &&
ln -s \"$site_root/builds/$short_hash/\" \"$site_root/releases/prod-tmp\" && \
    mv -Tf \"$site_root/releases/prod-tmp\" \"$site_root/releases/prod\"
"
ssh -t www.nateeag.com "$commands"

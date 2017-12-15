#! /bin/bash

# Make a build in a sub-folder of the targeted git revision.
#
# Since this is a completely static site, making a build is pretty easy.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <commit>"

    exit 2
fi

project_dir=$(dirname "$0")

cur_branch=$(git rev-parse --abbrev-ref HEAD)

if ! git diff --exit-code --quiet; then
    stash_saved=yes
    git stash save
fi

short_hash=$(git rev-parse --short "$1")

echo $short_hash

mkdir -p "$project_dir/build/$short_hash"

git checkout "$short_hash"

source "$project_dir/virtualenv/bin/activate"
python generator.py "$project_dir/build/$short_hash"

git checkout "$cur_branch"

if [ -n "$stash_saved" ]; then
    git stash pop
fi

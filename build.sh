#! /bin/bash

# Make a build in a sub-folder of the targeted git revision.
#
# Since this is a completely static site, making a build is pretty easy.

project_dir=$(dirname "$0")

cur_branch=$(git rev-parse --abbrev-ref HEAD)
git stash save

short_hash=$(git rev-parse --short "$1")

mkdir -p "$project_dir/build/$short_hash"

git checkout "$short_hash"

cp -r "$project_dir/src/" "$project_dir/build/$short_hash"

git checkout "$cur_branch"
git stash pop

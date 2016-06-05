#! /bin/sh

# A minimal wrapper script to render the project into the src/ directory, for
# use while developing.

project_dir=$(dirname "$0")

source "$project_dir/virtualenv/bin/activate"

python "$project_dir/generator.py" "$project_dir/src"

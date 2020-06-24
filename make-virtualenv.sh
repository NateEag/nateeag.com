#! /bin/bash

# Create the virtualenv for building this site.
project_dir=$(dirname $0);
python -m venv "$project_dir/virtualenv"

source "$project_dir/virtualenv/bin/activate"

pip install -r requirements.txt

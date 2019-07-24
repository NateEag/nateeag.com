#! /bin/sh

# Watch the content folder and re-render the site when it changes.

# Depends on the fswatch program. Mostly exists so I don't have to remember
# fswatch syntax.

project_path=$(dirname "$0")

. "$project_path/virtualenv/bin/activate"

# The xargs invocation is a bit labored in order to output the timestamp of
# each re-rendering, and xargs doesn't have long option names, so some
# explanation is due.
#
# We execute a new bash instance for each line of input, then run the specified
# command in it.
#
# The first part of the command is double-quoted to interpolate the path to the
# script safely in the face of whitespace, while the second half is defined as
# a variable, so that it will not be interpolated by the current shell, which
# would result in the same timestamp for all items.
#
# Instead, it is interpolated by the new bash instance that is spawned by the
# new line of output from fswatch, and therefore gets a
# roughly-accurate timestamp.

OUTPUT_DATE_CMD='echo $(date "+%Y-%m-%d %H:%M:%S"): Rendered site'

fswatch --one-per-batch \
        "$project_path/pages" \
        "$project_path/templates" \
        "generator.py" |
    xargs -L 1 bash -c "$project_path/generate.sh && $OUTPUT_DATE_CMD"

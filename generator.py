"""Generate static versions of the site's pages using Jinja2."""

# Standard library imports.
import os
import sys

# Third party imports.
import yaml

from jinja2 import Environment, FileSystemLoader



def load_page(page_path):
    pass


def render_page(path, source_dir, target_dir, jinja_env):
    """Render the page at `path` into `target_dir`."""

    f = open(path, 'r')
    page = yaml.load(f)
    f.close()

    template = jinja_env.get_template(page['template'])
    contents = template.render(**page)

    target_path = os.path.join(target_dir, path[len(source_dir) + 1:])
    target_path = os.path.splitext(target_path)[0]
    target_subdir = os.path.dirname(target_path)

    if not os.path.exists(target_subdir):
        os.makedirs(target_subdir)

    f = open(target_path, 'w')
    f.write(contents)
    f.close()

def get_page_paths(dir):
    """Return a list of page definition paths."""

    paths = []
    for dir_listing in os.walk(dir):
        if len(dir_listing[2]):
            for path in dir_listing[2]:
                path = os.path.join(dir_listing[0], path)
                paths.append(path)

    return paths


def main():

    project_path = os.path.dirname(os.path.realpath(__file__))

    templates_path = os.path.join(project_path, 'templates')
    env = Environment(loader=FileSystemLoader(templates_path))

    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s <output_dir>" % sys.argv[0]

        exit(2)

    pages_path = os.path.join(project_path, 'pages')
    for page_path in get_page_paths(pages_path):
        render_page(page_path, pages_path, sys.argv[1], env)


    # for page in pages:

if __name__ == '__main__':
    main()

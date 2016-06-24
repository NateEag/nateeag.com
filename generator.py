"""Generate static versions of the site's pages using Jinja2."""

# Standard library imports.
import os
import sys

# Third party imports.
import yaml
import markdown
import sass

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Markup


def markdown_filter(text):
    """Simple Markdown filter for Jinja2."""

    # Since Markdown only comes from my git repo, I don't have to worry
    # about XSS.
    return Markup(markdown.markdown(text))


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

                if path.endswith('.yaml'):
                    paths.append(path)

    return paths


def compile_stylesheets(src_dir, target_dir):
    """Generate CSS from SCSS stylesheets."""

    sass.compile(dirname=(src_dir, target_dir))


def main():
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s <output_dir>" % sys.argv[0]

        exit(2)

    project_path = os.path.dirname(os.path.realpath(__file__))

    templates_path = os.path.join(project_path, 'templates')
    env = Environment(loader=FileSystemLoader(templates_path))
    env.filters['markdown'] = markdown_filter

    pages_path = os.path.join(project_path, 'pages')
    for page_path in get_page_paths(pages_path):
        render_page(page_path, pages_path, sys.argv[1], env)

    stylesheet_dir = os.path.join(project_path, 'stylesheets')
    css_dir = os.path.join(project_path, sys.argv[1], 'static')
    compile_stylesheets(stylesheet_dir, css_dir)


if __name__ == '__main__':
    main()

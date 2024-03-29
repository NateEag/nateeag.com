"""Generate static versions of the site's pages using Jinja2."""

# Standard library imports.
import errno
import os
import re
import shutil
import sys
from io import StringIO

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


def render_page(path, source_dir, target_dir, project_path, jinja_env):
    """Render the page at `path` into `target_dir`."""

    f = open(path, 'r')

    yaml_header = ''
    body = ''
    num_matches = 0

    for line in f.readlines():
        if line == '---\n':
           num_matches += 1

           continue

        if num_matches < 2:
            yaml_header += line
        else:
            body += line

    f.close()

    if body == '':
        print(yaml_header)
        raise Exception(path + ' has no body!')

    page = yaml.load(StringIO(yaml_header))
    page['body'] = body

    docroot_relative_path = path[len(source_dir):]
    path_components = docroot_relative_path.split(os.path.sep)[1:]
    folders = path_components[:-1]
    article = path_components[-1]

    if 'spaced-repetition' in page:
        # Render this document as a simplified document for importing to a
        # spaced repetition review deck.
        flashcards_file_name = article.replace('.md', '-flashcards.md')

        flashcards_path = os.path.sep.join([project_path,
                                            'flashcard_exports',
                                            docroot_relative_path])

        flashcards_dir = os.path.dirname(flashcards_path)

        # Don't explode if a target directory already exists. mkdir -p,
        # essentially.
        #
        # TODO Use pathlib.Path.mkdir once I upgrade to Python 3.
        try:
            os.makedirs(flashcards_dir)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(flashcards_dir):
                pass
            else:
                raise

        # FIXME Preserve '---' lines in this export. Without them Ankidown
        # can't import my documents, which makes this pointless so far.
        f = open(flashcards_path, 'w')
        f.write(body)
        f.close()

    # Drafts should not be rendered.
    if 'draft' in page:
        return

    # Pages must have a title so we can show it in the link hierarchy.
    if page['title'] is None or page['title'] == '':
        raise Exception(path + ' has no title!')

    href = '/'
    breadcrumbs = [{
        'name': 'nateeag.com',
        'href': href
    }]

    for folder in folders:
        href += folder + '/'
        breadcrumbs.append({
            'name': folder.replace('-', ' '),
            'href': href
        })

    # Set the breadcrumb for the page to the document's title and link.

    breadcrumbs.append({
        'name': page['title'],
        # TODO Decide whether a relative link is the best way to do this. This
        # happens to work but it's certainly not the most obvious way to write
        # HTML.
        'href': article.replace('.md', '.html')
    })

    if path.endswith('/index.md'):
        # The document is redundant with the folder in this case, so throw it
        # out.
        del breadcrumbs[-1]

    page['breadcrumbs'] = breadcrumbs

    template = jinja_env.get_template(page['template'])
    contents = template.render(**page)

    target_path = os.path.join(target_dir, path[len(source_dir) + 1:])
    target_path = os.path.splitext(target_path)[0] + '.html'
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

                if path.endswith('.md'):
                    paths.append(path)

    return paths


def copy_assets(src_dir, target_dir):
    """Copy static assets from `src_dir` to `target_dir`.

    Exists largely so I can keep static assets in the same directories
    as the pages they belong to.

    """

    shutil.copytree(src_dir,
                    target_dir,
                    False,
                    shutil.ignore_patterns('*.md'))


def compile_stylesheets(src_dir, target_dir):
    """Generate CSS from SCSS stylesheets."""

    sass.compile(dirname=(src_dir, target_dir))


def main():
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s <output_dir>" % sys.argv[0]

        exit(2)


    # Blow away output directory, first thing.
    #
    # This is a bit dangerous in some ways, but otherwise you will have old
    # stuff lying around, and usually builds want clean envs.
    #
    # Also, we use shutil.copytree as the innards for copy_assets, and that
    # will fail if the directory exists.
    #
    # Rather than re-implement our own version of it that supports pre-existing
    # directories, we just copy assets first, thereby working around the issue.

    project_path = os.path.dirname(os.path.realpath(__file__))
    output_path = sys.argv[1]
    pages_path = os.path.join(project_path, 'pages')

    shutil.rmtree(output_path)

    copy_assets(pages_path, output_path)

    templates_path = os.path.join(project_path, 'templates')
    env = Environment(loader=FileSystemLoader(templates_path))
    env.filters['markdown'] = markdown_filter

    for page_path in get_page_paths(pages_path):
        render_page(page_path, pages_path, output_path, project_path, env)

    stylesheet_dir = os.path.join(project_path, 'stylesheets')
    css_dir = os.path.join(project_path, output_path)
    compile_stylesheets(stylesheet_dir, css_dir)


if __name__ == '__main__':
    main()

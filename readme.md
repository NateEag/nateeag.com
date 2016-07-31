nateeag.com
===========

This is the source code and content for www.nateeag.com.

It's statically generated using a few Python modules and a small amount of
wrapper code.

Usage
=====

To create a local sandbox, do the following:

    $ ./install-virtualenv.sh
    $ ./generate.sh

To view the generated code, just view it through a browser. An easy way:

    $ cd src
    $ python -m SimpleHTTPServer

then open a browser and hit localhost:8000.

`watch.sh` uses the [fswatch](https://github.com/emcrisostomo/fswatch) command
to re-render the site when something in the `pages/` directory changes.

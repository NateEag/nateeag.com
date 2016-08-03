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
    $ http-server -p 8000 src

assuming you have installed the
[Node http-server module](https://github.com/indexzero/http-server) globally.

then open a browser and hit localhost:8000.

`watch.sh` uses the [fswatch](https://github.com/emcrisostomo/fswatch) command
to re-render the site when something in the `pages/` directory changes.

Note that I used to use `cd src && python -m SimpleHTTPServer` to run my local
development server, but once I made the generation process erase src/ as the
first step, that ceased to be an option, as the Python process was
understandably confused by the loss of its containing directory.

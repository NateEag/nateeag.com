nateeag.com
===========

This is the source code and content for www.nateeag.com.

It's statically generated using a few Python modules and a small amount of
wrapper code.


Usage
=====

If you have direnv installed and configured, the following should work:

    $ make-virtualenv
    $ generate

To view the generated code, just view it through a browser. An easy way:

    $ run-devserver

then open a browser and hit localhost:$PORT, based on the CLI output.

Note that `bin/start-interactive-shells` takes care of that for you, if you're
a tmux user.


Production Environment
======================

A local test instance of a production environment can be started by running

    vagrant up

at a bash prompt.

After it spins for a bit, you should be able to access the site at
http://nateeag.local/.

For working on the site or its content, this is not necessary.

It's to help me develop the provisioning steps needed to host an instance of
the site on a production server.

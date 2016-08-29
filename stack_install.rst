Installing the LSST software stack
==================================

To use this guide you will need to install the LSST software
stack. Instructions on how to do this have been written by members of
the LSST project. These instructions are available at:
https://pipelines.lsst.io/install\ .

As you will be developing your own science pipeline, you will need to
perform the lsstsw installation. Once you have done this you must also
test your installation by performing the `demo
<https://pipelines.lsst.io/install/demo.html>`_\ . Finally, I
recommend that you run the ``lsstsw/bin/setup.sh`` script each time you open a
new shell by adding the command to you .bashrc file: ::
    . path/to/lsstsw/bin/setup.py

A note on the EUPS versioning system
------------------------------------

The LSST stack consists of many packages that are currently being
edited by more than one person on a daily basis. It easy to conceive
that an edit in one package may now be compatible with a simultaneous
edit by another person in a different package. To make sure this
doesn't cause problems, the LSST stack uses the EUPS versioning system
which allows you to specify which version of each package to use. That
way, if someone makes an edit in package A that isn't compatible with
your edit of package B, you can still test your edits of B using a
previous version of package A.

The reason this is important for this guide is that before you can use
a package that it already available in the installed stack (for
example, obs\_subaru) you must set it up with EUPS by issuing (for
this example) ::
     ``setup obs\_subaru``

Of course, the obs\_package you will develop using this guide is *not*
already available in the stack. Therefore, before you can use it you
must ``declare`` it to EUPS. Instructions explaining how to do this
are provided later in the tutorial, once your obs\_package is at a
suitable stage of readiness to be declared, setup, and used.

The `official manual <https://dev.lsstcorp.org/trac/wiki/EupsManual>`_
for the EUPS system is long, complicated and far more involved than
what you will need to set up your own obs\_package. Instead, if you
wish to learn more about the EUPS system and syntax, I recommend you
take a look at the EUPS tutorial at:
https://developer.lsst.io/build-ci/eups_tutorial.html.


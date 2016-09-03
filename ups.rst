The EUPS table
==============

To enable the stack to access your camera's obs\_package, the EUPS
system needs to know about it. To facilitate this, you need to
``declare`` it to EUPS, then set it up (more on this later). When you
do this, EUPS looks for a table file in the ``obs\_<package>/v1/ups``
directory you have made, named ``obs\_<package>.table`` (e.g.,
``obs_necam.table``). This table file tells the EUPS system what other
packages in the stack your obs\_package depends on, and thus also need
setting up. It also modifies your paths to include the directories in
which your scripts are contained.

To create your table file, open it in an editor and add the following
lines: ::
   
   setupRequired(pipe_tasks)
   envPrepend(PYTHONPATH, ${PRODUCT_DIR}/python)

This tells the EUPS system that when your obs\_package is set up, it
also needs to set up the ``pipe_tasks`` package.

Declaring your obs\_package
---------------------------

So that the EUPS systems knows where to find your ups table, you need
to declare its location within the filesystem to EUPS. You also need
to declare the version of the package. This is done using the ``eups
declare`` command, for example: ::

      eups declare obs_necam v1 -r $stack/obs_necam/v1

Here, I have named the packaged ``obs_necam`` and given it the version
``v1``. The input following ``-r`` tells EUPS the path to your
obs\_package.

You can check whether EUPS is aware of your obs\_package by issuing: ::

    eups list

and checking whether it appears in the resulting list.

Once a package has been declared, it is saved within the EUPS database
and does not need to be declared in any future sessions.

While your obs\_package has been declared, it has not been set
up. This means that, while EUPS is ``aware'' of it, the LSST stack
cannot yet access its contents. To explain why this is the case, we
need to consider package ``versions''.

Imagine a situation where your obs\_package is working, but you want
to add a new feature. You don't want to edit the working version in
case you break it, so you make a new directory: ``obs_<package>/v2/``
and copy over the contents of ``obs_<package>/v1/``. You make your
edits to add the new feature and ``declare`` it to EUPS: ::

      eups declare obs_necam v2 -r $stack/obs_necam/v2

But, how does EUPS know which version to use? To tell it, you need to
``setup`` a declared version. To use your ``v1`` to analyse some data,
you would issue, for example: ::

	  setup obs_necam v1

then, to switch to ``v2`` to test your new features, you would issue: ::

      setup obs_necam v2

This makes keeping separate versions and switching between them quick
and easy.

If you wish, you can tell EUPS which version to use by default by
telling it which is the ``current`` version using:

   eups declare -t current obs_necam v1

Unlike ``declare``, you must ``setup`` your obs\_package every time
you start a new session. Of course, you can automate this by adding
the ``setup`` command to your ``.bashrc`` file.

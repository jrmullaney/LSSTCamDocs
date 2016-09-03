The EUPS table
==============

To enable the stack to access your camera's obs\_package, the EUPS
system needs to know about it. To facilitate this, you need to
``declare`` it to EUPS, then set it up (more on this later). When you
do this, EUPS looks for a table file in the ``obs\_<package>/ups``
directory you have made, named ``obs\_<package>.table`` (e.g.,
``obs_necam``). This table file tells the EUPS system what other
packages in the stack your obs\_package depends on, and thus also need
setting up.


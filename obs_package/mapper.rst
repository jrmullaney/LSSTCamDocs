The obs mapper
==============

When you execute an LSST task, such as ``processCcd.py`` to perform
basic data reduction and source detection, the first thing it will do
is look for the "mapper" script. This python script tells the task
what obs\_package to use, where to find the file structure of the
data, where information on the physical properties of the detector is
stored, how to read the data, etc. As such, the mapper script is one
of the most important components of a camera's obs\_package.

Telling an LSST task the location of the mapper file
----------------------------------------------------

The location of the mapper script is provided to an LSST task via a file
named (reasonably enough) ``_mapper``, which is contained within the
topmost level of your input data directory. For example, if your
telescopes raw data is held in: ::
	   /path/to/my/data/raw/Night1/

then you may wish to put ``_mapper`` in the ``data/`` directory (the
one that contains the ``raw`` data). In that instance, the input
directory given to the LSST task would then be ``/path/to/my/data/``.

To enable the LSST stack to work with our ``obs_necam`` package,
``_mapper`` would need to contain a single line entry: ::
	    lsst.obs.necam.necamMapper.NecamMapper

(note to follow the single line with a carriage return).

The basics of a mapper file - Part 1
------------------------------------

Because it plays a very central role in the way an LSST task accesses
data, an obs\_package's mapper script can become rather extensive. As
such, in this tutorial we will build up the mapper script in separate
stages, returning to it as the obs\_package develops. In this first
part, we will use the mapper script to tell the called task where it can
find a configuration file as well as the information describing the
filestructure of our input data and the physical properties of the
detector.

The part of the mapper script described here can be found in the
obs\_necam GitHub repository (**need to provide link**).
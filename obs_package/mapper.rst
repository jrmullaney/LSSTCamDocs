The obs mapper
==============

When you execute an LSST task, such as ``processCcd.py`` to perform
basic data reduction and source detection, the first thing it will do
is look for the "mapper" file. This file tells the task what
obs\_package to use, where to find the file structure of the data,
where information on the physical properties of the detector is
stored, how to read the data, etc. As such, the mapper file is one of
the most important components of a camera's obs\_package.

When an LSST task is executed, it looks for a file called ``_mapper``
contained within the topmost level of the input data
directory. ``_mapper`` contains the location of the mapper which the
task will use to access the data from your detector. For example, if
your telescopes raw data is held in: ::
     /path/to/my/data/raw/Night1/

then you may wish to put ``_mapper`` in the ``data/`` directory (the
one that contains the ``raw`` data). In this instance, the input
directory given to the LSST task would then be
``/path/to/my/data/``.

To enable the LSST stack to work with our ``obs_necam`` package,
``_mapper`` would need to contain a single line entry: ::
lsst.obs.necam.necamMapper.NecamMapper

(note to follow the single line with a carriage return).


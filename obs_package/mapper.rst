The obs mapper
==============

When you submit an LSST task, such as ``processCcd.py`` to perform
basic data reduction and source detection, the first thing it will do
is look for the "mapper" file. This file tells the task what
obs\_package to use, where to find the file structure of the data,
where information on the physical properties of the detector is
stored, how to read the data, etc. As such, the mapper file is one of
the most important components of a camera's obs_package.
The policy file
===============

One of the most fundamental jobs of an obs\_package is to provide
executed LSST tasks with the locations of data files within the local
filesystem. These data files can include input raw images, as well as
output processed images and data tables. The locations of these files
are held within ``policy`` files, which are contained within the
``policy`` directory in the obs\_package.
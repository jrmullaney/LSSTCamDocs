The policy file
===============

One of the most fundamental jobs of an obs\_package is to provide
executed LSST tasks with the locations of data files within the local
filesystem. These data files can include input raw images, as well as
output processed images and data tables. The locations of these files
are held within ``policy`` files, which are contained within the
``policy`` directory in the obs\_package.

There is a policy file in the policy directory of obs\_necam; it's
called NecamMapper.paf. Before the bulk of the file that describes the
local filesystem, there are a couple of lines which tell the stack
whether there is a registry of calibration files and where to look for
a physical description of the camera. We'll cover those in more detail
later, but for now we'll just add the following two lines to the
policy file: ::
       needCalibRegistry: true
       camera: "../camera"


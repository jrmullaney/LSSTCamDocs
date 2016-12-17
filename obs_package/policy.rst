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

Next come a number of text blocks surrounded by curly brackets that
describe the locations of files of various types. Surrounding groups
of these blocks are classifiers called things like ``exposures``,
``calibrations``, ``datasets``, etc. Considering the first block
within the ``exposures`` classifier: ::
           Sci: {
    	    template:    "SCI/%(dateObs)s%(filter)s/Sci_%(frameId)04d.fts"
	     python:      "lsst.afw.image.DecoratedImageU"
	     persistable: "DecoratedImageU"
	     storage:     "FitsStorage"
	     level:       "Ccd"
	     tables:      "raw"
	     tables:      "raw_visit"
		   }

The first line ``Sci:{`` provides the stack with a shortname by which
this type of file is identified withing the stack. The next line
``template: ...`` describes the location of the stack within the
filesystem and includes variables in the form of
``%(<value>)s``. We'll explore these meaning of these variables
below. The next two lines (labelled ``python`` and ``persistable``)
tell the stack what type of data is contained within the file; for
example, whether it is an image file (with or without a header)
containing integer or float values, or a data table etc. The
``storage`` line describes the format of the file (e.g., fits image or
fits catalog). Finally, there are the ``level`` and ``table`` lines
which are associated with the registry (a database which helps to
identify files), which we'll cover later in the tutorial.

The ``template`` line contains a mixture of hard-coded and string
variables. The purpose of the variables is to allow the desired file
to be set either at run-time, or by referring to a registry. For
example, if you wanted to process the science file located at
``SCI/2016-01-01/V/Sci_0001.fts``, you would refer to it at run-time
with the ID: ::
     dateObs=2016-01-01 filter=V frameId=1

Note the variable format descriptor after the closing bracket (e.g.,
the ``s`` in ``%(<value>)s``), which tells the stack the format of
each ID in the filepath. Here, ``s`` refers to string, whereas ``04d``
means a number four characters long, padded with 0's if necessary.
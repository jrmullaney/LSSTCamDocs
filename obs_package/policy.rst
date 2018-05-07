The policy file
===============

One of the most fundamental jobs of an obs\_package is to provide executed LSST tasks with the locations of data files within the local filesystem. These data files can include input raw images, as well as output processed images and data tables. The locations of these files are held within ``policy`` files, which are contained within the ``policy`` directory in the obs\_package.

There is a policy file in the policy directory of obs_necam_ ; it is called ``NecamMapper.yaml``. Before the bulk of the file that describes the local filesystem, there are a couple of lines which tell the stack whether there is a registry of calibration files and where to look for a physical description of the camera. We'll cover those in more detail later, but for now we'll just add the following two lines to the policy file: ::

       needCalibRegistry: true
       camera: "../camera"

Next come a number of text blocks that describe the locations and contents of the stack's various input and output files. Surrounding groups of these blocks are classifiers called things like ``exposures``, ``calibrations``, ``datasets``, etc. Considering the first block within the ``exposures`` classifier: ::

        	raw:
	    		python:      "lsst.afw.image.DecoratedImageU"
    			persistable: "DecoratedImageU"
	     		template:    "SCI/%(dateObs)s%(filter)s/Sci_%(frameId)04d.fts"

The first line ``raw:`` provides the stack with a shortname by which this type of file is identified withing the stack. The first two lines (labelled ``python`` and ``persistable``) tell the stack what type of data is contained within the file; for example, whether it is an image file (with or without a header: ``DecoratedImage`` vs. ``Image``, respectively) containing integer or float values (``DecoratedImageU`` vs. ``DecoratedImageF``, respectively), or a data table etc. (N.B., I've tried looking for an online list of all possible file types, but to no avail. I'll post it here if I ever do find it).

The next line ``template: ...`` describes the location of the file within the filesystem *once it has been ingested/processed by the stack* - the policy file does not include a reference to how your data is stored prior to ingestion (see the `Ingest section`_ for a description of the ingest process). The ``template`` line includes variables in the form of ``%(<value>)s``. The purpose of the variables is to allow the desired file to be set either at run-time, or by the stack referring to a database (referred-to as a registry). For example, if you wanted to process the science file located at ``SCI/2016-01-01/V/Sci_0001.fts``, you would refer to it at run-time with the ID: ::

     dateObs=2016-01-01 filter=V frameId=1

Note the variable format descriptor after the closing bracket (e.g., the ``s`` in ``%(<value>)s``), which tells the stack the format of each ID in the filepath. Here, ``s`` refers to string, whereas ``04d`` means a number four characters long, padded with 0's if necessary.

We'll keep adding to the policy file as we develop the obs\_package as we progress through the guide. 

.. obs_necam: https://github.com/jrmullaney/obs_necam
.. `Ingest section`: _ingest
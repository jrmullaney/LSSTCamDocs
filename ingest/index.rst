Ingesting: Declaring file locations and types
=============================================

.. toctree::
   :maxdepth:10
   :hidden:

   mapper
   policy   

.. update index

Before the stack can process your data, it first needs to *ingest* it. Ingesting is performed by the ``ingestImages.py`` task, the execution of which will be described later. Ingesting achieves two main goals:

* it copies/moves/links (depending on your preference) your raw data to the location in your filesystem specified within your policy file;
* it places entries within a database that contain selected information about the observations (such as date of observation, filter, etc.)

Since we have already set up the policy file to tell the stack where to place our raw input data within our filesystem, ``ingestImages.py`` can achieve its first goal. To achieve its second goal, however, ``ingestImages.py`` needs to know what values must be held within the database in order to uniquely identify a given observation. This information is provided to ``ingestImages.py`` by the obs\_package via its own dedicated config file, which resides in the ``config`` directory and is called ``ingest.py``.

The ingest config file
----------------------

The ingest config tells the ingest task what information it needs to put into the data and where it can find this data (and how to parse it, where mecessary).

The first few lines in the ingest config file imports and retargets a module contained within your ``python/lsst/obs/necam`` directory that tells ingest how to _parse_ the various values it eventually puts into the database (more on parsing later).

Next is a _translation_ block (``config.parse.translation``) which tells ingest which header keywords to look up in your raw data files to find the values that need to go into the database. For example, the exposure time of the observation is stored in the "expTime" column in the database, but is associated with the "EXPTIME" keyword in your raw file's fits header.

The translation block works well for values that are already in the appropriate format within the fits header of your raw data files. However, in many cases this will not be the case. For example, the date in the fits header may be in YYYY-MM-DDTHH:MM:SS.FFFF ISO format, yet the database only accepts YYYY-MM-DD format. To accomodate such cases requires some degree of _parsing_, whereby a small python function takes the value from the header and parses it into the correct format. These parsing functions are contained within the ``python/lsst/obs/necam/ingest.py`` file as part of a ``NecamParseTask`` class and have appropriate names such as ``translateDate``. You'll need to write your own parsing functions where necessary, so feel free to use necams's translation functions as a guide. Having done that, you must tell the ingest config file which translator functions to use for each of the database entries that require it. This is done by the :: 

    config.parse.translators = {'dateObs':'translateDate',
                                'taiObs':'translateDate',
                                'visit':'translateVisit',
                                'ccd':'translateCcd'}

block in necam's ingest config file, which you should edit to suit your own requirements.



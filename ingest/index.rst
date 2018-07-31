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

The first few lines in the ingest config file imports and retargets a module contained within your ``python/lsst/obs/necam`` directory that tells ingest how to *parse* the various values it eventually puts into the database (more on parsing later).

Next is a *translation* block ::

    config.parse.translation = {'dataType':'IMGTYPE',
                                'expTime':'EXPTIME',
                                'frameId':'RUN-ID',
                                'filter':'FILTER',
                                'field':'OBJECT'}

which tells ingest which header keywords to look up in your raw data files to find the values that need to go into the database. For example, the exposure time of the observation is stored in the "expTime" column in the database, but is associated with the "EXPTIME" keyword in your raw file's fits header.

The translation block works well for values that are already stored in the appropriate format within the fits header of your raw data files. However, in many cases this will not be the case. For example, the date in the fits header may be in YYYY-MM-DDTHH:MM:SS.FFFF ISO format, yet the database only accepts YYYY-MM-DD format. To accomodate such cases requires some degree of *parsing*, whereby a small python function takes the value from the header and parses it into the correct format. These parsing functions are contained within the ``python/lsst/obs/necam/ingest.py`` file as part of a ``NecamParseTask`` class and have appropriate names such as ``translateDate``. You'll need to write your own parsing functions where necessary, so feel free to use necams's translation functions as a guide. Having done that, you must tell the ingest config file which translator functions to use for each of the database entries that require it. This is done by the following block in the ingest config file :: 

    config.parse.translators = {'dateObs':'translateDate',
                                'taiObs':'translateDate',
                                'visit':'translateVisit',
                                'ccd':'translateCcd'}

 which, again, you may wish to edit to suit your own requirements.

The ingest task now has everything it needs to know to extract and parse information from the fits headers of the input data. Next, it needs to know the column names this information should be stored under within the database and the format of the data (e.g., string, integer, etc.). It also needs to know which columns describe a ``raw_visit`` (it seems, however, this is may be a bit of a relic; see `this LSST community forum thread <https://community.lsst.org/t/appropriate-use-of-raw-and-raw-skytile-tables-in-mappers/1111>`_ ). Finally, it also needs to know what combination of data uniquely identifies an exposure -- for example, lots of exposures from a raft of CCDs may share a single visit number, but it may be the case that the combination of a visit number *and* a CCD number uniquely identifies an exposure. These three pieces of information are provided by the following three blocks in the ingest config file ::

    config.register.columns = {'frameId':'text',
                            'visit':'int',
                            'ccd':'int',
                            'filter':'text',
                            'dataType':'text',
                            'expTime':'double',
                            'dateObs':'text',
                            'taiObs':'text',
                            'field':'text' }

    config.register.visit = ['visit', 'ccd', 'filter', 'dateObs', 'taiObs']

    config.register.unique = ['visit', 'ccd']

This completes all the information that the ``ingestImages.py`` task needs to parse the necessary data from the headers of the raw images and ingest it into its database of images.




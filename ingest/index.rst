Ingesting: Declaring file locations and types
=============================================

.. toctree::
   :maxdepth:10
   :hidden:

   mapper
   policy   

.. update index

Before the stack can process your data, it first needs to *ingest* it. Ingesting is performed by the ``ingestImages.py`` task, the execution of which will be described later. Ingesting achieves two main goals:

* it copies/moves/links your raw data to the location in your filesystem specified within your policy file;
* it places entries within a database that contain selected information about the observations (such as date of observation, filter, etc.)

Since we have already set up the policy file to tell the stack where to place our raw input data within our filesystem, so ``ingestImages.py`` can achieve its first goal. To achieve its second goal, however, ``ingestImages.py`` needs to know what values must be held within the database in order to uniquely identify a given observation. This information is provided to ``ingestImages.py`` by the obs\_package via its own dedicated config file, which resides in the ``config`` directory and is called ``ingest.py``. 


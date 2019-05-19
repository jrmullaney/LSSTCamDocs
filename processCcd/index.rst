Processing a single science frame
=================================

.. toctree::
   :maxdepth: 5
   :hidden:   

   mastercal			
   processCcd			

.. update index

With the stack now installed and your data files ingested, we can start to process data. In this tutorial, we will use the stack to undertake the following processing steps:

* combine a set of calibration frames to create master bias, flat, and dark frames;
* correct a science frame using the master calibration frames;
* calibrate and characterise the science frame, which involves sky subtraction, PSF modelling, astrometric correction, and photometric calibration;
* source detection and measurement.

The first first item on the above list is performed by the ``constructBias.py``,  ``constructFlat.py`` and ``constructDark.py`` pipe tasks, which we will look at next. Following ingestion of the master calibration frames, the remaining items are all performed by a single task - ``processCcd.py``. This latter task will likely require more configuring than any other pipe task you will encounter. 

Before continuing, it is worth pointing out that pipe tasks run on a single core, and will thus process your data serially. Most pipe tasks, however, have multi-core equivalents known as ``pipe_drivers``, which farm out the pipe tasks to multiple cores. Configuring a pipe driver is similar to configuring a pipe tasks, so I've included a brief section on how to confgure and run the equivalent pipe driver after describing their associated pipe task.




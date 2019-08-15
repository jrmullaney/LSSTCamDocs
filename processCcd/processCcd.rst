Processing your data
====================

Among the first and most fundamental tasks that you will want the
LSST stack to do is to process your imaging data to remove instrument
signatures (e.g., overscan removal, bias subtraction, flat-fielding)
and perform source detection. Both these tasks are performed by
``processCcd.py``.

Like all of the data processing tasks in the LSST stack,
``processCcd.py`` resides in the ``pipe_tasks`` repository. This means
that, provided you have (a) setup the eups table in ``obs_necam``
following the instructions in `The EUPS table
<http://lsstcamdocs.readthedocs.io/en/latest/obs_package/ups.html>`_
section and (b) executed ``setup obs_necam`` command, then
``processCcd.py`` will be callable from the command line. To use
``processCcd.py``, we need to tell it where the input data is, and
where it should put any output data:
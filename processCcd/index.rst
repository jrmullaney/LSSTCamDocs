Processing your camara's data
=============================

One of the first and most fundamental tasks that you will want the
LSST stack to do is to process your imaging data to remove instrument
signatures (e.g., overscan removal, bias subtraction, flat-fielding)
and perform source detection. Both these tasks are performed by the
``processCcd.py`` task.
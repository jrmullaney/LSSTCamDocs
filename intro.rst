Introduction
============

A major component the LSST project is the development of a software
stack that will process the raw data from the raft of CCDs that form
the LSST's detector. The end product of the stack will be a database
containing the properties of billions of astronomical sources.

While the telescope itself will not see first light until 2019, it is
important that the software needed to process the first observations
is in a state of readiness prior to that date. As such, considerable
work has already been carried-out in developing this software - known
collectively as the LSST software stack. This stack is freely
available on github on an open source licence.

Despite being primarily developed for the LSST camera, since most
astronomical imaging systems fundamentally similar (i.e., detectors
consisting of one or more CCDs plus a set of filters), there is no
reason why the stack cannot be adapted to work with other
cameras. Indeed, it is already being used as the primary data analysis
pipeline for the Subaru Telescope's wide-field camera,
HyperSuprimeCam.

Why adapt the LSST stack for another camera?
--------------------------------------------
There are already 

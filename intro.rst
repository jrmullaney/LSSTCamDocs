Introduction
============

A major component the LSST project is the development of a software
stack that will process the raw data from the raft of CCDs that form
the LSST's detector. The end product of the stack will be a database
containing the properties of billions of astronomical sources.

While the telescope itself will not see first light until 2019, it is
important that the software needed to process the first observations
is in a reasonable state of readiness prior to that time. As such,
considerable work has already been carried-out in developing this
software - known collectively as the LSST software stack. This stack
is freely available on github on an open source licence.

Despite the stack being primarily developed for the LSST camera, since
most astronomical imaging systems fundamentally similar (i.e.,
detectors consisting of one or more CCDs plus a set of filters), there
is no reason why it cannot be adapted to work with other cameras,
especially those carrying out wide-field astronomical surveys. Indeed,
it is already being used as the primary data analysis pipeline for the
Subaru Telescope's wide-field camera, HyperSuprimeCam.

Why adapt the LSST stack for another camera?
-------------------------------------------- 

As software already exists to process astronomical imaging data, it is
reasonable to ask why we should bother adapting and using the LSST
stack to analyse data from other cameras. Here are my reasons, but you
may have your own:

* it enables the significant experience and expertise of the people developing the stack to be applied to our data;

* Speed: while the higher level tasks are performed with Python, the stack does all its ``heavy lifting'' using much faster pre-compiled C++ code. In addition, a number of the stack's top-level tasks can be parallelised, providing further speed-ups compared to other pipelines;

* the end stack will include many features that are not normally or easily implemented in other pipelines (e.g., forced photometry, multi-epoch stacking). Although some of these are still under development, adapting the stack to other cameras now means they can be exploited as and when they become available;

* the LSST stack is still under active development; by adapting the stack for other cameras, we can test it and provide feedback to improve it prior to the LSST's first light.

The reason for this guide
-------------------------

What this guide is
------------------

What this guide isn't
---------------------


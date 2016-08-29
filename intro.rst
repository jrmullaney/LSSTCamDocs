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

While developing the processing pipeline of a new wide field camera,
some colleagues and I decided to explore the prospect of using the
LSST software stack for this task. We soon discovered that to achieve
this goal, we would need to develop a set of Python scripts and
configuration files (hereafter, referred to as an 'obs package') that
tells the stack how to read and process our data. We also discovered,
however, that while obs packages do exists for other cameras, there
was very little documentation describing how they were developed. 

Cue many weeks of reverse-engineering the stack and the available obs
packages of other cameras and a trial-and-error process of producing
an our own obs package. We like to think of this guide as what we
wished we had at the start of this process.

What this guide is
------------------

This guide will explain how to develop a *basic* obs package that will
allow the stack to process data from an alternate camera. It covers:

** a brief description of how to install the stack,

** a section on how to ``ingest'' images into a format and filestructure that the stack can understand. 

** a description of how to process the raw images, including bias subtraction, flat fielding etc., to produce a final catalogue of detected sources.

The goal of the guide is simply to achieve these tasks without the
stack crashing.

As I played no role in developing the LSST stack, there are some parts
of the obs package that I don't fully understand. I just know that I
had to include them in order to achieve the end goal.

What this guide isn't
---------------------

Simply following this guide will not produce scientifically valid
images or catalogues. There are a huge number of parameters and
calibrations that need to be set, tweaked and re-tweaked depending on
your data. For example, I cannot tell you the what numbers to set for
the dimensions of your detector, nor its overscan region, let alone
its gain, pixel size or where to set the detection threshold
etc. etc. While the stack may not crash with your data using the
numbers I include in the examples, the output will certainly be
garbage.

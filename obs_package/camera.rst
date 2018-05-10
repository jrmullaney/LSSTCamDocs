The camera files
================

To be able to process your data, the stack needs to know a number of things about the physical properties of your camera. For example, it needs to know how many pixels are on the CCD(s), whether it has an overscan region that needs trimming, what the saturation limit is (so it can mask saturated sources), etc. This information is provided to the stack by the files that reside in directory declared in your policy file (via ``camera: "../camera"``).

I consider the camera files to be the most complex component of the obs\_package, and there are many components within them that I don't fully understand. I have, however, been able to get the stack working with my camera\'s data by emulating the camera files in other obs\_packages published in the LSST stack\'s github repositories.

The camera files consist of two main components:

* A python script called ``camera.py`` in which a large number of parameters are defined.
* A fits table containing a values that describe the physical properties of your camera's CCD(s).

Wide-area astronomical cameras often consist of multiple CCDs, and each one must have an associated fits table. Furthermore, a single CCD may consist of two or more sections, each driven by a different amp. The parameters describing each section are contained within separate rows within the fits table.

To create the fits table(s) describing the CCDs, I have written a python script called ``buildDetector.py`` and put it in the camera directory of obs_necam repository. Feel free to use this script to generate your own fits tables for your CCDs.

The camera files contained within obs\_necam are set to work with the simulated data that we will process throughout later in this guide. Clearly, you'll need to adjust a wide number of parameters to suit your own camera. Since there are so many parameters to set within the camera files (including within ``buildDetector.py``), and since there are a number that I don't fully understand myself, I haven't written an exhaustive list of them here. Instead, I refer you to the comments contained within the ``camera.py`` and ``buildDetector.py`` scripts.

With our obs\_package now containing all the files that it needs (if not yet complete), we can now start running our first LSST stack which will *ingest* our data. 
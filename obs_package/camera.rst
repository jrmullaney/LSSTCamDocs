The camera files
================

To be able to process your data, the stack needs to know a number of things about the physical properties of your camera. For example, it needs to know how many pixels are on the CCD(s), whether it has an overscan region that needs trimming, what the saturation limit is (so it can mask saturated sources), etc. This information is provided to the stack by the files that reside in directory declared in your policy file (via ``camera: "../camera"``).

I consider the camera files to be the most complex component of the obs\_package, and there are many components to them that I don't fully understand. I have, however, been able to get the stack working with my camera\'s data by emulating the camera files in other obs\_packages published in the LSST stack\'s github repositories.
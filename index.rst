.. LSSTCam documentation master file, created by
   sphinx-quickstart on Sat Aug 27 20:55:56 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Adapting the LSST stack for other cameras
=========================================

The aim of this documentation is to explain how to adapt the LSST
software stack to process data from other telescope+detector
combinations -- hereafter referred to as a ``camera''. 

The documentation takes the form of a tutorial based on the author's
trial-and-error experience of adapting the LSST stack to a wide field
camera. As such, while it will lead you through the steps needed to
set up your own camera, you will have to adjust a wide range of
parameters to suit your camera before it will produce reliable
results. Also note that any description of the stack's packages are
based on the author's own limited understanding which is, in turn,
based on (currently) very limited official documentation.

Accompanying this tutorial is a github repository, obs_necam
(pronounced "any cam"), which contains templates of the scripts and
files needed to adapt the LSST stack to an alternate camera. The
commits to this repository provide a set of snapshots which are
referred to at key stages throught the tutorial.

Finally, it is important to note that this documentation is in no way
affiliated with nor endorsed by the LSST organisation.

Table of contents
-----------------
.. toctree::
   :maxdepth: 10
   :includehidden:
   :titlesonly:   
   
   intro	
   stack_install
   obs_package/index
   ingest/index   
   processCcd/index   
      
.. update index

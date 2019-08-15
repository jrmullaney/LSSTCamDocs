.. LSSTCam documentation master file, created by
   sphinx-quickstart on Sat Aug 27 20:55:56 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Adapting the LSST stack for other cameras
=========================================

The aim of this documentation is to explain how to adapt the LSST
software stack to process data from other telescope+detector
combinations -- hereafter referred to as a "camera". 

The documentation takes the form of a tutorial based on the author's
trial-and-error experience of adapting the LSST stack to a wide field
camera. As such, while it will lead you through the steps needed to
set up your own camera, you will have to adjust a wide range of
parameters to suit your camera before it will produce reliable
results. Also note that any description of the stack's packages are
based on the author's own limited understanding which is, in turn,
based on (currently) very limited official documentation for the LSST stack.

Accompanying this tutorial is a github repository, `obs_necam <https://github.com/jrmullaney/obs_necam>`_
(pronounced "any cam"), which contains templates of the scripts and
files needed to adapt the LSST stack to an alternate camera. I recommend you refer to the contents of that repository while following this guide; indeed, feel free to fork and edit obs_necam_ as you progress.

**Important Note August 2019:** This tutorial is based on the Generation 2 ("Gen 2") stack. Currently, the stack is undergoing some major changes while transitioning to the next generation, Gen 3. While some of this tutorial will remain relevant for Gen 3, large parts will change. As such, while reading through this tutorial will introduce you to the broad concepts of developing your own obs package, we strongly recommend, if you can, that you hold off developing your own obs package until the stack has transitioned to Gen 3 with v.19 (due early 2020).   

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
   ingest   
   processCcd/index   
      
.. update index

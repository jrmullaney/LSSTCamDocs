A camera's ''obs'' package
==========================

.. toctree::
   :hidden:

   ups			
   python
   config	
   policy   
   camera

Adapting the LSST stack to a new camera involves setting up a new
package within the LSST stack. This package is usually called an
``obs_<package>``. I like to think of it as an interface between the
rest of the LSST stack and the data from the camara. Contained within
an ``obs_<package>`` is a set of Python scripts and configuration
files that tells the rest of the stack things like:

* the properties of your detector (e.g., dimensions, overscan region) and its filters,
* the file structure where your data is held,
* how to remove instrument signatures from your science frames (also known as bias subtraction, dark correction, flat fielding etc.)
* what tasks you'd like the stack to do, such as source detection, deblending, astrometric correction, photometric calibration etc.

Provided you only want to use the stack in its current form (i.e., you
don't want to edit the stack proper to add extra functionalities) then
making your own ``obs_<package>`` is the *only* thing you will need to
do to adapt the stack to your camera. Having said that, developing
your own ``obs_<package'' is no trivial task.

If you have already installed the LSST stack, you will note that it
already contains a number of ``obs_<packages>``; for example,
``obs_sdss``, ``obs_cfht`` and, the most useful and most developed,
``obs_subaru``. You can have a look around and familiarise yourself
with the contents of these packages, either within your own install or
in the `LSST github repository <https://github.com/lsst>`_ repository
(which is my preference, though bear in mind that the github
repository is constantly being updated, so it won't be long until your
installed stack is different to that on github).

You will notice that the various ``obs_<packages>`` already installed
are just directories. So, to create your own ``obs_<package>``, the
first think you will need to do is ``mkdir`` a new directory named
accordingly; I use ``obs_necam`` throughout. In the following, I
assume that the ``$stack`` variable points to the directory containing
installed LSST stack packages (e.g., in bash shell: ``export
stack=~/Workstuff/lsstsw/stack/Linux64/``): ::

	cd $stack
	mkdir obs_necam 

Next, within ``obs_necam``, you will need to ``mkdir`` five other
directories called: ::
	    
	    mkdir camera
	    mkdir config
	    mkdir policy
	    mkdir ups
	    mkdir -p python/lsst/obs/necam

Here, the ``-p`` option causes all the parent directories to be
created as well.

The next few pages will describe in detail the files that these
directories need to contain to process your camera's data. Here, I
just provide a brief description:

* **camera:** Files containing information that describe the properties of your camera, such as its dimensions, gain etc.
* **config:** Configuration files that tell the various stack process that access your data how to behave. 
* **policy:** Files describing the file structure and type of input and output data (e.g., image, table etc).
* **ups:** A file telling the eups system what other packages need to be set up to use this ``obs_<package>``.
* **python/lsst/obs/necam:** Various Python scripts that perform processes such as instrument signature removal.

Before populating these directories with the files described above,
you will need to add some ``__init__.py`` files to the
``python/lsst`` and ``python/lsst/obs`` directories: ::

	cd $stack/python/lsst/
	echo import pkgutil, lsstimport > __init__.py
	echo __path__ = pkgutil.extend_path(__path__, __name__) >> __init__.py	

Note the ``>>`` in the second line, which appends to the file. Next,
do the same in ``$stack/python/lsst/obs`` . If you make a mistake,
simply open up the file in your favourite editor (vim, emacs, etc.)
and correct it.



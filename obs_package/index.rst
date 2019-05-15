A camera's ''obs'' package
==========================

.. toctree::
   :maxdepth: 5
   :hidden:   

   ups			
   mapper			
   config
   policy
   camera   

.. update index

Adapting the LSST stack to a new camera involves writing your own
obs\_package. I like to think of an obs\_package as an interface between the
rest of the LSST stack and the data from the camara. Contained within
an obs\_package is a set of Python scripts and configuration
files that tells the rest of the stack information such as:

* the properties of your detector (e.g., dimensions, overscan region) and its filters,
* the file structure where your data is held,
* how to remove instrument signatures from your science frames (also known as bias subtraction, dark correction, flat fielding etc.)
* what tasks you'd like the stack to do, such as source detection, deblending, astrometric correction, photometric calibration etc.

Provided you only want to use the stack in its current form (i.e., you
don't want to add new modules to the stack proper to add extra functionalities) then
making your own obs\_package is the *only* thing you will need to
do to enable the stack to process the data from your camera. Having said that, developing
your own obs\_package is not a trivial task.

If you have already installed the LSST stack, you will note that it
already contains a number of obs\_packages; for example,
``obs_sdss``, ``obs_cfht`` and, the most developed and most useful as
a reference, ``obs_subaru``. You can have a look around and
familiarise yourself with the contents of these packages, either
within your own install or in the `LSST github repository
<https://github.com/lsst>`_ (which is my preference, though
bear in mind that the github repository is constantly being updated,
so it won't be long until your installed stack is different to that on
github).

You will notice that the various obs\_packages already installed
are just directories. So, to create your own obs\_package, the
first think you will need to do is ``mkdir`` a new directory named
accordingly; I use ``obs_necam`` throughout. In the following, I
assume that the ``$stack`` variable points to the directory containing
installed LSST stack packages (e.g., in bash shell: ``export
stack=~/Workstuff/lsstsw/stack/Linux64/``): ::

	cd $stack
	mkdir -p obs_necam/v1 

Here, the ``-p`` option causes the parent directory (i.e.,
``obs_necam``) to be created as well. Here, I have created the ``v1``
to contain the first version of the obs\_package.

Next, within ``obs_necam/v1``, you will need to ``mkdir`` five other
directories called: ::
	    
	    mkdir camera
	    mkdir config
	    mkdir policy
	    mkdir ups
	    mkdir -p python/lsst/obs/necam

The next few pages will describe in detail the files that these
directories must contain to process your camera's data. Here, I
just provide a brief description of the contents of each directory:

* **camera:** Files containing information that describe the properties of your camera, such as its dimensions, gain etc.
* **config:** Configuration files that tell the various stack process that access your data how to behave. 
* **policy:** Files describing the file structure and type of input and output data (e.g., image, table etc).
* **ups:** A file telling the eups system what other packages need to be set up to use this obs\_package.
* **python/lsst/obs/necam:** Various Python scripts that perform tasks such as instrument signature removal.

Before populating these directories with the files described above,
you will need to add some ``__init__.py`` files to the
``python/lsst`` and ``python/lsst/obs`` directories: ::

	cd $stack/obs_necam/v1/python/lsst/
	echo 'import pkgutil, lsstimport' > __init__.py
	echo '__path__ = pkgutil.extend_path(__path__, __name__)' >> __init__.py

Note the ``>>`` in the last line, which appends to the file. Next, do
the same in ``$stack/python/lsst/obs`` . If you make a mistake in the
above commands, edit the file using your favourite editor (vim, emacs,
VS Code, etc.).



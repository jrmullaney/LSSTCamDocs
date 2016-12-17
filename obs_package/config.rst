Task config files
=================

When you execute an LSST task, it first goes to the obs mapper script
(introduced on the previous page), then looks for an associated
configuration (hereafter, config) file within the obs\_package. All
config files are contained within the ``config`` directory (e.g.,
``obs_necam/v1/config/``) and are named after their associated task;
for example, the config file for the ``processCcd`` task has the
filename ``processCcd.py``.

The config file tells the executed LSST task what processes it should
carry-out and provides it with parameter values. For example, in the
case of the source detection task ``processCcd`` the config file may
instruct the task to measure the PSF and perform source deblending,
while also providing the flux cut used to select sources to define the
PSF. In this specific case, the config file plays a similar role as
the .sex configuration file used by SourceExtractor.

Each LSST task has its own set of configuration parameters that can be
set in the config file. Currently, there is no documentation listing
all the parameters that can set for a given task. To overcome this
problem, I wrote a small python script -- ``printDict`` -- which can
be called from within a config file that will list all of the
parameters that can be set, together with their current values: ::
	from lsst.obs.necam.printDict import printDict
	obj = printDict(config, path=['config'])

Once you have used ``printDict`` to see what parameters can be set,
changing their values is as straightforward as: ::
     	config.charImage.repair.cosmicray.nCrPixelMax = 1000000

There are potentially hundreds of parameters that can be set for each
task, and with the current lack of official documentation I am unable
to provide any description of them here. Thankfully, a lot of the
parameter names are quite self-explanatory, so I suggest you take a look
through them with ``printDict`` and experiment with changing some
parameters.


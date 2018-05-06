Task config files
=================

When you execute an task, such as ``processCcd``, it first goes to the obs mapper script
(introduced on the previous page), then looks for an associated
configuration (hereafter, config) file within the obs\_package. All
config files are contained within the ``config`` directory (e.g.,
``obs_necam/v1/config/``) and are named after their associated task;
for example, the config file for the ``processCcd`` task has the
filename ``processCcd.py``.

The config file tells the executed task what processes it should
carry-out and provides it with parameter values. For example, in the
case of the source detection task ``processCcd`` the config file may
instruct the task to measure the PSF and perform source deblending,
while also providing the flux cut used to select sources to define the
PSF. In this specific case, the config file plays a similar role as
the .sex configuration file used by SourceExtractor.

Each LSST task has its own set of configuration parameters that can be
set in the config file. If you execute a particular task at the command prompt and follow it with the option ``--show config``, e.g.: ::
	processCcd.py . --show config

then rather than executing the task, it will instead spit-out a list of all the configurable parameters for that task, together with short (mostly single-line) descriptions of what each parameter does. If you've already set up ``obs_necam`` you can run the above command and get a list of the thousands of parameters you can set for ``processCcd.py``.

Once you have used ``--show config`` to see what parameters can be set for a given task, then changing their values is as straightforward as putting, for example, the following line: ::
    config.charImage.repair.cosmicray.nCrPixelMax = 1000000

in the task's respective config file.

Since each task requires a different config file, we'll edit the config files as required when we start working with different tasks. Before that, however, your obs_package needs to tell the LSST stack how to organise your input and output data. It does this via the ``policy'' file, which I'll describe next.


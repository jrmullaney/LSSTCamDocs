Task config files
=================

When you execute an LSST task, it first goes to the obs mapper script
(introduced on the previous page), then looks for an associated
configuration (hereafter, config) file within the obs_\package. All
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
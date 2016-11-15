Task config files
=================

When you execute an LSST task, it first goes to the obs mapper script
(introduced on the previous page), then looks for an associated
configuration file within the obs_\package. All configuration files
are contained within the ``config`` directory (e.g.,
``obs_necam/v1/config``) and are named after their associated task;
for example, the configuration file for the ``processCcd`` task has
the filename ``processCcd.py``.
Combining and ingesting master calibration frames
=================================================

With the raw exposure now ingested, we can now start to process them. The first thing that needs to be done is to generate master calibration frames by combining the individual bias, dark, and flat frames. These master calibration frames will be used to correct the raw science frames for so-called ``instrument signatures''.

As part of the data ingestion step, the LSST stack 
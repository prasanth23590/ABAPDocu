---
title: "Time Stamps"
source_file: abentime_stamps.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Time Stamps

This section describes the representation of time-zone-independent [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) and the statements used for accessing such time stamps. There are two ways in which UTC time stamps can be handled in ABAP:

- [Time Stamp Fields with Time Stamp Type](abenutclong.md)

- [Time Stamps in Packed Numbers](abentime_stamps_packed.md)

Time stamps of the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) are [POSIX time stamps](../../abap-glossary/abenposix_timestamp_glosry.md) independent of time zone. This means, especially in conversions they are implicitly handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md).

## Hints

- In new programs, it is recommended that UTC time stamps in time stamp fields are used.

- The [system class for time stamps in packed numbers](abencl_abap_tstmp.md) contains methods for the conversion between the two representation types for UTC time stamps. These are necessary if time stamp fields are used in new programs, but existing repositories or interfaces must be accessed.

- There are no UTC time stamps for the missing days that exist due to the switch from the Julian to the Gregorian calendar. The UTC time stamp *1582-10-04T23:59:59.9999999* is followed by the UTC time stamp *1582-10-15T00:00:00.0000000*.

- The [POSIX time stamps](../../abap-glossary/abenposix_timestamp_glosry.md) of ABAP do not support [leap seconds](../../abap-glossary/abenleap_second_glosry.md).

---
title: "Rules for Time Zones"
source_file: abentime_zone_rules.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date, Time, Time Stamp, and Time Zones"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Rules for Time Zones

Conversion of the UTC reference time to the local date and the local time zone and vice versa, is based on a set of rules stored in AS ABAP system tables that can be accessed using [CDS views](../../abap-glossary/abencds_view_glosry.md). Conversions of this kind are caused by:

- The statements [`CONVERT UTCLONG`](abapconvert_utclong.md), [`CONVERT INTO UTCLONG`](abapconvert_date_utclong.md), [`CONVERT TIME STAMP`](abapconvert_time-stamp.md), and [`CONVERT INTO TIME STAMP`](abapconvert_date_time-stamp.md).

- The formatting option [`TIMEZONE`](abapcompute_string_format_options.md) for string templates.

The names of all associated tables start with `TTZ`, They contain:

- A list of possible time zones.

- A list of possible rules for the time difference between time zones and the UTC reference time.

- A list of all possible daylight saving time rules.

  - A list of fixed daylight saving time rules.

  - A list of variable daylight saving time rules

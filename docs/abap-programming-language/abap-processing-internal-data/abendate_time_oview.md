---
title: "Date, Time, Time Stamp, and Time Zones"
source_file: abendate_time_oview.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Date, Time, Time Stamp, and Time Zones

Dates, times, and time stamps specify times with varying levels of precision.

- A date or calendar date is a time specification for a calendar that is exact to a day, week, or month. AS ABAP always implicitly references the Gregorian calendar that is valid virtually worldwide. Output can be converted to [country-specific calendars](../abap-language-environment/abencountry_formats.md). Dates are generally interpreted as local dates that are valid in the current time zone.

- A time is a time of day specification that is exact to a second or minute with respect to a day. AS ABAP always saves times in 24-hour format. The output can have a [country-specific format](../abap-language-environment/abencountry_formats.md). Time specifications are generally interpreted as local times that are valid in the current time zone.

- A [time stamp](abentime_stamps.md) specifies a combined date and time that is exact to fractions of seconds or seconds with respect to a reference time. AS ABAP always implicitly references the [UTC](../../abap-glossary/abenutc_glosry.md) reference time. The values of [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md) or [time stamps in packed numbers](abentime_stamps_packed.md) are always handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md). A time stamp can be transformed to a local date and local time using statements and functions for which the required time zone is specified.

The relationship between the local date and local time on the one hand, and global [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) on the other, is established by a set of time zone rules, which are stored in database tables. These rules also respect daylight saving time.

- [Rules for Time Zones](abentime_zone_rules.md)

- [System Time Zone and User Time Zone](abensystem_user_time_zones.md)

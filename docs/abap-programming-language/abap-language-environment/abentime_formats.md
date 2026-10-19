---
title: "Time Formats"
source_file: abentime_formats.html
section: "ABAP Programming Language > ABAP - Language Environment > Formatting Settings > Country-Specific Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Time Formats

The country-specific format of times is determined by the fixed values of the [DDIC domain](../../abap-glossary/abendomain_glosry.md) `XUTIMEFM`. The mapping between countries and formats happens in a system table The following table shows the date formats represented by the fixed values of the domain, where *hh*, *mm*, and *ss* stand for hour, minute, and second. One 24-hour format and several 12-hour formats are available:

| **Fixed Value of `XUTIMEFM`** | **Date Format**                                          |
|-------------------------------|----------------------------------------------------------|
| blank                         | 24-hour format (default setting) `hh:mm:ss`              |
| *1*                           | 12-hour format (1 to 12) `hh:mm:ss AM` and `hh:mm:ss PM` |
| *2*                           | 12-hour format (1 to 12) `hh:mm:ss am` and `hh:mm:ss pm` |
| *3*                           | 12-hour format (0 to 11) `hh:mm:ss AM` and `hh:mm:ss PM` |
| *4*                           | 12-hour format (0 to 11) `hh:mm:ss am` and `hh:mm:ss pm` |

- The 24-hour format follows the ISO-8601 standard.

- The 12-hour formats are specific to certain English-speaking countries such as Australia, Canada, New Zealand, and the USA. `AM/am` stands for *Ante meridiem* (*before noon*) and `PM/pm` stands for *Post meridiem* (*after noon*).

- The formats for the values *1* and *2* or *3* and *4* differ only in the capitalization of `AM/PM` and `am/pm`.

- For the 12-hour formats of values *1* and *2*, midnight and noon are formatted as 12:00:00.

- For the 12-hour formats of values *3* and *2*, midnight and noon are formatted as 00:00:00.

The setting for the time format also affects the formatting of UTC time stamps in [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md).

## Hints

- All time formats are suitable for the representation of times. Only the 24-hour format is suitable for the representation of a duration, that is, the interval between two points in time. It does not make sense to use `AM/am` and `PM/pm` for a duration.

- The class `CL_ABAP_TIMEFM` contains helper methods for handling time formats.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output of a time and UTC time stamps with different time formats. By specifying a country that s available in the system table, the respective country-specific format is selected.

``` abap
cl_demo_output=>display( 
  |{ cl_demo_date_time=>get_user_time( )  COUNTRY = 'DE '   }\n{ 
     utclong_current( )                   COUNTRY = 'DE '   }| ).
```

## Executable Examples

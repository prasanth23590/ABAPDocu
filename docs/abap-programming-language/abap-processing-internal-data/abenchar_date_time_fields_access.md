---
title: "Access to Date Fields and Time Fields"
source_file: abenchar_date_time_fields_access.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date Fields and Time Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Access to Date Fields and Time Fields

Only in a few operand positions is it important that date fields and time fields contain a local date in the format *yyyymmdd* or a local time in the format *hhmmss*:

- When using date fields and time fields as source fields or target fields of a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md).

- In conversions of a local date and a local time to [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) using

  - [`CONVERT INTO UTCLONG`](abapconvert_date_utclong.md) and back using [`CONVERT UTCLONG`](abapconvert_utclong.md).

  - [`CONVERT INTO TIME STAMP`](abapconvert_date_time-stamp.md) and back using [`CONVERT TIME STAMP`](abapconvert_time-stamp.md).

- In output formatting using [string templates](abenstring_templates.md) or the statement `WRITE [TO]`

- When mapping to [asXML](../abap-data-interchange-formats/abenabap_xslt_asxml_elementary.md) or [JSON](../abap-data-interchange-formats/abenabap_asjson.md).

In all other operand positions, the handling of date fields and time fields is largely determined by the [conversion rules](abenconversion_elementary.md) and [comparison rules](../abap-program-flow-logic/abenlogexp_date_time.md) for these data types.

- The conversion rules are designed in such a way that data objects of the types `d` and `t` behave like character-like objects in character-like operand positions and numerically in numeric operand positions. In the latter case, the content of a date field is converted to the number of days since 01.01.0001 and the content of a time field is converted to the number of seconds since midnight.

- The comparison rules are designed so that a later date or later time is greater than an earlier date or earlier time.

Direct assignments or comparisons between the data types `d` and `t` do not make sense and are therefore forbidden. The following sections show examples of how to access date fields and time fields effectively.

- [Character-like access to date/time fields](abenchar_date_time_fields_charlike.md)

- [Numeric access to date/time fields](abenchar_date_time_fields_numlike.md)

## Hints

- The function modules of the function pool `SCAL` provide some additional information about character-like date specifications, for example the day of the week or the calendar week for a given date.

- Special [date functions and time functions](../../abap-dictionary-ddic/ddic-built-in-functions/abenddic_date_time_functions.md) can be used in the CDS DDL of the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) to process dates and times stored in database tables.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of an UTC time stamp to date and time fields and their type-friendly formatting using string templates.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
CONVERT UTCLONG utclong_current( ) 
        INTO DATE FINAL(date) 
             TIME FINAL(time) 
        TIME ZONE cl_demo_date_time=>get_user_time_zone( ). 
 
out->write( |{ date DATE = ISO 
                       }\n{ time TIME = ISO }| ). 
 
out->display( ).
```

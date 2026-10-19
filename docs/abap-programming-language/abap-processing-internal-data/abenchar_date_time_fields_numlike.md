---
title: "Numeric Access to Date Fields and Time Fields"
source_file: abenchar_date_time_fields_numlike.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date Fields and Time Fields > Access to Date Fields and Time Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Access to Date Fields and Time Fields

Numeric access to date fields and time fields exploits the fact that the [conversion](abenconversion_elementary.md) of the types `d` and `t` to numeric values produces an integer number of days or seconds. This applies particularly when using date fields and time fields in [numeric calculations](abencompute_expressions.md), where they are converted to the corresponding calculation type. This enables differences to be calculated or values to be added or subtracted from date fields or time fields. All other arithmetic operations are generally not useful here. To avoid unexpected results from such calculations, the [validity](abenchar_date_time_fields_validity.md) of the content of the date or time fields must be ensured.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following calculations provide the current day of the year as well as the hour, minutes, and seconds of the current time. The date and time are provided by an UTC time stamp.

``` abap
DATA: date      TYPE d, 
      time      TYPE t, 
      day       TYPE i, 
      hour      TYPE i, 
      minute    TYPE i, 
      second    TYPE i, 
      first_day TYPE d. 
 
FINAL(tzone) = cl_demo_date_time=>get_user_time_zone( ). 
CONVERT UTCLONG utclong_current( ) 
        INTO DATE date 
        TIME time 
        TIME ZONE tzone. 
 
first_day = date(4) && '0101'. 
day       = date - first_day + 1. 
second    = time. 
hour      = second DIV 3600. 
second    = second - hour * 3600. 
minute    = second DIV 60. 
second    = second - minute * 60.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following calculation provides the day of the week for a date field `date` containing any valid date. 1 means Monday, 2 means Tuesday, and so on.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
FINAL(day) = ( 5 + date  MOD 7 ) MOD 7 + 1. 
out->write( day ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following calculations provides the last day of the previous month.

``` abap
DATA(date) = cl_demo_date_time=>get_user_date( ). 
date+6(2) = '01'. 
date     = date - 1.
```

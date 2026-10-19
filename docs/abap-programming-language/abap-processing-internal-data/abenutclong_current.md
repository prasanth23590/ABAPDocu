---
title: "ts_func - utclong_current"
source_file: abenutclong_current.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamp Fields with Time Stamp Type > Time Stamp Functions (ts_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ts_func - utclong_current

## Syntax

``` abap
... utclong_current( ) ...  
```

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) creates a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) from the [system time](../../abap-glossary/abensystem_time_glosry.md) and the [system date](../../abap-glossary/abensystem_date_glosry.md) of an AS ABAP in accordance with [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md). The return value has the data type [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md).

## Hint

The precision of the decimal places of the created time stamp depends on the hardware (processor) of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md). Resolutions in the one-digit or two-digit microsecond range are realistic.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a table of UTC time stamps. Unlike the example [`GET TIME STAMP`](abapget_time-stamp.md), the time stamps do not need to be formatted differently in the output to be recognizable as such.

``` abap
DATA time_stamps TYPE TABLE OF utclong WITH EMPTY KEY. 
 
time_stamps = VALUE #( FOR i = 1 UNTIL i > 100 
                         ( utclong_current( ) ) ). 
 
cl_demo_output=>display( time_stamps ).
```

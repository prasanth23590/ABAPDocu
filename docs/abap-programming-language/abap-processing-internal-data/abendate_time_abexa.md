---
title: "Evaluating Date Fields and Time Fields"
source_file: abendate_time_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date Fields and Time Fields > Access to Date Fields and Time Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Evaluating Date Fields and Time Fields

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates calculations with date and time fields.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_data_date_time DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_data_date_time IMPLEMENTATION. 
  METHOD main. 
 
    DATA: ultimo  TYPE d, 
          t1      TYPE t VALUE '000000', 
          t2      TYPE t, 
          diff    TYPE i, 
          seconds TYPE i, 
          hours   TYPE i. 
 
    "date calculation 
 
    ultimo      = cl_demo_date_time=>get_user_date( ). 
    ultimo+6(2) = '01'. 
    ultimo     -= 1. 
    out->write( 
      |Last day of last month: { ultimo }| ). 
 
    "time calculation 
 
    t2 = cl_demo_date_time=>get_user_time( ). 
    diff = t2 - t1. 
    seconds = diff MOD 86400. 
    hours = seconds / 3600. 
    out->write( 
      |Number of hours since midnight: { hours }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the first part of the `main` method, the last day of the previous month is assigned to the date field `ultimo`. First, `ultimo` is filled with the current date. Then, the date is changed to the first day of the current month by specifying an offset. Finally, 1 is subtracted from `ultimo` so that the content of the field is changed to the last day of the previous month. Before the subtraction takes place, the system converts `ultimo` into the number of days since 01.01.0001 and converts the result back into a date.

In the second part, the number of hours between midnight and the current time are calculated. First, the difference between the time fields is calculated. The difference is then converted into the total number of seconds using the `MOD` operation. A positive difference remains unchanged. This step is only necessary for negative differences. Finally, the number of hours is calculated by dividing the number of seconds by 3600.

---
title: "string_tmpl - Time Zones"
source_file: abenstring_template_timezone_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Time Zones

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the formatting of an UTC time stamp using time zones.

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
CLASS cl_demo_str_template_timezones DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_timezones IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF timezone, 
             TimeZoneID   TYPE I_TimeZone-TimeZoneID, 
             TimeZoneText TYPE I_TimeZoneText-TimeZoneText, 
             datetime     TYPE string, 
           END OF timezone. 
 
    DATA: timezones TYPE TABLE OF timezone. 
 
    FIELD-SYMBOLS <timezone> TYPE timezone. 
 
    SELECT I_TimeZone~TimeZoneID, I_TimeZoneText~TimeZoneText 
           FROM I_TimeZone INNER JOIN I_TimeZoneText 
           ON I_TimeZone~TimeZoneID = I_TimeZoneText~TimeZoneID 
           WHERE I_TimeZone~TimeZoneID  NOT LIKE '%UTC%' AND 
                 I_TimeZoneText~Language = 'E' 
           INTO CORRESPONDING FIELDS OF TABLE @timezones 
           ##too_many_itab_fields. 
 
    FINAL(ts) = utclong_current( ). 
 
    LOOP AT timezones ASSIGNING <timezone>. 
      <timezone>-datetime = |{ ts TIMEZONE  = <timezone>-TimeZoneID 
                                  TIMESTAMP = USER }|. 
    ENDLOOP. 
 
    SORT timezones BY datetime. 
 
    out->write( 'Timezones Around the World' 
      )->write( timezones ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

All time zones with a geographical reference are read from the database table `TTZZ` into an internal table. An UTC time stamp is created in a time stamp field and, formatted using each of this time zones, and written to the internal table. The internal table is sorted and displayed in accordance with the formatted time stamp.

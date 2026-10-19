---
title: "itab - Index Access with Key"
source_file: abenmodify_itab_using_key_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab > MODIFY itab, itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Index Access with Key

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows an index access to a hashed table.

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
CLASS cl_demo_modify_table_using_key DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_modify_table_using_key IMPLEMENTATION. 
  METHOD main. 
    DATA: sflight_tab TYPE HASHED TABLE 
                      OF sflight 
                      WITH UNIQUE KEY primary_key 
                        COMPONENTS carrid connid fldate 
                      WITH NON-UNIQUE SORTED KEY plane_type 
                        COMPONENTS planetype, 
          sflight_wa  LIKE LINE OF sflight_tab, 
          count       TYPE i. 
 
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED 
           FROM sflight 
           WHERE carrid = 'LH' 
           INTO TABLE @sflight_tab. 
 
    LOOP AT sflight_tab INTO sflight_wa USING KEY plane_type 
                                        WHERE planetype = 'A310-300'. 
      sflight_wa-seatsmax += 20. 
      MODIFY sflight_tab INDEX sy-tabix 
                         USING KEY loop_key 
                         FROM  sflight_wa 
                         TRANSPORTING seatsmax. 
      IF sy-subrc = 0. 
        count += 1. 
      ENDIF. 
    ENDLOOP. 
 
    out->write( |{ count } flights modified| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `sflight_tab` is a hashed table with a unique primary key and a non-unique secondary sorted key. Since a secondary sorted key is specified in the statement `MODIFY` after `USING KEY`, it is possible to access the hashed table using the associated secondary table index.

This example only demonstrates the syntax. Generally, instead of using the statement `MODIFY`, modifications of this type should be made using a field symbol or a data reference:

``` abap
LOOP AT sflight_tab ASSIGNING <sflight_wa> USING KEY plane_type 
                    WHERE planetype = 'A310-300'. 
  <sflight_wa>-seatsmax = <sflight_wa>-seatsmax + 20. 
ENDLOOP.
```

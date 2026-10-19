---
title: "SELECT, Dynamic Query Clauses"
source_file: abendynamic_select_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Dynamic Query Clauses

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how [`SELECT`](abapselect.md) statements can be specified fully dynamically in a string.

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
CLASS cl_demo_dynamic_select_cloud DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_dynamic_select_cloud IMPLEMENTATION. 
  METHOD main. 
    DATA(key) = `UA`. 
    FINAL(in) = cl_demo_input=>new( ). 
    in->request( CHANGING field = key ). 
 
    DATA(dynamic_select) = `SELECT * FROM spfli WHERE carrid = ` && 
                            cl_abap_dyn_prg=>quote( to_upper( key ) ). 
 
    DATA: 
      result TYPE TABLE OF spfli WITH EMPTY KEY. 
 
    TRY. 
 
        WITH 
          (dynamic_select) 
            INTO TABLE @result. 
 
 
      CATCH cx_sy_dynamic_osql_semantics INTO FINAL(exc1). 
        out->write( exc1->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A [`SELECT`](abapselect.md) statement and all clauses in front of the [`INTO`](abapinto_clause.md) clause can be specified dynamically as the content of a string. For security reasons, only a part of the string can be passed from the outside and is checked by a method of `CL_ABAP_DYN_PRG`.

In ABAP SQL, a dynamic `SELECT` statement can be used in the dynamic form of the statement [`WITH`](abapwith.md).

## Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

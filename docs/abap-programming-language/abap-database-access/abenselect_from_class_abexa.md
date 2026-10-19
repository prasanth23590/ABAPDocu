---
title: "SELECT, Class Attribute as Data Source of a Query"
source_file: abenselect_from_class_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM @itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Class Attribute as Data Source of a Query

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an attribute of a class is accessed using an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md).

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
CLASS cl_demo_select_from_class DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_from_class IMPLEMENTATION. 
  METHOD main. 
    FINAL(join) = NEW cl_demo_scarr_spfli( ). 
 
    SELECT * 
           FROM @join->scarr_spfli_tab AS scarr_spfli 
           WHERE cityfrom = 'FRANKFURT' 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class `CL_DEMO_SCARR_SPFLI` has a tabular attribute `SCARR_SPFLI_TAB` that is filled with joined data from the database in its constructor. The above class reads data from this attribute with a `SELECT` statement in the same way as it would read from a CDS view.

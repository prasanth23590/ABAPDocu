---
title: "table_exp - Default Value"
source_file: abentable_exp_default_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp) > table_exp - default"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Default Value

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates default values for table expressions.

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
CLASS cl_demo_tab_exp_default DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_tab_exp_default IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line, 
        id    TYPE i, 
        value TYPE string, 
      END OF line, 
      itab TYPE SORTED TABLE OF line WITH UNIQUE KEY id. 
 
    FINAL(def) = VALUE line( id = 0 value = `not found` ). 
 
    FINAL(itab) = VALUE itab( ( id = 3 value = `CCC` ) 
                             ( id = 4 value = `DDD` ) 
                             ( id = 5 value = `EEE` ) ). 
 
    FINAL(result1) = VALUE #( itab[ id = 1 ] DEFAULT def ). 
    out->write( result1 ). 
 
 
    FINAL(result2) = VALUE #( itab[ id = 1 ]-value DEFAULT def-value ). 
    out->write_data( result2 ). 
 
    FINAL(result3) = VALUE #( itab[ id = 1 ] DEFAULT VALUE #( 
                             itab[ id = 2 ] DEFAULT VALUE #( 
                             itab[ id = 3 ] OPTIONAL ) ) ). 
    out->write_data( result3 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The result `result1` of the first table expression has the line type of the internal table `itab`. The specified line is not found, which means that the structure `def` specified after `DEFAULT` is returned instead.

The result `result2` of the second table expression results from a chaining with the structure component selector and is a component with the type `string`. Here, only the corresponding component of the structure `def` is specified as the default value.

The result `result3` of the third table expression again has the line type of the internal table `itab`. Further table expressions with default values are specified as the default value. In the case shown here, the table expression in the second default value finds a line and returns it. If no searches are successful, an initial line is returned due to the closing `OPTIONAL`.

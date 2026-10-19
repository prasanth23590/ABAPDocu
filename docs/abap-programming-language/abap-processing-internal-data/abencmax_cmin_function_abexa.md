---
title: "cstring_func - cmax, cmin, and segment"
source_file: abencmax_cmin_function_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - cmax, cmin, and segment

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the extremum functions [`cmax`](abencmax_cmin_functions.md) and [`cmin`](abennmax_nmin_functions.md), plus the segment function [`segment`](abensegment_functions.md).

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
CLASS cl_demo_cmax_cmin DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cmax_cmin IMPLEMENTATION. 
  METHOD main. 
    DATA: txt TYPE string, 
          max TYPE string, 
          min TYPE string, 
          msg TYPE string. 
    txt = `one two three four five six seven eight nine ten`. 
    max = ` `. 
    min = `&#x00A7;` ##STRING_OK. 
    DO. 
      TRY. 
          max = cmax( val1 = max 
                      val2 = segment( val   = txt 
                                      index = sy-index sep = ` ` ) ). 
          min = cmin( val1 = min 
                      val2 = segment( val   = txt 
                                      index = sy-index sep = ` ` ) ). 
        CATCH cx_sy_strg_par_val. 
          EXIT. 
      ENDTRY. 
    ENDDO. 
    out->write( 
      |Maximum is { max } and minimum is { min }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This class determines the minimum and the maximum segment of a character string with respect to the current [code page](../../abap-glossary/abencodepage_glosry.md).

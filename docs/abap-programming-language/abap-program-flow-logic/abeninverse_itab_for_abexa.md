---
title: "Inverse Reads on Internal Table without STEP"
source_file: abeninverse_itab_for_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > FOR, Iteration Expressions > Examples of Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Inverse Reads on Internal Table without STEP

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) implemented by a conditional iteration.

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
CLASS cl_demo_for_reverse_iteration DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_reverse_iteration IMPLEMENTATION. 
  METHOD main. 
    DATA 
      itab TYPE STANDARD TABLE OF i 
           WITH EMPTY KEY 
           WITH NON-UNIQUE SORTED KEY sort_key COMPONENTS table_line. 
 
    itab = VALUE #( ( 2 ) ( 5 ) ( 1 ) ( 3 ) ( 4 ) ). 
 
    FINAL(output) = 
      REDUCE string( 
        INIT o = `` 
        FOR  i = lines( itab ) THEN i - 1 WHILE i > 0 
        NEXT o &&= COND #( LET r = itab[ KEY sort_key INDEX i ] IN 
                           WHEN r > 2 THEN r && ` ` ) ). 
 
    out->write( output ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows how an inverse [table iteration](../abap-processing-internal-data/abenfor_itab.md) could be performed by an iteration expression accessing a table expression before the addition [`STEP`](../abap-processing-internal-data/abenfor_cond.md) was introduced for direct table iterations.

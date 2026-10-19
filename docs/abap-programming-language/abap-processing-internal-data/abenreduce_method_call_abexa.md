---
title: "itab - Table Reduction, Method Calls"
source_file: abenreduce_method_call_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Reductions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Reduction, Method Calls

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a [reduction](../abap-program-flow-logic/abenconstructor_expression_reduce.md) of the columns of an internal table to an object.

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
CLASS cl_demo_reduce_method_call DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS to_string IMPORTING wa          TYPE scarr 
                      RETURNING VALUE(text) TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_method_call IMPLEMENTATION. 
  METHOD main. 
    DATA carriers TYPE TABLE OF scarr. 
    SELECT * FROM scarr INTO TABLE @carriers. 
 
    DATA o TYPE REF TO if_demo_output. 
    o = REDUCE #( 
            INIT o1 = out 
            FOR wa IN carriers 
            NEXT o1 = o1->write( to_string( wa ) ) ). 
  ENDMETHOD. 
  METHOD to_string. 
    DO. 
      ASSIGN wa-(sy-index) TO FIELD-SYMBOL(<wa>). 
      IF sy-subrc <> 0. 
        EXIT. 
      ENDIF. 
      FINAL(olen) = CAST cl_abap_elemdescr( 
          cl_abap_typedescr=>describe_by_data( <wa> ) )->output_length. 
      text = |{ text }{ CONV string( <wa> ) WIDTH = olen + 2 }|. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, a call of a method `to_string` transforms the lines of the internal table `carriers` after the [`FOR` expression](abenfor_in_itab.md) to a text string. This string is then passed to the instance method `WRITE` of an object of the class `CL_DEMO_OUTPUT`. This object is created after `INIT` and referenced by the local reference variable `o`. The return value of the method `WRITE` returns a reference to its own object, which means that the assignment to `o` does not modify its value but meets the syntax rule that `o` must be filled. At the end of processing, the reference to the object in `o` is assigned to the reference variable `out` and the content of the internal table written to the object can be displayed using the method `DISPLAY`.

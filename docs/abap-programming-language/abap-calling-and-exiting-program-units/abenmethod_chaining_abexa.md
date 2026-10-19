---
title: "Method Chaining"
source_file: abenmethod_chaining_abexa.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls > ... meth1( ... )->meth2( ... )->..., Method Chaining"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Method Chaining

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates method chaining in an operand position.

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
CLASS cl_demo_method_chaining DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS meth  IMPORTING str        TYPE string 
                  RETURNING VALUE(ref) 
                              TYPE REF TO cl_demo_method_chaining. 
    DATA text TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_method_chaining IMPLEMENTATION. 
  METHOD main. 
    out->write( 
      NEW cl_demo_method_chaining( )->meth( 
        `Hello ` )->meth( `world` )->meth( `!` )->text ). 
  ENDMETHOD. 
  METHOD meth. 
    text &&= str. 
    ref = me. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the actual parameter passed to the method `DISPLAY_TEXT`, [chained attribute access](../../abap-glossary/abenchained_attribute_acc_glosry.md) is applied to the attribute `text` of the class `demo`. The attribute is changed using three chained method calls.

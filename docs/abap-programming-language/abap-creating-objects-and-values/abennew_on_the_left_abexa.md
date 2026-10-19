---
title: "Instance Operator NEW on the Left"
source_file: abennew_on_the_left_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator > NEW, Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Instance Operator NEW on the Left

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Constructor expression with `NEW` on the left side of an expression.

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
CLASS cl_demo_new_on_the_left DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS class DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS frame DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA oref TYPE REF TO class. 
ENDCLASS. 
 
CLASS class IMPLEMENTATION. 
  METHOD constructor. 
    frame=>oref = me. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_new_on_the_left IMPLEMENTATION. 
  METHOD main. 
 
    NEW class( )->attr = 'foo'. 
    out->write( frame=>oref->attr ). 
 
    TRY. 
        NEW class( )->('attr') = 'foo'. 
        out->write( frame=>oref->attr ). 
        NEW class( )->('foo') = 'foo'. 
        out->write( frame=>oref->attr ). 
      CATCH cx_sy_assign_illegal_component INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Although the reference variable only exists during the statement, the reference to the object is assigned to the reference variable `user=>oref` in the constructor of the class `class`, thus preserving the object. The example also shows dynamic specifications and the exception that is raised in case of an invalid attribute.

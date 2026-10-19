---
title: "Case Distinction CASE TYPE OF for RTTI"
source_file: abencase_type_of_rtti_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Branches > CASE TYPE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Case Distinction CASE TYPE OF for RTTI

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the case distinction [`CASE TYPE OF`](abapcase_type.md) for type description classes.

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
CLASS cl_demo_case_type_of_rtti DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS meth IMPORTING param TYPE any. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_case_type_of_rtti IMPLEMENTATION. 
  METHOD main. 
    DATA: elem TYPE i, 
          BEGIN OF struc, 
            comp1 TYPE i, 
            comp2 TYPE i, 
          END OF struc, 
          itab LIKE STANDARD TABLE OF struc WITH EMPTY KEY, 
          dref TYPE REF TO i. 
 
    meth( elem ). 
    meth( struc ). 
    meth( itab ). 
    meth( dref ). 
 
  ENDMETHOD. 
  METHOD meth. 
    FINAL(typedescr) = cl_abap_typedescr=>describe_by_data( param ). 
    CASE TYPE OF typedescr. 
      WHEN TYPE cl_abap_elemdescr INTO FINAL(elemdescr). 
        out->write( elemdescr->type_kind ). 
      WHEN TYPE cl_abap_structdescr INTO FINAL(structdescr). 
        out->write( structdescr->components ). 
      WHEN TYPE cl_abap_tabledescr INTO FINAL(tabledescr). 
        out->write( tabledescr->table_kind ). 
      WHEN OTHERS. 
        out->write( 'Not supported' ). 
    ENDCASE. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Actual parameters of different types are passed to the generically typed parameter `param` of the method `main`, and an [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) [type description object](../../abap-glossary/abentype_object_glosry.md) is created, to which the general object reference variable `typedescr` points. The case distinction [`CASE TYPE OF`](abapcase_type.md) is used to determine a more specific suitable RTTI type description class. An inline declaration after the addition `INTO` of the statement `WHEN TYPE` is used to create an object reference variable of this static type and assign the reference to the type description object. Special attributes of the type description objects are accessed in the associated statement blocks.

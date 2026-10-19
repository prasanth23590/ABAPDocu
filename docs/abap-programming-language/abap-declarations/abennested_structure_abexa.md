---
title: "Declaration of a Nested Structure"
source_file: abennested_structure_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA > DATA, BEGIN OF struc"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Declaration of a Nested Structure

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the declaration of a nested structure with substructures.

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
CLASS cl_demo_nested_structure DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_nested_structure IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      BEGIN OF address, 
        BEGIN OF name, 
          title   TYPE string VALUE `Mr.`, 
          prename TYPE string VALUE `Duncan`, 
          surname TYPE string VALUE `Pea`, 
        END OF name, 
        BEGIN OF street, 
          name   TYPE string VALUE `Vegetable Lane`, 
          number TYPE string VALUE `11`, 
        END OF street, 
        BEGIN OF city, 
          zipcode TYPE string VALUE `349875`, 
          name    TYPE string VALUE `Botanica`, 
        END OF city, 
      END OF address. 
    out->write( address-name 
      )->write( address-street 
      )->write( address-city ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Declaration of a nested local structure `address` with three structured components. When the method `DISPLAY` of class `CL_DEMO_OUTPUT` is called, each substructure is addressed using the structure component selector (`-`).

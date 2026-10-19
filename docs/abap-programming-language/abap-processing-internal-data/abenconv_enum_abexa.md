---
title: "Conversion Operator, Enumerated Types"
source_file: abenconv_enum_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > CONV, Conversion Operator > CONV, Conversion of Enumerated Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Operator, Enumerated Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the conversion operator [`CONV`](abenconstructor_expression_conv.md) for enumerated types.

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
CLASS cl_demo_conv_enum DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_conv_enum IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF ENUM planet, 
        mercury, 
        venus, 
        earth, 
        mars, 
        jupiter, 
        saturn, 
        uranus, 
        neptune, 
      END OF ENUM planet. 
 
    DATA number TYPE i. 
    cl_demo_input=>new( )->request( CHANGING field = number ). 
 
    TRY. 
        FINAL(planet) = CONV planet( CONV i( earth ) + number ). 
        out->write( planet ). 
      CATCH cx_sy_conversion_no_enum_value. 
        out->write( 'Enter a number between -2 and 5' ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The inner conversion operator [`CONV`](abenconstructor_expression_conv.md) return the value of the enumerated constant `earth` in the base type `i` of the [enumerated type](../../abap-glossary/abenenum_type_glosry.md) `planet`. An input value is added to this. Applying the conversion operator to the result determines a planet, which has the specified distance of `earth`.

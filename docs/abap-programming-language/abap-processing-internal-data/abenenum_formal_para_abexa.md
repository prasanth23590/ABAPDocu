---
title: "enum, Parameter Passing"
source_file: abenenum_formal_para_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Enumerated Objects (enum)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# enum, Parameter Passing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the passing [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) to a method.

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
CLASS cl_demo_enum_para_pass DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
 
  PRIVATE SECTION. 
    METHODS meth 
      IMPORTING 
        VALUE(psimple) TYPE simple 
        VALUE(penum)   TYPE demo_cds_enum_weekday . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_enum_para_pass IMPLEMENTATION. 
  METHOD main. 
    meth( psimple = demo_cds_enum_weekday-sat 
          penum   = demo_cds_enum_weekday-fri ). 
  ENDMETHOD. 
  METHOD meth. 
*    IF psimple = demo_cds_enum_weekday-mon. "Syntax error 
*      out->write( `Sunday Bloody Sunday` ). 
*    ENDIF. 
    psimple = demo_cds_enum_weekday-mon. 
    FIELD-SYMBOLS <enum> TYPE demo_cds_enum_weekday. 
    ASSIGN psimple TO <enum>. 
    IF <enum> = demo_cds_enum_weekday-mon. 
      out->write( `I Don't Like Mondays` ). 
    ENDIF. 
    IF penum = demo_cds_enum_weekday-fri. 
      out->write( `Thank God It's Friday` ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `meth` has a parameter `psimple` of generic type `simple` and a parameter `penum` of CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`. Enumerated objects of this enumerated type can be passed to both. `psimple` cannot be used in a comparison where the other operand is an enumerated object. But it is possible to use `psimple` at a write position and to assign it to a field symbol that is typed with the enumerated type and use that in the comparison. Note that the assignment to the field symbol works since the operand position after `ASSIGN` is not handled as a read position.

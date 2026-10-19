---
title: "CDS DDL - CDS Enumerated Type, Type Description"
source_file: abencds_enum_description_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Enumerated Types > CDS DDL - DEFINE TYPE ENUM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Enumerated Type, Type Description

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates type description for CDS enumerated types.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Class that uses RTTI to evaluate a CDS 
"! enumerated type</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cds_enum_type DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_enum_type IMPLEMENTATION. 
  METHOD main. 
    TYPES my_type TYPE demo_cds_enum_weekday. 
 
    FINAL(descr) = cl_abap_enumdescr=>describe_by_name( 
      'DEMO_CDS_ENUM_WEEKDAY' ). 
 
    out->next_section( 'CL_ABAP_ENUMDESCR' 
    )->write( descr ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The type description class `CL_ABAP_ENUMDESCR` returns properties of the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`.

---
title: "enum, Type Description"
source_file: abenenum_description_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Enumerated Objects (enum)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# enum, Type Description

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates type description for [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md).

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
CLASS cl_demo_rtti_enums DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rtti_enums IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: 
      BEGIN OF ENUM size, 
        s, m, l, xl, xxl, 
      END OF ENUM size. 
 
    FINAL(size) = VALUE size( ). 
 
    out->next_section( 'CL_ABAP_ENUMDESCR' ). 
 
    FINAL(enum_descr) = CAST cl_abap_enumdescr( 
      cl_abap_typedescr=>describe_by_data( size ) ). 
 
    out->write_data( enum_descr->kind 
      )->write_data( enum_descr->type_kind 
      )->write_data( enum_descr->base_type_kind 
      )->write_data( enum_descr->members ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The type description class `CL_ABAP_ENUMDESCR` return properties of an enumerated variable `size` of an identically named enumerated type.

See also [CDS Enumerated Type, Type Description](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_enum_description_abexa.md)

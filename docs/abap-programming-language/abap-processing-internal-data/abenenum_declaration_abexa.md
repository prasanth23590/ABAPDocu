---
title: "enum, Declaration"
source_file: abenenum_declaration_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Enumerated Objects (enum)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# enum, Declaration

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the declaration of [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md).

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
CLASS cl_demo_declare_enums DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_declare_enums IMPLEMENTATION. 
  METHOD main. 
 
    out->next_section( 'ABAP Enumerated Type' ). 
 
    "ABAP enumerated type with enumerated structure 
    TYPES: 
      BEGIN OF ENUM abap_wd STRUCTURE abap_wd BASE TYPE int1, 
        mon, 
        tue, 
        wed, 
        thu, 
        fri, 
        sat, 
        sun, 
      END OF ENUM abap_wd STRUCTURE abap_wd. 
 
    "Addressing the enumerated structure and its components 
    DATA abap_wd_struc LIKE abap_wd. 
    out->write( abap_wd 
      )->write( abap_wd-fri 
      )->write( abap_wd_struc 
      )->write( abap_wd_struc-fri ). 
 
    "Declaring an enumerated variable of the ABAP enumerated type 
    DATA wd_abap TYPE abap_wd. 
    "Assigning an enumerated constant 
    wd_abap = abap_wd-tue. 
    "Assigning an enumerated constant to an inline declaration 
    FINAL(wd_abap_wed) = abap_wd-wed. 
    "Assigning enumerated constants to the variable structure 
    abap_wd_struc = abap_wd. 
    out->write( wd_abap 
      )->write( wd_abap_wed 
      )->write( abap_wd_struc ). 
 
    out->next_section( 'CDS Enumerated Type' ). 
 
    "Addressing the enumerated structure and its components 
    "DATA cds_wd_struc LIKE demo_cds_enum_weekday. "Syntax error 
    out->write( demo_cds_enum_weekday 
      )->write( demo_cds_enum_weekday-fri ). 
    DATA cds_wd_struc LIKE demo_cds_enum_weekday. "No syntax error 
    out->write( cds_wd_struc 
      )->write( cds_wd_struc-fri ). 
 
    "Declaring an enumerated variable of the CDS enumerated type 
    DATA wd_cds TYPE demo_cds_enum_weekday. 
    "Assigning an enumerated constant 
    wd_cds = demo_cds_enum_weekday-tue. 
    "Assigning an enumerated constant to an inline declaration 
    FINAL(wd_cds_wed) = demo_cds_enum_weekday-wed. 
    "Assigning enumerated constants to the variable structure 
    cds_wd_struc = CORRESPONDING #( demo_cds_enum_weekday ). 
    out->write( wd_cds 
      )->write( wd_cds_wed 
      )->write( cds_wd_struc ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example shows enumerated objects defined with reference to an [ABAP enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) and to an [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md):

- ABAP enumerated type

  - The ABAP enumerated type `abap_wd` is defined with an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) that has the same name.

  - The enumerated structure `abap_wd` is created by the declaration and can be referred to by `LIKE` to create a second structure with the same components. The second structure is not a constant structure.

  - The components of the constant structure `abap_wd` contain the [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type.

  - The components of the variable structure declared by `LIKE` contain their initial value 0 or `MON` respectively.

  - A variable `wd_abap` is declared with reference to the ABAP enumerated type and assigned the enumerated constant `abap_wd-tue`.

  - An [immutable variable](../../abap-glossary/abenimmutable_variable_glosry.md) `wd_abap_wed` is declared inline and assigned the enumerated constant `abap_wd-wed`.

  - The enumerated constant structure `abap_wd` is assigned to the variable structure `abap_wd_struc` declared by `LIKE`. Each component is assigned a different enumerated constant.

- CDS enumerated type

  The CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY` is defined as follows:

``` abap
@EndUserText.label: 'Days of the week' 
define type DEMO_CDS_ENUM_WEEKDAY : abap.int1 enum 
{  
  @EndUserText.label: 'Monday' 
  MON = initial; 
  @EndUserText.label: 'Tuesday' 
  TUE =       1; 
  @EndUserText.label: 'Wednesday' 
  WED =       2; 
  @EndUserText.label: 'Thursday' 
  THU =       3; 
  @EndUserText.label: 'Friday' 
  FRI =       4; 
  @EndUserText.label: 'Saturday' 
  SAT =       5; 
  @EndUserText.label: 'Sunday' 
  SUN =       6; 
} 
 
 
```

``` abap
It can be used in ABAP in the same way as the ABAP enumerated type with two major differences:
```

- The enumerated structure `demo_cds_enum_weekday` is created with the first read access. It cannot be used after `LIKE` before it is used for the first time.

- The components of the enumerated structure `demo_cds_enum_weekday` are ordered alphabetically and not according to the definition.

Note that only enumerated constants or variables with the same enumerated type are assigned to enumerated variables.

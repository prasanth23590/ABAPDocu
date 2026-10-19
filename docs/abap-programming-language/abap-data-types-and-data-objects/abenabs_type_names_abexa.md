---
title: "Absolute Type Names, Executable Example"
source_file: abenabs_type_names_abexa.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Absolute Type Names"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Absolute Type Names, Executable Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the composition of [absolute type names](../../abap-glossary/abenabsolute_typename_glosry.md).

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
CLASS cl_demo_absolute_type_names DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
 
  PRIVATE SECTION. 
    TYPES struc TYPE scarr. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_absolute_type_names IMPLEMENTATION. 
  METHOD main. 
 
    TYPES itab  TYPE TABLE OF scarr. 
 
    DATA dref TYPE REF TO data. 
 
 
    DATA(struc_type) = 
      `\class=cl_demo_absolute_type_names` && 
      `\type=struc`. 
    TRY. 
        CREATE DATA dref TYPE (struc_type). 
        dref->* =  VALUE scarr( carrid = 'CC' ). 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO DATA(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    DATA(comp_type) = 
      `\class=cl_demo_absolute_type_names` && 
      `\type=struc-carrid`. 
    TRY. 
        CREATE DATA dref TYPE (comp_type). 
        dref->* =  'XX'. 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    DATA(line_type) = 
      `\class=cl_demo_absolute_type_names` && 
      `\method=main\type=itab\line`. 
    TRY. 
        CREATE DATA dref TYPE (line_type). 
        dref->* = VALUE scarr( carrid = 'YY' ). 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    comp_type = 
      `\class=cl_demo_absolute_type_names` && 
      `\method=main\type=itab\line-carrid`. 
    TRY. 
        CREATE DATA dref TYPE (comp_type). 
        dref->* =  'ZZ'. 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    comp_type = 
      `\type=spfli-carrid`. 
    TRY. 
        CREATE DATA dref TYPE (comp_type). 
        dref->* =  'DDX'. 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    line_type = 
      `\type=spfli_key_tab\line`. 
    TRY. 
        CREATE DATA dref TYPE (line_type). 
        dref->* = VALUE spfli( carrid = 'DDY' ). 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    comp_type = 
      `\type=spfli_key_tab\line-carrid`. 
    TRY. 
        CREATE DATA dref TYPE (comp_type). 
        dref->* =  'DDZ'. 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO exc. 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The following absolute type names are composed and used for creating [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) with dynamic type specifications:

- `\class=cl_demo_absolute_type_names\type=struc`

  Specifies the structured type `struc` of class `CL_DEMO_ABSOLUTE_TYPE_NAMES`.

- `\class=cl_demo_absolute_type_names\type=struc-carrid`

  Specifies the type of the component `carrid` of the structured type `struc` of class `CL_DEMO_ABSOLUTE_TYPE_NAMES`.

- `\class=cl_demo_absolute_type_names\method=main\type=itab\line`

  Specifies the line type of the tabular type `itab` defined in method `MAIN` of class `CL_DEMO_ABSOLUTE_TYPE_NAMES`.

- `\class=cl_demo_absolute_type_names\method=main\type=itab\line-carrid`

  Specifies the type of the component `carrid` of the tabular type `itab` defined in method `MAIN` of class `CL_DEMO_ABSOLUTE_TYPE_NAMES`.

- `\type=spfli-carrid`

  Specifies the type of the component `carrid` of the [DDIC structure](../../abap-glossary/abenddic_structure_glosry.md) `SPFLI`.

- `\type=spfli_key_tab\line`

  Specifies the line type of the [DDIC table type](../../abap-glossary/abenddic_table_type_glosry.md) `SPFLI_KEY_TAB`.

- `\type=spfli_key_tab\line-carrid`

  Specifies the type of the component `carrid` of the line type of the [DDIC table type](../../abap-glossary/abenddic_table_type_glosry.md) `SPFLI_KEY_TAB`.

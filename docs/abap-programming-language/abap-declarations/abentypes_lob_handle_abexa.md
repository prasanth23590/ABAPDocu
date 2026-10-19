---
title: "Deriving LOB Handle Structures"
source_file: abentypes_lob_handle_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, LOB HANDLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Deriving LOB Handle Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how [LOB handle structures](../../abap-glossary/abenlob_handle_structure_glosry.md) are derived using the statement [`TYPES`](abaptypes_lob_handle.md).

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
CLASS cl_demo_types_lob_handle DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      lob_handle_structure_1 TYPE demo_lob_table 
                             READER FOR COLUMNS clob1 blob1, 
      lob_handle_structure_2 TYPE demo_lob_table 
                             LOB HANDLE FOR ALL COLUMNS, 
      lob_handle_structure_3 TYPE demo_lob_table 
                             LOCATOR FOR ALL BLOB COLUMNS 
                             WRITER FOR ALL CLOB COLUMNS, 
      lob_handle_structure_4 TYPE demo_lob_table 
                             READER FOR COLUMNS clob1 clob2 
                             LOB HANDLE FOR ALL BLOB COLUMNS 
                             LOCATOR FOR ALL OTHER CLOB COLUMNS, 
      lob_handle_structure_5 TYPE demo_lob_table 
                             READER FOR COLUMNS blob1 blob2 blob3 
                             LOCATOR FOR COLUMNS clob1 clob2 clob3 
                             LOB HANDLE FOR ALL OTHER COLUMNS, 
      lob_handle_structure_6 TYPE demo_lob_table 
                             READER FOR COLUMNS blob1 
                             LOCATOR FOR COLUMNS blob2 
                             LOB HANDLE FOR COLUMNS blob3 
                             LOB HANDLE FOR ALL CLOB COLUMNS. 
 
  PRIVATE SECTION. 
    METHODS output_type IMPORTING struct TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_types_lob_handle IMPLEMENTATION. 
  METHOD main. 
    DO 6 TIMES. 
      output_type( |LOB_HANDLE_STRUCTURE_{ sy-index }| ). 
    ENDDO. 
  ENDMETHOD. 
  METHOD output_type. 
 
    TYPES: BEGIN OF result, 
             component_name TYPE string, 
             absolute_name  TYPE string, 
           END OF result, 
           results TYPE TABLE OF result WITH EMPTY KEY. 
 
    out->next_section( struct 
      )->write_data( 
           VALUE results( 
             FOR component IN CAST cl_abap_structdescr( 
               cl_abap_structdescr=>describe_by_name( struct ) 
                 )->components 
             WHERE ( type_kind = cl_abap_typedescr=>typekind_oref ) 
             ( VALUE #( 
                 component_name = component-name 
                 absolute_name  = CAST cl_abap_refdescr( 
                   cl_abap_typedescr=>describe_by_name( 
                     struct && `-` && component-name ) 
                       )->get_referenced_type( 
                       )->absolute_name ) ) ) ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The package-visible area of the class `demo_lob_handles` contains different derivations of LOB handle structures from the database table `DEMO_LOB_TABLE`. The methods of this class are used to output of the static type of the derived [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md).

The `DEMO_LOB_TABLE` database table contains a key field of type `INT4`, as well as three columns `CLOB1`, `CLOB2`, `CLOB3` of type `STRING` and three columns `BLOB1`, `BLOB2`, `BLOB3` of type `RAWSTRING`.

The derivations listed here work as follows:

- In the structured type `lob_handle_structure_1`, `clob1` and `blob1` become LOB handle components by column specifications directly after `READER`. The component `clob1` contains the static type `CL_ABAP_DB_C_READER` and `blob1` contains the static type `CL_ABAP_DB_X_READER`. All other components are represented in accordance with the [regular rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) for their built-in types.

- In the structured type `lob_handle_structure_2`, all LOB components are converted into LOB handle components by specifying `FOR ALL COLUMNS`. The static type of the components of type `STRING` is `IF_ABAP_DB_CLOB_HANDLE` and the static type for the components of type `RAWSTRING` is `IF_ABAP_DB_BLOB_HANDLE`.

- In the structured type `lob_handle_structure_3`, all LOB components are converted into LOB handle components. The static type of the components of type `STRING` is converted into `CL_ABAP_DB_C_WRITER` by specifying `WRITER FOR ALL CLOB COLUMNS` and the static type for the components of type `RAWSTRING` is converted into `CL_ABAP_DB_X_LOCATOR` by specifying `LOCATOR FOR ALL BLOB COLUMNS`.

- In the structured type `lob_handle_structure_4`, all LOB components are converted into LOB handle components. The static type of the components `clob1` and `clob2` is converted into `CL_ABAP_DB_C_READER` by specifying `READER` directly. All components of the type `RAWSTRING` are converted into reference types for `IF_ABAP_DB_BLOB_HANDLE` by specifying `LOB HANDLE FOR ALL BLOB COLUMNS`. The remaining components of the type `STRING` are converted into reference types for `CL_ABAP_DB_C_LOCATOR` by specifying `LOCATOR FOR ALL OTHER CLOB COLUMNS`.

- In the structured type `lob_handle_structure_5`, all LOB components are listed directly, and thus converted into the corresponding LOB handle components with the static types `CL_ABAP_DB_C_LOCATOR` for `clob1`, `clob2`, and `clob3` and `CL_ABAP_DB_X_READER` for `blob1`, `blob2`, and `blob3`. The specification `LOB HANDLE FOR ALL OTHER COLUMNS` has no direct effect, but only affects any enhancements to the database table with further LOBs, which then preserve their type-compliant interface reference type.

- In the structured type `lob_handle_structure_6`, all LOB components are converted into handle LOB components, whereby here the maximum number of column specifications is demonstrated. `FOR ALL CLOB COLUMNS` can only be specified since no components of type `STRING` were covered by previous statements.

---
title: "Variants of MOVE-CORRESPONDING and the CORRESPONDING Operator Using Deep Structures"
source_file: abencorresponding_variants_s_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Variants of MOVE-CORRESPONDING and the CORRESPONDING Operator Using Deep Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates variants of statements with [`MOVE-CORRESPONDING`](abapmove-corresponding.md) and the [`CORRESPONDING`](abenconstructor_expr_corresponding.md) operator using [deep structures](../../abap-glossary/abendeep_structure_glosry.md).

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
CLASS cl_demo_crrspndng_variants_st DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF line1, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF line1, 
           BEGIN OF line2, 
             col2 TYPE i, 
             col3 TYPE i, 
             col4 TYPE i, 
           END OF line2. 
    DATA: 
      "deep structures 
      BEGIN OF struc1, 
        comp1 TYPE c LENGTH 1 VALUE 'W', 
        BEGIN OF struc_nested, 
          comp1 TYPE c LENGTH 1 VALUE 'X', 
          BEGIN OF comp2, 
            col1 TYPE c LENGTH 1 VALUE 'Y', 
            col2 TYPE c LENGTH 1 VALUE 'Z', 
          END OF comp2, 
        END OF struc_nested, 
        itab  TYPE TABLE OF line1 WITH EMPTY KEY, 
      END OF struc1, 
      BEGIN OF struc2, 
        BEGIN OF struc_nested, 
          comp1 TYPE string, 
          comp2 TYPE string, 
          comp3 TYPE string, 
        END OF struc_nested, 
        itab  TYPE TABLE OF line2 WITH EMPTY KEY, 
        comp4 TYPE i, 
      END OF struc2. 
    METHODS: 
      fill_deep_structures. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_variants_st IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 
     `Demo: Variants of MOVE-CORRESPONDING and the CORRESPONDING` && 
     ` operator using deep structures` 
       )->write_doc( '<b>Content of deep structures</b>' 
       )->write( struc1 
       )->write( struc2 
       )->line( ). 
 
    "MOVE-CORRESPONDING without additions 
 
    MOVE-CORRESPONDING struc1 TO struc2. 
 
    out->write_doc( `<b>MOVE-CORRESPONDING without additions</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 12, 12 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                    cl_demo_output_helper=>get_info_html( 1 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "MOVE-CORRESPONDING with addition EXPANDING NESTED TABLES 
 
    MOVE-CORRESPONDING struc1 TO struc2 EXPANDING NESTED TABLES. 
 
    out->write_doc( `<b>MOVE-CORRESPONDING with the addition ` && 
    `EXPANDING NESTED TABLES</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 25, 25 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 2 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "MOVE-CORRESPONDING with addition KEEPING TARGET LINES 
 
    MOVE-CORRESPONDING struc1 TO struc2 KEEPING TARGET LINES. 
 
    out->write_doc( `<b>MOVE-CORRESPONDING with the addition ` && 
    `KEEPING TARGET LINES</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 39, 39 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 3 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "MOVE-CORRESPONDING with addition 
    "EXPANDING NESTED TABLES KEEPING TARGET LINES 
 
    MOVE-CORRESPONDING struc1 TO struc2 
      EXPANDING NESTED TABLES KEEPING TARGET LINES. 
 
    out->write_doc( `<b>MOVE-CORRESPONDING with the additions ` && 
    `EXPANDING NESTED TABLES KEEPING TARGET LINES</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 54, 55 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 4 ) ) 
    )->write( struc2 
    )->line( ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator without addition 
 
    struc2 = CORRESPONDING #( struc1 ). 
 
    out->write_doc( `<b>CORRESPONDING operator without addition</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 70, 70 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 5 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator with the addition DEEP 
 
    struc2 = CORRESPONDING #( DEEP struc1 ). 
 
    out->write_doc( 
          ` <b>CORRESPONDING operator with the addition DEEP</b>` 
        )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
           source = cl_demo_output_helper=>get_caller( ) && 
           `, 83, 83 ` ) 
        )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                         cl_demo_output_helper=>get_info_html( 6 ) ) 
        )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator with the addition BASE 
 
    struc2 = CORRESPONDING #( BASE ( struc2 ) struc1 ). 
 
    out->write_doc( 
        `<b>CORRESPONDING operator with the addition BASE</b>` 
        )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
           source = cl_demo_output_helper=>get_caller( ) && 
           `, 96, 96 ` ) 
        )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                         cl_demo_output_helper=>get_info_html( 7 ) ) 
        )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator with the additions DEEP BASE 
 
    struc2 = CORRESPONDING #( DEEP BASE ( struc2 ) struc1 ). 
 
    out->write_doc( `<b>CORRESPONDING operator with the additions ` && 
                    `DEEP BASE</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 109, 109 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 8 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator with the additions APPENDING BASE 
 
    struc2 = CORRESPONDING #( APPENDING ( struc2 ) struc1 ). 
 
    out->write_doc( `<b>CORRESPONDING operator with the addition ` && 
                    `APPENDING</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 123, 123 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 9 ) ) 
    )->write( struc2 ). 
 
    fill_deep_structures( ). 
 
    "CORRESPONDING operator with the additions DEEP APPENDING BASE 
 
    struc2 = CORRESPONDING #( DEEP APPENDING ( struc2 ) struc1 ). 
 
    out->write_doc( `<b>CORRESPONDING operator with the additions ` && 
                    `DEEP APPENDING</b>` 
    )->write_doc( cl_demo_output_helper=>get_abap_source_code_html( 
       source = cl_demo_output_helper=>get_caller( ) && `, 137, 137 ` ) 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
                     cl_demo_output_helper=>get_info_html( 10 ) ) 
    )->write( struc2 ). 
  ENDMETHOD. 
  METHOD fill_deep_structures. 
    "Clear all contents of struc2. 
    CLEAR struc2. 
    "Fill nested tables in deep structures. 
    struc2-struc_nested = VALUE #( comp1 = `aaa` 
                                   comp2 = `bbb` 
                                   comp3 = `ccc` ). 
 
    struc1-itab = VALUE #( 
      ( col1 = 111 col2 = 222 ) 
      ( col1 = 333 col2 = 444 
      ) ). 
 
    struc2-itab = VALUE #( 
      ( col2 = 1 col3 = 2 col4 = 3 ) 
      ( col2 = 4 col3 = 5 col4 = 6 ) 
      ( col2 = 7 col3 = 8 col4 = 9 ) 
      ). 
    "Fill individual component that is not shared by both structures. 
    struc2-comp4 = 999. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    fill_deep_structures( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two structures, `struc1` and `struc2`, are declared. Both contain an identically named [nested structure](../../abap-glossary/abennested_structure_glosry.md) and nested table as deep components. The nested structures `struc_nested` differ in terms of the components' data types. The number of components in the nested structures as well as in the two nested internal tables `itab` is different.

The example covers statements with `MOVE-CORRESPONDING` and the `CORRESPONDING` operator demonstrating the differences in the result when using the various additions. The source code contains explanations on those differences.

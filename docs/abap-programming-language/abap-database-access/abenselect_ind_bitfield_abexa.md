---
title: "SELECT, Byte Field Indicators"
source_file: abenselect_ind_bitfield_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Null Values > indicators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Byte Field Indicators

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a [condensed indicator structure](../../abap-glossary/abencondensed_ind_structure_glosry.md) as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) in a `SELECT` statement. It shows the difference between position-based and name-based assignments of indicator bits without and with `CORRESPONDING FIELDS`.

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
CLASS cl_demo_indicators_bitfield DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_indicators_bitfield IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: 
      BEGIN OF data_line, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
        col4 TYPE i, 
        col5 TYPE i, 
      END OF data_line. 
 
    DATA data_tab TYPE STANDARD TABLE OF data_line WITH EMPTY KEY. 
 
    data_tab = VALUE #( ( col2 = 10 col3 = 10 col4 = 10 ) ). 
 
    TYPES: 
      BEGIN OF wa_ind, 
        col5     TYPE i, 
        colx     TYPE i, 
        col3     TYPE i, 
        coly     TYPE i, 
        col1     TYPE i, 
        col2     TYPE i, 
        col4     TYPE i, 
        null_ind TYPE x LENGTH 1, 
      END OF wa_ind. 
 
    DATA: 
      wa_ind1 TYPE wa_ind, 
      wa_ind2 TYPE wa_ind. 
 
    SELECT SINGLE 
           FROM @data_tab AS data_tab 
           FIELDS CASE WHEN 1 = 0 THEN 0 END AS col1 , 
                  col2, 
                  CASE WHEN 1 = 0 THEN 0 END AS col3, 
                  CASE WHEN 1 = 0 THEN 0 END AS col4, 
                  col5 
           INTO @wa_ind1 INDICATORS NULL BITFIELD null_ind. 
 
    DATA binary_ind1 TYPE string. 
    WHILE sy-index <= xstrlen( wa_ind1-null_ind ) * 8. 
      GET BIT sy-index OF wa_ind1-null_ind INTO FINAL(bit1). 
      binary_ind1 &&= bit1. 
    ENDWHILE. 
 
    SELECT SINGLE 
           FROM @data_tab AS data_tab 
           FIELDS CASE WHEN 1 = 0 THEN 0 END AS col1, 
                  col2, 
                  CASE WHEN 1 = 0 THEN 0 END AS col3, 
                  CASE WHEN 1 = 0 THEN 0 END AS col4, 
                  col5 
           INTO CORRESPONDING FIELDS OF @wa_ind2 
                INDICATORS NULL BITFIELD null_ind. 
 
    DATA binary_ind2 TYPE string. 
    WHILE sy-index <= xstrlen( wa_ind2-null_ind ) * 8. 
      GET BIT sy-index OF wa_ind2-null_ind INTO FINAL(bit2). 
      binary_ind2 &&= bit2. 
    ENDWHILE. 
 
    out->write( wa_ind1 
     )->write_data( binary_ind1 
     )->write( wa_ind2 
     )->write_data( binary_ind2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Data are selected with and without `CORRESPONDING FIELDS` from an internal table `@data_tab` with five columns `col1` to `col5`. In the result set, columns `col1` `col3` and `col4` contain the [null value](../../abap-glossary/abennull_value_glosry.md). The target areas contains a byte field `null_ind` as the last component but are differently structured than the result set in front of `null_ind`. The following figure illustrates the behavior: ![figure](images_indicators.png)

The assignments take place as follows:

- Without `CORRESPONDING FIELDS`, the values from the columns of the result set are assigned from left to right to the components of the target area. Accordingly. the first five bits of the null indicator are set from left to right. The bits at positions 1, 3, and 4 are set to 1. The bit at positions 2 and 5 as well as the excess bits at positions 6 to 8 are set to 0.

- With `CORRESPONDING FIELDS`, the columns of the result set are assigned to the components of the target area that have the same name. Since the positions of the columns named `col1` to `col5` in the target are 5, 6, 3, 7, and 1, the respective bits are set in the null indicator: The bits at positions 3, 5 and 7 are set to 1 and the bits at positions 1 and 6 are set to 0. `colx` and `coly` at positions 2 and 4 of the target area do not correspond to columns of the result set and the bits at these positions as well as the excess bit at position 8 are set to 0.

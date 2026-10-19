---
title: "itab_func - Index Function"
source_file: abenline_index_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Built-in Functions (itab_func) > itab_func - line_index"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab_func - Index Function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the built-in function [`line_index`](abenline_index_function.md).

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
CLASS cl_demo_line_index DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA 
      flight_tab 
        TYPE STANDARD TABLE OF spfli 
        WITH EMPTY KEY 
        WITH UNIQUE HASHED KEY id COMPONENTS carrid connid 
        WITH NON-UNIQUE SORTED KEY cities COMPONENTS cityfrom cityto. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_line_index IMPLEMENTATION. 
  METHOD main. 
    DATA idx TYPE TABLE OF i. 
 
    DATA(carrid_placeholder) = 'xx'. 
    DATA(connid_placeholder) = 'yyyy'. 
 
    idx = VALUE #( 
          ( line_index( flight_tab[ carrid = 'UA' 
                                    connid = '0941' 
                                    ##primkey[id] ] ) ) 
          ( line_index( flight_tab[ KEY id 
                                    carrid = 'UA' 
                                    connid = '0941' ] ) ) 
          ( line_index( flight_tab[ KEY id 
                                    carrid = carrid_placeholder 
                                    connid = connid_placeholder ] ) ) 
          ( line_index( flight_tab[ cityfrom = 'FRANKFURT' 
                                    cityto   = 'NEW YORK' 
                                    ##primkey[cities] ] ) ) 
          ( line_index( flight_tab[ KEY cities 
                                    cityfrom = 'FRANKFURT' 
                                    cityto   = 'NEW YORK'  ] ) ) 
          ( line_index( flight_tab[ KEY cities 
                                    cityfrom = 'xxxxxxxx' 
                                    cityto   = 'yyyyyyyy'  ] ) ) ). 
 
    out->write( idx ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    SELECT * 
           FROM spfli 
           ORDER BY carrid, connid 
           INTO TABLE @flight_tab. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Different line numbers in the same internal table as in the executable example for [specified lines](abentable_exp_itab_line_abexa.md) are read and inserted into an internal table, `idx`:

1.  The line number of a line in the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) found using a free search key.

2.  The number `-1`, since the secondary hash key `id` is used.

3.  The number `0`, since no line is found (`0` overrides `-1`).

4.  The line number of a line in the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) found using a different free search key.

5.  The line number of a line found in the assigned [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) using the sorted table key `cities`.

6.  The number `0`, since no line is found.

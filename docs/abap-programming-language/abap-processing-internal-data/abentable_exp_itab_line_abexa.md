---
title: "table_exp - Line Specification"
source_file: abentable_exp_itab_line_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp) > table_exp - itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Line Specification

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the line is specified in table expressions.

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
CLASS cl_demo_tab_exp_line DEFINITION 
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
CLASS cl_demo_tab_exp_line IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        out->begin_section( 
           `Primary index line 1` 
           )->write( 
             flight_tab[ 1 ] ). 
 
        out->next_section( 
          `Secondary index CITIES line 1` 
          )->write( 
            flight_tab[ KEY cities INDEX 1 ] ). 
 
        out->next_section( 
          `Free key CARRID, CONNID not optimized` 
          )->write( 
            flight_tab[ carrid = 'UA' 
                        connid = '0941' ] ) ##primkey[id]. 
 
        out->next_section( 
          `Secondary key ID fully optimized` 
          )->write( 
            flight_tab[  KEY id COMPONENTS carrid = 'UA' 
                                           connid = '0941' ] ). 
 
        out->next_section( 
          `Secondary key ID fully optimized` 
          )->write( 
            flight_tab[ TABLE KEY id COMPONENTS carrid = 'UA' 
                                                connid = '0941' ] ). 
 
        out->next_section( 
          `Secondary key CITIES partly optimized` 
          )->write( 
            flight_tab[ KEY cities cityfrom = 'FRANKFURT' ] ). 
 
        out->next_section( 
          `Secondary key CITIES fully optimized` 
          )->write( 
            flight_tab[ TABLE KEY cities cityfrom = 'FRANKFURT' 
                                         cityto   = 'NEW YORK' ] ). 
 
      CATCH cx_sy_itab_line_not_found. 
        out->write( `Nothing found` ). 
    ENDTRY. 
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

Table expressions that specify different lines are used as input parameters of the method `WRITE_DATA` of the output class `CL_DEMO_OUTPUT`. The following output is produced:

1.  The first line of the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md)

2.  The first line of the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) that is assigned to the [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) `cities`.

3.  A line with specific content in the columns `CARRID` and `CONNID`. This search with a free key is not optimized and the associated syntax check warning is hidden here using a [pragma](../../abap-glossary/abenpragma_glosry.md).

4.  The same line as before, but with a read that is fully optimized by using the secondary hash key `id`. All key fields must be specified.

5.  The same line as before, where the secondary hash key `id` is used by the syntax `TABLE KEY`. For hash keys, there is no difference between using `KEY` and `TABLE KEY`.

6.  A line with specific content in the columns `CITYFROM` and `CITYTO`. The search is partly optimized using the secondary sorted key `cities` and specifying the first key field.

7.  The same line as before, where the secondary sorted key `cities` is used by the syntax `TABLE KEY`. Here all key fields must be specified and the search is fully optimized.

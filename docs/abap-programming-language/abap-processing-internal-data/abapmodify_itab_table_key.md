---
title: "MODIFY itab, table_key"
source_file: abapmodify_itab_table_key.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab > MODIFY itab, itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab, table_key

## Syntax

``` abap
... TABLE itab [USING KEY keyname] ...   
```

[`keyname`](abenkeyname.md)

## Description

For `wa`, a work area compatible to the line type of the internal table must be specified. It is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The first line found in the internal table is processed whose values in the columns of the table key used match those of the corresponding components of `wa`.

If the `USING KEY` addition is not specified, the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is used. If the `USING KEY` addition is specified, the table key specified in [`keyname`](abenkeyname.md) is used.

The same applies when searching for a line to be modified as to key access using the statement [`READ`](abapread_table_key.md).

If the [primary table key](../../abap-glossary/abenprimary_key_glosry.md) is used to access a [standard table](../../abap-glossary/abenstandard_table_glosry.md) and the key is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), the first line of the internal table is modified. If this is known statically, the syntax check produces a warning.

## Hint

When using the primary table key, it should be noted that this key can be the [standard key](../../abap-glossary/abenstandard_key_glosry.md), which can also have unexpected consequences:

- For structured line types, the standard key covers all character-like and byte-like components.

- The standard key of a standard table can be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the local currency of an airline using primary key access to the internal table `scarr_tab`. The structure of the work area is constructed using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) from the result of a read with a [table expression](../../abap-glossary/abentable_expression_glosry.md), in which the component `currcode` is assigned the new value. The addition `TRANSPORTING` modifies this component only in the associated table line.

``` abap
DATA: carrid   TYPE scarr-carrid   VALUE 'LH', 
      currcode TYPE scarr-currcode VALUE 'EUR'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = currcode )->request( ). 
 
DATA scarr_tab TYPE SORTED TABLE OF scarr 
               WITH UNIQUE KEY carrid. 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
MODIFY TABLE scarr_tab 
       FROM VALUE #( 
              BASE scarr_tab[ KEY primary_key carrid = carrid ] 
              currcode = currcode ) 
       TRANSPORTING currcode.
```

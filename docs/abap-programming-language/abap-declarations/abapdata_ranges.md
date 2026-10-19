---
title: "DATA, RANGE OF"
source_file: abapdata_ranges.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, RANGE OF

## Syntax

``` abap
DATA range_tab {TYPE RANGE OF type}|{LIKE RANGE OF dobj}   
               [INITIAL SIZE n]   
               [VALUE IS INITIAL]   
               [READ-ONLY].  
```

[`[VALUE IS INITIAL]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

This statement defines a [ranges table](../../abap-glossary/abenranges_table_glosry.md) `range_tab` with the table type described in the section [`TYPES` - `RANGE OF`](abaptypes_ranges.md). The table type defined here, however, is not a standalone type, but exists as a property of the data object `range_tab`.

The addition [`VALUE IS INITIAL`](abapdata_options.md) can be used to specify an initial [start value](../../abap-glossary/abenstart_value_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, a ranges table is declared, filled, and evaluated in the [`WHERE`](../abap-database-access/abapwhere.md) condition of a [`SELECT`](../abap-database-access/abapselect.md) statement.

``` abap
DATA carrid_range TYPE RANGE OF spfli-carrid. 
 
carrid_range = VALUE #( 
  ( sign = 'I' option = 'BT' low = 'AA' high = 'LH' ) ). 
 
SELECT * 
       FROM spfli 
       WHERE carrid IN @carrid_range 
       INTO TABLE @FINAL(spfli_tab).
```

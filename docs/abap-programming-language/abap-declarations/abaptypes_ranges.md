---
title: "TYPES, RANGE OF"
source_file: abaptypes_ranges.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, RANGE OF

## Syntax

``` abap
TYPES dtype {TYPE RANGE OF type}|{LIKE RANGE OF dobj}   
            [INITIAL SIZE n].  
```

## Description

Derivation of a table type for a [ranges table](../../abap-glossary/abenranges_table_glosry.md). A ranges table is a [standard table](../../abap-glossary/abenstandard_table_glosry.md) in which a [ranges condition](../../abap-glossary/abenranges_condition_glosry.md) can be stored. It has a [standard key](../../abap-glossary/abenstandard_key_glosry.md) and a special structured line type whose internal definition can be represented as follows in ABAP syntax:

``` abap
TYPES: BEGIN OF linetype, 
         sign   TYPE c LENGTH 1, 
         option TYPE c LENGTH 2, 
         low    {TYPE type}|{LIKE dobj}, 
         high   {TYPE type}|{LIKE dobj}, 
       END OF linetype.
```

The additions `TYPE` and `LIKE` determine the data type of the components `low` and `high`:

- `type` can be a non-generic data type from the ABAP Dictionary, a non-generic public data type of a global class, a non-generic data type local to a program, a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md), or any ABAP type from the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md). The generic ABAP types `c`, `n`, `p`, and `x` are extended implicitly to the standard length without [decimal places](../../abap-glossary/abendecimal_place_glosry.md) from the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of built-in ABAP types.

- `dobj` can be a data object visible at this position, whose type is inherited for both components. Generically typed formal parameters cannot be specified for `dobj` within a [procedure](../../abap-glossary/abenprocedure_glosry.md).

The addition `INITIAL SIZE` is equivalent to the definition of regular internal [table types](abaptypes_itab.md).

A ranges table can be used in a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) with the [comparison operator](../../abap-glossary/abencomp_operator_glosry.md) [`IN`](../abap-program-flow-logic/abenlogexp_select_option.md) or in a [similar expression](../abap-database-access/abenwhere_logexp_seltab.md) in a `WHERE` condition in ABAP SQL.

## Hints

- The `sign` and `option` columns of a ranges table declared using `RANGE OF` do not refer to data types in the ABAP Dictionary. For a ranges table defined in the ABAP Dictionary, these columns refer to the data elements `DDSIGN` and `DDOPTION`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a table type for a ranges table and its use for an inline declaration of a ranges table on the left side of a constructor expression with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md).

``` abap
TYPES carrid_range TYPE RANGE OF spfli-carrid. 
 
FINAL(carrid_range) = VALUE carrid_range( 
  ( sign = 'I' option = 'BT' low = 'AA' high = 'LH' ) ). 
 
SELECT * 
       FROM spfli 
       WHERE carrid IN @carrid_range 
       INTO TABLE @FINAL(spfli_tab).
```

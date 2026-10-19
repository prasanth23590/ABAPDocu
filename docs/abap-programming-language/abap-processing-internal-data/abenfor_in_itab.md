---
title: "FOR ... IN itab"
source_file: abenfor_in_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR ... IN itab

## Syntax

``` abap
... FOR wa|<fs> IN itab [INDEX INTO idx] [cond] [let_exp]  ...  
```

[`cond`](abenfor_cond.md) · [`let_exp`](../abap-declarations/abaplet.md)

### Addition

[`... INDEX INTO idx`](abenfor_in_itab.md#addition)

## Overview

### Description

This variant of an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) for [table iterations](../../abap-glossary/abentable_iteration_glosry.md) using [`FOR`](abenfor_itab.md) evaluates an internal table `itab` sequentially, like a [line variant](abaploop_at_itab.md) of a [`LOOP`](abaploop_at_itab_variants.md). `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). As in [`LOOP`](abaploop_at_itab.md), the order of the lines read depends on the table category or a key specified in [`cond`](abenfor_cond.md).

[`cond1`](abenfor_cond.md) can be used to set conditions for the evaluation. For each read line, the result is either assigned to a local work area `wa1` or to a field symbol `<fs>`. The work area or the field symbol is declared implicitly with the line type of the internal table and bound locally to the `FOR` expression as a subexpression of the entire constructor expression. The same applies to the namespace and visibility as to the helper fields declared in [`LET` expressions](../abap-declarations/abaplet.md). After the `FOR` expression, the work area or the field symbol can either be used in further subexpressions or to construct the result of a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) or [table reduction](../../abap-glossary/abentable_reduction_glosry.md).

### Hints

- Instead of using directly specified internal tables `itab`, this variant of `FOR` expressions can also be created using [mesh paths](abenmesh_for.md), where `FOR` expressions from both categories can be used together in the same constructor expression.

- Changes to the content of the internal table specified after `IN` within the `FOR` expression can only be made using method calls. Deleting or replacing the table completely always produces a runtime error.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table `flights` in a table iteration with `FOR` with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) ([table comprehension](../../abap-glossary/abentable_comprehension_glosry.md)). The lines of the internal table are merged from the content of two existing internal tables `scarr_tab` and `spfli_tab`.

``` abap
SELECT carrid, carrname 
       FROM scarr 
       INTO TABLE @FINAL(scarr_tab). 
 
SELECT carrid, connid, cityfrom, cityto 
       FROM spfli 
       ORDER BY carrid, connid, cityfrom, cityto 
       INTO TABLE @FINAL(spfli_tab). 
 
TYPES: 
  BEGIN OF flight, 
    carrier     TYPE scarr-carrname, 
    number      TYPE spfli-connid, 
    departure   TYPE spfli-cityfrom, 
    destination TYPE spfli-cityto, 
  END OF flight, 
  flights TYPE TABLE OF flight WITH EMPTY KEY. 
 
FINAL(flights) = 
  VALUE flights( FOR <fs> IN spfli_tab 
    ( carrier     = VALUE #( 
                      scarr_tab[ carrid = <fs>-carrid ]-carrname 
                      DEFAULT '???' ) 
      number      = <fs>-connid 
      departure   = <fs>-cityfrom 
      destination = <fs>-cityto ) ). 
 
cl_demo_output=>display( flights ).
```

## Executable Examples

- [Examples of Table Comprehensions](abentable_comprehensions_abexas.md)

- [Examples of Table Reductions](abentable_reductions_abexas.md)

## Addition

`... INDEX INTO idx`

### Description

For each read line of the associated `FOR` expression, this addition sets the helper variable `idx` to the value to which the system field `sy-tabix` would be set in a corresponding [`LOOP`](abaploop_at_itab.md). The helper variable `idx` is declared implicitly with the type `i` and bound locally to the `FOR` expression as a subexpression of the entire constructor expression. The same applies to the namespace and visibility as to the helper fields declared in [`LET` expressions](../abap-declarations/abaplet.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table `carriers` from an existing internal table `scarr_tab`. The first column is provided with the line index of the existing table.

``` abap
SELECT carrid, carrname 
       FROM scarr 
       INTO TABLE @FINAL(scarr_tab). 
 
TYPES: 
  columns LIKE LINE OF scarr_tab, 
  BEGIN OF carrier, 
    no TYPE i. 
    INCLUDE TYPE columns. 
TYPES: 
  END OF carrier, 
  carriers TYPE TABLE OF carrier WITH EMPTY KEY. 
 
FINAL(carriers) = 
  VALUE carriers( FOR wa IN scarr_tab INDEX INTO i 
    ( no = i carrid = wa-carrid carrname = wa-carrname ) ). 
 
cl_demo_output=>display( carriers ).
```

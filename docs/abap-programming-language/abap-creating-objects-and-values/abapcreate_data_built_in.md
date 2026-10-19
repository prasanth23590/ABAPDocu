---
title: "CREATE DATA, TYPE abap_type"
source_file: abapcreate_data_built_in.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA, TYPE abap_type

## Syntax

``` abap
CREATE DATA dref     
                 TYPE {abap_type|(name)}   
                      [LENGTH len] [DECIMALS dec].  
```

## Description

Creation of a data object with an explicitly specified data type. For the data type, all [built-in data types](../../abap-glossary/abenbuiltin_data_type_glosry.md), apart from `b` and `s`, can be used that are more specific than the static type of `dref` or are identical to it. The name of the type can be specified as follows:

- `abap_type`

  Direct static specification as `abap_type`.

- `(name)`

  Specification as the content of a character-like data object `name` without case-sensitivity. The following can be specified for `name`:

  - Literal or constant

    If the data object `name` is specified as a character literal or as a constant, it can be evaluated statically and the specified type is recognized as the used object.

  - Variable

    If the data object `name` is specified as a variable, it is specified only dynamically and the content is not evaluated statically. When the statement is executed, `name` is not evaluated until runtime (in both cases).

For the ABAP types `c`, `n`, `p`, and `x`, the length of the data type `dtype` can be determined by specifying a numeric data object `len` after the addition `LENGTH`, which, when the statement is executed, contains a value within the [length range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) specified for the respective type. If the addition `LENGTH` is not specified, the standard length from the table is used. For all other ABAP types, the length is determined by the value in the table and the addition `LENGTH` cannot be specified.

For the ABAP type `p`, the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) can be determined by specifying a numeric data object `dec` after the addition `DECIMALS`. If `DECIMALS` is specified, the same applies as to the statement [`TYPES`](../abap-declarations/abaptypes_simple.md). If the addition `DECIMALS` is not specified, no decimal places are created.

## Hint

If a data type `abap_type` is used, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) acts like the statement `CREATE DATA dref TYPE abap_type` and can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). The dynamic specification of `name` is not possible here.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object of the type of a packed number with length specification and decimal places.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO data. 
 
CREATE DATA dref TYPE p LENGTH 8 DECIMALS 3. 
 
dref->* = 1 / 3. 
 
out->write( dref->* ). 
 
out->display( ).
```

## Executable Example

[Creating Elementary Data Objects](abencreate_simple_data_abexa.md)

---
title: "NEW, Initial Value for All Types"
source_file: abennew_constructor_params_initial.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Initial Value for All Types

## Syntax

``` abap
... NEW dtype|class|#( ) ...  
```

## Description

If no parameter is specified,

- an anonymous data object retains its type-specific initial value,

- no values are passed to the instance constructor of an object.

This is possible for every non-generic data type `dtype`. The instance constructor of a class `class` can either have only optional input parameters or no input parameters at all. The `#` symbol can stand for corresponding types.

## Hint

If `dtype` or `#` stand for an [enumerated type](../../abap-glossary/abenenum_type_glosry.md), its initial value is created according to its [base type](../../abap-glossary/abenbase_type_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the following program section is executed, `dref` points to an empty internal table with the line type `T100`. Both constructor expressions have the same function.

``` abap
TYPES t_itab TYPE TABLE OF t100 WITH EMPTY KEY. 
 
DATA dref TYPE REF TO t_itab. 
 
dref = NEW #( ). 
dref = NEW t_itab( ).
```

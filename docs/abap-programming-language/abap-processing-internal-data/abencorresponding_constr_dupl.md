---
title: "CORRESPONDING, duplicates"
source_file: abencorresponding_constr_dupl.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CORRESPONDING, Component Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, duplicates

## Syntax

``` abap
... DISCARDING DUPLICATES ...  
```

## Description

Addition for handling duplicate lines in the component operator [`CORRESPONDING`](abenconstructor_expr_corresponding.md). The addition `DISCARDING DUPLICATES` can be specified:

- After a tabular parameter `itab` in the [basic form](abencorresponding_constr_arg_type.md).

- After [mapping relationships](abencorresponding_constr_mapping.md) `t1 = s1`, `t2 = s2`, ... for tabular components.

The addition `DISCARDING DUPLICATES` prevents an exception when duplicate entries occur with respect to a unique [primary](../../abap-glossary/abenprimary_table_key_glosry.md) or secondary table key in assignments to a target table. In the basic form, this also applies to the lines that exist in an internal table specified after [`BASE`](abencorresponding_constr_arg_type.md).

By default, the addition `DISCARDING DUPLICATES` affects the source table after which it is specified. That is, either to `itab` of the basic form or to`s1`, `s2`, ... of mapping relationships. If `DISCARDING DUPLICATES` is specified with the addition `DEEP` after `itab` in the basic form, it also affects the statements of nested internal tables.

The addition `DISCARDING DUPLICATES` specifies that, when lines of a source table are inserted sequentially into a target table, the lines that are already in the target table with the same unique primary or secondary table key are ignored in the source table and do not raise an exception.

If the addition `DISCARDING DUPLICATES` is specified for an operand for which a unique table key is not known statically, the syntax check produces a warning.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `DISCARDING DUPLICATES` in the [executable example](abencorresponding_duplicates_abexa.md).

``` abap
... CORRESPONDING itab2( itab1 DISCARDING DUPLICATES 
                         MAPPING y1 = x1 
                                 y2 = x2 DISCARDING DUPLICATES ) ...
```

## Executable Example

[Handling Duplicates](abencorresponding_duplicates_abexa.md)

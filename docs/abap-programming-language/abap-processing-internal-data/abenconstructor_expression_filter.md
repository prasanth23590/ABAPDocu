---
title: "FILTER, Filter Operator"
source_file: abenconstructor_expression_filter.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Filter Operator

## Syntax Forms

**[Basic Form](abenconstructor_expr_filter_basic.md)**

``` abap
1. ... FILTER type( itab [EXCEPT] [USING KEY keyname] 
                        WHERE c1 op {op f1}|{IS [NOT] INITIAL} 
                         [AND c2 op {op f2}|{IS [NOT] INITIAL} [...]] ) ...
```

**[Filter Table](abenconstructor_expr_filter_table.md)**

``` abap
2. ... FILTER type( itab [EXCEPT] IN ftab [USING KEY keyname] 
                        WHERE c1 op f1 [AND c2 op f2 [...]] ) ...
```

[`keyname`](abenkeyname.md) · [`keyname`](abenkeyname.md)

### Addition

[`... EXCEPT`](abenconstructor_expression_filter.md#addition)

## Overview

### Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the component operator `FILTER` creates a result of a table type specified using `type`. The lines are taken from an existing internal table `itab` in accordance with the condition after `WHERE`, converted to the line type of `type`, and inserted into the target table in accordance with the rules of [`INSERT`](abapinsert_itab.md) ... [`INTO TABLE`](abapinsert_itab_position.md). The order in which the lines are taken from `itab` depends on its [table category](../../abap-glossary/abentable_category_glosry.md) and the addition `USING KEY` and is the same as for [`LOOP AT itab`](abaploop_at_itab.md).

- In the [basic form](abenconstructor_expr_filter_basic.md), the condition is created with single values.

- When using a [filter table](abenconstructor_expr_filter_table.md), the condition is created with values from the filter table `ftab`.

The following can be specified for `type`:

- A non-generic [table type](../../abap-glossary/abentable_type_glosry.md).

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md). If the data type required in an operand position is not unique and not known completely, the type of `itab` is used if known.

`itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The line type of `itab` must be convertible to the line type of the target type `type`. `USING KEY` can or must be used to specify a table key for evaluating `itab` or `ftab`, depending on the variant.

### Hints

- Table filtering can also be performed using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) or a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) with an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) for [table iterations](../../abap-glossary/abentable_iteration_glosry.md) with [`FOR`](abenfor_itab.md). The operator `FILTER` provides a shorter notation for this special case and is more efficient to execute.

- A table filter constructs the result line by line. If the result contains almost all lines in the source table, this method can be slower than copying the source table and deleting the surplus lines from the target table.

## Addition

`... EXCEPT`

### Description

If `EXCEPT` is not specified, those lines from `itab` are used that meet the `WHERE` condition. If `EXCEPT` is specified, those lines from `itab` are used that do not meet the `WHERE` condition.

### Hint

The addition `EXCEPT` is not the same as a negation of the `WHERE` condition, particularly in the variant with a [filter table](abenconstructor_expr_filter_table.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the addition `EXCEPT` in the [basic form](abenconstructor_expr_filter_basic.md) of the `FILTER` operator. The constructed table contains messages of all languages except *D*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA messages TYPE SORTED TABLE OF t100 WITH NON-UNIQUE KEY sprsl. 
SELECT * 
       FROM t100 
       WHERE arbgb = 'SABAPDEMOS' 
       ORDER BY msgnr 
       INTO TABLE @messages. 
 
out->write( 
  FILTER #( messages EXCEPT WHERE sprsl = 'D' ) ). 
 
out->display( ).
```

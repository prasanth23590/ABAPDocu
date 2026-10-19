---
title: "FILTER, Basic Form"
source_file: abenconstructor_expr_filter_basic.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FILTER, Filter Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Basic Form

## Syntax

``` abap
... FILTER type( itab [EXCEPT] [USING KEY keyname] 
                       WHERE c1 {op f1}|{IS [NOT] INITIAL} 
                        [AND c2 {op f2}|{IS [NOT] INITIAL} [...]] ) ...  
```

[`keyname`](abenkeyname.md)

### Addition

[1. `... USING KEY keyname`](abenconstructor_expr_filter_basic.md#addition-1)

[2. `... WHERE c1 {op f1}|{IS [NOT] INITIAL} [AND c2 {op f2}|{IS [NOT] INITIAL} [...]]`](abenconstructor_expr_filter_basic.html#addition-2)

## Overview

### Description

This variant of the filter operator [`FILTER`](abenconstructor_expression_filter.md) filters `itab` using single values. The columns of a table key of `itab` are compared with single values in the `WHERE` condition. Those lines of `itab` are used that meet the `WHERE` condition or do not meet it when `EXCEPT` is specified.

Here, the internal table `itab` must have at least one [sorted key](../../abap-glossary/abensorted_key_glosry.md) or one [hash key](../../abap-glossary/abenhash_key_glosry.md) used for access. This can be

- either the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) used without specifying `USING KEY` or by specifying its name `primary_key` after `USING KEY`,

- or a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) used by specifying its name after `USING KEY`.

This variant of the filter operator is not possible for an internal table `itab` without a sorted key or hash key.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filtering of the messages of a work area from the database table `T100` by language.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA messages TYPE SORTED TABLE OF t100 WITH NON-UNIQUE KEY sprsl. 
SELECT * 
       FROM t100 
       WHERE arbgb = 'SABAPDEMOS' 
       ORDER BY msgnr 
       INTO TABLE @messages. 
 
out->write( FILTER #( messages WHERE sprsl = 'D' ) ). 
out->write( FILTER #( messages WHERE sprsl = 'E' ) ). 
 
out->display( ).
```

## Addition 1

`... USING KEY keyname`

### Description

Specifies the table key [`keyname`](abenkeyname.md) with which the `WHERE` condition is evaluated. A sorted key or a hash key of the table `itab` can be specified. If the primary key of `itab` is not a sorted key or hash key, `itab` must have a secondary key of this type and it must be specified using `USING KEY`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the preceding example, but here a secondary table key must be specified explicitly since the internal table `messages` is a standard table without a primary key.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA messages TYPE STANDARD TABLE OF t100 
                   WITH NON-UNIQUE SORTED KEY langu COMPONENTS sprsl. 
SELECT * 
       FROM t100 
       WHERE arbgb = 'SABAPDEMOS' 
       ORDER BY msgnr 
       INTO TABLE @messages. 
 
out->write( FILTER #( messages USING KEY langu 
                                          WHERE sprsl = 'D' ) ). 
out->write( FILTER #( messages USING KEY langu 
                                          WHERE sprsl = 'E' ) ). 
out->display( ).
```

## Addition 2

`... WHERE c1{op f1}|{IS [NOT] INITIAL} [AND c2 {op f2}|{IS [NOT] INITIAL} [...]]`

### Description

A condition for the table key used in the `FILTER` expression must be specified after `WHERE`:

- In the case of a hash key, exactly one [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md) [`c = f`](../abap-program-flow-logic/abenlogexp_any_operand.md) or [`c IS INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md) for each key component. The only [comparison operator](../../abap-glossary/abencomp_operator_glosry.md) allowed for `op` is [`=`](../abap-program-flow-logic/abenlogexp_any_operand.md). The condition [`IS NOT INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md) is not allowed.

- In the case of a sorted key, an initial part of the key must be covered by [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md) [`c op f`](../abap-program-flow-logic/abenlogexp_any_operand.md) or [`c IS [NOT] INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md). `op` can be any [binary comparison operator](../abap-program-flow-logic/abenlogexp_any_operand.md).

Multiple comparisons can be combined using [`AND`](../abap-program-flow-logic/abenlogexp_and.md) only. There can be no further comparisons apart from those mentioned for key components. In the basic form, key components of the internal table `itab` must be specified for the left operands `c1`, `c2`, ... On the right side, operands `f1`, `f2`, ... must be specified after `=` or `op` that are compatible with the left side. `f1`, `f2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

### Hints

- The Boolean operators [`NOT`](../abap-program-flow-logic/abenlogexp_not.md), [`OR`](../abap-program-flow-logic/abenlogexp_or.md), and [`EQUIV`](../abap-program-flow-logic/abenlogexp_equiv.md) cannot be used in the `WHERE` condition. Note that the `NOT` in `IS NOT INITIAL` is not a Boolean operator.

### Executable Example

[Table Filtering, Single Values](abenfilter_value_condition_abexa.md)

---
title: "FILTER, Filter Table"
source_file: abenconstructor_expr_filter_table.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FILTER, Filter Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Filter Table

## Syntax

``` abap
... FILTER type( itab {[EXCEPT] IN ftab [USING KEY keyname]} 
                    | {[USING KEY keyname] [EXCEPT] IN ftab} 
                       WHERE c1 op f1 [AND c2 op f2 [...]] ) ...  
```

[`keyname`](abenkeyname.md) · [`keyname`](abenkeyname.md)

### Addition

[1. `... USING KEY keyname`](abenconstructor_expr_filter_table.md#addition-1)

[2. `... WHERE c1 op v1 [AND c2 op v2 [...]]`](abenconstructor_expr_filter_table.html#addition-2)

## Overview

### Description

This variant of the filter operator [`FILTER`](abenconstructor_expression_filter.md) filters `itab` using values from an internal table `ftab`. In the `WHERE` condition, the columns of `itab` are compared with the values of the columns of the table key of the lines of the filter table `ftab`. Those lines in `itab` are used for which at least one line in `ftab` meets the `WHERE` condition or for which there is no line in `ftab` when `EXCEPT` is specified. `ftab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

Depending on its position, `USING KEY` can be used to specify either a key of the table `ftab` or the table `itab`, which is then used to access the table. If `USING KEY` is not used, the filter table `ftab` must have a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md) as the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md), which is then used to access the filter table.

### Hint

The line types of `itab` and `ftab` do not need to be identical.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filtering of three lines of the internal table `carriers`. The filter table has a sorted primary key. This is used implicitly and the addition `USING KEY` does not have to be specified.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(carriers). 
 
DATA filter TYPE SORTED TABLE OF scarr-carrid 
                 WITH UNIQUE KEY table_line. 
filter = VALUE #( ( 'AA ' ) ( 'LH ' ) ( 'UA ' ) ). 
 
out->write( FILTER #( 
  carriers IN filter WHERE carrid = table_line ) ). 
 
out->display( ).
```

## Addition 1

`... USING KEY keyname`

### Description

Specification of the table key [`keyname`](abenkeyname.md) with which the `WHERE` condition is evaluated. A sorted key or a hash key of the filter table can be specified after `ftab` or of the source table after `itab`. This can be the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) or a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) that is specified using `primary_key` or the corresponding name.

- When `USING KEY` is specified for the filter table `ftab`, it must have a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md). There are no requirements on the table keys of `itab`. The specified key is used to access the filter table.

- When `USING KEY` is specified for the source table `itab`, it must have a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md). There are no requirements on the table keys of `ftab`. The specified key is used to access the source table.

- If `USING KEY` is not specified for `ftab` or `itab`, the filter table `ftab` must be a sorted table or a hashed table and the primary table key is used implicitly when accessing the filter table. There are no requirements on the table keys of `itab`.

### Hint

The tables for which a key is specified depends on the optimization to be achieved.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but here the addition `USING KEY` must be used for one of the tables, since the internal table `filter` is a standard table without a primary key.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(carriers). 
 
DATA filter TYPE STANDARD TABLE OF scarr-carrid 
                 WITH EMPTY KEY 
                 WITH UNIQUE SORTED KEY line COMPONENTS table_line. 
filter = VALUE #( ( 'AA ' ) ( 'LH ' ) ( 'UA ' ) ). 
 
out->write( FILTER #( 
  carriers IN filter USING KEY line 
           WHERE carrid = table_line ) ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but here the addition `USING KEY` is used for the other table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA carriers TYPE SORTED TABLE OF scarr 
              WITH UNIQUE KEY carrid. 
SELECT * 
       FROM scarr 
       INTO TABLE @carriers. 
 
DATA filter TYPE STANDARD TABLE OF scarr-carrid 
                 WITH EMPTY KEY. 
filter = VALUE #( ( 'AA ' ) ( 'LH ' ) ( 'UA ' ) ). 
 
out->write( FILTER #( 
  carriers USING KEY primary_key IN filter 
           WHERE carrid = table_line ) ). 
 
out->display( ).
```

## Addition 2

`... WHERE c1 op f1 [AND c2 op f2 [...]]`

### Description

A condition for the table key used in the `FILTER` expression must be specified after `WHERE`:

- In the case of a hash key, exactly one [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md) `c op f` for each key component. The only [comparison operator](../../abap-glossary/abencomp_operator_glosry.md) allowed for `op` is [`=`](../abap-program-flow-logic/abenlogexp_any_operand.md).

- In the case of a sorted key, an initial part of the key must be covered by [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md) `c op f`. `op` can be any [binary comparison operator](../abap-program-flow-logic/abenlogexp_any_operand.md).

Multiple comparisons can only be combined using [`AND`](../abap-program-flow-logic/abenlogexp_and.md) only. There can be no further comparisons apart from those mentioned for key components. In the variant with the filter table, key components of the filter table `ftab` must be specified for the right operands `f1`, `f2`, .... On the left side, components of the internal table `itab` must be specified that are compatible with the right side.

### Hints

- The Boolean operators [`NOT`](../abap-program-flow-logic/abenlogexp_not.md), [`OR`](../abap-program-flow-logic/abenlogexp_or.md), and [`EQUIV`](../abap-program-flow-logic/abenlogexp_equiv.md) cannot be used in the `WHERE` condition.

## Executable Examples

- [Table Filtering, Filter Table](abenfilter_table_abexa.md)

- [Table Filtering, Filterings with Filter Table](abenfilter_table_condition_abexa.md)

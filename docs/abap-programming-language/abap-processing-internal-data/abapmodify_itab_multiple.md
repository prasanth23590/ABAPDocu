---
title: "MODIFY itab, itab_lines"
source_file: abapmodify_itab_multiple.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab, itab_lines

## Syntax

``` abap
... itab FROM wa [USING KEY keyname] 
         TRANSPORTING comp1 comp2 ... WHERE log_exp|(cond_syntax).  
```

[`keyname`](abenkeyname.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`log_exp`](../abap-program-flow-logic/abenlogexp.md)

### Addition

[1. `... WHERE log_exp`](abapmodify_itab_multiple.md#addition-1)

[2. `... USING KEY keyname`](abapmodify_itab_multiple.md#addition-2)

[3. `... WHERE (cond_syntax)`](abapmodify_itab_multiple.md#addition-3)

## Overview

### Description

In this variant, the statement `MODIFY` assigns the content of the components `comp1 comp2 ...` of the work area `wa` specified after `TRANSPORTING` to all lines of the table `itab` that meet the condition after `WHERE`. `wa` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The work area `wa` must be [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of the internal table.

The addition `TRANSPORTING` has the same effect as [changing individual lines](abapmodify_itab_single.md). The addition `WHERE` can only be specified together with the addition `TRANSPORTING`.

## Addition 1

`... WHERE log_exp`

### Description

Static `WHERE` condition. All lines are modified for which the condition after `WHERE` is met. If a static `WHERE` condition is specified, the line type of the internal table must be known statically. `WHERE` can be specified for all table categories.

A [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) [`log_exp`](../abap-program-flow-logic/abenlogexp.md) can be specified after `WHERE`, in which the first operand of each [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) is a [component](abenitab_components.md) of the internal table. The following can be specified as relational expressions:

- All [comparison expressions](../abap-program-flow-logic/abenlogexp_comp.md)

- The following [predicate expressions](../../abap-glossary/abenpredicate_expression_glosry.md):

  - [`IS [NOT] INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md)

  - [`IS [NOT] BOUND`](../abap-program-flow-logic/abenlogexp_bound.md)

  - [`IS [NOT] INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md)

No other [predicates](../abap-program-flow-logic/abenpredicate.md) can be specified. The components of the internal table must be specified as individual operands and not as part of an expression. Parenthesized character-like data objects cannot be used to specify a component dynamically here. The remaining operands of a relational expression are [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md) at which any [suitable](../abap-program-flow-logic/abenlogexp_rules.md) individual operands or [expressions](../../abap-glossary/abenexpression_glosry.md) can be specified, but no components of the internal table. The specified components can have any data type. The corresponding [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) apply to the evaluation, whereby a different [rule](../abap-program-flow-logic/abenlogexp_rules_expr_char.md) applies to a string expression on the right side than to general logical expressions.

The evaluation of the `WHERE` condition depends on the [table category](../../abap-glossary/abentable_category_glosry.md) and the [table key](../../abap-glossary/abentable_key_glosry.md) used as follows:

- When [standard tables](../../abap-glossary/abenstandard_table_glosry.md) are accessed without a secondary key specification, the search is not optimized. This means that the logical expression of the `WHERE` addition is applied to each line of the internal table that is relevant for the current statement.

- When using a [sorted key](../../abap-glossary/abensorted_key_glosry.md) or a [hash key](../../abap-glossary/abenhash_key_glosry.md), that is, when accessing a [sorted table](../../abap-glossary/abensorted_table_glosry.md), a [hashed table](../../abap-glossary/abenhashed_table_glosry.md), or a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), the compiler tries to optimize the search as described under [Optimization of the `WHERE` Condition](abenitab_where_optimization.md). The prerequisites are:

  - The entire logical expression or a part of it can be transformed into a key access.

  - The transformable part of the logical expression has the same result as the resulting key access.

    If an optimization is not possible, the behavior is as follows:

  - If a sorted table or a hashed table is accessed using the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md), the full `WHERE` condition is applied to each line of the table that is relevant for the current statement.

  - If the table is accessed using a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), a syntax error or an exception is raised.

### Hints

- When using a `WHERE` condition, it should be noted that the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for incompatible data types apply when comparing incompatible data objects. Here, the data types involved determine which operand is converted. If the additions [`WITH TABLE KEY`](abapread_table_key.md) and [`WITH KEY`](abapread_table_free.md) of the statement `READ` are used or if the corresponding [keys are specified](abentable_exp_itab_line.md) in [table expressions](abentable_expressions.md), however, the content of the specified data objects is always converted to the data type of the columns before the comparison, which can produce varying results.

- The difference between comparison rules in a `WHERE` condition and conversion rules when reading individual lines is particularly significant for [enumerated types](../../abap-glossary/abenenum_type_glosry.md) for which the comparison rules are more restrictive than conversion rules. [Conversions](abenconversion_enumerated.md) of an enumerated object to a character-like type produce a message from the extended program check.

- If possible, all operands of the logical expression should be in [compatible](../../abap-glossary/abencompatible_glosry.md) pairs, so that the [`WHERE` condition can be optimized](abenitab_where_optimization.md).

- If a comparison expression with a [ranges table](../../abap-glossary/abenranges_table_glosry.md) is specified after [`IN`](../abap-program-flow-logic/abenlogexp_select_option.md) as a logical expression, the expression for the initial table is always true and then all lines are found.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the column `col2` of the internal table `itab`, the `MODIFY` statement replaces every negative value with the number 0.

``` abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE SORTED TABLE OF line 
               WITH UNIQUE KEY col1. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                        min  = 1 
                                        max  = 20 ). 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
itab = VALUE #( FOR i = 1 UNTIL i > 26 
                ( col1 = substring( val = abcde 
                                    off = i - 1 
                                    len = 1 ) 
                                    col2 = rnd->get_next( ) - 10 ) ). 
 
MODIFY itab FROM VALUE line( col2 = 0 ) TRANSPORTING col2 
            WHERE col2 < 0.
```

## Addition 2

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) with which the processing is executed. The specified table key affects the order in which the table lines are accessed, and the evaluation of the remaining conditions.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified, the processing behaves in the same way as if no key were explicitly specified. If a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified, the order in which the lines are accessed is as follows:

- **Specification of a [sorted key](../../abap-glossary/abensorted_key_glosry.md)**

  The lines are processed by ascending line number in the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md)

- **Specification of a [hash key](../../abap-glossary/abenhash_key_glosry.md)**

  The lines are processed in the order in which they were inserted into the table.

### Hints

- Unlike the processing of a hashed table when a primary key is used, a preceding sort using the statement `SORT` has no effect on the processing order when a secondary hash key is specified.

- If a secondary table key is specified, any `WHERE` condition must be [optimizable](abenitab_where_optimization.md). Otherwise a syntax error occurs, or an exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the internal table `itab`, the `MODIFY` statement replaces the value in the column `col1` with *\_* if the column `col2` contains the value 0. The `WHERE` condition is evaluated in an optimized way using the secondary key `mkey`.

``` abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE TABLE OF line 
               WITH EMPTY KEY 
               WITH NON-UNIQUE SORTED KEY mkey COMPONENTS col2. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                        min  = 1 
                                        max  = 10 ). 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
itab = VALUE #( FOR i = 1 UNTIL i > 26 
                ( col1 = substring( val = abcde 
                                    off = i - 1 
                                    len = 1 ) 
                                    col2 = rnd->get_next( ) - 5 ) ). 
 
MODIFY itab FROM VALUE line( col1 = '_' ) USING KEY mkey 
            TRANSPORTING col1 WHERE col2 = 0.
```

## Addition 3

`... WHERE (cond_syntax)`

### Description

Dynamic `WHERE` condition. For `cond_syntax` any character-like data object or [standard table](../../abap-glossary/abenstandard_table_glosry.md) with character-like line type can be specified that, when the statement is executed and with the following exceptions, contains the syntax of a logical expression in accordance with the rules of the static `WHERE` condition or is initial. The following are not supported in a dynamic `WHERE` condition:

- [String expressions](../../abap-glossary/abenstring_expression_glosry.md) and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md)

- [String functions](../../abap-glossary/abenstring_function_glosry.md)

- [Time stamp functions](../../abap-glossary/abentimestamp_function_glosry.md) with the exception of `utclong_current`

- [Constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md)

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md)

The syntax in `cond_syntax` is not case-sensitive as in the static syntax. When an internal table is specified, the syntax can be distributed across multiple lines. If `cond_syntax` is initial when the statement is executed, the logical expression is true. Invalid logical expressions raise an exception from the class `CX_SY_ITAB_DYN_LOOP`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](abenescape_functions.md).

### Hint

The dynamic `WHERE` condition is not evaluated for an empty table for optimization reasons. Therefore, if an internal table is empty, and a logical expression has errors, no exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the example for static `WHERE` conditions, but with a condition for the column `col2` that can be entered dynamically.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA condition TYPE string VALUE '< 0'. 
cl_demo_input=>request( CHANGING field = condition ). 
condition = `col2 ` && condition. 
 
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE SORTED TABLE OF line 
               WITH UNIQUE KEY col1. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                         min  = 1 
                                         max  = 20 ). 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
itab = VALUE #( FOR i = 1 UNTIL i > 26 
                ( col1 = substring( val = abcde 
                                    off = i - 1 
                                    len = 1 ) 
                                    col2 = rnd->get_next( ) - 10 ) ). 
TRY. 
    MODIFY itab FROM VALUE line( col2 = 0 ) TRANSPORTING col2 
                WHERE (condition). 
    out->write( itab ). 
  CATCH cx_sy_itab_dyn_loop INTO FINAL(exc). 
    ... 
ENDTRY. 
 
out->display( ).
```

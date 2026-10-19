---
title: "FOR GROUPS ... OF"
source_file: abenfor_groups_of.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR GROUPS ... OF

## Syntax

``` abap
... FOR GROUPS [group|<group>] OF wa|<fs> IN itab 
        [INDEX INTO idx] [cond] 
        GROUP BY group_key 
        [ASCENDING|DESCENDING [AS TEXT]] 
        [WITHOUT MEMBERS] 
        [let_exp] ...  
```

[`cond`](abenfor_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`let_exp`](../abap-declarations/abaplet.md)

### Addition

[`... INDEX INTO idx`](abenfor_groups_of.md#addition)

## Overview

### Description

This variant of an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) for [table iterations](../../abap-glossary/abentable_iteration_glosry.md) with [`FOR`](abenfor_itab.md) evaluates an internal table `itab` in the same way as a [`LOOP`](abaploop_at_itab_variants.md) with the addition [`GROUP BY`](abaploop_at_itab_group_by.md) in two phases:

- Grouping of all lines that meet the condition in [`cond`](abenfor_cond.md) by the group key specified in [`group_key`](abaploop_at_itab_group_by_key.md). The same applies to `group_key` as in [`LOOP AT ...GROUP BY`](abaploop_at_itab_group_by.md). In this phase, each line read is either written to the local work area `wa` or assigned to the local field symbol `<fs>` and can then be evaluated when the group key is constructed.

- Evaluation of the groups. Specifying `group` or `<group>` (optional) results in the [group key binding](abaploop_at_itab_group_by_binding.md) in which the current group key is written to the local data object `group` or assigned to the local field symbol `<group>`. If `group` or `<group>` is not specified, the [representative binding](abaploop_at_itab_group_by_binding.md) applies, in which the first line of a group is written to the local work area `wa` or assigned to the local field symbol `<fs>`. In the group key binding, `wa` or `<fs>` are initial after the `FOR` expression.

`itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The same applies to the additions `ASCENDING`, `DESCENDING`, and `WITHOUT MEMBERS` as in [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md). In particular, `WITHOUT MEMBERS` can be specified only if a group key binding is defined after `GROUPS` by specifying `group` or `<group>`.

Depending on the type of binding, the work area `wa` or `group` or the field symbol `<fs>` or `<group>` after the `FOR` expression can either be used in further subexpressions or to construct the result of a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) or [table reduction](../../abap-glossary/abentable_reduction_glosry.md). In particular, it can be specified in the expression [`FOR ... IN GROUP`](abenfor_in_group.md) to evaluate the members of the current group.

### Hint

If a constructor expression contains a `FOR` expression with group key binding and the group key is to be used as the result of the constructor expression, a suitable data type or a data object with this type must exist for this expression explicitly. It is not possible to derive this type here using an inline declaration as in [`LOOP AT`](abaploop_at_itab_group_by.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of all values of the column `carrid` that occur in `spfli`. The result of the [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) is a single-column internal table that contains all group key values. The `FOR` loop works with a group key binding. Here, each group key is assigned to the local data object `carrier`.

``` abap
SELECT * FROM spfli INTO TABLE @FINAL(spfli). 
 
TYPES group_keys TYPE STANDARD TABLE OF spfli-carrid WITH EMPTY KEY. 
 
cl_demo_output=>display( 
  VALUE group_keys( 
    FOR GROUPS carrier OF wa IN spfli 
    GROUP BY wa-carrid 
    ASCENDING 
    WITHOUT MEMBERS 
    ( carrier ) ) ).
```

## Addition

`... INDEX INTO idx`

### Description

For each evaluated group, this addition sets the helper variable `idx` as follows:

- In the case of [representative bindings](abaploop_at_itab_group_by_binding.md), to the value that would be set by the addition `INDEX INTO` in evaluations using [`FOR ... IN itab`](abenfor_in_itab.md) for the representative line.

- In the case of [group key bindings](abaploop_at_itab_group_by_binding.md), the groups are counted from the value 1.

The same applies to the local data object `idx` as in the variant [`FOR ... IN itab`](abenfor_in_itab.md).

`idx` cannot be addressed in [`group_key`](abaploop_at_itab_group_by_key.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Grouping and sorting of an internal table with random numbers by the numbers and sorts it. The differences between the group number in `i` and the random number demonstrate the deviation from the uniform distribution.

``` abap
DATA itab TYPE TABLE OF i WITH NON-UNIQUE KEY table_line. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                         min  = 1 
                                         max  = 10 ). 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( rnd->get_next( ) ) ). 
 
DATA jtab LIKE itab. 
jtab = VALUE #( FOR GROUPS <fs> OF wa IN itab 
                    INDEX INTO i 
                    GROUP BY wa 
                    ASCENDING 
                ( i - <fs> ) ). 
 
cl_demo_output=>display( jtab ).
```

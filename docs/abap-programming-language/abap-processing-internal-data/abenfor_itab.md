---
title: "FOR, Table Iterations"
source_file: abenfor_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR, Table Iterations

## Syntax Forms

**[Read Lines of Internal Tables](abenfor_in_itab.md)**

``` abap
1. ... FOR wa|<fs> IN itab [INDEX INTO idx] [cond] [let_exp]  ...
```

**[Group Lines of Internal Tables](abenfor_groups_of.md)**

``` abap
2. ... FOR GROUPS [group|<group>] OF wa|<fs> IN itab 
          [INDEX INTO idx] [cond] 
          GROUP BY group_key 
          [ASCENDING|DESCENDING [AS TEXT]] 
          [WITHOUT MEMBERS] 
          [let_exp] ...
```

**[Read Group Members of Internal Tables](abenfor_in_group.md)**

``` abap
3. ... FOR { wa|<fs> IN GROUP group [INDEX INTO idx] [WHERE ( log_exp )] } 
        | { GROUPS OF 
            wa|<fs> IN GROUP group [INDEX INTO idx] [WHERE ( log_exp )] 
            GROUP BY group_key 
            [ASCENDING|DESCENDING [AS TEXT]] 
            [WITHOUT MEMBERS] } [let_exp] ...
```

[`cond`](abenfor_cond.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`cond`](abenfor_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`WHERE ( log_exp )`](abenfor_cond.md) · [`WHERE ( log_exp )`](abenfor_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`let_exp`](../abap-declarations/abaplet.md)

## Description

These syntax forms of an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) using [`FOR`](../abap-program-flow-logic/abenfor.md) perform [table iterations](../../abap-glossary/abentable_iteration_glosry.md).

- When used in a constructor expression with the reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md), these are known as [table reductions](../../abap-glossary/abentable_reduction_glosry.md).

- When used in a constructor expression with the instance operator [`NEW`](../abap-creating-objects-and-values/abennew_constructor_params_itab.md) or with the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) for internal tables, these are known as [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md).

A `FOR` expression like this evaluates the content of an internal table and its result can be used to construct the result of the wrapper constructor expression. The three variants of a `FOR` expression for internal tables work in the same way as the following variants of the statement [`LOOP AT itab`](abaploop_at_itab_variants.md):

- The first variant [`FOR ... IN itab`](abenfor_in_itab.md) works in the same way as the regular line variant [`LOOP AT itab`](abaploop_at_itab.md) without the addition `GROUP BY`.

- The second variant [`FOR GROUPS ... OF`](abenfor_groups_of.md) works in the same way as the variant for grouping lines with the addition [`GROUP BY`](abaploop_at_itab_group_by.md).

- The third variant [`FOR ... IN GROUP`](abenfor_in_group.md) works in the same way as the variant [`LOOP AT GROUP`](abaploop_at_group.md) for [member loops](../../abap-glossary/abenmember_loop_glosry.md).

The variables or field symbols declared in the `FOR` expressions are local here. The local data from all outer `FOR` expressions can be used when their values are defined. As an option, `LET` expressions [`let_exp`](../abap-declarations/abaplet.md) can be specified to define local helper fields at the end of each `FOR` expression that can be used in the context of the `FOR` loop. The helper fields are filled in every iteration step.

The system field `sy-tabix` is not set by a `FOR` expression. The addition `INDEX INTO` can be used instead.

## Hints

- Multiple consecutive `FOR` expressions with different variants (including the [conditional iteration](../abap-program-flow-logic/abenfor_conditional.md)) can be specified in a constructor expression. These expressions then work in the same way as nested loops.

- The clearing or replacement of the complete table body of the internal table that is currently processed in a `FOR` expression is not allowed. Any attempt leads to the runtime error `TABLE_FREE_IN_LOOP`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Generation of an internal table `jtab` from an internal table `itab` using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md). Generation of a text string `str` from the internal table `jtab` using a [table reduction](../../abap-glossary/abentable_reduction_glosry.md). The result in `str` is the character string `1, 9, 25`.

``` abap
TYPES itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(itab) = 
  VALUE itab( ( 1 ) ( 3 ) ( 5 ) ). 
 
FINAL(jtab) = 
  VALUE itab( FOR wa IN itab ( ipow( base = wa exp = 2 ) ) ). 
 
FINAL(str) = 
  REDUCE string( INIT s = `` 
                 FOR wa IN jtab 
                 NEXT s = COND #( WHEN s = `` THEN |{ wa }| 
                 ELSE |{ s }, { wa }| ) ).
```

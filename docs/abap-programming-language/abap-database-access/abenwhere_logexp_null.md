---
title: "sql_cond - IS NULL"
source_file: abenwhere_logexp_null.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - IS NULL

## Syntax

``` abap
... operand IS [NOT] NULL ...  
```

## Description

This relational expression is true if the value of the operand `operand` is (is not) the [null value](../../abap-glossary/abennull_value_glosry.md).

The following applies to `operand`:

- [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

- In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](abapselect_aggregate.md) can also be used.

- Unlike in other relational expressions, the data type can also be [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Hints

- The relational expression `IS [NOT] NULL` is the only expression for which the result is true or false when the operand contains the null value. The result is unknown for all other possible relational expressions in a condition [`sql_cond`](abenasql_cond.md) when one of the operands in question contains the null value. This concerns in particular also expressions specified as operands when their result is the null value. This is especially true for the [null expression `NULL`](abensql_null.md) that contains the null value by definition.

- The expression `IS [NOT] NULL` must not be confused with the expression [`IS [NOT] INITIAL`](abenwhere_logexp_initial.md).

- The relational expression with the predicate syntax `IS [NOT] NULL` must not be confused with the expression [`NULL`](abensql_null.md).

- Null values can also be evaluated using a [null indicator](../../abap-glossary/abennull_indicator_glosry.md).

- `IS [NOT] NULL` can be used to check [LOBs](../../abap-glossary/abenlob_glosry.md) and [geodata types](../../abap-glossary/abengeo_data_type_glosry.md). As in all other relational expressions, operands of the data types [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comparison of the results of an inner and a left outer [join](../../abap-glossary/abenjoin_glosry.md). The row with null values produced by the left outer join is removed again by the `WHERE` condition with `IS NOT NULL`, so the results are the same.

``` abap
DELETE FROM demo_join1. 
INSERT demo_join1 FROM TABLE @( VALUE #( 
  ( a = 'a1' b = 'b1' c = 'c1'  d = 'd1' ) 
  ( a = 'a2' b = 'b2' c = 'c2'  d = 'd2' ) ) ). 
 
DELETE FROM demo_join2. 
INSERT demo_join2 FROM TABLE @( VALUE #( 
  ( d = 'd1' e = 'e1' f = 'f1'  g = 'g1'  h = 'h1' ) ) ). 
 
SELECT * 
       FROM demo_join1 AS d1 
         INNER JOIN demo_join2 AS d2 
           ON d1~d = d2~d 
       INTO TABLE @FINAL(result1). 
 
SELECT * 
       FROM demo_join1 AS d1 
         LEFT OUTER JOIN demo_join2 AS d2 
           ON d1~d = d2~d 
       WHERE d2~d IS NOT NULL 
         AND CAST( NULL AS CHAR( 2 ) ) IS NULL 
       INTO TABLE @FINAL(result2). 
 
ASSERT result1 = result2.
```

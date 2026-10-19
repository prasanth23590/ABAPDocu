---
title: "CDS DDL - DDIC-Based View, cds_cond"
source_file: abencds_conditional_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond

## Syntax

``` abap
... rel_expr 
  | [NOT] cds_cond [AND|OR cds_cond] ...  
```

## Description

Logical expression `cds_cond` for formulating a condition in ABAP CDS. A logical expression is either a single relational expression `rel_exp`, or an expression composed of the Boolean operators `NOT`, `AND`, `OR` and one or more logical expressions, in which parentheses are possible. An atomic component of a compound logical expression is always one relational expression.

Possible relational expressions `rel_expr` from which a condition `cds_cond` can be constructed:

- Comparisons with [comparison operators](abencds_cond_expr_comp_v1.md)

- Interval comparisons using [`BETWEEN`](abencds_cond_expr_betw_v1.md)

- Pattern comparisons using [`LIKE`](abencds_cond_expr_like_v1.md)

- Checks on the [null value](../../abap-glossary/abennull_value_glosry.md) using [`IS NULL`](abencds_cond_expr_null_v1.md)

- Checks on the [initial value](../../abap-glossary/abeninitial_value_glosry.md) using [`IS INITIAL`](abencds_cond_expr_initial_v1.md)

The Boolean operators work as follows:

- `NOT` negates the result of the following condition.

- An `AND` combination is true if both combined conditions are true.

- An `OR` combination is true if at least one of the combined conditions is true.

The operator `NOT` has a stronger binding than `AND`, which itself has a stronger binding than `OR`. This produces implicit parentheses, which can be overridden by explicit parentheses.

In SQL, the order in which two expressions are evaluated that are combined by `AND` is not defined. Results can be different on different database platforms.

## Hint

If multiple expressions are combined by `AND`, rules such as the following are not reliable: If one expression is false, then the following expressions are no longer evaluated. For example a condition `col1 <> 0 AND col2 / col1 > 1` can raise an exception. To avoid such exceptions, `CASE` expressions can be used.

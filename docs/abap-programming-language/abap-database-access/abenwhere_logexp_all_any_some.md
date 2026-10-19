---
title: "sql_cond - ALL, ANY, SOME"
source_file: abenwhere_logexp_all_any_some.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements > sql_cond - Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - ALL, ANY, SOME

## Syntax

``` abap
... operand operator [ALL|ANY|SOME] ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...  
```

[`operator`](abenwhere_logexp_compare.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

## Description

Comparison of an operand `operand` with the result set of a [subquery](../../abap-glossary/abensubquery_glosry.md). The clauses in the subquery [`subquery_clauses`](abenwhere_logexp_subquery.md) must represent a scalar subquery. The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply to specifying clauses.

Any [SQL expressions](abapsql_expr.md) except [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified for `operand`. In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can also be used.

`operator` stands for a [comparison operator](abenwhere_logexp_compare.md). Result sets can be single row or multirow.

### Single Row Result Set

If the result set of the subquery defined by the clause [`subquery_clauses`](abenwhere_logexp_subquery.md) contains only one row, the comparison can be performed without specifying `ALL`, `ANY`, or `SOME`. The expression is true if the corresponding comparison of the value of the operand `operand` with the result of the scalar subquery `subquery` returns *true*. If the result set for the subquery contains multiple rows, a catchable exception is raised when the statement is executed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the flights with the most passengers.

``` abap
SELECT * 
       FROM sflight 
       WHERE seatsocc = ( SELECT MAX( seatsocc ) 
                                 FROM sflight ) 
       INTO TABLE @FINAL(flights).
```

### Multirow Result Set

If the result set of the subquery defined by the clause [`subquery_clauses`](abenwhere_logexp_subquery.md) contains more than one row, `ALL`, `ANY`, or `SOME` must be specified.

- If using `ALL`, the expression is true if the comparison is true for all rows in the result set of the scalar subquery `subquery`.

- If the addition `ANY` or `SOME` is used, the expression is true if the comparison is true for at least one of the rows in the result set of the subquery.

## Hint

The equality operator (`=` or `EQ`) in conjunction with `ANY` or `SOME` acts like [`IN subquery`](abenwhere_logexp_operand_in.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the customer numbers of the customers who made the most bookings.

``` abap
SELECT customid, COUNT( * ) 
       FROM sbook 
       GROUP BY customid 
       HAVING COUNT( * ) >= ALL ( SELECT COUNT( * ) 
                                         FROM sbook 
                                         GROUP BY customid ) 
       INTO (@FINAL(id), @FINAL(cnt)). 
  ... 
ENDSELECT.
```

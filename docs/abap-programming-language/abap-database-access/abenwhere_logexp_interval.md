---
title: "sql_cond - BETWEEN"
source_file: abenwhere_logexp_interval.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - BETWEEN

## Syntax

``` abap
... operand [NOT] BETWEEN operand1 AND operand2 ...  
```

## Description

This relational expression is true if the content of the operand `operand` is (is not) between the values of the operands `operand1` and `operand2`.

- The following applies to `operand`:

  - Numeric [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

  - A column [`col`](abenabap_sql_columns.md) specified individually cannot be numeric.

  - In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can also be used.

- The following applies to `operand1` and `operand2`:

  - Elementary [SQL operands](abensql_operands.md) can be specified.

  - Columns [`col`](abenabap_sql_columns.md) must have a numeric data type and they need to be prefixed with the name of the [data source](abapselect_data_source.md) using `~`. In this case, `operand` must also be numeric.

  - Numeric [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

  - [Cast expressions](abensql_cast.md) can be specified.

  - The content of ABAP objects, that is, untyped literals, host variables, and host expressions must match the data type of `operand` in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md).

The interval limits are included. The comparison is made in the same way as for

... [`[NOT] ( operand >= operand1 AND operand <= operand2 )`](abenwhere_logexp_compare.md) ...

and the corresponding rules and notes apply.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads all flights within the next 30 days.

``` abap
FINAL(today) = cl_demo_date_time=>get_system_date( ). 
FINAL(date) = CONV d( today + 30 ). 
 
SELECT carrid, connid, fldate 
       FROM sflight 
       WHERE fldate BETWEEN @today AND @date 
       INTO TABLE @FINAL(sflight_tab).
```

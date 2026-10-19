---
title: "sql_exp - cds_scalar_func"
source_file: abensql_cds_scalar_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - cds_scalar_func

## Syntax

``` abap
... cds_scalar_func( p1 = sql_exp1, p2 = sql_exp2  ... )  .
```

## Description

Calls a [SQL-based scalar function](../../abap-glossary/abencds_sql_scalar_glosry.md) in ABAP SQL. The actual parameters passed to the formal parameters of the scalar function can be any SQL expression `sql_exp` with an appropriate type. The result is the return value of the CDS scalar function.

## Hints

- Specifying a SQL-based scalar function always means specifying a [SQL expression](abapsql_expr.md). SQL-based scalar functions can only be called in operand positions for which SQL expressions are possible.

- SQL-based scalar functions cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- [Analytical scalar function](../../abap-glossary/abencds_ana_scalar_glosry.md) cannot be used as operands in ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet uses a scalar function described in the topic [`DEFINE SCALAR FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md).

``` abap
DELETE FROM demo_expressions. 
 
INSERT demo_expressions FROM @( VALUE #( id = 'X' ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS demo_cds_scalar_helloworld( ) 
       WHERE id = 'X' 
       INTO @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[`sql_exp` - CDS Scalar Function](abensql_expr_cds_scalar_abexa.md)

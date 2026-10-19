---
title: "sql_exp - sql_searched_case"
source_file: abensql_searched_case.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_case"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_searched_case

## Syntax

``` abap
... CASE WHEN sql_cond1 THEN result1 
        [WHEN sql_cond2 THEN result2] 
        [WHEN sql_cond3 THEN result3] 
          ... 
        [ELSE resultn|sql_null] 
    END ...  
```

[`sql_cond1`](abenabap_sql_expr_logexp.md) · [`sql_cond2`](abenabap_sql_expr_logexp.md) · [`sql_cond3`](abenabap_sql_expr_logexp.md)

## Description

[Complex case distinction](../../abap-glossary/abencomplex_case_glosry.md) (searched case) in ABAP SQL. This SQL expression evaluates logical expressions [`sql_cond1`](abenabap_sql_expr_logexp.md), [`sql_cond2`](abenabap_sql_expr_logexp.md), ... and produces the operand `result` as a result after the first `THEN` for which the logical expression is true. If no logical expressions are true, the `result` specified after `ELSE` is selected. If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md). The null value can be specified explicitly by the [null expression](abensql_null.md) `sql_null`. The results `result1`, `result2`, ... can be any [SQL expressions](abapsql_expr.md).

The results must be compatible with each other in such a way that a common result type can be determined: The data types `result1`, `result2`, ... must be either the same or the data type must be able to fully represent the value of all other data types. If this is not the case, a static specification raises a syntax error and a dynamic specification raises an exception of the class `CX_SY_DYNAMIC_OSQL_SEMANTICS`. The result has the dictionary type of the specification with the greatest value range.

If a complex `CASE` is used in a [condition](abenasql_cond.md) of an ABAP SQL statement, the [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source of a query or of the target of a write statement cannot be used as the operand of a `WHEN` condition due to [implicit client handling](abenabap_sql_client_handling.md).

## Hints

- The SQL standard specifies the result of a case distinction, but not the order in which the operands are evaluated. Potentially, the result may even be evaluated before the associated condition. This means that any expressions specified as operands must have no side effects and must not be dependent on each other.

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), operands are evaluated in parallel for reasons of optimization. The order in which the operands are evaluated is undefined. If an exception is raised when an operand is evaluated, the entire case distinction is canceled. In this case, it does not matter which conditions apply and the order in which they are listed. For this reason, it is advisable not to use any exceptions in expressions specified as operands. For more information, see the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- If the case distinction is processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md), the order of processing is preserved and there is no termination when an operand is evaluated whose condition is not true.

- The [relational expressions](abenabap_sql_expr_logexp.md) that can be used after `CASE` are a subset of the [relational expressions for statements](abenabap_sql_stmt_logexp.md), but also allow [SQL expressions](abapsql_expr.md) as operands on the right side.

- A client column can be used as an operand only if [implicit client handling](abenabap_sql_client_handling.md) is disabled using the obsolete addition `CLIENT SPECIFIED` for the query or the write statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Evaluation of the column `FLTIME` in a complex `CASE`.

``` abap
SELECT FROM spfli 
       FIELDS carrid, 
              connid, 
              cityfrom, 
              cityto, 
              CASE WHEN fltime < 100 THEN 'short' 
                   WHEN fltime BETWEEN 100 AND 300 THEN 'medium' 
                   ELSE 'long' 
              END AS fltime 
       ORDER BY carrid, connid 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[SQL Expressions, Complex `CASE`](abensql_expr_searched_case_abexa.md)

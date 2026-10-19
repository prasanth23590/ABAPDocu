---
title: "sql_exp - sql_simple_case"
source_file: abensql_simple_case.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_case"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_simple_case

## Syntax

``` abap
... CASE sql_exp 
         WHEN sql_exp1 THEN result1 
        [WHEN sql_exp2 THEN result2] 
         ... 
        [ELSE resultn|sql_null] 
    END ...  
```

## Description

[Simple case distinction](../../abap-glossary/abensimple_case_glosry.md) (simple case) in ABAP SQL. This SQL expression compares the values of the operand `sql_exp` with the operands `sql_exp1`, `sql_exp2`, ..., and returns the operand `result` as the result after the first `THEN` for which the comparison is true. If no matches are found, the `result` specified after `ELSE` is selected. If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md). The null value can be specified explicitly by the [null expression](abensql_null.md) `sql_null`.

The operands `sql_exp`, `sql_exp1`, `sql_exp2`, ..., and the results `result1`, `result2`, ... can be any [SQL expressions](abapsql_expr.md). They can have any dictionary types except `ACCP`, `LCHR`, `LRAW`, `PREC`, `RAWSTRING`, `STRING`, and `GEOM_EWKB`.

The data type of the operand `sql_exp` must be [comparable](abenwhere_logexp_compare_types.md) with the data types of the operands `sql_exp1`, `sql_exp2`, .... If this is not the case, a static specification raises a syntax error and a dynamic specification raises an exception of the class `CX_SY_DYNAMIC_OSQL_SEMANTICS`. The results must also be compatible to produce a common result type: The data types `result1`, `result2`, ... must be either the same or the data type must be able to completely represent the value of all other data types. The result has the dictionary type of the specification with the greatest value range.

If an operand of a comparison has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of this comparison is unknown.

## Hints

- The SQL standard specifies the result of a case distinction, but not the order in which the operands are evaluated. Potentially, the result may even be evaluated before the associated condition. This means that any expressions specified as operands must have no side effects and must not be dependent on each other.

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), operands are evaluated in parallel for reasons of optimization. The order in which the operands are evaluated is undefined. If an exception is raised when an operand is evaluated, the entire case distinction is canceled. In this case, it does not matter which conditions apply and the order in which they are listed. For this reason, it is advisable not to use any exceptions in expressions specified as operands. For more information, see the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- If the case distinction is evaluated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md), the order of processing is preserved and there is no termination when an operand is evaluated whose condition is not true.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the distances specified in miles to kilometers. The conversion factor is specified as the host variable whose value has already been calculated using an SQL expression in a `SELECT` statement. This task could also be performed more generally in a subquery of a [`WITH`](abapwith.md) statement.

``` abap
SELECT SINGLE 
       FROM t006 
       FIELDS division( zaehl,nennr * 1000,2 ) AS factor 
       WHERE msehi = 'MI' 
       INTO @FINAL(factor). 
 
SELECT FROM spfli 
       FIELDS carrid, 
              connid, 
              cityfrom, 
              cityto, 
              CASE distid 
                   WHEN 'MI' THEN distance * @factor 
                   ELSE distance 
              END AS distance, 
       'KM' AS distid 
       WHERE distid = 'KM' OR distid = 'MI' 
       ORDER BY carrid, connid 
       INTO TABLE @FINAL(result). 
cl_demo_output=>display( result ). 
```

## Executable Example

[SQL Expressions, Simple `CASE`](abensql_expr_case_string_abexa.md)

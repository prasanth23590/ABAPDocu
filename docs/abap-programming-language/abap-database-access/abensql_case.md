---
title: "sql_exp - sql_case"
source_file: abensql_case.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_case

## Syntax Forms

**[Simple Case Distinction](abensql_simple_case.md)**

``` abap
1. ... CASE sql_exp 
           WHEN sql_exp1 THEN result1 
          [WHEN sql_exp2 THEN result2] 
           ... 
          [ELSE resultn|sql_null] 
      END ...
```

**[Complex Case Distinction](abensql_searched_case.md)**

``` abap
2. ... CASE WHEN sql_cond1 THEN result1 
          [WHEN sql_cond2 THEN result2] 
          [WHEN sql_cond3 THEN result3] 
            ... 
          [ELSE resultn|sql_null] 
      END ...
```

## Description

Case distinction in ABAP SQL. Either a [simple case distinction](abensql_simple_case.md) (simple case) or a [complex case distinction](abensql_searched_case.md) (searched case).

## Hints

- Specifying a case distinction always means specifying an [SQL expression](abapsql_expr.md). Case distinctions can only be specified for operand positions in which SQL expressions are possible.

- A conflict between SQL language element `CASE` and a column named `CASE` cannot occur because the ABAP Dictionary does not allow a column with this name to be created. However, if a column with this name does exist, it must be prefixed with the escape character [`!`](../abap-operands/abennames_escaping.md) when it is specified in an ABAP SQL statement.

- A maximum of 10 case distinctions can be nested with `CASE`.

- A case distinction can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and internal tables with [`FROM @itab`](abapselect_itab.md).

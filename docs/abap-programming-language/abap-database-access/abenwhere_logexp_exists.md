---
title: "sql_cond - EXISTS"
source_file: abenwhere_logexp_exists.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - EXISTS

## Syntax

``` abap
... EXISTS ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...  
```

[`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

## Description

Checks the result set of a subquery. The relational expression is true if the result set of the subquery defined by the clauses [`subquery_clauses`](abenwhere_logexp_subquery.md) contains at least one row. The expression is possible for any result sets that can be defined using subquery clauses [`subquery_clauses`](abenwhere_logexp_subquery.md). The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses.

## Hint

The specified columns in the [`SELECT` list](abapselect_list.md) of the subquery are not important for `EXISTS`. Therefore, explicit lists are not useful. It is recommended that one [literal](abenabap_sql_literals.md) is specified as the only column.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads all available flights leaving from New York from the DDIC database table `SFLIGHT` to the internal table `free_flights`.

``` abap
DATA city TYPE spfli-cityfrom VALUE 'NEW YORK'. 
 
SELECT * 
       FROM sflight AS s 
       WHERE seatsocc < s~seatsmax AND 
             EXISTS ( SELECT 'X' 
                             FROM spfli 
                             WHERE carrid   =  s~carrid AND 
                                   connid   =  s~connid AND 
                                   cityfrom = @city ) 
       INTO TABLE @FINAL(free_flights).
```

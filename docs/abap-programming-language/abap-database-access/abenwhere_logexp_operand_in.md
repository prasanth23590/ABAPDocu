---
title: "sql_cond - operand IN ( ... )"
source_file: abenwhere_logexp_operand_in.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements > sql_cond - IN ( ... )"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - operand IN ( ... )

## Syntax

``` abap
... operand [NOT] IN { (operand1[, operand2[, ...]]) } 
                   | { ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) } ...  
```

[`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

### Variant

[1. `... operand [NOT] IN (operand1[, operand2[, ...]])`](abenwhere_logexp_operand_in.html#variant-1)

[2. `... operand [NOT] IN ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`](abenwhere_logexp_operand_in.md#variant-2)

## Overview

### Description

Checks whether the value of an operand `operand` matches a value in a set of values specified in parentheses. The set of values can be specified as follows:

- Using a comma-separated list of individual literals or host variables.

- Using a [scalar subquery](../../abap-glossary/abenscalar_subquery_glosry.md).

The following applies to `operand`:

- [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

- [Aggregate expressions](abapselect_aggregate.md) can also be used in a [`HAVING`](abaphaving_clause.md) clause.

## Variant 1

`... operand [NOT] IN (operand1[, operand2[, ...]])`

### Description

This relational expression is true if the value of the operand `operand` matches (does not match) the content of one of the operands `operand1, operand2 ...` in a parenthesized comma-separated value list.

The following applies to `operand1`, `operand2`, ...:

- [Literals](abenabap_sql_literals.md) and [host variables](abenabap_sql_host_variables.md) can be specified.

- The content of untyped literals and host variables must match the data type of `operand` in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md).

It is also possible to specify just one operand `operand1` in the parentheses. Blanks can be placed after the opening parenthesis, in front of the closing parenthesis, and after the commas. If blank is placed after the opening parenthesis, there must also be a blank in front of the closing parenthesis.

### Hint

No columns [`col`](abenabap_sql_columns.md), no [host expressions](abenabap_sql_host_expressions.md), and no other [SQL expressions](abapsql_expr.md) can be specified here on the right side. SQL expressions are, however, specified in the variant of `IN` with an [operand list](abenwhere_logexp_list_in.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the bookings in which the class is not in the value range (C - Business, F - First, Y - Economy) of the corresponding domain in the ABAP Dictionary.

``` abap
SELECT * 
       FROM sbook 
       WHERE class NOT IN ('C','F','Y') 
       INTO TABLE @FINAL(sbook_tab). 
 
IF sy-subrc = 0. 
  "Error handling 
ENDIF.
```

## Variant 2

`... operand [NOT] IN ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`

### Description

This relational expression is true if the value of the operand `operand` is (is not) contained in the result set of a [subquery](../../abap-glossary/abensubquery_glosry.md). The clauses in the subquery [`subquery_clauses`](abenwhere_logexp_subquery.md) must represent a [scalar subquery](../../abap-glossary/abenscalar_subquery_glosry.md). The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the geographical latitude and longitude of a city from the DDIC database table `SGEOCITY`, where this city is the city of origin of a flight in the DDIC database table `SPFLI`.

``` abap
DATA: carr_id TYPE spfli-carrid VALUE 'LH', 
      conn_id TYPE spfli-connid VALUE '400'. 
 
SELECT SINGLE city, latitude, longitude 
       FROM sgeocity 
       WHERE city IN ( SELECT cityfrom 
                              FROM spfli 
                              WHERE carrid = @carr_id AND 
                                    connid = @conn_id ) 
       INTO (@FINAL(city), @FINAL(lati), @FINAL(longi)).
```

---
title: "sql_cond - ( operand1, operand2, ... ) IN ( ... )"
source_file: abenwhere_logexp_list_in.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements > sql_cond - IN ( ... )"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - ( operand1, operand2, ... ) IN ( ... )

## Syntax

``` abap
... ( operand1, operand2[, ...] ) IN { ( ( operand11, operand21[, ...] )[, 
                                         ( operand12, operand22[, ...] )] ) } 
                                   | { ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) } ...  
```

[`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

### Variant

[1. `... ( operand1, operand2[, ...] ) IN ( ( operand11, operand21[, ...] )[, ...] ) )`](abenwhere_logexp_list_in.md#variant-1)

[2. `... ( operand1, operand2[, ...] ) IN ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`](abenwhere_logexp_list_in.md#variant-2)

## Overview

### Description

Checks whether the values of the operands `operand1`, `operand2`, ... specified on the left side as a parenthesized comma-separated list match a value tuple from a set of value tuples specified in parentheses. The set of value tuples can be specified as follows:

- Using a comma-separated list of parenthesized tuples `( operand11, operand21[, ...] )`, `( operand12, operand22[, ...] )`, ...

- Using a [subquery](../../abap-glossary/abensubquery_glosry.md).

The following applies to `operand1`, `operand2`, ...:

- Any [SQL expressions](abapsql_expr.md) except [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

- [Aggregate expressions](abapselect_aggregate.md) can be used in a [`HAVING`](abaphaving_clause.md) clause.

At least one blank must be placed after every opening parenthesis and in front of every closing parenthesis. The comma-separated list `operand1`, `operand2`, ... must contain at least two elements.

### Hint

The operator `NOT` is currently not supported.

## Variant 1

`... ( operand1, operand2[, ...] ) IN ( ( operand11, operand21[, ...] )[, ...] ) )`

### Description

This relational expression is true if the value of every operand `operand1`, `operand2`, ... on the left side matches the content of the operand of a parenthesized value tuple `( operand11, operand21[, ...] )` in the same place on the right side. Every value tuple must contain the same number of elements as the comma-separated list `operand1`, `operand2`, ... on the left side. The value tuples themselves are specified as a parenthesized comma-separated list, which can also consist of only one element.

`operand11`, `operand21`, ... of a value tuple can be any [SQL expressions](abapsql_expr.md) except [window expressions](abapselect_over.md). [Aggregate expressions](abapselect_aggregate.md) are currently only possible in a [`HAVING`](abaphaving_clause.md) clause. [Literals](abenabap_sql_literals.md), [host variables](abenabap_sql_host_variables.md), and [host expressions](abenabap_sql_host_expressions.md) are handled like [elementary SQL expressions](abensql_elem.md), which means they are mapped to dictionary types instead of being converted.

### Hints

- This variant of `IN` can also be expressed using individual comparisons combined using `AND` and `OR` and the [comparison operator `=`](abenwhere_logexp_compare.md), but SQL expressions are not possible on the right side. This is also how this variant of `IN` is distinguished from the variant with a [single operand](abenwhere_logexp_operand_in.md).

- When this variant of `IN` is used and not only column specifications are used on the left side of `IN` and not only host variables or expressions are used on the right side, ABAP SQL bypasses [table buffering](../../abap-glossary/abentable_buffering_glosry.md) for buffering types [single record buffering](abenbuffer_single_buffering.md) and [generic buffering](abenbuffer_generic_buffering.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The query finds all rows in which the values of the three columns on the left side match one of the two value tuples on the right side.

``` abap
DATA cityfrom TYPE spfli-cityfrom VALUE 'Frankfurt'. 
DATA cityto   TYPE spfli-cityto   VALUE 'New York'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field = cityfrom 
  )->add_field( CHANGING field = cityto 
  )->request( ). 
cityfrom =  to_upper( cityfrom ). 
cityto   =  to_upper( cityto ). 
 
SELECT * 
       FROM spfli 
       WHERE ( carrid, cityfrom, cityto ) 
         IN ( ( 'LH', @cityfrom, @cityto ), 
              ( 'UA', @cityfrom, @cityto ) ) 
       INTO TABLE @FINAL(itab). 
 
cl_demo_output=>display( itab ).
```

## Variant 2

`... ( operand1, operand2[, ...] ) IN ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`

### Description

This relational expression is true if the value of every operand `operand1`, `operand2`, ... on the left side matches the content of the result set of the [subquery](../../abap-glossary/abensubquery_glosry.md). The result set of the subquery must contain the same number of elements in the same position as in the comma-separated list `operand1`, `operand2`, ... on the left side. The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, the rules for [`query_clauses`](abapunion_clause.md) apply.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the country of origin and the country of destination from the DDIC database table `SPFLI` for all flights which cost more than USD 100. The condition 'price \> 100' is checked in a subquery that reads from the DDIC database table `SFLIGHT`.

``` abap
SELECT countryfr, countryto 
       FROM spfli 
       WHERE ( carrid,connid ) IN ( SELECT carrid,connid 
                                           FROM sflight 
                                           WHERE price > 100 ) 
       INTO TABLE @FINAL(result).
```

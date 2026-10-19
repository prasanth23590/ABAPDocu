---
title: "sql_cond - IN range_tab"
source_file: abenwhere_logexp_seltab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - IN range_tab

## Syntax

``` abap
... operand [NOT] IN @range_tab ...  
```

## Description

This variant of the operator `IN` checks whether the operands on the left side match a [ranges condition](../../abap-glossary/abenranges_condition_glosry.md) in a [ranges table](../../abap-glossary/abenranges_table_glosry.md). The relational expression is true if the value of the operand `operand` is (is not) in the result set described in the rows of the [ranges table](../../abap-glossary/abenranges_table_glosry.md) `range_tab` specified as a [host variable](abenabap_sql_host_variables.md).

- The following applies to `operand`:

  - [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

  - In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can also be used.

- Any internal table whose row type corresponds to that of a [ranges table](../../abap-glossary/abenranges_table_glosry.md) can be specified for the ranges table `range_tab`.

The ranges table is evaluated in the same way as in [comparison expressions](../abap-program-flow-logic/abenlogexp_select_option.md), with the difference that any comparisons using the operators `CP` and `NP` are transformed into [`LIKE` conditions](abenwhere_logexp_like.md) for which the ABAP SQL escape character *\#* is defined. The pattern after `CP` or `NP` is transformed to a pattern for `LIKE` as follows:

- If the ABAP SQL wildcard characters *%* and *\_* are contained in the pattern, the *\#* escape character is inserted in front of these characters.

- Any wildcard characters *\** and *+* that are not prefixed with the escape character *\#* are transformed to the ABAP SQL wildcard characters *%* and *\_*.

- Any *\#* escape characters that do not prefix themselves or the ABAP SQL wildcard characters *%* and *\_* are removed.

If the ranges table is initial, the expression `IN range_tab` is always true. This overrides the general rule that the result of a [relational expression](abenabap_sql_stmt_logexp.md) is unknown if an operand has the [null value](../../abap-glossary/abennull_value_glosry.md).

The content of the columns `LOW` and `HIGH` in the ranges table must match the data type of the operand in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md).

## Hints

- `LIKE` conditions resulting from `CP` or `NP` are case-sensitive, which is not the case in ABAP comparison expressions.

- If no conditions are specified apart from `IN range_tab`, all rows of the data source are selected if the ranges table is initial.

- The conditions specified in the ranges table are passed by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) to the database as SQL statement input values. The maximum number of input values depends on the database system and is usually between 2000 and 10000. If the maximum number is exceeded an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

- For an initial ranges table, no condition is passed to the database and therefore, the result is always true.

- If the ranges table contains invalid values, an uncatchable exception is raised.

- No [host expression](abenabap_sql_host_expressions.md) can be specified on the right side whose result represents a ranges table.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A ranges table is filled as follows and the order of the rows is not important:

``` abap
SIGN  OPTION  LOW              HIGH 
--------------------------------------- 
I     EQ      01104711 
I     BT      10000000         19999999 
I     GE      90000000 
E     EQ      10000911 
E     BT      10000810         10000815 
E     CP      1%2##3#+4++5*
```

When used in `sql_cond`, this generates the following combination of relational expressions:

``` abap
... ( ID = '01104711'                      OR 
      ID BETWEEN '10000000' AND '19999999' OR 
      ID >= '90000000' )                     AND 
    ID <> '10000911'                         AND 
    ID NOT BETWEEN '10000810' AND '10000815' AND 
    ID NOT LIKE '1#%2##3+4__5%' ESCAPE '#'   ...
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a ranges table in a `WHERE` clause.

``` abap
DATA airlines TYPE RANGE OF spfli-carrid. 
 
airlines = VALUE #( 
  ( sign = 'I' option = 'EQ' low = 'AA' ) 
  ( sign = 'I' option = 'BT' low = 'SQ' high = 'ZZ' ) ). 
 
SELECT carrid, connid, cityfrom, cityto 
       FROM spfli 
       WHERE carrid IN @airlines 
       INTO TABLE @FINAL(flights). 
 
cl_demo_output=>display( flights ).
```

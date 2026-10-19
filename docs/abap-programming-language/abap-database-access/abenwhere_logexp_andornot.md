---
title: "sql_cond - AND, OR, NOT, ( )"
source_file: abenwhere_logexp_andornot.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - AND, OR, NOT, ( )

## Syntax

``` abap
... sql_cond1 AND sql_cond2 AND sql_cond3 ...  

... sql_cond1 OR sql_cond2 OR sql_cond3 ...  

... NOT sql_cond ...  

... ( sql_cond ) ...  
```

## Description

Any number of logical [`sql_cond`](abenabap_sql_stmt_logexp.md) expressions can be combined into one logical expression using `AND` or `OR` and the result of a logical expression can be negated using `NOT`. The same [rules](../abap-program-flow-logic/abenlogexp_boole.md) apply as to general logical expressions, with the difference that the operator `NOT` cannot be specified more than once in direct succession. In particular, the explicit use of `( )` parentheses is also possible.

In SQL, the order in which two expressions are evaluated that are combined by `AND` is not defined. Results can be different on different database platforms.

The following additional rules apply to logical expressions whose result is unknown because an operand has the [null value](../../abap-glossary/abennull_value_glosry.md):

- An `AND` combination of two unknown expressions or a true expression with an unknown expression produces an unknown expression. An `AND` combination of a false expression with an unknown expression produces a false expression.

- An `OR` combination of two unknown expressions or one false expression with an unknown expression produces an unknown expression. An `OR` combination of one true and one unknown expression produces a true expression.

- The negation of an unknown expression with `NOT` produces an unknown expression.

## Hints

- In particular, the expressions specified [dynamically](abenwhere_logexp_dynamic.md) as `(cond_syntax)` are also possible as logical expressions within a combination or negation.

- The operator `NOT` in a `WHERE` clause cannot be supported by an [index](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_index.md). For this reason, it is best to use the reverse comparison operator instead of `NOT`, for example `col <= dobj` instead of `NOT col > dobj`.

- Two `NOT` operators can only be specified consecutively if they are separated by an opening parenthesis. If not, an even number of consecutive `NOT` operators has the same meaning as none, and an odd number of consecutive `NOT` operators has the same meaning as a single `NOT` and should be used accordingly.

- If multiple expressions are combined using `AND`, rules such as the following cannot be relied on: If one expression is false, then the following expressions are not evaluated any more. For example, a condition `col1 <> 0 AND col2 / col1 > 1` can lead to an exception. To avoid such exceptions, `CASE` expressions can be used.

- The rules for unknown expressions establish an important difference to the rules for a false expression. While a single unknown expression behaves mostly the same as a false expression in the sense that both are not true, the results of applying the operators can be unexpected. Especially an unknown expression cannot be made true by applying `NOT`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads flights from Frankfurt to Los Angeles or San Francisco.

``` abap
SELECT * 
       FROM spfli 
       WHERE cityfrom = 'FRANKFURT' AND 
             ( cityto = 'LOS ANGELES' OR 
               cityto = 'SAN FRANCISCO' ) 
       INTO TABLE @FINAL(spfli_tab).
```

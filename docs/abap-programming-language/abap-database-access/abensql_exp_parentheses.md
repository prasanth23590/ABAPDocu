---
title: "sql_exp - ( )"
source_file: abensql_exp_parentheses.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - ( )

## Syntax

``` abap
... ( sql_exp ) ...  
```

[`sql_exp`](abapsql_expr.md)

## Description

Every full SQL expression [`sql_exp`](abapsql_expr.md) can be enclosed in parentheses `( ... )`. There must be a blank after the opening parenthesis and in front of the closing parenthesis. Parenthesis affect the priority with which expressions are evaluated. Parenthesis levels are evaluated from inside out and from left to right. The result of a parenthesis is the result of the outermost expression in the parenthesis.

## Hints

- Using parentheses always means specifying an [SQL expression](abapsql_expr.md). Parentheses can only be used for operand positions for which SQL expressions are possible. This particularly applies to placing parentheses around [elementary SQL expressions](abensql_elem.md). Without parentheses, they can also be used in specific operand positions in which no SQL expressions are possible.

- Parentheses are used especially in [arithmetic expressions](abensql_arith.md) to affect the priority of calculations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Parenthesizing of a subtraction as the dividend in a division.

``` abap
SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              fldate, 
       ( CAST( seatsmax AS FLTP ) -  CAST( seatsocc AS FLTP ) ) 
       / CAST( seatsmax AS FLTP ) AS availability 
       ORDER BY carrid, connid, fldate 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

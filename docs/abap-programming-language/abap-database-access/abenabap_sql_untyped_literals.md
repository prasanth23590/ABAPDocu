---
title: "ABAP SQL - Untyped Literals"
source_file: abenabap_sql_untyped_literals.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem > ABAP SQL - literal"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Untyped Literals

## Syntax

``` abap
... { [+|-]n[n[n[...]]] 
    | 'c[c[c[...]]]' | `[c[c[c[...]]]]` } ...  
```

## Description

[Untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md) in ABAP SQL correspond to general [ABAP literals](../abap-declarations/abenliteral.md) and the same rules apply. In ABAP SQL, untyped literals can be specified in read positions of ABAP SQL statements where [host variables](abenabap_sql_host_variables.md) are possible. The following applies, depending on the operand position:

- If an untyped literal is specified in an operand position in which it is handled like an [elementary SQL expression](abensql_elem.md), the corresponding rules apply and the untyped literal is mapped to a dictionary type and evaluated accordingly on the database.

- If an untyped literal is specified in an operand position in which it is not handled like an SQL expression, it is handled like a [host variable](abenabap_sql_host_variables.md). If necessary, an ABAP specific type conversion takes place and a [lossless assignment](../abap-processing-internal-data/abapmove_exact.md) to the data type required in the operand position must be possible. Non-matching untyped literals produce, syntax errors.

## Hints

- While general ABAP supports untyped literals only, ABAP SQL also supports [typed literals](abenabap_sql_typed_literals.md) which should be preferred.

- In some operand positions in which untyped literals are allowed and [host expressions](abenabap_sql_host_expressions.md) are forbidden, an untyped literal can be specified with the syntax `@( literal )` and is handled as an untyped literal and not as an expression.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of data from the DDIC database table `SPFLI` using ABAP SQL. The read rows are specified as untyped text literals in the `WHERE` condition. After `UP TO`, an untyped numeric literal specifies the maximum number of rows to read.

``` abap
SELECT FROM spfli 
       FIELDS 'Lufthansa' AS name, 
              cityfrom, 
              cityto 
       WHERE carrid = 'LH'  AND 
             countryfr = 'DE' 
       INTO TABLE @FINAL(wa) 
       UP TO 10 ROWS.
```

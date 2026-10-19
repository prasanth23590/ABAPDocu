---
title: "Chained Statements"
source_file: abenchained_statements.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Chained Statements

## Syntax

``` abap
initial_part: remaining_part1, 
              remaining_part2, 
              ... .  
```

## Description

Consecutive statements that have the same initial part can be combined into in a single chained statement as follows:

- The identical initial part `initial_part` is specified once and closed with a colon (`:`).

- The remaining parts `remaining_part1`, `remaining_part2`, ... are then listed separately, divided by commas (`,`), and closed with a period (`.`).

When the syntax is checked and the program is executed, a chained statement is handled in the same way as the corresponding sequence of individual ABAP statements.

## Hints

- The identical starting parts are not limited to the keyword.

- When using chained statements, it must be ensured that no syntactically correct statements with incorrect behavior are created by mistake. The risk of this is especially high for more complex statements, as well as when using [expressions](../../abap-glossary/abenexpression_glosry.md) or function calls where chained statements should be avoided all together.

- If further colons are listed after the first colon of a chained statement, they are handled like blanks.

---
title: "table_exp - Write Positions"
source_file: abentable_exp_lhs.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Write Positions

Table expressions and their [chainings](abentable_exp_chaining.md) can be specified as [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) in [result positions](../../abap-glossary/abenresult_position_glosry.md). The result of a table expression in these positions is always a temporary field symbol.

- If a single table expression is specified, or a [chaining](abentable_exp_chaining.md) whose last position is a table expression, the entire line found is modified in the write position.

- If a [chaining](abentable_exp_chaining.md) is specified whose last position is a structure component after a structure component selector, this component is modified in the write position.

In the case of writes performed on the temporary field symbol, the same rules apply as to a field symbol assigned a table line using [`READ TABLE ASSIGNING`](abapread_table_outdesc.md). More specifically, the read-only character of key fields must be respected. Table expressions that return a line of a sorted table or hashed table to write positions such as the left side of an assignment or as actual parameters for output parameters always raise an exception.

## Hint

The constructor operators `VALUE` and `REF` used to control the [result](abentable_exp_result.md) of the table expression cannot be used in write positions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An internal table is prefilled with initial lines, which are overwritten with a value in the [`DO`](../abap-program-flow-logic/abapdo.md) loop.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 5 ( ) ). 
 
DO lines( itab ) TIMES. 
  itab[ sy-index ] = sy-index ** 2. 
ENDDO.
```

## Executable Example

[Table Expressions, Write Position](abentable_exp_itab_changing_abexa.md)

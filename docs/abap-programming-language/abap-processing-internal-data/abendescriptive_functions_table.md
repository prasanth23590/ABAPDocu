---
title: "itab_func - lines"
source_file: abendescriptive_functions_table.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Built-in Functions (itab_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab_func - lines

## Syntax

``` abap
... lines( arg ) ...  
```

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) function `lines` returns the number of lines in an internal table. The argument `arg` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md) that expects an internal table. The return value has the type `i`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The number of lines in an internal table filled from a database table must match the number of lines on the database.

``` abap
SELECT carrid 
       FROM scarr 
       INTO TABLE @FINAL(itab). 
 
SELECT COUNT(*) 
       FROM scarr 
       INTO @FINAL(lines). 
 
ASSERT lines( itab ) = lines.
```

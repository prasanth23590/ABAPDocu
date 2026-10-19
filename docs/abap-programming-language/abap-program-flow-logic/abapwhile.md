---
title: "WHILE"
source_file: abapwhile.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Loops"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WHILE

## Syntax

``` abap
WHILE log_exp   
  [statement_block]   
ENDWHILE.  
```

[`log_exp`](abenlogexp.md)

## Description

Conditional loop. The statements `WHILE` and `ENDWHILE` define a control structure that can contain a complete [statement block](../../abap-glossary/abenstatement_block_glosry.md) `statement_block`. After `WHILE`, any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) [`log_exp`](abenlogexp.md) can follow.

The statement block is repeated as long as the logical expression is true, or until it is exited with one of the statements to exit loops. In particular, the statement [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md) is intended for exiting a loop completely. Within the statement block, the system field `sy-index` contains the number of previous loop passes, including the current pass. In nested loops, `sy-index` always refers to the current loop.

## Hints

- If `WHILE` loops are used to construct values or fill internal tables, they can usually be expressed more elegantly using conditional iterations with [`FOR`](abenfor_conditional.md) in constructor expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of an internal table with 100 lines. A [`FOR`](abenfor.md) expression can now also be used for that purpose.

``` abap
DATA itab TYPE TABLE OF i. 
 
WHILE lines( itab ) < 100. 
  itab = VALUE #( BASE itab ( sy-index ) ). 
ENDWHILE.
```

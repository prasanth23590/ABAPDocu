---
title: "CHECK, loop"
source_file: abapcheck_loop.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Loops"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CHECK, loop

## Syntax

``` abap
CHECK log_exp.  
```

[`log_exp`](../abap-program-flow-logic/abenlogexp.md)

## Description

If the statement `CHECK` is listed in a [loop](../../abap-glossary/abenloop_glosry.md) and `log_exp` is false, the statement `CHECK` immediately terminates the current loop pass and the program continues with the next loop pass. Any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) can be specified for [`log_exp`](../abap-program-flow-logic/abenlogexp.md).

## Hints

- Within a loop, `CHECK log_exp` has the same effect as:

  `IF NOT log_exp. CONTINUE. ENDIF.`

- Outside a loop, the statement `CHECK` exits the current [processing block](../../abap-glossary/abenprocessing_block_glosry.md) (see [`CHECK`](abapcheck_processing_blocks.md)), however it is recommended that `CHECK` is used inside loops only.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Termination of a loop pass using `CHECK` if the loop index `sy-index` is an odd number.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA remainder TYPE i. 
DO 20 TIMES. 
  remainder = sy-index MOD 2. 
  CHECK remainder = 0. 
  out->write_text( |{ sy-index }| ). 
ENDDO. 
out->display( ).
```

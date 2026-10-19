---
title: "EXIT, loop"
source_file: abapexit_loop.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Loops"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXIT, loop

## Syntax

``` abap
EXIT.  
```

## Description

If the `EXIT` statement is listed within a [loop](../../abap-glossary/abenloop_glosry.md), it exits the loop by terminating the current loop pass. The program flow resumes after the closing statement of the loop.

## Hint

Outside of a loop, the statement `EXIT` exits the current [processing block](../../abap-glossary/abenprocessing_block_glosry.md) (see [`EXIT` - Processing Block](abapexit_processing_blocks.md)). `EXIT`, however, it should only be used within loops.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exit of a loop using `EXIT` if the loop index `sy-index` is greater than a number `limit`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA limit TYPE i VALUE 10. 
DO. 
  IF sy-index > limit. 
    EXIT. 
  ENDIF. 
  out->write( |{ sy-index } | ). 
ENDDO. 
 
out->display( ).
```

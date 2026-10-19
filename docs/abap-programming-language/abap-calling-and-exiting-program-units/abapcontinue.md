---
title: "CONTINUE"
source_file: abapcontinue.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Loops"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONTINUE

## Syntax

``` abap
CONTINUE.  
```

## Description

The statement `CONTINUE` may only be used in [loops](../../abap-glossary/abenloop_glosry.md). If it is used, the current loop pass is terminated immediately and the program flow is continued with the next loop pass.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exit of a loop pass using `CONTINUE` if the loop index `sy-index` is an odd number.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA remainder TYPE i. 
DO 20 TIMES. 
  remainder = sy-index MOD 2. 
  IF remainder <> 0. 
    CONTINUE. 
  ENDIF. 
  out->write_text( |{ sy-index }| ). 
ENDDO. 
 
out->display( ).
```

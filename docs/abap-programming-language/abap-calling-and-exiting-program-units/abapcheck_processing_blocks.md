---
title: "CHECK, processing_block"
source_file: abapcheck_processing_blocks.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CHECK, processing_block

## Syntax

``` abap
CHECK log_exp.  
```

[`log_exp`](../abap-program-flow-logic/abenlogexp.md)

## Description

If the statement `CHECK` is listed outside a [loop](../../abap-glossary/abenloop_glosry.md) and `log_exp` is false, it terminates the current [processing block](../../abap-glossary/abenprocessing_block_glosry.md). Any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) can be specified for [`log_exp`](../abap-program-flow-logic/abenlogexp.md).

After the processing block is exited, the runtime framework behaves in the same way as when the [processing block is exited in the regular way](abenend_processing_blocks.md). In particular, the output parameters of procedures are passed on to the bound actual parameters.

## Hints

- In a procedure (a method, function module, or subroutine), `CHECK log_exp` works outside a loop in the same way as:

  `IF NOT log_exp. RETURN. ENDIF.`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows a case where `CHECK` can be used outside a loop. At the start of a procedure, a prerequisite for executing the procedure is checked and the procedure exited if the check is not successful. In this case, the procedure must not be executed in the background.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    CHECK sy-batch IS INITIAL. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    demo=>meth( ). 
  ENDMETHOD. 
ENDCLASS.
```

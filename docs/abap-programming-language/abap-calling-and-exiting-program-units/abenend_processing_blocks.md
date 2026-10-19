---
title: "Regular Exiting of a Processing Block"
source_file: abenend_processing_blocks.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Regular Exiting of a Processing Block

A processing block is terminated regularly when its end is reached.

Depending on the processing block that is exited, the runtime framework behaves as follows:

- In [procedures](../../abap-glossary/abenprocedure_glosry.md), the program returns to the position after the procedure call. The output parameters for which [pass by values](../../abap-glossary/abenpass_by_value_glosry.md) are defined are passed to the bound actual parameters.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output before, during, and after execution of a procedure.

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
    cl_demo_output=>write( `In procedure` ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    cl_demo_output=>write( `Before procedure` ). 
    demo=>meth( ). 
    cl_demo_output=>display( `After procedure` ). 
  ENDMETHOD. 
ENDCLASS.
```

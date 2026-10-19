---
title: "EXIT, processing_block"
source_file: abapexit_processing_blocks.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXIT, processing_block

## Syntax

``` abap
EXIT.  
```

## Description

If the statement `EXIT` is outside a [loop](../../abap-glossary/abenloop_glosry.md), it immediately terminates the current [processing block](../../abap-glossary/abenprocessing_block_glosry.md).

After the processing block is exited, the runtime framework behaves in the same way as when the [processing block is exited in a regular way](abenend_processing_blocks.md). In particular, the output parameters of procedures are passed on to the bound actual parameters.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The method `meth` contains two `EXIT` statements. Whereas the first statement exits the `LOOP` loop, the second statement exits the entire method. Therefore, the `RETURN` statement should be used instead of the second `EXIT` statement.

``` abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE string, 
    col2 TYPE string, 
  END OF line, 
  itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth IMPORTING char TYPE string 
                                 itab TYPE itab. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    LOOP AT itab INTO FINAL(wa). 
      FIND char IN wa-col1 RESPECTING CASE. 
      IF sy-subrc = 0. 
        EXIT. 
      ENDIF. 
    ENDLOOP. 
    FIND to_upper( char ) IN wa-col2 RESPECTING CASE. 
    IF sy-subrc <> 0. 
      EXIT.                   "works as RETURN here! 
    ENDIF. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(itab) = VALUE itab( 
        ( col1 = `aaaa` col2 = `AAAA` ) 
        ( col1 = `bbbb` col2 = `XXXX` ) 
        ( col1 = `cccc` col2 = `CCCC` ) ). 
    demo=>meth( char = `b` 
                itab = itab ). 
  ENDMETHOD. 
ENDCLASS.
```

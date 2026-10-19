---
title: "REPLACE SECTION OF"
source_file: abapreplace_in_position.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > REPLACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE SECTION OF

## Syntax

``` abap
REPLACE SECTION [OFFSET off] [LENGTH len] OF dobj WITH new   
                [IN {CHARACTER|BYTE} MODE].  
```

### Addition

[`... IN {CHARACTER|BYTE} MODE`](abapreplace_in_position.md#addition)

## Overview

### Description

In position-based replacements, the section in `dobj` is replaced starting at the offset specified in `off` for the length specified in `len` with the content of the operand `new`. The same applies to the additions `OFFSET` and `LENGTH` as to [`FIND SECTION OF`](abapfind_section_of.md).

## Addition

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is performed. Depending on the processing type, `dobj` and `new` must be character-like or byte-like.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `FIND` determines the offset and length of the first word *know* in the data objects `text1` and `text2` and to replace this section in a position-based manner in `text1` and `text2` with *should know that*. After the first `REPLACE` statement, `text1` contains the complete content *I should know that you know* and `sy-subrc` contains 0. After the second `REPLACE` statement, `text2` contains the truncated content *I should know that* and `sy-subrc` contains 2.

``` abap
DATA: text1 TYPE string, 
      text2 TYPE c LENGTH 18, 
      off   TYPE i, 
      len   TYPE i. 
 
text1 = text2 = 'I know you know'. 
 
FIND 'know' IN text1 MATCH OFFSET off 
                     MATCH LENGTH len. 
 
REPLACE SECTION OFFSET off LENGTH len OF: 
                text1 WITH 'should know that', 
                text2 WITH 'should know that'.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Specified offset or length violated the bounds of the string `dobj`.

  *Runtime error:* `REFI_WRONG_SECTION`

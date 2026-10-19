---
title: "Offset/Length Specifications"
source_file: abendata_process_fields_abexa.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands > Offset/Length Specifications for Substring Access"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Offset/Length Specifications

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how substrings can be accessed using offset/length specifications.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_data_process_fields DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_data_process_fields IMPLEMENTATION. 
  METHOD main. 
 
    DATA time TYPE t VALUE '172545'. 
 
    DATA: f1(8)  TYPE c VALUE 'ABCDEFGH', 
          f2(20) TYPE c VALUE '12345678901234567890'. 
 
    DATA: f3(8) TYPE c VALUE 'ABCDEFGH', 
          f4(8) TYPE c. 
    DATA: o TYPE i VALUE 2, 
          l TYPE i VALUE 4. 
 
    DATA: text(20)  TYPE c, 
          number(8) TYPE c VALUE '123456', 
          offset    TYPE i VALUE 8, 
          length    TYPE i VALUE 12. 
 
    out->begin_section( `Example 1` 
      )->write( time 
      )->write( time+2(2) 
      )->write( time+2(4) ). 
    CLEAR time+2(4). 
    out->write( time ). 
 
    out->next_section( `Example 2` ). 
    f2+6(5) = f1+3(5). 
    out->write( f1 
      )->write( f2 ). 
 
    out->next_section( `Example 3` ). 
    f4 = f3. 
    out->write( f4 ). 
    f4 = f3+o(l). 
    out->write( f4 ). 
    f4+o(l) = f3. 
    out->write( f4 ). 
    CLEAR f4. 
    f4+o(l) = f3. 
    out->write( f4 ). 
    f4+o(l) = f3+o(l). 
    out->write( f4 ). 
 
    out->next_section( `Example 4` ). 
 
    text+offset(length) = |{ number(6) ALIGN = LEFT WIDTH = length }|. 
    out->write( text ). 
    CLEAR text. 
    text+offset(length) = |{ number(6) ALIGN = CENTER WIDTH = length }|. 
    out->write( text ). 
    CLEAR text. 
    text+offset(length) = |{ number(6) ALIGN = RIGHT WIDTH = length }|. 
    out->write( text ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the first part, the minutes of a time field are selected by specifying an offset. Then the minutes and seconds are set to their initial values by specifying an offset in the `CLEAR` statement.

In the second part, the five digit sequence `78901` from the field `f2` is replaced with `DEFGH` from `f1` by specifying offsets and lengths.

In the third part, assignments are used. First, the content of `f1` is assigned to `f2` without offset specifications. The same is then done with offsets and lengths for `f1`. The next three assignments overwrite the content of `f2` with an offset of 2. Note that `f2` is padded on the right with blanks, in accordance with the conversion rule for source type `c`.

In the fourth part, string templates are used. The first six places of the field `number` are written left-aligned, centered, and right-aligned to the last 12 places of the `text` field

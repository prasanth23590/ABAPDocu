---
title: "SHIFT"
source_file: abapshift.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SHIFT

## Syntax

``` abap
SHIFT dobj [ {[places][direction]} | deleting ]   
           [IN {CHARACTER|BYTE} MODE].  
```

[`places`](abapshift_places.md) · [`direction`](abapshift_direction.md) · [`deleting`](abapshift_deleting.md)

### Addition

[`... IN {CHARACTER|BYTE} MODE`](abapshift.md#addition)

## Overview

### Description

This statement shifts the content of a variable `dobj`. In [`places`](abapshift_places.md), the number of places to be shifted can be specified and in [`direction`](abapshift_direction.md), the direction of the shift. In [`deleting`](abapshift_deleting.md), the characters to be deleted from the data object by the shift can be specified. If no additions are specified, the content is shifted to the left by one place.

By default, free places created by the shift are filled with blanks or hexadecimal 0 for data objects of fixed length, depending on the processing method. Data objects of type `string` or `xstring` are truncated by the number of shifted places when shifted to the left and lengthened by the number of shifted places when shifted to the right.

In character string processing, the trailing blanks are respected for data objects `dobj` of fixed length.

### Hint

To shift a string in an operand position, [shift functions](abenshift_functions.md) that cover part of the functions of the statement `SHIFT` can be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The shortest form of the statement `SHIFT`. The content of `str` is moved one place to the left.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `0123456789`. 
SHIFT str. 
out->write( str ). 
 
out->display( ).
```

## Addition

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is performed. Depending on the processing method, `dobj`, [`substring`](abapshift_places.md) and [`mask`](abapshift_deleting.md) must be character-like or byte-like.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Shifting a byte string one byte to the left.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(xstr) = CONV xstring( `AABBCCDDEEFF` ). 
SHIFT xstr IN BYTE MODE. 
out->write( xstr ). 
 
out->display( ).
```

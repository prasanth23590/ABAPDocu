---
title: "SHIFT, direction"
source_file: abapshift_direction.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > SHIFT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SHIFT, direction

## Syntax

``` abap
... [LEFT|RIGHT] [CIRCULAR] ...  
```

### Addition

[1. `... LEFT|RIGHT`](abapshift_direction.md#addition-1)

[2. `... CIRCULAR`](abapshift_direction.md#addition-2)

## Addition 1

`... LEFT|RIGHT`

### Description

The shift direction is defined using `LEFT` or `RIGHT`. If neither of the additions is specified, `LEFT` is used implicitly. If the data object `dobj` is a string and the addition `CIRCULAR` is not specified, it is truncated when shifted to the left by the places shifted and extended accordingly when shifted to the right.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of text field `text` is moved one place to the right, which means that the digit *9* is lost. The data type `string` would extend the string by one space.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(text) = '0123456789'. 
SHIFT text RIGHT. 
out->write( text ). 
 
out->display( ).
```

## Addition 2

`... CIRCULAR`

### Description

Using the addition `CIRCULAR`, the content shifted from the data object to the left or to the right, is inserted again in the places that become available on the opposite side. If the addition `CIRCULAR` is specified, data objects of the type `string` or `xstring` are not truncated or extended. Instead, they are handled like data objects of fixed length.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example is a variant of the second example under [`places`](abapshift_places.md). Using the addition `CIRCULAR` makes the result *you know I know*.

``` abap
DATA text TYPE string VALUE `I know you know `. 
 
SHIFT text UP TO 'you' LEFT CIRCULAR.
```

---
title: "Byte-Like Source Fields"
source_file: abenbyte_source_fields.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Byte-Like Source Fields

- [`x`](abenconversion_type_x.md)

- [`xstring`](abenconversion_type_xstring.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the byte field from hexadecimal content `FFFF` to different target types. The type-compliant formatted output is `65535`, `FFFF`, `FFFF`, `01800605`. The date of type `d` is 65535 days since 01.01.0001.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA hex TYPE x LENGTH 2 VALUE `FFFF`. 
 
out->write( 
  |i:       { CONV i( hex ) }\n| && 
  |string:  { CONV string( hex ) }\n| && 
  |xstring: { CONV xstring( hex ) }\n| && 
  |d:       { CONV d( hex ) }\n| ). 
 
out->display( ).
```

---
title: "Character-Like Source Fields"
source_file: abencharacter_source_fields.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Character-Like Source Fields

- [`c`](abenconversion_type_c.md)

- [`n`](abenconversion_type_n.md)

- [`string`](abenconversion_type_string.md)

The following special formats must be respected in conversions of character-like data objects to numeric data objects:

- [Representation of Numeric Values in Character-Like Fields](abennumerical_value.md)

- [Representation of Time Stamps in Character-Like Fields](abents_value.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the text string `053000` to different target types. The type-compliant formatted output is `53000`, `0000053000`, `053000`, `053000`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA str TYPE string VALUE `053000`. 
 
TYPES n10 TYPE n LENGTH 10. 
out->write( 
  |i:           { CONV i( str ) }\n| && 
  |n LENGTH 10: { CONV n10( str ) }\n| && 
  |xstring:     { CONV xstring( str ) }\n| && 
  |t:           { CONV t( str ) }\n| ). 
 
out->display( ).
```

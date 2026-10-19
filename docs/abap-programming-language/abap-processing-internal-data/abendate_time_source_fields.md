---
title: "Date Fields, Time Fields, and Time Stamp Fields as Source Fields"
source_file: abendate_time_source_fields.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Date Fields, Time Fields, and Time Stamp Fields as Source Fields

- [`d`](abenconversion_type_d.md)

- [`t`](abenconversion_type_t.md)

- [`utclong`](abenconversion_type_utclong.md)

## Hints

- The conversion rules are designed in such a way that operands of the types `d` and `t` behave like character-like operands in character-like operand positions and behave numerically in numeric operand positions.

- In [substring access](../abap-operands/abenoffset_length.md) to an operand of the type `d` or `t`, the substring is handled like an operand of the type `n` and the corresponding conversion rules apply.

- Operands of the type `utclong` can only be converted to the types `c` and `string`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of a target field with the value *144414* to different target types. The type-compliant formatted output is `53054`, `144414`, `CF3E`. The number 53054 corresponds to the number of seconds since midnight for the time 144414.

``` abap
DATA time TYPE t VALUE '144414'. 
 
cl_demo_output=>display( 
  |i:       { CONV i( time ) }\n| && 
  |string:  { CONV string( time ) }\n| && 
  |xstring: { CONV xstring( time ) }\n| ).
```

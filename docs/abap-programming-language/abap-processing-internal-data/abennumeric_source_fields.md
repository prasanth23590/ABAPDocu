---
title: "Numeric Source Fields"
source_file: abennumeric_source_fields.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Source Fields

- [`i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)

- [`p`](abenconversion_type_p.md)

- [`decfloat16`, `decfloat34`](abenconversion_type_decfloat.md)

- [`f`](abenconversion_type_f.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the integer 100 to different target types. The type-compliant formatted output is `1E+02`, `0000000100`, `64`, `000140`.

``` abap
DATA num TYPE i VALUE 100. 
 
TYPES n10 TYPE n LENGTH 10. 
cl_demo_output=>display( 
  |decfloat34:  { CONV decfloat34( num ) STYLE = SCIENTIFIC }\n| && 
  |n LENGTH 10: { CONV n10( num ) }\n| && 
  |xstring:     { CONV xstring( num ) }\n| && 
  |t:           { CONV t( num ) }\n| ).
```

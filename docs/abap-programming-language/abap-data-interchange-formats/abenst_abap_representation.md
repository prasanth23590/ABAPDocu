---
title: "ST - Representation of ABAP Values"
source_file: abenst_abap_representation.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Representation of ABAP Values

Some ST statements require ABAP values `value` to be specified, depending on the [built-in ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) as a function of the type. In two cases, however, `value` can also be specified directly. The initial value can always be specified regardless of the ABAP type.

| **Data Type**                                                          | **Representation**                           |
|------------------------------------------------------------------------|----------------------------------------------|
| Initial value (all ABAP types)                                         | `Initial`                                    |
| 4 byte integer (ABAP type `i`)                                         | `I(value) \| value`                          |
| 8 byte integer (ABAP type `int8`)                                      | `INT8(value)`                                |
| Binary floating point numbers (ABAP type `f`)                          | `F('value')`                                 |
| Byte strings (ABAP types `x` and `xstring`)                            | `X('value')`                                 |
| Decimal floating point numbers (ABAP types `decfloat16`, `decfloat34`) | `DECFLOAT16('value')`, `DECFLOAT34('value')` |
| Packed numbers (ABAP type `p`)                                         | `P(value)`                                   |
| Numeric text fields (ABAP type `n`)                                    | `N('value')`                                 |
| Character strings (ABAP types `c` and `string`)                        | `C('value') \| 'value'`                      |
| Date fields and time fields (ABAP types `d` and `t`)                   | `D('value')`, `T('value')`                   |
| Time stamp fields (ABAP type `utclong`)                                | `UTCLONG('value')`                           |

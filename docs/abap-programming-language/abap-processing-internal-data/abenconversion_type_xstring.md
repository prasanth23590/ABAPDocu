---
title: "Source Field Type xstring"
source_file: abenconversion_type_xstring.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Byte-Like Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type xstring

- [Numeric Target Fields](abenconversion_type_xstring.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_xstring.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_xstring.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_xstring.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                              |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | Content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the source field has length 0, the target field is assigned the value 0. |
| `p`                        | Content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the source field has length 0, the target field is assigned the value 0. |
| `decfloat16`, `decfloat34` | Content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the source field has length 0, the target field is assigned the value 0. |
| `f`                        | Content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the source field has length 0, the target field is assigned the value 0. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *123456789*. The first three bytes `FFFFFF` of the source field are ignored.

``` abap
DATA hex TYPE xstring VALUE 'FFFFFF075BCD15'. 
 
FINAL(result) = CONV i( hex ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the target field is padded with blank characters.              |
| `n`        | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the target field is padded with the character *0*.             |
| `string`   | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the length of the target field is also 0 after the assignment. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `FFFFFF075BCD15`. All bytes of the source field are included in the conversion.

``` abap
DATA hex TYPE xstring VALUE 'FFFFFF075BCD15'. 
 
FINAL(result) = CONV string( hex ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the target field is padded with the hexadecimal 0.             |
| `xstring`  | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the length of the target field is also 0 after the assignment. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `FFFFFF075BCD15`. All bytes of the source field are included in the conversion.

``` abap
DATA hex TYPE xstring VALUE 'FFFFFF075BCD15'. 
 
FINAL(result) =  hex.
```

## Date/Time Fields as Target Fields

| **&#x200E;Target** | **Conversion**                                                                                                                                                                                 |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`                | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the target field is padded with the character *0*. |
| `t`                | The content is handled in the same way as a [source field of type `x`](abenconversion_type_x.md). If the length of the source field is 0, the target field is padded with the character *0*. |
| `utclong`          | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`.                                                                                               |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value of the date field resulting from the conversion is `20170111` corresponding to 736341 days since 01/01/0001. The first three bytes `FFFFFF` of the source field are ignored.

``` abap
DATA hex TYPE xstring VALUE 'FFFFFF000B3C55'. 
 
FINAL(result) = CONV d( hex ).
```

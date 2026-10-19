---
title: "Source Field Type n"
source_file: abenconversion_type_n.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Character-Like Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type n

The conversion rules are designed in such a way that when data objects of type [`n`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) are assigned to character-like data objects they behave like character-like objects, and when assigned to numeric data objects they behave numerically. Valid data for data objects of type `n` is in the form of digit-only strings. When assigning valid data to numeric data objects, the numeric value of the string of digits is assigned to the target object. The conversion rules, however, also allow the assignment of numeric text fields that contain invalid data. The latter is not recommended.

- [Numeric Target Fields](abenconversion_type_n.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_n.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_n.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_n.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                 |
|----------------------------|------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) |
| `p`                        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) |
| `decfloat16`, `decfloat34` | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) |
| `f`                        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) |

### Hint

The class [`CL_ABAP_DECFLOAT`](abencl_abap_decfloat_doc.md) contains the methods `READ_DECFLOAT34` and `READ_DECFLOAT16` for converting character strings into decimal floating point numbers. The exceptions of these methods are more significant than those of a regular assignment. Furthermore, the methods return a return value that reveals information about the rounding that was performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *0*.

``` abap
DATA num4 type n LENGTH 4 VALUE IS INITIAL. 
 
FINAL(result) = CONV i( num4 ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                      |
| `n`        | The characters in the source field are passed right-aligned to the target field. Trailing blanks are passed. If the target field is longer than the characters passed, the field is padded with *0* characters on the left. If the target field is shorter, the characters are cut off on the left. |
| `string`   | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                      |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `0000001234`.

``` abap
DATA num4 TYPE n LENGTH 4 VALUE '1234'. 
 
TYPES num10 TYPE n LENGTH 10. 
FINAL(result) = CONV num10( num4 ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content of the source field is first converted to data type `i` (see above) and then to type `x` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).       |
| `xstring`  | The content of the source field is first converted to data type `i` (see above) and then to type `xstring` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `04D2`.

``` abap
DATA num4 TYPE n LENGTH 4 VALUE '1234'. 
 
FINAL(result) = CONV xstring( num4 ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                   |
|------------|--------------------------------------------------------------------------------------------------|
| `d`        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)   |
| `t`        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)   |
| `utclong`  | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value of the date field resulting from the conversion is the unchanged value *20000101* of the source field.

``` abap
DATA num8 TYPE n LENGTH 8 VALUE '20000101'. 
 
FINAL(result) = CONV d( num8 ).
```

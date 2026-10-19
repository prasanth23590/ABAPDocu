---
title: "Source Field Type t"
source_file: abenconversion_type_t.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Date Fields, Time Fields, and Time Stamp Fields as Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type t

The conversion rules are designed in such a way that, when data objects of time type [`t`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) are assigned to character-like data objects, they behave like character-like objects and numerically in assignments to numeric data objects. The latter is the basis for calculating time in arithmetic expressions. If the content of data objects of type `t` is time specifications in the format *hhmmss*, and the values only correspond to valid times of day (*hh* is between 00 and 23, *mm* and *ss* are between 00 and 59), the value assigned to a numeric data object corresponds to the number of seconds since midnight.

Although the conversion rules actually allow the assignment of time fields that contain invalid data, this is not recommended.

- [Numeric Target Fields](abenconversion_type_t.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_t.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_t.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_t.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | If the source field contains only digits, the content is interpreted as a time specification in the format *hhmmss* from which the value *hh\*3600+mm\*60+ss* is calculated and then converted to the internal representation of the corresponding integer. If the source field does not only contain digits, the target field is given the value 0. If the [value range](../../abap-glossary/abenvalue_range_glosry.md) of the internal data types `b` and `s` is not sufficient, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. |
| `p`                        | If the source field contains only digits, the content is interpreted as a time specification in the format *hhmmss* from which the value *hh\*3600+mm\*60+ss* is calculated and then converted to the internal representation of a packed number. If the value range of the target field is too small, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. If the source field does not contain only digits, the target field receives the value 0.                                                                  |
| `decfloat16`, `decfloat34` | If the source field contains only digits, the content is interpreted as a time specification in the format *hhmmss* from which the value *hh\*3600+mm\*60+ss* is calculated and then converted to the internal representation of a decimal floating point number with [scaling](../../abap-glossary/abenscale_glosry.md) of 0. If the source field does not contain only digits, the target field is given the value 0.                                                                                                                           |
| `f`                        | If the source field contains only digits, the content is interpreted as a time specification in the format *hhmmss* from which the value *hh\*3600+mm\*60+ss* is calculated and then converted to the internal representation of a binary floating point number. If the source field does not contain only digits, the target field is given the value 0.                                                                                                                                                                       |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *66656*. This is the number of seconds of the specified time since midnight.

``` abap
DATA tim TYPE t VALUE '183056'. 
 
FINAL(result) = CONV i( tim ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                           |
| `n`        | The characters in the source field are inserted in the target field, left-aligned. Trailing blanks in the source field are transferred. If the target field is longer than the source field, it is padded on the right with the character *0*. If the target field is shorter, it is truncated on the right. |
| `string`   | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                           |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is *18*. Four characters *3056* are cut off on the right.

``` abap
DATA tim TYPE t VALUE '183056'. 
 
TYPES n2 TYPE n LENGTH 2. 
FINAL(result) = CONV n2( tim ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content of the source field is first converted to data type `i` (see above) and then to type `x` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).       |
| `xstring`  | The content of the source field is first converted to data type `i` (see above) and then to type `xstring` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is *010460*. This is the integer 66655 or the number of seconds since midnight.

``` abap
DATA tim TYPE t VALUE '183056'. 
 
FINAL(result) = CONV xstring( tim ).
```

## Date/Time Fields as Target Fields

| **&#x200E;Target** | **Conversion**                                                                                   |
|--------------------|--------------------------------------------------------------------------------------------------|
| `d`                | Not supported. Produces a syntax error or runtime error.                                         |
| `t`                | The content of the source field is transferred unconverted.                                      |
| `utclong`          | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The conversion of `t` to `d`, which is not known statically, is not supported and produces the runtime error `MOVE_NOT_SUPPORTED`.

``` abap
DATA(time) = cl_demo_date_time=>get_user_time( ). 
 
FIELD-SYMBOLS <fs> TYPE data. 
 
ASSIGN time TO <fs>. 
FINAL(result) = CONV d( <fs> ).
```

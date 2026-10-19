---
title: "Source Field Type d"
source_file: abenconversion_type_d.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Date Fields, Time Fields, and Time Stamp Fields as Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type d

The conversion rules are designed in such a way that when data objects of the date type [`d`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) are assigned to character-like data objects they behave like character-like objects and numerically in assignments to numeric data objects. The latter is the basis for date calculations in arithmetic expressions.

Only dates in the format *yyyymmdd* are valid for data objects of type `d` where *00010101* is the first valid value. The conversion rules, however, also allow the assignment of date fields that contain invalid data. The latter is not recommended.

- [Numeric Target Fields](abenconversion_type_d.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_d.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_d.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_d.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | If the source field contains a valid date in the format *yyyymmdd*, it is used to calculate the number of days since 01.01.0001, and this value is then converted to the internal representation of the corresponding integer. If the source field contains an invalid date, the target field is assigned the value 0. If the [value range](../../abap-glossary/abenvalue_range_glosry.md) for the internal data types `b` and `s` is insufficient, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. |
| `p`                        | If the source field contains a valid date in the format *yyyymmdd*, it is used to calculate the number of days since 01.01.0001, and this value is then converted to the internal representation of a packed number. If the value range of the target field is too small, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. If the source field contains an invalid date, the target field is assigned the value 0.                                                                 |
| `decfloat16`, `decfloat34` | If the source field contains a valid date in the format *yyyymmdd*, it is used to calculate the number of days since 01.01.0001, and this value is then converted to the internal representation of a decimal floating point number with a [scaling](../../abap-glossary/abenscale_glosry.md) of 0. If the source field contains an invalid date, the target field is assigned the value 0.                                                                                                                        |
| `f`                        | If the source field contains a valid date in the format *yyyymmdd*, it is used to calculate the number of days since 01.01.0001, and this value is then converted to the internal representation of a binary floating point number. If the source field contains an invalid date, the target field is assigned the value 0.                                                                                                                                                                      |

### Hints

- The conversion of a date into the number of days since 01.01.001 is designed in such a way that the transition from the Julian to Gregorian calendar is respected: 4.10.1582 results in 577,736 and 15.10.1582 in 577,737. Converting the dates for the nonexistent days between 5.10.1582 and 14.10.1582 produces the same result as converting the existing days from 15.10.1582 to 24.10.1582.

- The assignment of the values *00000000* and *00010101* to a numeric type produces the value 0 in each case. The [assignment](abenconversion_type_ibs.md) of the value 0 to a date field produces *00000000*. This means that the assignment of the value *00010101* to a numeric type is not reversible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *736341*. This is the number of days of the specified date since 01.01.0001.

``` abap
DATA dat TYPE d VALUE '20170111'. 
 
FINAL(result) = CONV i( dat ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                   |
| `n`        | The characters in the source field are passed left-aligned to the target field. Trailing blanks in the source field are passed. If the target field is longer than the source field, it is padded on the right with the character *0*. If the target field is shorter, it is truncated on the right. |
| `string`   | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md)                                                                                                                                                                                                   |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `2017`. Four characters `0111` are cut off on the right.

``` abap
DATA dat TYPE d VALUE '20170111'. 
 
TYPES n4 TYPE n LENGTH 4. 
FINAL(result) = CONV n4( dat ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content of the source field is first converted to data type `i` (see above) and then to type `x` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).       |
| `xstring`  | The content of the source field is first converted to data type `i` (see above) and then to type `xstring` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `0B3C55`. This is the integer 736341 or the number of days since 01.01.0001.

``` abap
DATA dat TYPE d VALUE '20170111'. 
 
FINAL(result) = CONV xstring( dat ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                   |
|------------|--------------------------------------------------------------------------------------------------|
| `d`        | The content of the source field is passed unconverted.                                           |
| `t`        | Not supported. Produces a syntax error or runtime error.                                         |
| `utclong`  | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The conversion of `d` to `t`, which is not known statically, is not supported and produces the runtime error `MOVE_NOT_SUPPORTED`.

``` abap
DATA(date) = cl_demo_date_time=>get_user_time( ). 
 
FIELD-SYMBOLS <fs> TYPE data. 
 
ASSIGN date TO <fs>. 
FINAL(result) = CONV t( <fs> ).
```

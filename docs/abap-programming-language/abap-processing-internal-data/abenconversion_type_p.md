---
title: "Source Field Type p"
source_file: abenconversion_type_p.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Numeric Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type p

If the program property [*fixed point arithmetic*](../../abap-glossary/abenfixed_point_arithmetic_glosry.md) is not set, the decimal separator in source fields with the type [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) is ignored, except in assignments to character-like target fields with the types `c` and `string`.

- [Numeric Target Fields](abenconversion_type_p.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_p.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_p.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_p.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | The value of the packed number is rounded commercially to an integer number. If this number is within the [value range](../../abap-glossary/abenvalue_range_glosry.md) for the data type `i`, (`b`, `s`), it is converted to the internal representation of the corresponding integer number. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                                              |
| `p`                        | The value of the packed number is rounded commercially to the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) of the target field. If this number is within the value range for the data type of the target field, it is converted to the internal representation of this packed number. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                       |
| `decfloat16`, `decfloat34` | The value of the packed number is converted into the internal format of a decimal floating point number. If the number of places for a target field of type `decfloat16` is greater than 16 when the assignment is performed, commercial rounding to 16 places is applied. If the mantissa of the target field is long enough, the [scaling](../../abap-glossary/abenscale_glosry.md) is set to the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) of the source field. An invalid value in the source field raises the catchable exception `CX_SY_CONVERSION_NO_NUMBER`. |
| `f`                        | The value of the packed number is converted into the internal format of a binary floating point number. If the decimal number cannot be represented as a binary floating point number, the nearest value is used. An invalid value in the source field produces undefined behavior.                                                                                                                                                                                                                                                                                |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value `8.1499999999999995E-01`.

``` abap
DATA pack TYPE p DECIMALS 3 VALUE '0.815'. 
 
FINAL(result) = CONV f( pack ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The value of the packed number is formatted in [commercial notation](abennumerical_value.md) and passed right-aligned to the target field. The character *-* is set in the last position for a negative value and a blank is set in the last place for a positive value. If the target field is longer than the string of digits, including the plus/minus sign, it is padded with blanks on the left. If it is too short, the number representation is moved to the right by one position for positive values. If the target field is still too short (and for negative values), it is truncated on the left and the character *\** is set in the first position of the target field. |
| `n`        | The value of the packed number is rounded commercially to an integer number. The absolute value is passed to the target field as a right-aligned string of digits. If the target field is longer than the string of digits, the field is padded with zeros on the left. If it is too short, the values on the left are cut off.                                                                                                                                                                                                                                                                                                                                                          |
| `string`   | The value of the packed number is formatted in [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md) and passed to the target field without gaps. The character *-* is set in the last position for a negative value and a blank is set in the last position for a positive value. The resulting length of the target field is determined by the number of digits, plus the places for the plus/minus sign and the decimal separator.                                                                                                                                                                                                                                               |

### Hint

If the number of decimal places in the source field is greater than the number of digits calculated from 2 x the length of `dobj` - 1, the corresponding number of zeros is inserted between decimal separators and digits in assignments to data objects of the types `c` and `string` and the longer string of digits is assigned.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `123.456-`.

``` abap
DATA pack TYPE p DECIMALS 3 VALUE '-123.456'. 
 
FINAL(result) = CONV string( pack ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content of the source field is first converted to data type `i` (see above) and then to type `x` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).       |
| `xstring`  | The content of the source field is first converted to data type `i` (see above) and then to type `xstring` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `0000007C` and matches the result of the conversion of the rounded number `124`.

``` abap
DATA pack TYPE p DECIMALS 3 VALUE '123.999'. 
 
TYPES hex TYPE x LENGTH 4. 
FINAL(result) = CONV hex( pack ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`        | The content of the source field is first converted to data type `i` (see above) and then to type `d` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |
| `t`        | The content of the source field is first converted to data type `i` (see above) and then to type `t` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |
| `utclong`  | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`.                                                                                                           |

### Hint

The method `TSTMP2UTCLONG` of the class [`CL_ABAP_TSTMP`](abencl_abap_tstmp.md) converts UTC [time stamps in packed numbers](abentime_stamps_packed.md) to [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md) of the type `utclong`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value of the date field resulting from the conversion is `20170111`.

``` abap
DATA pack TYPE p VALUE 736341. 
 
FINAL(result) = CONV d( pack ).
```

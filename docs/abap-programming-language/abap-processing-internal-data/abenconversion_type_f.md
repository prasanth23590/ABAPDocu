---
title: "Source Field Type f"
source_file: abenconversion_type_f.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Numeric Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type f

- [Numeric Target Fields](abenconversion_type_f.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_f.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_f.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_f.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | The value of the binary floating point number is rounded up to an integer. If this number is within the [value range](../../abap-glossary/abenvalue_range_glosry.md) for the data type `i`, `int8`, (`b`, `s`), it is converted to the internal representation of the corresponding integer number. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                 |
| `p`                        | The value of the binary floating point number is rounded to the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) in the target field. If this number is within the value range for the data type of the target field, it is converted to the internal representation of a packed number. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. |
| `decfloat16`, `decfloat34` | The value of the binary floating point number is rounded to 17 places, depending on the platform, and converted to the value of a decimal floating point number. The representation in the decimal floating point number is such that the mantissa has no trailing zeros.                                                                                                   |
| `f`                        | The content of the source field is passed unconverted.                                                                                                                                                                                                                                                                                                                      |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the rounded value *1234.57*.

``` abap
DATA fltp TYPE f VALUE '1.2345678E+3'. 
 
TYPES pack TYPE p LENGTH 8 DECIMALS 2. 
FINAL(result) = CONV pack( fltp ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The value of the binary floating point number is formatted in the same way as when converting to the data type `string`. If the target field is shorter than the complete notation, the mantissa is rounded up. If the target field is not long enough to include at least one digit of the mantissa in addition to the exponent and the minus sign (for a negative value), the target field is padded with *\** characters. If the target field is longer than the complete notation, it is padded with blanks on the left.                                              |
| `n`        | The value of the floating point number is rounded up to an integer. The absolute value of this number is passed as a right-aligned string of digits to the target field. If the target field is longer than the string of digits, the field is padded with zeros on the left. If it is too short, it is truncated on the left.                                                                                                                                                                                                                                            |
| `string`   | The value of the binary floating point number is formatted in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) and transferred to the target field without gaps. The exponent is always displayed with a plus/minus sign and at least two places, and the mantissa with one integer digit and 16 decimal places. To do this, the internal representation of the floating point number is rounded to 17 places (depending on the platform). Depending on the sign and the length of the exponent, the resulting length of the target field is between 22 and 24. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `-1.2345678000000001E-04`.

``` abap
DATA fltp TYPE f VALUE '-1.2345678E-4'. 
 
FINAL(result) = CONV string( fltp ).
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
DATA fltp TYPE f VALUE '1.23999E+2'. 
 
TYPES hex TYPE x LENGTH 4. 
FINAL(result) = CONV hex( fltp ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`        | The content of the source field is first converted to data type `i` (see above) and then to type `d` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |
| `t`        | The content of the source field is first converted to data type `i` (see above) and then to type `t` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)). |
| `utclong`  | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`.                                                                                                           |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value of the time field resulting from the conversion of the result of a calculation with calculation type `f` is `181216`.

``` abap
FINAL(result) = CONV t( 2 ** 16 ).
```

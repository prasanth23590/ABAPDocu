---
title: "Source Field Type decfloat16, decfloat34"
source_file: abenconversion_type_decfloat.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Numeric Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type decfloat16, decfloat34

If the source field does not contain a [valid decimal floating point number](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), the catchable exception `CX_SY_CONVERSION_NO_NUMBER` is raised, except in the case of assignments to another decimal floating point number. In ABAP, invalid decimal floating point numbers are also the special values *+Infinity*, *-Infinity*, *NaN*, and *sNaN*, which represent infinity or invalid numbers and are designated in standard IEEE-754-2008.

- [Numeric Target Fields](abenconversion_type_decfloat.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_decfloat.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_decfloat.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_decfloat.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | The value of the decimal floating point number is rounded up to an integer. If this number is within the [value range](../../abap-glossary/abenvalue_range_glosry.md) for the data type `i`, `int8`, (`b`, `s`), it is converted to the internal representation of the corresponding integer. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                             |
| `p`                        | The value of the decimal floating point number is rounded to the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) in the target field. If this number is within the value range for the data type of the target field, it is converted to the internal representation of a packed number. Otherwise, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                      |
| `decfloat16`, `decfloat34` | If an assignment is made to the same data type, the content is passed unconverted. In assignments from `decfloat34` to `decfloat16`, the mantissa is truncated from 34 to 16 places and, if necessary, rounded commercially. If the mantissa of the target field is long enough, the [scaling](../../abap-glossary/abenscale_glosry.md) is preserved. If the [value range](../../abap-glossary/abenvalue_range_glosry.md) of `decfloat16` is exceeded, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. |
| `f`                        | The value of the decimal floating point number is converted to the value of a binary floating point number. If the decimal number cannot be represented as a binary floating point number, the nearest value is used. If the value is outside the value range for binary floating point numbers, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                   |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the rounded value *1234.57*.

``` abap
DATA decf TYPE decfloat34 VALUE '1234.5678'. 
 
TYPES pack TYPE p LENGTH 8 DECIMALS 2. 
FINAL(result) = CONV pack( decf ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The content of the source field is first converted to a [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) or [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md), as described for the data type `string`. The result of this conversion is then passed right-aligned to the target field. If the target field is longer than the text string, it is padded on the left with blanks. If the target field is shorter than the text string, mathematical notation is converted to scientific notation and, if necessary, the mantissa is commercially rounded. If the length is not sufficient for at least one position of the mantissa, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `n`        | The value of the decimal floating point number is rounded up to an integer. The absolute value is passed to the target field as a right-aligned string of digits. If the target field is longer than the string of digits, the field is padded with zeros on the left. If it is too short, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `string`   | If the exponent of the decimal floating point number is less than or equal to 0 and the absolute value of the number is greater than or equal to 1E-6, the floating point number is formatted in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) without gaps as follows: the string of digits consists of the mantissa of the decimal floating point number without leading zeros. If the exponent of the decimal floating point number is less than 0, a decimal point is set at the corresponding position. If the exponent of the decimal floating point number is greater than 0 or the absolute value of the number is less than 1E-6, the floating point number is formatted in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) as follows: the mantissa is made up of the mantissa of the decimal floating point number without leading zeros. If the mantissa consists of more than one place, a decimal point is set after the first place. The exponent is always represented by a plus/minus sign and without leading zeros. In both representations, the minus sign is used for negative values but not for positive. Both representations are also used if the value of the decimal floating point number is 0. The maximum length of the target field is 24 for `decfloat16` and 42 for `decfloat34`. |

### Hints

- The conversion rule for floating point numbers to text strings is as follows: a text string that was filled by the assignment of a decimal floating point number produces the same internal representation as in the original decimal floating point number (the [scaling](../../abap-glossary/abenscale_glosry.md) is preserved).

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
DATA decf TYPE decfloat34 VALUE '123.999'. 
 
TYPES hex TYPE x LENGTH 4. 
FINAL(result) = CONV hex( decf ).
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

The value of the time field resulting from the conversion is `100001`.

``` abap
DATA decf TYPE decfloat34 VALUE '36000.999'. 
 
FINAL(result) = CONV t( decf ).
```

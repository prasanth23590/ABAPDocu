---
title: "Source Field Type c"
source_file: abenconversion_type_c.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Character-Like Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type c

- [Numeric Target Fields](abenconversion_type_c.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_c.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_c.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_c.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | The source field must contain a number in mathematical or commercial notation, otherwise the catchable exception `CX_SY_CONVERSION_NO_NUMBER` is raised. **Exception:** A source field that contains only blank characters is interpreted as the number zero. Scientific notation is not allowed, unless it can be interpreted as a mathematical notation. [Decimal places](../../abap-glossary/abendecimal_place_glosry.md) are rounded commercially to integer values. If the number is in the value range of data types `i`, `int8`, (`b`, `s`), it is converted to the corresponding internal representation of an integer, otherwise the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `p`                        | The source field must contain a number in mathematical or commercial notation, otherwise the catchable exception `CX_SY_CONVERSION_NO_NUMBER` is raised. **Exception:** A source field that contains only blank characters is interpreted as the number zero. Scientific notation is not allowed, unless it can be interpreted as a mathematical notation. Decimal places are rounded commercially to the number of decimal places in the target field. If the number is in the value range of the data type of the target field, it is converted to the internal representation of a packed number, otherwise the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `decfloat16`, `decfloat34` | The source field must contain a number in [mathematical](../../abap-glossary/abenmathematical_notation_glosry.md), [scientific](../../abap-glossary/abenscientific_notation_glosry.md), or [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md), otherwise the catchable exception `CX_SY_CONVERSION_NO_NUMBER` is raised. **Exception:** A source field that contains only blank characters is interpreted as the number zero. If the number of digits is greater than 16 or 34, it is rounded commercially to 16 or 34 places. If the absolute value of the number is less than 1E-398 or 1E-6176, it is rounded to 0. If the number is in the value range of the data types `decfloat16` or `decfloat34`, it is converted to the internal representation of a decimal floating point number, otherwise the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. If the mantissa of the target field is long enough, the [scaling](../../abap-glossary/abenscale_glosry.md) of the source field is preserved. The sign is always preserved, even if the number has the value 0.                                                                                                                                                                              |
| `f`                        | The source field must contain a number in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md), with the first blank after a number completing this number. If not, the catchable exception `CX_SY_CONVERSION_NO_NUMBER` is raised. **Exception:** A source field that contains only blanks or that starts with a blank that is not followed by a valid number is interpreted as zero. [Mathematical](../../abap-glossary/abenmathematical_notation_glosry.md) or [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md) is not allowed unless it can be interpreted as scientific notation. **Exception:** Commercial notation where the plus/minus sign on the right is not separated by blanks is valid if the character string starts directly with the string of digits. If the mantissa contains more than 17 digits, surplus digits are rounded up or down. If the number is in the [value range](../../abap-glossary/abenvalue_range_glosry.md) of data type `f`, it is converted to the internal representation of a binary floating point number, otherwise the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. If the decimal number cannot be represented as a binary floating point number, the nearest value is used. |

### Hint

The class [`CL_ABAP_DECFLOAT`](abencl_abap_decfloat_doc.md) contains the methods `READ_DECFLOAT34` and `READ_DECFLOAT16` for converting character strings into decimal floating point numbers. The exceptions of these methods are more significant than those of a regular assignment. Furthermore, the methods return a return value that reveals information about the rounding that was performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first conversion raises an exception, since numbers in scientific notation cannot be converted to the type `i`. Two conversions take place in the `CATCH` block. The conversion operator `CONV` converts from `c` to `decfloat34` and this result is converted to `i` when assigned to `result`.

``` abap
FINAL(scientific) = '1.123E+3'. 
 
TRY. 
    DATA(result) = CONV i( scientific ). 
  CATCH cx_sy_conversion_no_number. 
    result = CONV decfloat34( '1.123E+3' ). 
ENDTRY.
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                             |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The characters in the source field are passed left-aligned to the target field, including any leading blanks. Trailing blanks in the source field are not passed. If the target field is longer than the number of characters passed, it is padded with blanks on the right. If the target field is shorter, it is truncated on the right. |
| `n`        | The characters in the source field that represent digits are passed right-aligned to the target field. Other characters are ignored. If the target field is longer than the number of digits in the source field, it is padded on the left with the character *0*. If the target field is shorter, it is truncated on the left.            |
| `string`   | The characters in the source field are passed to the target field, including any leading blanks. Trailing blanks in the source field are not passed. The length of the target field is determined by the number of characters passed.                                                                                                      |

### Hints

- In ABAP, the [trailing blanks](abenabap_data_string.md) in source fields of type `c` are ignored, by default. An assignment from source type `c` to target type `t` is an exception to this rule.

- To assign source fields of type `c` to target fields (particularly target fields of type `string`) and respect the trailing blanks, the addition `RESPECTING BLANKS` of the statement [`CONCATENATE`](abapconcatenate.md) can be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `abcd` with length 4. The trailing blanks of the literal with type `c` and length 8 are not passed.

``` abap
FINAL(result) = CONV string( 'abcd    ' ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The characters in the source field are interpreted as the representation of the value of a half-byte in hexadecimal representation. If the valid characters *0* to *9* and *A* to `F` appear, the corresponding half-byte value is passed left-aligned to the memory of the target field. If the target field is longer than the number of half-bytes passed, it is padded on the right with hexadecimal 0. If it is too short, it is truncated on the right. The first invalid character terminates the conversion from the position of this character and the half-bytes not filled up to that point are padded with hexadecimal 0. If an invalid character can be detected by the syntax check, it produces a warning. |
| `xstring`  | The same conversion rules apply as to a field of type `x`. Half-bytes are passed to the target field whereby the length of the target field is determined by the number of valid characters in the source field. If number of valid characters in the source field is odd, the last remaining half-byte in the target field is padded with hexadecimal 0.                                                                                                                                                                                                                                                                                                                                                                 |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `0123456789ABCDEF`. If the literal were specified directly as the argument of the conversion, the syntax check would produce a warning.

``` abap
FINAL(text) = '0123456789ABCDEFXXXXXXX'. 
 
FINAL(result) = CONV xstring( text ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`        | The same conversion rules apply as to a field of type `c` of length 8.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `t`        | The same conversion rules apply as to a field of type `c` with the length 6, with the exception that trailing blanks are passed and if the target field is longer than the number of characters passed, the field is padded on the right with the character *0*.                                                                                                                                                                                                             |
| `utclong`  | The source field must contain a valid [representation of an UTC time stamp](abents_value.md), such as *yyyy-mm-ddThh:mm:ss.fffffff*, which is converted to the internal representation of a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md). An initial source field is converted to the initial value of a time stamp field. In all other cases, or if an invalid time stamp were to be created, an exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is raised. |

### Hints

- If, when converting to the type `d`, the source field does not contain a valid date in the format *yyyymmdd* in the first eight places, the target field contains an invalid date after the conversion. Similarly, a conversion to the type `t` can result in an invalid time.

- In conversions to the type `utclong`, the dates *1582-10-05* to *1582-10-14* cannot be specified (due to the switch from the Julian to the Gregorian calendar). No leap seconds (*23:59:60.fffffff*) are supported.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion is the invalid time `XX 00`.

``` abap
FINAL(invalid_time) = 'XX  '. 
 
FINAL(result) = CONV t( invalid_time ). 
 
cl_demo_output=>display( result ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Both conversions produce the same UTC time stamp. Such a time stamp produced from fixed values can, for example, serve for comparisons with real UTC time stamps retrieved by function [`utclong_current`](abenutclong_current.md).

``` abap
FINAL(ts)  = CONV utclong( '2019-04-08 24:00:00.00' ). 
FINAL(tsl) = CONV utclong( '2019-04-09T00:00:00,0000' ). 
 
ASSERT ts = tsl. 
 
ASSERT tsl < utclong_current( ).
```

---
title: "Suitable Values for Lossless Assignments"
source_file: abenmove_exact_elementary_fit.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules > Checking Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Suitable Values for Lossless Assignments

When an operand with an elementary data type of the operator [`EXACT`](abenconstructor_expression_exact.md) is converted to an incompatible elementary data type, the operand must contain a value suitable for the target type as shown in the following tables. This avoids loss of values and provides a valid value for the target type.

- [Numeric Target Types](abenmove_exact_elementary_fit.md#numeric-target-types)

  - [Target Type with Numeric Type (Except f)](abenmove_exact_elementary_fit.md#target-type-with-numeric-type-except-f)

  - [Target Type of Type f](abenmove_exact_elementary_fit.md#target-type-of-type-f)

- [Character-Like Target Types](abenmove_exact_elementary_fit.md#character-like-target-types)

  - [Target Type of Type c](abenmove_exact_elementary_fit.md#target-type-of-type-c)

  - [Target Type of Type string](abenmove_exact_elementary_fit.md#target-type-of-type-string)

  - [Target Type of Type n](abenmove_exact_elementary_fit.md#target-type-of-type-n)

- [Byte-Like Target Types](abenmove_exact_elementary_fit.md#byte-like-target-types)

  - [Target Type of Type x](abenmove_exact_elementary_fit.md#target-type-of-type-x)

  - [Target Type of Type xstring](abenmove_exact_elementary_fit.md#target-type-of-type-xstring)

- [Date/Time Types as Target Types](abenmove_exact_elementary_fit.md#datetime-types-as-target-types)

  - [Target Type of Type d](abenmove_exact_elementary_fit.md#target-type-of-type-d)

  - [Target Type of Type t](abenmove_exact_elementary_fit.md#target-type-of-type-t)

  - [Target Type of Type utclong](abenmove_exact_elementary_fit.md#target-type-of-type-utclong)

## Numeric Target Types

### Target Type with Numeric Type (Except f)

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Numbers from the value range of the target type that do not have to be rounded. Inappropriate values raise exceptions from the class `CX_SY_CONVERSION_ROUNDING` or `CX_SY_CONVERSION_OVERFLOW`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | Numbers from the value range of the target type that do not have to be rounded. In operands of type `c` or `string`, appropriate number [representations](abennumerical_value.md) according to the [conversion rules](abencharacter_source_fields.md) are allowed if their value lies within the value range and does not have to be rounded. Operands of type `c` or `string` are also allowed if they contain only blanks or empty strings. Operands of type `n` can contain as many digits after leading zeros as fit in the value range. Inappropriate values raise exceptions from the class `CX_SY_CONVERSION_ROUNDING` or `CX_SY_CONVERSION_OVERFLOW`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Not allowed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | In operands of types `d` and `t`, all [valid](abenmove_exact_elementary_valid.md) date and times (if specified) are allowed, but they cannot be assigned to the target types `b` and `s`. Inappropriate values raise exceptions from the class `CX_SY_CONVERSION_ROUNDING` or `CX_SY_CONVERSION_OVERFLOW`. The time stamp type `utclong` is not allowed.                                                                                                                                                                                                                                                                                                        |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because rounding would have to take place.

``` abap
FINAL(result1) = EXACT i( '123' ). 
 
FINAL(result2) = EXACT i( '123.4' ).
```

### Target Type of Type f

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Integers with a maximum of 15 digits. In operands of type `i` (`b`, `s`), all values are allowed. In operands of types `int8`, `p`, `decfloat16`, and `decfloat34`, a maximum of 15 places, but no decimal places are allowed. Inappropriate values raise an exception from class `CX_SY_CONVERSION_INEXACT_FLTP`.                                                                                                                                                                             |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | Integers with a maximum of 15 digits. In operands of type `c` or `string`, numeric representations in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) are allowed, whose values are integers with a maximum of 15 places. Operands of type `c` or `string` are also allowed if they contain only blanks or empty strings. Operands of type `n` can contain up to 15 digits after leading zeros. Inappropriate values raise an exception from class `CX_SY_CONVERSION_INEXACT_FLTP`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Not allowed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | In operands of types `d` and `t`, all [valid](abenmove_exact_elementary_valid.md) date and time specifications are allowed. Inappropriate values raise an exception from class `CX_SY_CONVERSION_NO_DATE` or `CX_SY_CONVERSION_NO_TIME` The time stamp type `utclong` is not allowed.                                                                                                                                                                                                        |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossfree assignment raises an exception because the value of the operand is not an integer.

``` abap
FINAL(result1) = EXACT f( '3.33E+2' ). 
 
FINAL(result2) = EXACT f( '3.33E+1' ).
```

## Character-Like Target Types

### Target Type of Type c

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Numbers for which the result from the [conversion](abennumeric_source_fields.md) to type `c` is not longer than the target type, but the result cannot be rounded. Positive signs represented as blanks are ignored. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_OVERFLOW` or `CX_SY_CONVERSION_ROUNDING`. |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | Character strings that are not longer than the target type. In operands of type `c`, trailing blanks are ignored. In operands of type `string`, no characters are ignored, including trailing blanks. Inappropriate values raise an exception from class `CX_SY_CONVERSION_DATA_LOSS`.                                                |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Byte chains for which the result from the [conversion](abenbyte_source_fields.md) to type `c` is not longer than the target type. Inappropriate values raise an exception from class `CX_SY_CONVERSION_DATA_LOSS`.                                                                                                                  |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | [Valid](abenmove_exact_elementary_valid.md) date, time, or time stamp specifications. The result of the conversion must not be longer than the target type. Values that are too long raise an exception from class `CX_SY_CONVERSION_DATA_LOSS`.                                                                                    |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because the character string would be truncated.

``` abap
TYPES c4 TYPE c LENGTH 4. 
 
FINAL(result1) = EXACT c4( 'abcd' ). 
 
FINAL(result2) = EXACT c4( 'abcdef' ).
```

### Target Type of Type string

| **Operand**                                                                                                                          | **Suitable Values**                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Any [valid](abenmove_exact_elementary_valid.md) numbers.                               |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | Any character strings.                                                                   |
| [Byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Any byte chains.                                                                         |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Any [valid](abenmove_exact_elementary_valid.md) date, time, or time stamp information. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This program section never raises an exception.

``` abap
DATA text TYPE c LENGTH 80 VALUE 'Never say never again'. 
cl_demo_input=>request( CHANGING field = text ). 
 
FINAL(result) = EXACT string( text ).
```

### Target Type of Type n

| **Operand**                                                                                                                           | **Suitable Values**                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                                | Positive integers including 0, whose number of digits does not exceed the length of the target type. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_OVERFLOW` or `CX_SY_CONVERSION_ROUNDING`.                                                                                  |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                        | A closed string of digits that cannot be longer than the target type apart from leading zeros. Operands of type `c` and `string` can contain additional leading and trailing blanks. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_NO_NUMBER` or `CX_SY_CONVERSION_OVERFLOW`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                             | Not allowed                                                                                                                                                                                                                                                                                          |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md). | Operands of type `d` and `t` cannot contain blanks and the target type must have the same length as the source fields. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_NO_NUMBER` or `CX_SY_CONVERSION_OVERFLOW`. The time stamp type `utclong` is not allowed.                 |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because not enough places are available for all digits.

``` abap
TYPES n8 TYPE n LENGTH 8. 
 
FINAL(result1) = EXACT n8( 12345678 ). 
 
FINAL(result2) = EXACT n8( 1234567890 ).
```

## Byte-Like Target Types

### Target Type of Type x

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Not allowed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | An even number of characters between *0* and *9* and *A* and *F* in a closed sequence. The number of bytes represented must correspond exactly to the length of the target type. Other characters are not allowed, with the exception that trailing blanks in operands of type `c` are ignored. Operands of the type `n` are not allowed. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_SRC_TOO_SHORT`, `CX_SY_CONVERSION_DATA_LOSS`, or `CX_SY_CONVERSION_NO_RAW`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | A byte chain that has exactly the same length as the target type. Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_SRC_TOO_SHORT` or `CX_SY_CONVERSION_DATA_LOSS`.                                                                                                                                                                                                                                                                                                     |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Arguments of the types `d`, `t`, and `utclong` are not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because the byte string would be truncated.

``` abap
TYPES hex TYPE x LENGTH 1. 
 
FINAL(result1) = EXACT hex( 'FF' ). 
 
FINAL(result2) = EXACT hex( 'FFFF' ).
```

### Target Type of Type xstring

| **Argument**                                                                                                                         | **Suitable Values**                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Not allowed                                                                                                                                                                                                                                                                                                                     |
| [Character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | An even number of characters between *0* and *9* and *A* and *F* in a closed sequence. Other characters are not allowed, with the exception that trailing blanks in arguments of type `c` are ignored. Arguments of the type `n` are not allowed. Inappropriate values raise an exception from class `CX_SY_CONVERSION_NO_RAW`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | A byte chain of any length.                                                                                                                                                                                                                                                                                                     |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Operands of the types `d`, `t`, and `utclong` are not allowed.                                                                                                                                                                                                                                                                  |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because the number of characters is uneven.

``` abap
FINAL(result1) = EXACT xstring( 'FF' ). 
 
FINAL(result2) = EXACT xstring( 'FFF' ).
```

## Date/Time Types as Target Types

### Target Type of Type d

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Positive integers between 0 and 3652060 (which corresponds to the date 12/31/9999). Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_OVERFLOW` or `CX_SY_CONVERSION_ROUNDING`.                                                                                                                       |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | A left-aligned [valid date](abenmove_exact_elementary_valid.md) specification with the format *yyyymmdd*. Operands of type `n` and `string` can contain these eight digits only. Operands of type `c` can also contain trailing blanks. Inappropriate values raise an exception from class `CX_SY_CONVERSION_NO_DATE`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Not allowed                                                                                                                                                                                                                                                                                                              |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Valid date specification in an operand of type `d`. An operand of type `t` or `utclong` is not allowed.                                                                                                                                                                                                                  |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because the date is invalid.

``` abap
FINAL(result1) = EXACT d( '20160729' ). 
 
FINAL(result2) = EXACT d( '20160700' ).
```

### Target Type of Type t

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Positive integers between 0 and 86399 (which corresponds to the time 23:59:59). Inappropriate values raise exceptions from classes `CX_SY_CONVERSION_OVERFLOW` or `CX_SY_CONVERSION_ROUNDING`.                                                                                                                       |
| [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | A left-aligned [valid time](abenmove_exact_elementary_valid.md) specification with the format *hhmmss*. Operands of type `n` and `string` can contain only these six digits. Operands of type `c` can also contain trailing blanks. Inappropriate values raise an exception from class `CX_SY_CONVERSION_NO_TIME`. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Not allowed                                                                                                                                                                                                                                                                                                          |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Valid time specification in an operand of type `t`. An operand of type `d` or `utclong` is not allowed.                                                                                                                                                                                                              |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because the numeric value exceeds the number of seconds in a day.

``` abap
FINAL(result1) = EXACT t( 10000 ). 
 
FINAL(result2) = EXACT t( 100000 ).
```

### Target Type of Type utclong

| **Operand**                                                                                                                          | **Suitable Values**                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md)                                                                               | Not allowed                                                                                                                                                                                                                                                                                                      |
| [Character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md)                                                                       | A left-aligned valid [character-like representation](abents_value.md) of a time stamp, such as *yyyy-mm-ddThh:mm:ss.fffffff* or an initial value with any number of trailing blanks. Inappropriate values raise an exception from class `CX_SY_CONVERSION_NO_DATE_TIME`. Operands of type `n` are not allowed. |
| [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md)                                                                            | Not allowed                                                                                                                                                                                                                                                                                                      |
| [Date type](../../abap-glossary/abendate_type_glosry.md), [time type](../../abap-glossary/abentime_type_glosry.md), or [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | Valid time stamp in an operand of type `utclong`. Operands of type `d` or `t` are not allowed.                                                                                                                                                                                                                   |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A character string composed correctly can be assigned to a time stamp without loss.

``` abap
FINAL(time_zone) = cl_demo_date_time=>get_user_time_zone( ). 
CONVERT UTCLONG utclong_current( ) 
        INTO DATE FINAL(dat) 
              TIME FINAL(tim) 
              FRACTIONAL SECONDS FINAL(fs) 
              TIME ZONE time_zone. 
 
FINAL(ts) = EXACT utclong( |{ dat DATE = ISO } { 
                              tim TIME = ISO }{ 
                              shift_left( val = |{ fs }| 
                                          places = 1 ) }| ).
```

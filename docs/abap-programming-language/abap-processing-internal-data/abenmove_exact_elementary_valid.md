---
title: "Valid Values for Lossless Assignments"
source_file: abenmove_exact_elementary_valid.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules > Checking Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Valid Values for Lossless Assignments

When a lossless conversion of an operand with an elementary data type of the operator [`EXACT`](abenconstructor_expression_exact.md) to an incompatible data type is performed, the operand must, depending on its data type, represent a valid value according to the following tables:

- [Numeric Operands](abenmove_exact_elementary_valid.md#numeric-operands)

- [Character-Like Operands](abenmove_exact_elementary_valid.md#character-like-operands)

- [Byte-Like Operands](abenmove_exact_elementary_valid.md#byte-like-operands)

- [Date Fields, Time Fields, and Time Stamp Fields as Operands](abenmove_exact_elementary_valid.md#date-fields-time-fields-and-time-stamp-fields-as-operands)

## Numeric Operands

| **Operand**                | **Valid Values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | All content is valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `decfloat16`, `decfloat34` | All values that can result from assignments and calculations in ABAP are valid. The special values that indicate infinity or invalid numbers are invalid. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_NUMBER`.                                                                                                                                                                                                                                                                                                                                                                    |
| `p`                        | All values that can result from assignments and calculations in ABAP are valid. If, however, the type has more decimal places than available places, this type is always invalid. (This means that the last half byte can contain only the hexadecimal values *A*, *C*, *E*, or *F*, for a positive sign, or *B* or *D* for a negative sign. The remaining half bytes can contain only the hexadecimal values *0* to *9*.) If, however, the type has more decimal places than available places, this type is always invalid. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_NUMBER`. |
| `f`                        | Integers with a maximum of 15 digits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Hint

Decimal numbers with decimal places cannot generally be represented precisely by binary floating point numbers of type `f`. The operator `EXACT` therefore restricts the valid value range to integers with a maximum of 15 places.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception, caused by the attempt to convert a number with decimal places.

``` abap
DATA arg TYPE f. 
 
arg = 123. 
FINAL(result1) = EXACT i( arg ). 
 
arg = '123.456'. 
FINAL(result2) = EXACT i( arg ).
```

## Character-Like Operands

| **Operand**   | **Valid Values**                                                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `c`, `string` | All content is valid. No check is made to determine whether a byte or string of bytes contains valid characters for the current code page. |
| `n`           | The operand can only contain the digits *0* to *9* only. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_NUMBER`.    |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because `numtext` does not contain a valid value.

``` abap
DATA numtext TYPE n LENGTH 6. 
DATA time    TYPE t. 
 
numtext = time = '115500'. 
FINAL(result1) = EXACT string( numtext ). 
 
FINAL(invalid_time) = '1155__'. 
numtext = time = invalid_time. 
FINAL(result2) = EXACT string( numtext ).
```

## Byte-Like Operands

| **Operand**    | **Valid Values**      |
|----------------|-----------------------|
| `x`, `xstring` | All content is valid. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The lossless assignment does not raise an exception for any of the randomly generated byte strings.

``` abap
DATA hex TYPE x LENGTH 1. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( 
  seed = CONV i( t ) min = 0 max = 1 ). 
 
DO 8 TIMES. 
  SET BIT sy-index OF hex TO rnd->get_next( ). 
ENDDO. 
 
FINAL(result) = EXACT string( hex ).
```

## Date Fields, Time Fields, and Time Stamp Fields as Operands

| **Operand** | **Valid Values**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`         | The operand must contain a valid date in the format *yyyymmdd*, for which the following values are possible: *yyyy* (year): 0001 to 9999, *mm* (month): 01 to 12, *dd* (day): 01 to 31. In addition, the initial value *00000000* is also a valid date. The value *00010101* is only a valid date in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and nowhere else in ABAP. The smallest valid value that corresponds to one day is *00010102*. The values *15821005* to *15821014* are also invalid due to the switch from the Julian to the Gregorian calendar, where 04.10.1582 is followed directly by 15.10.1582. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_DATE`. |
| `t`         | The operand must contain a valid time in the format *hhmmss*, for which the following values are allowed: *hh* (hours): 00 to 23, *mm* (minutes): 01 to 59, *ss* (seconds): 01 to 59. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_TIME`.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `utclong`   | The operand must contain a value from the value range for [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), meaning a valid time stamp, or be initial. Invalid values raise an exception from the class `CX_SY_CONVERSION_NO_DATE_TIME`.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Hints

- The values that the operator `EXACT` allows for date fields of type `d` are different from those defined by the [value range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md). The initial value *00000000*, which does not lie within the value range and is normally considered an invalid date, is considered valid here, whereas the value *00010101*, which lies within the value range, is considered invalid. Only in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) is the value *00010101* also accepted as a valid date and handled like the initial value *00000000* in operand positions for which values must meet the rule for lossless assignments.

- The rule for time stamps of data type `utclong` does not differ from the standard [conversion rule](abenconversion_type_utclong.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second lossless assignment raises an exception because `date` does not contain a valid value.

``` abap
DATA date TYPE d. 
 
date = '20160729'. 
FINAL(result1) = EXACT i( date ). 
 
FINAL(invalid_date) = '201607__'. 
date = invalid_date. 
FINAL(result2) = EXACT i( date ).
```

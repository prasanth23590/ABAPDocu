---
title: "Source Field Type utclong"
source_file: abenconversion_type_utclong.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Date Fields, Time Fields, and Time Stamp Fields as Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type utclong

- [Numeric Target Fields](abenconversion_type_utclong.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_utclong.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_utclong.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_utclong.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                   |
|----------------------------|--------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `p`                        | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `decfloat16`, `decfloat34` | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `f`                        | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |

### Hint

The methods `UTCLONG2TSTMP` and `UTCLONG2TSTMP_SHORT` of class [`CL_ABAP_TSTMP`](abencl_abap_tstmp.md) convert [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md) of the type `utclong` to [time stamps in packed numbers](abentime_stamps_packed.md).

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The internal representation of the UTC time stamp is converted to a character string that represents the time stamp in the notation *yyyy-mm-dd hh:mm:ss.fffffff*. Between the date and time specification there is a space, and a period (`.`) is used as a decimal separator. If the target field is shorter than 27, the character string is truncated on the right. If the target field is longer than 27, the field is padded with blanks on the right. If the source field is initial, the target field is filled with blanks. If the source field contains an invalid value, an exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is raised. |
| `n`        | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `string`   | As for a target field of type `c`. The resulting length of the target field is 27. If the source field is initial, the target field is an empty string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Hint

The formatting of an UTC time stamp of type `utclong` during the conversion follows the SQL standard according to ISO 9075 and corresponds to the formatting option [`TIMESTAMP`](abapcompute_string_format_options.md) with the value `SPACE` for embedded expressions in string templates.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example compares the formatting of the conversion with the corresponding formatting in a string template.

``` abap
FINAL(ts) = utclong_current( ). 
 
ASSERT CONV string( ts ) = 
       |{ ts TIMESTAMP = SPACE }|.
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                   |
|------------|--------------------------------------------------------------------------------------------------|
| `x`        | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `xstring`  | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |

## Date/Time Fields as Target Fields

| **&#x200E;Target** | **conversion**                                                                                   |
|--------------------|--------------------------------------------------------------------------------------------------|
| `d`                | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `t`                | Not supported. Produces a syntax error or raises the exception `CX_SY_CONVERSION_NOT_SUPPORTED`. |
| `utclong`          | The content of the source field is passed unconverted.                                           |

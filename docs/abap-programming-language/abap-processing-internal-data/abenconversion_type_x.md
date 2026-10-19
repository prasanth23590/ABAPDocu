---
title: "Source Field Type x"
source_file: abenconversion_type_x.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Byte-Like Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type x

- [Numeric Target Fields](abenconversion_type_x.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_x.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_x.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_x.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, (`b`, `s`)            | Only the last 4 bytes of the source field are converted. If the source field is shorter than 4 bytes, it is extended on the left with the hexadecimal 0 until it is 4 bytes long. The content of these bytes is interpreted as a number stored in big endian order, of type `i`. The hexadecimal values from *00000000* to *7FFFFFFF* are assigned to numbers from +0 to +2147483647 and the hexadecimal values from *80000000* to *FFFFFFFF* are assigned to the numbers -2147483648 to -1. The number obtained in this way is converted to the internal representation of the corresponding integer. If the [value range](../../abap-glossary/abenvalue_range_glosry.md) of data types `b` or `s` is not sufficient, the catchable exception `CX_SY_CONVERSION_OVERFLOW` is raised. |
| `int8`                     | Only the last 8 bytes of the source field are converted. If the source field is shorter than 8 bytes, it is extended on the left with the hexadecimal 0 until it is 8 bytes long. The content of these bytes is interpreted as a number stored in big endian order, of type `int8`. The hexadecimal values from *0000000000000000* to *7FFFFFFFFFFFFFFF* are assigned to numbers from +0 to +9223372036854775807 and the hexadecimal values from *8000000000000000* to *FFFFFFFFFFFFFFFF* are assigned to the numbers --9223372036854775808 to -1. The number obtained in this way is converted in the internal representation of the corresponding integer.                                                                                                        |
| `p`                        | The content of the source field is first converted to data type `i` (see above) and then to type `p` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `decfloat16`, `decfloat34` | The content of the source field is first converted into data type `i` (see above) and then into type `decfloat16` or `decfloat34` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `f`                        | The content of the source field is first converted to data type `i` (see above) and then to type `f` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *10000*.

``` abap
DATA hex TYPE x LENGTH 2 VALUE '2710'. 
 
FINAL(result) = CONV i( hex ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                                                                                             |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The values of each half-byte in the source field are converted to the hexadecimal characters *0* to *9* and *A* to *F* and passed left-aligned to the target field. If the target field is longer than the number of characters passed, it is padded on the right with blank characters. If it is too short, it is truncated on the right. |
| `n`        | The content of the source field is first converted to data type `i` (see above) and then to type `n` (see [conversion table for source field type `i`, `int8`, (`b`, `s`)](abenconversion_type_ibs.md)).                                                                                                                                 |
| `string`   | The values of each half-byte in the source field are converted to the hexadecimal characters *0* to *9* and *A* to *F* and passed to the target field. The resulting length of the target field is determined by the number of characters passed.                                                                                          |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the conversion is `27`. Two characters `10` are cut off on the right.

``` abap
DATA hex TYPE x LENGTH 2 VALUE '2710'. 
 
TYPES c2 TYPE c LENGTH 2. 
FINAL(result) = CONV c2( hex ).
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                        |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The bytes in the source field are passed left-aligned to the target field. If the target field is longer than the number of bytes passed, it is padded with hexadecimal 0 on the right. If the target field is shorter, it is truncated on the right. |
| `xstring`  | The bytes in the source field are placed in the target field. The resulting length of the target field is determined by the number of bytes passed.                                                                                                   |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `27100000`.

``` abap
DATA hex2 TYPE x LENGTH 2 VALUE '2710'. 
 
TYPES hex4 TYPE x LENGTH 4. 
FINAL(result) = CONV hex4( hex2 ).
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

The value of the time field resulting from the conversion is `024640` (or 10000 seconds after midnight).

``` abap
DATA hex TYPE x LENGTH 2 VALUE '2710'. 
 
FINAL(result) = CONV t( hex ).
```

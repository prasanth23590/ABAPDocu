---
title: "Source Field Type string"
source_file: abenconversion_type_string.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Character-Like Source Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Source Field Type string

- [Numeric Target Fields](abenconversion_type_string.md#numeric-target-fields)

- [Character-Like Target Fields](abenconversion_type_string.md#character-like-target-fields)

- [Byte-Like Target Fields](abenconversion_type_string.md#byte-like-target-fields)

- [Date/Time Fields as Target Fields](abenconversion_type_string.md#datetime-fields-as-target-fields)

## Numeric Target Fields

| **Target**                 | **Conversion**                                                                                                                                                                   |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `i`, `int8`, (`b`, `s`)    | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md). If the source field has a length of 0, the target field is assigned the value 0. |
| `p`                        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md). If the source field has a length of 0, the target field is assigned the value 0. |
| `decfloat16`, `decfloat34` | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md). If the source field has a length of 0, the target field is assigned the value 0. |
| `f`                        | Content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md). If the source field has a length of 0, the target field is assigned the value 0. |

### Hint

The class [`CL_ABAP_DECFLOAT`](abencl_abap_decfloat_doc.md) contains the methods `READ_DECFLOAT34` and `READ_DECFLOAT16` for converting character strings into decimal floating point numbers. The exceptions of these methods are more significant than those of a regular assignment. Furthermore, the methods return a return value that reveals information about the rounding that was performed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following conversion has the value *1123*.

``` abap
FINAL(result) = CONV decfloat34( `1.123E+3` ).
```

## Character-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                              |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md), with the difference that trailing blanks are passed. If the length of the source field is 0, the target field is padded with blanks.                                    |
| `n`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) If the length of the source field is 0, the target field is padded with the character *0*.                                                                               |
| `string`   | No conversion takes place. After the assignment, the internal reference of the target field points to the same string as the source field. A new string is only created in the memory if a change request for the content of the source field or target field is submitted. |

### Hints

- In ABAP, the [trailing blanks](abenabap_data_string.md) are respected for source fields of type `string` but not for data objects of type `c`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string resulting from the assignment is \*abcd \* with length 8. The trailing blanks of the literal with type `string` and length 8 are respected.

``` abap
FINAL(result) = `abcd    `.
```

## Byte-Like Target Fields

| **Target** | **Conversion**                                                                                                                                                                                            |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `x`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) If the length of the source field is 0, the target field is padded with hexadecimal 0.                 |
| `xstring`  | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) If the length of the source field is 0, the length of the target field is also 0 after the assignment. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte chain resulting from the conversion is `FFFF0000`.

``` abap
TYPES hex TYPE x LENGTH 4. 
FINAL(result) = CONV hex( `FFFF` ).
```

## Date/Time Fields as Target Fields

| **Target** | **Conversion**                                                                                                                                                                                                                                                               |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md), with the difference that trailing blanks are passed. If the length of the source field is 0, the target field is padded with the character *0*.                          |
| `t`        | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) and, in particular, the trailing blanks are passed. If the length of the source field is 0, the target field is padded with the character *0*.                            |
| `utclong`  | The content is handled in the same way as a [source field of type `c`](abenconversion_type_c.md) and, in particular the trailing blanks are ignored. An initial source field and a source field that contains only blanks produce the initial value of a time stamp field. |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value of the date field resulting from the conversion is `00000000`. If, on the other hand, a text field of type `c` containing only blanks is converted, this produces a target field containing eight blanks, despite the cutting off of all trailing blanks.

``` abap
final(invalid_date) = ``. 
 
FINAL(result) = CONV d( invalid_date ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of a text string composed of date and time specifications in ISO format 8601 to a value in a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md) `ts_conv`. The value in `ts_conv` is a valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) but not the real UTC time stamp that belongs to the system date and system time in the system time zone. For the latter, the statement [`CONVERT INTO UTCLONG`](abapconvert_date_utclong.md) can be used that performs a real time stamp conversion instead of a simple concatenation.

``` abap
FINAL(time) = cl_demo_date_time=>get_system_time( ). 
FINAL(date) = cl_demo_date_time=>get_system_date( ). 
FINAL(conv_ts) = CONV utclong( |{ date DATE = ISO }T{ 
                                  time TIME = ISO }| ). 
 
CONVERT DATE date TIME time 
        TIME ZONE cl_demo_date_time=>GET_SYSTEM_TIME_ZONE( ) 
        INTO UTCLONG FINAL(real_ts). 
 
cl_demo_output=>new( 
 )->write( conv_ts 
 )->write( real_ts )->display( ).
```

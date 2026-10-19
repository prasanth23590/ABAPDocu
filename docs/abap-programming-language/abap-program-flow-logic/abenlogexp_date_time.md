---
title: "rel_exp - Comparison Type of Date Fields, Time Fields, and Time Stamp Fields"
source_file: abenlogexp_date_time.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Date Fields, Time Fields, and Time Stamp Fields

The following tables show the [comparison types](../../abap-glossary/abencomparison_type_glosry.md) for comparisons between date/time types and other data types. If the type of an operand is not the same as the comparison type, it is [converted](../abap-processing-internal-data/abenconversion_elementary.md) to this type. The [comparison rules for the comparison types](abencomparison_type.md) determine how the comparison is performed. If no comparison type is specified for a combination, no comparison is possible.

- [Comparisons with Numeric Data Types](abenlogexp_date_time.md#comparisons-with-numeric-data-types)

- [Comparisons with Character-Like Data Types](abenlogexp_date_time.md#comparisons-with-character-like-data-types)

- [Comparisons with Byte-Like Data Types](abenlogexp_date_time.md#comparisons-with-byte-like-data-types)

- [Comparisons with Date Types, Time Types, or Time Stamp Types](abenlogexp_date_time.md#comparisons-with-date-types-time-types-or-time-stamp-types)

## Comparisons with Numeric Data Types

| \-                             | **d**, **t** | **utclong** |
|--------------------------------|--------------|-------------|
| **decfloat16**, **decfloat34** | `decfloat34` | `-`         |
| **f**                          | `f`          | `-`         |
| **p**                          | `p`          | `-`         |
| **int8**                       | `int8`       | `-`         |
| **i**, **s**, **b**            | `i`          | `-`         |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of the `syst_datum` type data object `date` is converted to the number of days since 01/01/0001 in the comparison and compared with the content of `days`.

``` abap
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
DATA(days) = CONV decfloat34( date ). 
cl_demo_input=>request( CHANGING field = days ). 
 
cl_demo_output=>display( 
  COND #( WHEN days > date THEN |{ days } > { date }| 
          WHEN days < date THEN |{ days } < { date }| 
                               ELSE |{ days } = { date }| ) ).
```

## Comparisons with Character-Like Data Types

| \-         | **d**, **t** | **utclong** |
|------------|--------------|-------------|
| **string** | `string`     | `utclong`   |
| **c**      | `c`          | `utclong`   |
| **n**      | `n`          | `-`         |

**Length Adjustments**

- For comparisons between data types `c`, `n`, or `string` on the one hand and `d` on the other, the longer field is truncated on the right to the length of the shorter field, if only blanks are truncated.

- For comparisons between data types `c` or `n` on the one hand and `t` on the other, the longer field is truncated on the right to the length of the shorter field, if only blanks or characters *0* are truncated.

- Lengths are not adjusted for comparisons between the data type `string` and the data type `t`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comparison of any text string with the `syst_datum` type data object `date`.

``` abap
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
DATA(text) = CONV string( date ). 
cl_demo_input=>request( CHANGING field = text ). 
 
cl_demo_output=>display( 
  COND #( WHEN text > date THEN |{ text } > { date }| 
          WHEN text < date THEN |{ text } < { date }| 
                               ELSE |{ text } = { date }| ) ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An UTC time stamp formatted as a character string with the formatting option [`TIMESTAMP`](../abap-processing-internal-data/abapcompute_string_format_options.md) can be converted to `utclong` and compared with a time stamp field. Instead of `ISO`, `SPACE` could also be specified.

``` abap
FINAL(ts) = utclong_current( ). 
FINAL(text) = |{ ts TIMESTAMP = ISO }|. 
ASSERT ts = text.
```

## Comparisons with Byte-Like Data Types

| \-                 | **d**, **t** | **utclong** |
|--------------------|--------------|-------------|
| **x**, **xstring** | `i`          | `-`         |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A hexadecimal number that is the result of the conversion of a valid time is equal to this time.

``` abap
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
FINAL(hex) = CONV xstring( time ). 
 
ASSERT hex = time. 
cl_demo_output=>display( |{ time } { hex }| ).
```

## Comparisons with Date Types, Time Types, or Time Stamp Types

\|-\|**d**\|**t**\|**utclong** \| \|:---\|:---\|:---\| \|**d**\|`d`\|`-`\|`-` \| \|**t**\|`-`\|`t`\|`-` \| \|**utclong**\|`-`\|`-`\|`utclong`\|

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The time generated through the addition of the value 86399 to the current time is compared with the current time. It is smaller than the current time.

``` abap
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
IF CONV t( time + 86399 ) < time. 
  cl_demo_output=>display( |CONV t( time + 86399 ) < time| ). 
ENDIF.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A later time stamp is always greater than an earlier time stamp.

``` abap
FINAL(ts) = utclong_current( ). 
WAIT UP TO 1 SECONDS. 
ASSERT utclong_current( ) > ts.
```

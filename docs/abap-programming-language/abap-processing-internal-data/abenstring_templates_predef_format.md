---
title: "embd_exp - Predefined Formats"
source_file: abenstring_templates_predef_format.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - embedded_expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# embd_exp - Predefined Formats

The following predefined formatting rules apply to embedded expressions in string templates. These rules can be overridden by explicit formatting options [`format_options`](abapcompute_string_format_options.md).

- [Text Length](abenstring_templates_predef_format.md#text-length)

- [Alignment](abenstring_templates_predef_format.md#alignment)

- [Character-Like Data Types and Date/Time Types](abenstring_templates_predef_format.md#character-like-data-types-and-datetime-types)

- [Byte-Like Data Types](abenstring_templates_predef_format.md#byte-like-data-types)

- [Numeric Data Types](abenstring_templates_predef_format.md#numeric-data-types)

- [Time Stamp Type](abenstring_templates_predef_format.md#time-stamp-type)

## Text Length

The predefined text length is the minimum length required to represent the entire result of the embedded expression.

### Hint

The predefined text length can be overridden using the formatting option [`WIDTH`](abapcompute_string_format_options.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The length of the result of the following string template is 5. It consists of 4 digits and a decimal separator.

``` abap
FINAL(text) = |{ CONV decfloat34( 1234 / 10 ) }|.
```

## Alignment

The predefined alignment for all data types is left-aligned.

### Hint

The predefined alignment can be overridden using the formatting option [`ALIGN`](abapcompute_string_format_options.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the character string shown below it.

``` abap
FINAL(text) = |{ 1 WIDTH = 5 }{ 2 WIDTH = 5 }{ 3 WIDTH = 5 }<-|.
```

1 2 3 \<-

## Character-Like Data Types and Date/Time Types

For character-like data types with fixed lengths (`c` and `n`) and the date/time types (`d`, `t`), the content is passed ignoring trailing blanks. The content of text strings with the type `string` is passed completely.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the character string shown below, depending on the date and time. The format is independent of the [formatting settings](../abap-language-environment/abencountry.md).

``` abap
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
FINAL(text) = |{ date } { time }|.
```

20160909 081545

## Byte-Like Data Types

Values of the byte-like data types `x` and `xstring` are formatted in hexadecimal format, where one byte is represented by two characters.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the character string shown below it.

``` abap
FINAL(text) = 
  |{ cl_abap_conv_codepage=>create_out( )->convert( 'Hello World!' ) }|.
```

48656C6C6F20576F726C6421

## Numeric Data Types

The following rules apply to the representation of numeric values:

- For negative values, the minus sign is placed on the left of the number, without a blank. No sign is placed in front of positive numbers by default.

- The period (`.`) is always used as the decimal separator.

- **No** thousands separators are inserted.

The following applies to the individual numeric data types:

- Values of data type (`b`, `s`), `i`, `int8`, and `p` are formatted in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md) and all decimal places are considered.

- Values with the data types `decfloat16` and `decfloat34` are formatted by default in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md), that is, without an exponent. The formatting option [`EXPONENT`](abapcompute_string_format_options.md) can be used to represent the exponent. Trailing zeros in decimal places are not displayed by default. The formatting option [`DECIMALS`](abapcompute_string_format_options.md) can be used to determine the required number of decimal places.

- Values with the data type `f` are formatted by default in [mathematical notation](../../abap-glossary/abenmathematical_notation_glosry.md), without an exponent. The formatting option [`EXPONENT`](abapcompute_string_format_options.md) can be used to represent the exponent. Trailing zeros in decimal places are not displayed by default. The formatting option [`DECIMALS`](abapcompute_string_format_options.md) can be used to determine the required number of decimal places.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the string below, with a platform-dependent result for the data type `f`. If the [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) is not specified, the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of the embedded expression is `i`.

``` abap
FINAL(text) = |{                  - 2 / 3   }, { 
                CONV decfloat34( - 2 / 3 ) }, { 
                CONV          f( - 2 / 3 ) }|.
```

-1, -0.6666666666666666666666666666666667, -0.66666666666666663

## Time Stamp Type

A valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard in a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md) with the [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) `utclong` is formatted as *yyyy-mm-dd hh:mm:ss.fffffff* in accordance with the SQL standard ISO 9075. A blank is placed between the date and time and the period (`.`) is used as the default decimal separator. An initial time stamp field is represented by a string of 27 blanks. A time stamp field whose value is greater than or equal to the last second or is between *9999-12-31 23:59:59.0000000* and *"9999-12-31 23:59:59.9999999* is represented as *9999-12-31 23:59:59.9999999*.

This setting can be overwritten using formatting options such as [`TIMESTAMP`](abapcompute_string_format_options.md), [`COUNTRY`](abapcompute_string_format_options.md), or [`DECIMALS`](abapcompute_string_format_options.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the character string shown below it.

``` abap
FINAL(text) = |{ utclong_add( val     = VALUE utclong( ) 
                             days    = CONV #( CONV d( '20190402' ) ) 
                             hours   = 10 
                             minutes = 30 
                             seconds = CONV #( '12.3456789' ) ) }|.
```

2019-04-02 10:30:12.3456789

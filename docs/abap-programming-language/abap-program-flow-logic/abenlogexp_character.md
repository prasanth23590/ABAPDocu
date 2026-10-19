---
title: "rel_exp - Comparison Type of Character-Like Data Objects"
source_file: abenlogexp_character.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Character-Like Data Objects

The following tables show the [comparison types](../../abap-glossary/abencomparison_type_glosry.md) for comparisons between character-like data types and other data types. If the type of an operand is not the same as the comparison type, it is [converted](../abap-processing-internal-data/abenconversion_elementary.md) to this type. The [comparison rules for the comparison types](abencomparison_type.md) determine how the comparison is performed. If no comparison type is specified for a combination, no comparisons are possible.

- [Comparisons with Numeric Data Types](abenlogexp_character.md#comparisons-with-numeric-data-types)

- [Comparisons with Character-Like Data Types](abenlogexp_character.md#comparisons-with-character-like-data-types)

- [Comparisons with Byte-Like Data Types](abenlogexp_character.md#comparisons-with-byte-like-data-types)

- [Comparisons with Date Types, Time Types, or Time Stamp Types](abenlogexp_character.md#comparisons-with-date-types-time-types-or-time-stamp-types)

## Comparisons with Numeric Data Types

\|- \|**string**, **c**, **n** \| \|:---\|:---\|:---\| \|**decfloat16**, **decfloat34**\|`decfloat34` \| \|**f**\|`f` \| \|**p**\|`p` \| \|**int8**\|`int8` \| \|**i**, **s**, **b**\|`i`\|

**Value Ranges and Length Adjustments**

- When the types `string` and `c` are compared with packed numbers of the type `p`, the comparison type `p` has 31 places with the number of decimal places of the operand of type `p`, which can raise exceptions if overflows occur.

- When the type `n` is compared with packed numbers of the type `p`, the numeric text can contain up to 31 digits, excluding leading zeros and regardless of how many decimal places are in the operand with type `p`.

- When the types `string`, `c`, and `n` are compared with integers of the types `int8`, `i`, `s`, and `b`, the numeric value in the character-like operand does not have to fit the value range of the comparison type `i`. If the numeric value is not in the value range, the comparison returns the correct result and no exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comparison of a numeric text with an integer. If `numtext` contains an invalid value, an uncatchable exception is raised with the runtime error `CONVT_NO_NUMBER`.

``` abap
DATA numtext TYPE n LENGTH 3. 
cl_demo_input=>add_field( CHANGING field = numtext ). 
DATA num TYPE int1. 
cl_demo_input=>request( CHANGING field = num ). 
 
cl_demo_output=>display( 
  COND #( WHEN numtext < num THEN |{ numtext } < { num }| 
          WHEN numtext > num THEN |{ numtext } > { num }| 
                             ELSE |{ numtext } = { num }| ) ).
```

## Comparisons with Character-Like Data Types

\|- \|**string**\|**c**\|**n** \| \|:---\|:---\|:---\| \|**string**\|`string`\|`string`\|`p` \| \|**c**\|`string`\|`c`\|`p` \| \|**n**\|`p`\|`p`\|`n`\|

**Length Adjustments**

- Operands with a different length of data type `string` never match. If the content of the operands match for the length of the shorter operand, the shorter operand is smaller than the longer one. Otherwise, the surplus places in the longer field are truncated on the right, and then the content is compared.

- In comparisons between two operands of data type `c` with the same length, the entire length is compared, which means the trailing blanks are respected. In comparisons between two operands of data type `c` with different lengths, the shorter field is [converted](../abap-processing-internal-data/abenconversion_type_c.md) to the longer field, with blanks used as padding on the right.

- In comparisons between two operands of data type `n`, the shorter field is [converted](../abap-processing-internal-data/abenconversion_type_n.md) to the longer field, with the character *0* used as padding on the left.

### Hint

In comparisons between text fields of the type `c` and text strings of the type `string`, any trailing blanks are ignored by conversions from `c` to `string`. This can lead to unexpected results. The conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) can be used here to force other comparison types (see the example there).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following comparison, the comparison type is `c` and the comparison is performed in the current code page, in accordance with the binary representation. In most code pages, *a* is greater than *Z*. See also the example for [`CONVERT TEXT`](../abap-processing-internal-data/abapconvert_text.md).

``` abap
IF 'a' > 'Z'. 
  cl_demo_output=>display_text( `'a' > 'Z'` ). 
ELSE. 
  cl_demo_output=>display_text( `'a' < 'Z'` ). 
ENDIF.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparison is false, which is probably unexpected. The value returned by [`boolc`](abenboole_functions.md) has the type `string` and contains a blank, whereas the constant `abap_false` has the type `c`. For the comparison, the value of `abap_false` is converted to an empty string, since the blank it contains is ignored.

``` abap
IF boolc( 1 = 2 ) = abap_false. 
  cl_demo_output=>display_text( 'yes' ). 
ELSE. 
  cl_demo_output=>display_text( 'no' ). 
ENDIF.
```

The following comparison, however, is true, since the return value of [`xsdbool`](abenboole_functions.md) has the same ABAP type as the constant `abap_false`.

``` abap
IF xsdbool( 1 = 2 ) = abap_false. 
  cl_demo_output=>display_text( 'yes' ). 
ELSE. 
  cl_demo_output=>display_text( 'no' ). 
ENDIF.
```

### Executable Example

[Comparing Text Strings of Different Length](abenstring_comparison_abexa.md)

## Comparisons with Byte-Like Data Types

\|- \|**string**\|**c**\|**n** \| \|:---\|:---\|:---\| \|**xstring**\|`string`\|`string`\|`p` \| \|**x**\|`string`\|`c`\|`p`\|

**Length Adjustments**

- In comparisons of data type `c` with `x` or `xstring`, the shorter field is adjusted to the length of the longer field after conversions from `x` to `c` or `xstring` to `string`. Blanks are used as padding on the right.

- Lengths are not adjusted in comparisons between the data type `string` on one side and `x` or `xstring` on the other.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression `CONV xstring( 255 ) = 'FF'` is true.

``` abap
FINAL(int) = 255. 
 
ASSERT CONV xstring( int ) = 'FF'.
```

## Comparisons with Date Types, Time Types, or Time Stamp Types

\|- \|**string**\|**c**\|**n** \| \|:---\|:---\|:---\| \|**d**, **t**\|`string`\|`c`\|`n` \| \|**utclong**\|`utclong`\|`utclong`\|`-`\|

**Length Adjustments**

- For comparisons between data types `c`, `n`, or `string` on the one hand and `d` on the other, the longer field is truncated on the right to the length of the shorter field, if only blanks are truncated.

- For comparisons between data types `c` or `n` on the one hand and `t` on the other, the longer field is truncated on the right to the length of the shorter field, if only blanks or characters *0* are truncated.

- Lengths are not adjusted for comparisons between the data type `string` and `t`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the length adjustment in a comparison of a time field with a character string. Both comparisons are true.

``` abap
IF CONV t( '120000' ) = '12'. 
  cl_demo_output=>write( |CONV t( '120000' ) = '12'| ). 
ENDIF. 
 
IF CONV t( '123000' ) <> '12'. 
  cl_demo_output=>write( |CONV t( '123000' ) <> '12'| ). 
ENDIF. 
 
cl_demo_output=>display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparison is always true. The initial text string literal is converted to the initial value of a time stamp field and this is smaller than any real time stamp.

``` abap
ASSERT utclong_current( ) > ``.
```

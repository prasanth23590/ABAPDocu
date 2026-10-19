---
title: "rel_exp - Comparison Type of Byte-Like Data Objects"
source_file: abenlogexp_byte.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Byte-Like Data Objects

The following tables show the [comparison types](../../abap-glossary/abencomparison_type_glosry.md) for comparisons between byte-like data types and other data types. If the type of an operand is not the same as the comparison type, it is [converted](../abap-processing-internal-data/abenconversion_elementary.md) to this type. The [comparison rules for the comparison types](abencomparison_type.md) determine how the comparison is performed.

- [Comparisons with Numeric Data Types](abenlogexp_byte.md#comparisons-with-numeric-data-types)

- [Comparisons with Character-Like Data Types](abenlogexp_byte.md#comparisons-with-character-like-data-types)

- [Comparisons with Byte-Like Data Types](abenlogexp_byte.md#comparisons-with-byte-like-data-types)

- [Comparisons with Date Types, Time Types, or Time Stamp Types](abenlogexp_byte.md#comparisons-with-date-types-time-types-or-time-stamp-types)

## Comparisons with Numeric Data Types

| \-                             | **xstring**, **x** |
|--------------------------------|--------------------|
| **decfloat16**, **decfloat34** | `decfloat34`       |
| **f**                          | `f`                |
| **p**                          | `p`                |
| **int8**                       | `int8`             |
| **i**, **s**, **b**            | `i`                |

**Length Adjustments**

The comparison type `p` has 31 places and the number of decimal places for the operand of type `p`.

### Hint

In [conversions](../abap-processing-internal-data/abenbyte_source_fields.md) of byte-like data types to any numeric type except `int8`, only the last four bytes are respected. In the case of `int8`, the last 8 bytes are respected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Since the decimal places are lost in the conversion between numeric and byte-like types, the comparison for inequality is true.

``` abap
TYPES pack TYPE p LENGTH 6 DECIMALS 2. 
 
DATA pack TYPE pack VALUE '1234.56'. 
FINAL(hex) = CONV xstring( pack ). 
 
IF hex <> pack. 
  cl_demo_output=>display( |{ CONV pack( hex ) } <> { pack }| ). 
ENDIF.
```

## Comparisons with Character-Like Data Types

\|- \|**xstring**\|**x** \| \|:---\|:---\| \|**string**\|`string`\|`string` \| \|**c**\|`string`\|`c` \| \|**n**\|`p`\|`p`\|

**Length Adjustments**

- In comparisons of data type `c` with `x` or `xstring`, the shorter field is adjusted to the length of the longer field after conversions from `x` to `c` or `xstring` to `string`. Blanks are used as padding on the right.

- Lengths are not adjusted in comparisons between the data type `string` on one side and `x` or `xstring` on the other.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The comparison uses the appropriate [conversion rules](../abap-processing-internal-data/abenconversion_type_x.md) to convert the hexadecimal content *FF00* of `hex` to the string *FF00*, which is then compared with *FFxx*. The operands are not equal.

``` abap
DATA hex   TYPE x LENGTH 2. 
DATA text  TYPE c LENGTH 4. 
 
hex  = 'FF00'. 
text = 'FFxx'. 
 
IF hex <> text. 
  cl_demo_output=>display( |{ hex } <> { text } | ). 
ENDIF.
```

## Comparisons with Byte-Like Data Types

\|- \|**xstring**\|**x** \| \|:---\|:---\| \|**xstring**\|`xstring`\|`xstring` \| \|**x**\|`xstring`\|`x`\|

**Length Adjustments**

- Operands of the data type `xstring` with different lengths never match. If the content of the operands matches the length of the shorter operand, the shorter operand is smaller than the longer one. Otherwise the surplus bytes in the longer field are truncated on the right, and then the content is compared.

- In comparisons between two operands of the data type `x`, the shorter field is [converted](../abap-processing-internal-data/abenconversion_type_x.md) to the longer field, with hexadecimal 0 used as padding on the right.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Before the comparison, the appropriate [conversion rules](../abap-processing-internal-data/abenconversion_type_c.md) are used to convert the content of *FFxx* from `text` to the hexadecimal value *FF00* in the helper variable `hex_helper`, and this value is compared with the content of `hex`.

``` abap
DATA hex  TYPE x LENGTH 2. 
DATA text TYPE c LENGTH 4. 
 
hex  = 'FF00'. 
text = 'FFxx'. 
 
... 
 
DATA hex_helper TYPE x LENGTH 2. 
hex_helper = text. 
IF hex = hex_helper. 
  cl_demo_output=>display( |{ hex } = { hex_helper } | ). 
ENDIF.
```

## Comparisons with Date Types, Time Types, or Time Stamp Types

| \-           | **xstring**, **x** |
|--------------|--------------------|
| **d**, **t** | `i`                |
| **utclong**  | `-`                |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A hexadecimal number that is the result of the conversion of a valid date is equal to this date.

``` abap
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
FINAL(hex) = CONV xstring( date ). 
 
ASSERT hex = date. 
cl_demo_output=>display( |{ date } { hex }| ).
```

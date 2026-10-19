---
title: "rel_exp - Comparison Type of Numeric Data Objects"
source_file: abenlogexp_numeric.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Numeric Data Objects

The following tables show the [comparison types](../../abap-glossary/abencomparison_type_glosry.md) for comparisons between numeric data types and other data types. If the type of an operand is not the same as the comparison type, it is [converted](../abap-processing-internal-data/abenconversion_elementary.md) to this type. The [comparison rules for the comparison types](abencomparison_type.md) determine how the comparison is executed.

- [Comparisons with Numeric Data Types](abenlogexp_numeric.md#comparisons-with-numeric-data-types)

- [Comparisons with Character-Like Data Types](abenlogexp_numeric.md#comparisons-with-character-like-data-types)

- [Comparisons with Byte-Like Data Types](abenlogexp_numeric.md#comparisons-with-byte-like-data-types)

- [Comparisons with Date Types, Time Types, or Time Stamp Types](abenlogexp_numeric.md#comparisons-with-date-types-time-types-or-time-stamp-types)

## Hint

If a [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) is involved in a comparison, the comparison always takes place with the type `decfloat34`.

## Comparisons with Numeric Data Types

| \-                             | **decfloat16**, **decfloat34** | **f**        | **p**        | **int8**     | **i**        | **s**        | **b**        |
|--------------------------------|--------------------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| **decfloat16**, **decfloat34** | `decfloat34`                   | `decfloat34` | `decfloat34` | `decfloat34` | `decfloat34` | `decfloat34` | `decfloat34` |
| **f**                          | `decfloat34`                   | `f`          | `f`          | `f`          | `f`          | `f`          | `f`          |
| **p**                          | `decfloat34`                   | `f`          | `p`          | `p`          | `p`          | `p`          | `p`          |
| **int8**                       | `decfloat34`                   | `f`          | `p`          | `int8`       | `int8`       | `int8`       | `int8`       |
| **i**                          | `decfloat34`                   | `f`          | `p`          | `int8`       | `i`          | `i`          | `i`          |
| **s**                          | `decfloat34`                   | `f`          | `p`          | `int8`       | `i`          | `s`          | `s`          |
| **b**                          | `decfloat34`                   | `f`          | `p`          | `int8`       | `i`          | `s`          | `b`          |

**Value Ranges and Length Adjustments**

- When two operands with data type `p` are compared, numbers with more than 31 places are used internally to ensure that there is no overflow.

  - When two operands with data type `p` but with different lengths are compared, the shorter operand is [converted](../abap-processing-internal-data/abenconversion_type_p.md) to the greater length.

  - When two operands with data type `p` but with different numbers of decimal places are compared, the operand with fewer decimal places is [converted](../abap-processing-internal-data/abenconversion_type_p.md) to a number with the same number of decimal places as the other operand.

- When an operand with type `p` is compared with an operand with type `int8`, `i`, `s`, or `b`, the comparison type `p` has 31 places and the number of decimal places of the operand of type `p`.

- If the value of an operand of type `int8` does not match the value range of a comparison type `p`, the exception is caught internally, and the comparison delivers the correct result.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of this example is a surprise at first, but is caused by the fact that the value *0.15* cannot be represented exactly as a binary floating point number.

``` abap
cl_demo_output=>display( 
  COND #( 
    WHEN CONV f( '0.15' ) = CONV decfloat34( '0.15' ) 
      THEN `OK` 
      ELSE `Surprise, surprise ...` ) ).
```

## Comparisons with Character-Like Data Types

\|- \|**decfloat16**, **decfloat34**\|**f**\|**p** \|**int8**\|**i**, **s**, **b** \| \|:---\|:---\|:---\|:---\|:---\|:---\|:---\|:---\| \|**string**, **c**, **n**\|`decfloat34`\|`f`\|`p`\|`int8`\| `i`\|

**Value Ranges and Length Adjustments**

- When the types `string` and `c` are compared with packed numbers of the type `p`, the comparison type `p` has 31 places with the number of decimal places of the operand of type `p`, which can raise exceptions if overflows occur.

- When the type `n` is compared with packed numbers of the type `p`, the numeric text can contain up to 31 digits, excluding leading zeros and regardless of how many decimal places are in the operand with type `p`.

- When the types `string`, `c`, and `n` are compared with integers of the types `int8`, `i`, `s`, and `b`, the numeric value in the character-like operand does not have to fit the value range of the comparison type `i`. If the numeric value is not in the value range, the comparison returns the correct result and no exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Both comparisons are true. Whereas the comparison type of the first comparison is character-like and different strings do not match, the comparison type of the second comparison, on the other hand, is numeric due to the numeric literal `-1`. The string `1-` contains a number in commercial notation, which is converted to an integer number with the value *-1*.

``` abap
IF '-1' <> '1-'. 
  cl_demo_output=>write( |'-1' <> '1-'| ). 
ENDIF. 
 
IF -1 = '1-'. 
  cl_demo_output=>write( |-1 = '1-'| ). 
ENDIF. 
 
cl_demo_output=>display( ).
```

## Comparisons with Byte-Like Data Types

\|- \|**decfloat16**, **decfloat34**\|**f**\|**p** \|**int8**\|**i**, **s**, **b** \| \|:---\|:---\|:---\|:---\|:---\|:---\|:---\|:---\| \|**xstring**, **x**\|`decfloat34`\|`f`\|`p`\|`int8`\| `i`\|

**Length Adjustments**

The comparison type `p` has 31 places and the number of decimal places for the operand of type `p`.

### Hint

In [conversions](../abap-processing-internal-data/abenbyte_source_fields.md) of byte-like data types to any numeric type except `int8`, it should be noted that only the last four bytes are respected. In the case of `int8`, the last 8 bytes are respected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The comparison is true for all valid integer numbers of the type `i`. In the comparison, the byte string created from a number is converted into the original number.

``` abap
DATA(num) = -2147483648. 
cl_demo_input=>request( CHANGING field = num ). 
 
FINAL(hex) = CONV xstring( num ). 
 
IF hex = num. 
  cl_demo_output=>display( hex ). 
ENDIF.
```

## Comparisons with Date Types, Time Types, or Time Stamp Types

\|- \|**decfloat16**, **decfloat34**\|**f**\|**p** \|**int8**\|**i**, **s**, **b** \| \|:---\|:---\|:---\|:---\|:---\|:---\|:---\|:---\| \|**d**, **t**\|`decfloat34`\|`f`\| `p`\| `int8`\|`i` \| \|**utclong**\|`-`\|`-`\| `-`\| `-`\|`-`\|

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A valid time specification in `time` is converted to the number of seconds since midnight in the comparisons. This number is compared with the number of seconds that corresponds to noon.

``` abap
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
cl_demo_output=>display( 
  COND #( WHEN time <  43200 THEN 'AM' 
          WHEN time >= 43200 THEN 'PM' ) ).
```

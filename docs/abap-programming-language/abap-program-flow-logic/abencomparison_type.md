---
title: "rel_exp - Comparison Rules for Comparison Types"
source_file: abencomparison_type.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Rules for Comparison Types

When operands with elementary data types are compared, the comparison is performed according to a comparison type that is determined by the involved operands, as described for [elementary data objects](abenlogexp_rules_operands_dobj.md) and [calculation expressions](abenlogexp_rules_expressions.md). The comparison type can be one of the [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md). When incompatible operands are compared, the operands that do not have the comparison type are converted to this type.

- [Numeric Comparison Type](abencomparison_type.md#numeric-comparison-type)

- [Character-Like Comparison Type](abencomparison_type.md#character-like-comparison-type)

- [Byte-Like Comparison Type](abencomparison_type.md#byte-like-comparison-type)

- [Date/Time Type as Comparison Type](abencomparison_type.md#datetime-type-as-comparison-type)

- [Time Stamp Type as Comparison Type](abencomparison_type.md#time-stamp-type-as-comparison-type)

## Numeric Comparison Type

If the comparison type is one of the [numeric data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), the numeric values are compared.

### Hints

- Since platform-dependent rounding errors may occur with data type `f`, a comparison for equality often does not make any sense for binary floating point numbers.

- [Scale](../../abap-glossary/abenscale_glosry.md) and [precision](../../abap-glossary/abenprecision_glosry.md) are not relevant in comparisons between decimal floating point numbers.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The comparison of a text string with an integer is performed with numeric comparison type `i`. If the text string cannot be converted to `i`, an uncatchable exception would be raised in the comparison. Convertibility is therefore checked first using the conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA char TYPE string. 
cl_demo_input=>add_field( CHANGING field = char ). 
DATA num TYPE i. 
cl_demo_input=>request(   CHANGING field = num ). 
 
TRY. 
    FINAL(test) = CONV i( char ). 
  CATCH cx_sy_conversion_error. 
    out->write( `Try again!` ). 
    RETURN. 
ENDTRY. 
 
out->write( 
  COND #( WHEN char > num THEN `CHAR is greater than NUM` 
          WHEN char = num THEN `CHAR equals NUM` 
                          ELSE `CHAR is lower than NUM` ) ). 
 
out->display( ).
```

## Character-Like Comparison Type

If the comparison type is one of the [character-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), the content is compared from left to right. Based on the internal binary representation in the [code page](../../abap-glossary/abencodepage_glosry.md) used, the first differing character from the left determines which operand is greater.

### Hints

- For operands of types `c` and `string`, the content is not compared with the [locale](../../abap-glossary/abenlocale_glosry.md) of the current [text environment](../../abap-glossary/abentext_environment_glosry.md). The statement [`CONVERT TEXT`](../abap-processing-internal-data/abapconvert_text.md) can be used to determine the order of the locale.

- For operands of type `n` that contain a valid string of digits, the proportions of the numbers represented are determined correctly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows whether the binary representation of uppercase letters is larger, the same or smaller than the binary representation of lowercase letters for individual characters. For the Unicode character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md) used by ABAP, uppercase letters are smaller than lowercase letters. Numbers and special characters are not case-sensitive and the result of the comparison for equality is true.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA char TYPE c LENGTH 1. 
cl_demo_input=>request( CHANGING field = char ). 
 
out->write( 
  COND #( WHEN to_upper( char ) > to_lower( char ) 
               THEN `Upper case is greater than lower case` 
          WHEN to_upper( char ) = to_lower( char ) 
               THEN `Upper case is equal to lower case` 
               ELSE `Upper case is lower than lower case` ) ). 
 
out->display( ).
```

## Byte-Like Comparison Type

If the comparison type is one of the [byte-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), the content is compared from left to right. Based on the byte values, the first differing byte from the left determines which operand is greater.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A byte-like comparison type is achieved by comparing byte-like operands. Invalid values are converted into hexadecimal zeros here when they are entered.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA hex1 TYPE x LENGTH 1. 
cl_demo_input=>add_field( CHANGING field = hex1 ). 
DATA hex2 TYPE x LENGTH 1. 
cl_demo_input=>request( CHANGING field = hex2 ). 
 
out->write( 
  COND #( WHEN hex1 > hex2 
               THEN `HEX1 is greater than HEX2` 
          WHEN hex1 = hex2 
               THEN `HEX1 equals HEX2` 
               ELSE `HEX1 is lower than HEX2` ) ). 
 
out->display( ).
```

## Date/Time Type as Comparison Type

If the comparison type is one of the [date/time types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), the content is compared from left to right. Based on the internal binary representation in the [code page](../../abap-glossary/abencodepage_glosry.md) used, the first differing character from the left determines which operand is greater.

### Hint

For operands of types `d` and `t` that contain a valid date or a valid time, the later date or time is always greater than the earlier one.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comparison of a date obtained by the addition of a numeric value from the current date to the original date. The later date is always greater than the earlier date.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(date) = cl_demo_date_time=>get_user_date( ). 
cl_demo_input=>add_field( CHANGING field = date ). 
DATA(days) = CONV int2( 0 ). 
cl_demo_input=>request( CHANGING field = days ). 
 
FINAL(new_date) = CONV d( date + days ). 
 
out->write( 
  COND #( WHEN new_date > date 
               THEN `NEW_DATE is greater than DATE` 
          WHEN new_date = date 
               THEN `NEW_DATE equals DATE` 
               ELSE `NEW_DATE is lower than DATE` ) ). 
 
out->display( ).
```

## Time Stamp Type as Comparison Type

If the comparison type is the [time stamp type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), the times are compared, whereby a later time is always the greater value and the initial value is always less than every real time stamp.

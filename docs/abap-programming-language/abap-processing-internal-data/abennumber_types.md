---
title: "Numeric Data Types"
source_file: abennumber_types.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Data Types

ABAP supports the numeric data types [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`int8`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`decfloat16`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`decfloat34`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), and [`f`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), as well as the internal types [`b`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`s`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The latter cannot be specified directly in programs but are created with reference to the built-in types `INT1` or `INT2` from the ABAP Dictionary. They are generally used in the same way as the type `i` and are often converted to `i` internally.

The numeric data types are used to store numeric values and are intended for calculations. Calculations with fields of the types `i`, `int8`, and type `f` can more or less be mapped directly to the machine commands of the operating system of the current AS instance [host computer](../../abap-glossary/abenhost_computer_glosry.md). In contrast, calculations with packed numbers of type `p` are implemented in the kernel of the ABAP runtime framework and are therefore somewhat slower. Operations using the decimal floating point numbers `decfloat16` and `decfloat34` are executed using a library integrated into the ABAP kernel until they are supported by the hardware of the host computer.

- [Integer Numbers](abennumber_types.md#integer-numbers)

- [Packed Numbers](abennumber_types.md#packed-numbers)

- [Floating Point Numbers](abennumber_types.md#floating-point-numbers)

  - [Decimal Floating Point Numbers](abennumber_types.md#decimal-floating-point-numbers)

  - [Binary Floating Point Numbers](abennumber_types.md#binary-floating-point-numbers)

The common generic type of the numeric data types is `numeric`.

## Hints

- To a great extent, [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md) of the types `decfloat16` and `decfloat34` replace the [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md) with type `f`.

- The built-in type `n` (numeric text field) is not a numeric number type, even though its values are only strings of digits. Instead, it is a character-like type, which should not be used in calculations. Typical examples of numeric text fields are account numbers and article numbers, postal codes, and so on.

## Integer Numbers

The data types for integer numbers [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`int8`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) have a [value range](../../abap-glossary/abenvalue_range_glosry.md) from -2147483648 to +2147483647 for `i` and -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 for `int8` and only cover integers. Integer numbers with the type `i` can be specified directly in the program as [numeric literals](../../abap-glossary/abennumeric_literal_glosry.md).

All interim results in [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) of the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `i` or `int8` are stored in helper fields of the type `i` or `int8`. Otherwise, type `i` or `int8` arithmetic behaves like the type `p` without [decimal places](../../abap-glossary/abendecimal_place_glosry.md). In particular, the division rounds numbers rather than truncating them and an overflow raises an exception. The data type `i` and `int8` is typically used for counters, quantities, indexes, and offsets, and time periods.

### Hint

The data types [`b`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`s`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), and [`int8`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) provide a complete set of data types for 1-, 2-, 4-, and 8-byte integer numbers. The types `b` and `s` for short integer numbers, however, cannot be specified directly in ABAP programs but have to be specified using the built-in types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) from the ABAP Dictionary. These types also do not have their own calculation type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typical use of the data type `i`.

``` abap
DATA counter TYPE i. 
... 
counter += 1. 
...
```

## Packed Numbers

The data type [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) for [packed numbers](../../abap-glossary/abenpacked_number_glosry.md) has a [value range](../../abap-glossary/abenvalue_range_glosry.md) that depends on the length and the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md). Data objects of type `p` can be 1 to 16 bytes long, with two [places](../../abap-glossary/abenplace_glosry.md) packed in each byte, and one place and the plus/minus sign packed in the last byte. A packed number consists of the length multiplied by 2 minus 1 digits and can have a maximum of 14 decimal places. Packed numbers implement [fixed point numbers](../../abap-glossary/abenfixed_point_number_glosry.md). The decimal places of a packed number are a property of its data type and are predefined for it.

Packed numbers with decimal places cannot be specified directly in the program. Instead, [character literals](../../abap-glossary/abencharacter_literal_glosry.md) must be used whose content can be interpreted as a packed number, that is, a number in [mathematical](../../abap-glossary/abenmathematical_notation_glosry.md) or [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md). [Scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) is not allowed unless it can be interpreted as a mathematical notation.

Helper fields for interim results in [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) of [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `p` are always 16 bytes long and can thus include up to 31 places. Before an overflow occurs, an arithmetic expression is calculated again with helper fields that are twice as large or 63 places. In [comparisons](../abap-program-flow-logic/abenlogexp_numeric.md) between packed numbers, the operand with fewer decimal places is also converted to such a helper field, but an overflow occurs if the sum of the integer digits and decimal places exceeds 31.

If packed numbers are used, the [program property](../../abap-glossary/abenprogram_property_glosry.md) must always be set to *fixed point arithmetic* since only this setting ensures that the decimal point is calculated correctly. Otherwise, all numbers are interpreted as integers and all interim results are rounded up to the next integer.

Calculations using calculation type `p` are performed using [fixed point arithmetic](../../abap-glossary/abenfixed_point_arithmetic_glosry.md). In other words, a calculation is performed *commercially*, as is the case when using a pocket calculator or paper and pencil. Type `p` is typically used for values such as lengths, weights, and sums of money.

### Hint

The number of decimal places in a packed number should not be greater than the number of digits; otherwise the decimal separator might be outside the sequence of digits. A packed number that has more decimal places than places can raise exceptions when converted to external formats such as data types of the database in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or in serializations to [asXML](../../abap-glossary/abenasxml_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typical use of the data type `p`.

``` abap
DATA price TYPE p LENGTH 16 DECIMALS 2.
```

## Floating Point Numbers

In floating point numbers, the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) is part of the value and not a part of the data type.

### Decimal Floating Point Numbers

The data types for [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md) are [`decfloat16`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`decfloat34`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The value range is `-(1-1E-16)*1E385` to `-1E-383`, `0`, `+1E-383` to `(1-1E-16)*1E385` for `decfloat16` and `-(1-1E-34)*1E6145` to `-1E-6143`, `0`, `+1E-6143` to `(1-1E-34)*1E6145` for `decfloat34`. The maximum precision is 16 places or 34 places. In addition to its value, a decimal floating point number has a [scaling](../../abap-glossary/abenscale_glosry.md) and a [precision](../../abap-glossary/abenprecision_glosry.md). These properties are not relevant for calculations and comparisons of values, but are used in [conversion rules](abenconversion_elementary.md) and for formatting output.

Decimal floating point numbers with decimal places or exponents cannot be specified directly in the program. Instead, [character literals](../../abap-glossary/abencharacter_literal_glosry.md) must be used whose content can be interpreted as a packed number, that is, a number in [mathematical](../../abap-glossary/abenmathematical_notation_glosry.md), [scientific](../../abap-glossary/abenscientific_notation_glosry.md), or [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md).

[Arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) with decimal floating point numbers always have the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `decfloat34`. Each calculation is performed using [decimal floating point arithmetic](../../abap-glossary/abendecfloat_arith_glosry.md). Decimal floating point numbers are the best choice if precision and a large range of values are of importance. They do not have the disadvantages of binary floating point numbers described below, which cannot represent each decimal number within their value range exactly and they have a much larger value range and a higher level of precision than packed numbers.

The lossless operator [`EXACT`](abenconstructor_expression_exact.md) can be used to force a lossless calculation for decimal floating point numbers under certain circumstances. No rounding is allowed and raises an exception in lossless calculations.

Internally, decimal floating point numbers are represented by a 16-digit or 34-digit decimal mantissa and a decimal exponent, which is between -383 and +384 or -6143 and + 6144, respectively. Apart from potential roundings in assignments and calculations, the effects discussed below for binary floating point numbers do not occur, since every 16-digit or 34-digit decimal number can be represented exactly.

### Binary Floating Point Numbers

The data type for [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md), [`f`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), has a [value range](../../abap-glossary/abenvalue_range_glosry.md) of 2.2250738585072014E-308 to 1.7976931348623157E+308, positive, negative, and the number 0, with a precision of at least 15 places. 17 places are represented in ABAP. Integers can be represented exactly up to an absolute value of 2\*\*53, which is equivalent to 9,007,199,254,740,992. Any larger numbers are rounded.

Binary floating point numbers cannot be specified directly in the program. Instead, [character literals](../../abap-glossary/abencharacter_literal_glosry.md) must be used whose content can be interpreted as floating point numbers, that is, a number in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md). [Mathematical](../../abap-glossary/abenmathematical_notation_glosry.md) or [commercial notation](../../abap-glossary/abencommercial_notation_glosry.md) is not allowed unless it can be interpreted as scientific notation.

[Arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) with [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `f` are performed using [binary floating point arithmetic](../../abap-glossary/abenbinfloat_arith_glosry.md). The following features of binary floating point arithmetic should be considered.

Internally, binary floating point numbers are represented by a dual fraction and a dual exponent. This can lead to unexpected results despite the high degree of intrinsic precision. These occur mainly when converting from and to type `f`.

- For example, the number 1.5 can be represented exactly in this notation since 1.5 = 1\*2\*\*0 + 1\*2\*\*(-1), but the number 0.15 can only be represented approximately by the number 0.14999999999999999. If 0.15 is rounded up to 1 valid digit, the result is 0.1 rather than the 0.2 as expected. On the other hand, the number 1.5E-12 is represented by the number 1.5000000000000001E-12, which would be rounded up to 2E-12.

- A further real-life example: 7.27% of 73050 needs to be calculated and rounded to 2 decimal places. The interim result is 5.3107349999999997E+03, since the correct result, 5310.735, cannot be represented exactly in two parts with 53 bits. (If the hardware cannot represent a real number exactly, it uses the next representable binary floating point number). After rounding, the result 5310.73 is produced, rather than 5310.74 as expected.

The ABAP runtime framework always rounds commercially and not numerically like the underlying machine arithmetic. According to the rounding algorithm of the latter, the end digit 5 must always be rounded to the nearest even number (not the next largest number), that is, from 2.5 to 2 and from 3.5 to 4.

It should also be noted that multiplication using powers of 10 (positive or negative) is not an exact operation.

- Example: Although it can be represented exactly in two parts, a binary floating point number `f` of value 100.5, after the operation

  `f = f / 100 * 100.` has the value 100.49999999999999.

In addition to rounding errors, the restricted number of decimal places for the mantissa can lead to the loss of trailing digits.

- Example: `1 - 1.0000000000000001` produces zero.

This means that the final places in binary floating point arithmetic are not reliable. In particular, it is not usually worth testing two binary floating point numbers `a` and `b` for equality. Instead, it is best to check whether the relative difference `abs((a - b)/a)` is less than a predefined limit, for example 10\*\*(-7).

Ultimately, the representation and therefore the value of a binary floating point number stored in the database can be platform-dependent.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the calculation in `result1` is `0.81499999999999995` whereas in `result2` it is the expected value *0.815*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: result1 TYPE f, 
      result2 TYPE decfloat34. 
 
result1 = 815 / 1000. 
result2 = 815 / 1000. 
 
out->write( |Binary  floating point: { result1 }\n| && 
            |Decimal floating point: { result2 }\n| ). 
 
out->display( ).
```

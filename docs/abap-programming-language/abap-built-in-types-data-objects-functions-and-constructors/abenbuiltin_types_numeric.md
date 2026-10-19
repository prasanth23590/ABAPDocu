---
title: "Built-In Numeric Types"
source_file: abenbuiltin_types_numeric.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types > Built-In ABAP Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Numeric Types

The data objects of the [numeric data types](../../abap-glossary/abennumeric_data_type_glosry.md) are used to store numeric values.

**Properties**

| **Type**     | **Length**    | **Standard Length** | **Meaning**                                                                        | **Data Object**                                                          |
|--------------|---------------|---------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `b`          | 1 byte        |                     | Internal 1-byte [integer type](../../abap-glossary/abeninteger_type_glosry.md)                       | 1 byte [integer](../../abap-glossary/abeninteger_glosry.md)                                |
| `s`          | 2 byte        |                     | Internal 2-byte [integer type](../../abap-glossary/abeninteger_type_glosry.md)                       | 2 byte [integer](../../abap-glossary/abeninteger_glosry.md)                                |
| `i`          | 4 byte        |                     | 4-byte [integer type](../../abap-glossary/abeninteger_type_glosry.md)                                | 4 byte [integer](../../abap-glossary/abeninteger_glosry.md)                                |
| `int8`       | 8 byte        |                     | 8-byte [integer type](../../abap-glossary/abeninteger_type_glosry.md)                                | 8 byte [integer](../../abap-glossary/abeninteger_glosry.md)                                |
| `p`          | 1 to 16 bytes | 8 byte              | [Packed number type](../../abap-glossary/abenpacked_number_type_glosry.md)                           | [Packed number](../../abap-glossary/abenpacked_number_glosry.md)                           |
| `decfloat16` | 8 byte        |                     | [Decimal floating point number type](../../abap-glossary/abendecfloat_type_glosry.md) with 16 places | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) with 16 places |
| `decfloat34` | 16 byte       |                     | [Decimal floating point number type](../../abap-glossary/abendecfloat_type_glosry.md) with 34 places | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) with 34 places |
| `f`          | 8 byte        |                     | [Binary floating point number type](../../abap-glossary/abenbinfloat_type_glosry.md) with 17 places  | [Binary floating point number](../../abap-glossary/abenbinfloat_glosry.md) with 17 places  |

**Value Ranges and Initial Values**

| **Type**     | **Value Range**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Initial Value** |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| `b`          | *0* to *255*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *0*               |
| `s`          | *-32,768* to *+32,767*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *0*               |
| `i`          | *-2,147,483,648* to *+2,147,483,647*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *0*               |
| `int8`       | *-9,223,372,036,854,775,808* to *+9,223,372,036,854,775,807*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *0*               |
| `p`          | The valid length for packed numbers is between 1 and 16 bytes. Two places are packed into one byte, where the last byte contains only one place and the sign, which is the number of places or places calculated from `2 * len1`. After the decimal separator, up to 14 [decimal places](../../abap-glossary/abendecimal_place_glosry.md) are allowed (the number of decimal places should not exceed the number of places). Depending on the field length `len` and the number of decimal places `dec`, the value range is: *(-10<sup>(2len-1) +1) / (10</sup>(+dec))* to *(+10<sup>(2len-1) -1) /(10</sup>(+dec))* in increments of *10^(-dec)*. Any intermediate values are rounded decimally. Invalid content produces undefined behavior. | *0*               |
| `decfloat16` | Decimal floating point numbers of this type are represented internally with 16 places in accordance with the IEEE-754-2008 standard. Valid values are numbers between *-(1-1E-16)\*1E385* and *-1E-383* for the negative range, *0*, and numbers between *+1E-383* to *(1-1E-16)\*1E385(* for the positive range. Values between the ranges form the subnormal range and are rounded. Outside of the subnormal range, each 16-digit decimal number can be represented exactly with a decimal floating point number of this type.                                                                                                                                                                                             | *0*               |
| `decfloat34` | Decimal floating point numbers of this type are represented internally with 34 places in accordance with the IEEE-754-2008 standard. Valid values are numbers between *-(1-1E-34)\*1E6145* and *-1E-6143* for the negative range, *0*, and numbers between *+1E-6143* and *(1-1E-34)\*1E6145* for the positive range. Values between the ranges form the subnormal range and are rounded. Outside of the subnormal range, each 34-digit decimal number can be represented exactly using a decimal floating point number.                                                                                                                                                                                                     | *0*               |
| `f`          | Binary floating point numbers are represented internally according to the IEEE-754 standard (double precision). In ABAP, 17 places are represented (one integer digit and 16 decimal places). Valid values are numbers between *-1.7976931348623157E+308* and *-2.2250738585072014E-308* for the negative range and between *+2.2250738585072014E-308* and *+1.7976931348623157E+308* for the positive range, plus 0. Both validity intervals are extended to the value zero by subnormal numbers according to IEEE-754. Not every 16-digit number can be represented exactly by a binary floating point number.                                                                                                             | *0*               |

## Hints

- The numeric data objects are used to store numeric values and [numeric calculations](../abap-processing-internal-data/abencompute_expressions.md). Here, the data type `f` for binary floating point numbers is replaced largely by the types `decfloat16` and `decfloat34` for decimal floating point numbers.

- The types `b` and `s` are internal and cannot be specified either statically or dynamically in ABAP statements. User-defined data types and data objects in ABAP programs have the data types `b` or `s`, provided that they were defined with reference to data elements of the ABAP Dictionary that have the DDIC data types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The system class [`CL_ABAP_MATH`](../abap-processing-internal-data/abenfloating_point_class.md) contains constants for the minimum and maximum values of most numeric types. The methods `GET_MIN_VALUE` and `GET_MAX_VALUE` in the class `CL_ABAP_EXCEPTIONAL_VALUES` can also be used.

- The system class `CL_ABAP_ELEMDESCR` of [RTTS](../abap-processing-internal-data/abenrtti.md) contains constants `TYPE_P_MAX_LENGTH` and `TYPE_P_MAX_DECIMALS` for the maximum length and the maximum number of decimal places for the type `p`.

- Due to the internal representation of the decimal places of a floating point number of type `f` as dual fractions, there is not an exact equivalent for every number that can be represented in the decimal system. This can cause rounding errors in assignments and interim results of calculations. These errors can be avoided by using a two-level rounding procedure (see [Example](../abap-processing-internal-data/abenfloating_point_class.md)).

- The type `p`, for which a length interval is specified in the second column of the first table, is [generic](abenbuilt_in_types_generic.md), which means that the length is not part of the type description. In addition to the length, the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) is undefined. The entry in the column `Standard Length` determines the length that is used in declarations of data objects when using types with generic lengths, if no explicit length is specified in the corresponding statement.

- The data type `p` is used to implement [fixed point numbers](../../abap-glossary/abenfixed_point_number_glosry.md). The number of decimal places in a packed number with the type `p` is a type property that is defined using the addition [`DECIMALS`](../abap-declarations/abaptypes_simple.md) and that is not stored with the number. Technically, the numeric value is determined by dividing the stored string of digits of the packed number by 10 to the power of the number of decimal places (`10^(+dec)`). In the definition of a packed number, the number of decimal places should not be greater than the number of places calculated from `2 * len - 1`. Otherwise, the decimal separator is outside the strings of digits and not all decimal places can be given values. For example, a packed number with length 1 and two decimal places would have a value range of `-0.09` to `+0.09` in increments of `0.01` but there cannot be a value for which the first decimal place is also filled, as for example `0.14`.

- A number with the data type `p` that has more decimal places than places can raise exceptions when converting to external formats such as data types of the database in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or during serializations to [asXML](../../abap-glossary/abenasxml_glosry.md).

- The [built-in types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) of the ABAP Dictionary mapped to the data type `p` cannot have more decimal places than places. In ABAP, such declarations, if known statically, produce a syntax check warning.

- See also [Numeric Data Types](../abap-processing-internal-data/abennumber_types.md).

- For data objects with data type `p`, the [program property](../../abap-glossary/abenprogram_property_glosry.md) *Fixed Point Arithmetic* must be set so that the decimal separator is respected. Otherwise, the content is handled in all operations as if there were no decimal separator. The sequence of digits in the variables of type `p` is interpreted as an integer value. Exceptions are:

  - Representation on screens

  - [Assignments](../abap-processing-internal-data/abenconversion_type_p.md) to character-like objects with the types `c` and `string`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of variables with built-in numeric ABAP types for a numeric calculation.

``` abap
DATA: num1   TYPE i, 
      num2   TYPE i, 
      result TYPE decfloat34. 
 
... 
 
result = num1 / num2.
```

## Executable Example

[Value Ranges of Packed Numbers](abentype_p_value_range_abexa.md)

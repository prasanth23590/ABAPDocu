---
title: "TYPES, TYPE abap_type"
source_file: abaptypes_simple.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, TYPE abap_type

## Syntax

``` abap
TYPES { {dtype[(len)] TYPE abap_type [DECIMALS dec]}   
      | {dtype TYPE abap_type [LENGTH len] [DECIMALS dec]}}.  
```

### Addition

[`... DECIMALS dec`](abaptypes_simple.md#addition)

## Overview

### Description

By specifying a [built-in data type](../../abap-glossary/abenbuiltin_abap_type_glosry.md) `abap_type`, a non-generic elementary data type is defined. For `abap_type`, all [built-in data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) can be used, except for the internal types `b` and `s`.

For the ABAP types `c`, `n`, `p`, and `x`, the length of the data type `dtype` must be specified by entering a number directly or by specifying a corresponding numeric constant `len` within the [length range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) defined for the type in question. For all other ABAP types, the length is determined by the value in the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of built-in ABAP types and no length can be specified in `len`.

The length `len` is specified either in parentheses directly after the type name `dtype`, or after the addition `LENGTH`. The specified length must be positive. If the length is not specified explicitly for the ABAP types `c`, `n`, `p`, and `x`, the [standard length](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) is defined implicitly.

### Hints

- For reasons of legibility, it is best to always use the addition `LENGTH` instead of parentheses to specify the length `len`.

- The non-specifiable internal types `b` and `s` can be achieved by referencing the built-in data types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

These statements create three elementary data types that are local to the program. Values for the unspecified technical properties of the built-in types `c` and `p` are specified.

``` abap
TYPES: text10 TYPE c LENGTH 10, 
       text20 TYPE c LENGTH 20, 
       number TYPE p LENGTH 8 DECIMALS 2.
```

## Addition

`... DECIMALS dec`

### Description

In the ABAP type [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), the number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) must be defined using the addition `DECIMALS` and by specifying an unsigned number directly or a corresponding numeric constant `dec`. The addition cannot be specified in other data types.

A maximum of 14 decimal places can be specified. If the number of decimal places is greater than the number of places or digits calculated from `2 * len - 1`, a syntax check warning occurs. This is because only the last `2 * len - 1` decimal places can be filled with digits.

For the decimal separator to be respected in operations with packed numbers, the [program property](../../abap-glossary/abenprogram_property_glosry.md) *fixed point arithmetic* must be set.

### Hint

If the number of decimal places is greater than the number of digits, the decimal separator is outside the sequence of digits, which should be respected in assignments and outputs. Such a number can raise exceptions in conversions to external formats such as data types of the database in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or during serializations to [asXML](../../abap-glossary/abenasxml_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a numeric type for a packed number with three digits and two decimal places. The value range is -9.99 to +9.99 in increments of 0.01.

``` abap
TYPES number TYPE p LENGTH 2 DECIMALS 2.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines a numeric type for a packed number with three digits and five decimal places. This statement produces a syntax check warning. The value range is -0.00999 to +0.00999 in increments of 0.00001. Not all decimal places can be used.

``` abap
TYPES number TYPE p LENGTH 5 DECIMALS 5.
```

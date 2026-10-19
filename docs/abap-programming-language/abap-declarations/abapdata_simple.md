---
title: "DATA, TYPE abap_type"
source_file: abapdata_simple.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, TYPE abap_type

## Syntax

``` abap
DATA { {var[(len)] TYPE abap_type [DECIMALS dec]}   
     | {var [TYPE abap_type [LENGTH len] [DECIMALS dec]]} }   
     [VALUE val|{IS INITIAL}]   
     [READ-ONLY].  
```

[`[VALUE val|{IS INITIAL}]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

By specifying a [built-in data type](../../abap-glossary/abenbuiltin_data_type_glosry.md) `abap_type`, an elementary variable `var` is defined. For `abap_type`, all [built-in data types](../../abap-glossary/abenbuiltin_abap_type_glosry.md) can be used, except for the internal types `b` and `s`.

The syntax and meaning of `LENGTH`, `len`, `DECIMALS`, and `dec` are identical to the definition of elementary data types using [`TYPES`](abaptypes_simple.md) and must be specified within the specified [areas](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). Here, however, they are used to create a bound data type. If `len` or `dec` are not specified for the ABAP types `c`, `n`, `p`, and `x`, the bound type is created using the [type-specific standard length](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) and, for `p`, without decimal places.

## Hints

- For reasons of legibility, it is best to include all information and always use the addition `LENGTH` instead of parentheses to specify the length `len`.

- The non-specifiable internal types `b` and `s` can be applied by referencing the built-in data types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) from the ABAP Dictionary.

- A data type that is constructed with the statement `DATA` is a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md) that only exists as a property of the data object. It has a [technical type name](../../abap-glossary/abentechnical_type_name_glosry.md), that can be retrieved as part of an [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md) by [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

These statements declare three variables and set their start values.

``` abap
DATA: text  TYPE string VALUE `Text`, 
      count TYPE i VALUE 1, 
      price TYPE p LENGTH 8 DECIMALS 2 VALUE '1.99'.
```

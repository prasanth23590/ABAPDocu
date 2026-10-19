---
title: "CONSTANTS"
source_file: abapconstants.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONSTANTS

## Syntax

``` abap
CONSTANTS const [options].  
```

[`options`](abapdata.md)

## Description

This statement declares a constant data object or a constant `const` for short. Its content cannot be changed at runtime of an ABAP program. It can only be used as an operand in [read positions](../../abap-glossary/abenread_position_glosry.md) of ABAP statements. Constants declared in the declaration part of a class or an interface belong to their [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md).

The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `const`. The syntax of the additions `options` of the statement `CONSTANTS` for declaring constants matches the statement [`DATA`](abapdata.md) for declaring variables. Only the additions [`READ-ONLY`](abapdata_options.md) and [`BOXED`](abapdata_boxed.md) are not possible. In addition, the statement `INCLUDE` cannot be used within the declaration of a structure.

Unlike the statement `DATA`, an [initial value](../../abap-glossary/abenstart_value_glosry.md) with the addition [`VALUE`](abapdata_options.md) must be specified in the statement `CONSTANTS`. The same restrictions as for `DATA` apply. This has the following implications for the declaration of constants with [deep](../../abap-glossary/abendeep_glosry.md) data types:

- A start value `val` can only be specified for the ABAP types `string` and `xstring` only.

- Constant internal tables, reference variables, and structures with non-character-like and flat components can only be assigned their [initial value](../../abap-glossary/abeninitial_value_glosry.md) by `IS INITIAL` only, and are therefore always initial.

## Hints

- If the class component selector is used, the interface name can also be used to access static attributes of interfaces declared using `CONSTANTS`.

- The values of constants are stored in the [PXA](../../abap-glossary/abenpxa_glosry.md) memory area.

- Constants cannot be declared with [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) and results of expressions cannot be assigned to constants. For such purposes, ABAP supports [immutable variables](../../abap-glossary/abenimmutable_variable_glosry.md) that can be declared with the declaration operator [`FINAL(var)`](abenfinal_inline.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statements below declare a numeric constant, a constant structure, and a constant reference. The latter can be used in comparisons or in passing to [procedures](../../abap-glossary/abenprocedure_glosry.md).

``` abap
CONSTANTS pi TYPE p LENGTH 8 DECIMALS 14 
             VALUE '3.14159265358979'. 
 
CONSTANTS: BEGIN OF sap_ag, 
             zip_code TYPE n LENGTH 5 VALUE '69189', 
             city     TYPE string VALUE `Walldorf`, 
             country  TYPE string VALUE `Germany`, 
           END OF sap_ag. 
 
CONSTANTS null_pointer TYPE REF TO object VALUE IS INITIAL.
```

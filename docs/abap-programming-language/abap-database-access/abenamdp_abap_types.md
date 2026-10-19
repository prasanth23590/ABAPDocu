---
title: "AMDP - Macro for ABAP Types"
source_file: abenamdp_abap_types.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Macros"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Macro for ABAP Types

## Syntax

``` abap
... "$ABAP.type( [name =] abap_type )" ...  
```

## Description

Specifies the predefined [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md) `$ABAP.type` for an ABAP type.

In an AMDP method implemented in SQLScript, the AMDP macro `$ABAP.type` can be used to access the ABAP type `abap_type`. For `abap_type`, all [elementary](../../abap-glossary/abenelementary_data_type_glosry.md) non-[generic](../../abap-glossary/abengeneric_data_type_glosry.md) types can be specified that would be possible after a `TYPE` addition in an ABAP implementation of the method. These are as follows:

- The [built-in ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) `i`, `int8`, `decfloat16`, `decfloat34`, `f`, `string`, `xstring`, `d` and `t`.

- All elementary types that are defined with [`TYPES`](../abap-declarations/abaptypes.md) and that are visible at this place. These can be types of the own class, a different class or an interface.

- All elementary types defined in the [ABAP Dictionary](../../abap-dictionary-ddic/abenabap_dictionary.md), such as data elements or elementary components of structured types.

The ABAP runtime framework replaces this expression in accordance with the rules specified in the [mapping tables](abenamdp_hdb_sqlscript_mapping.md) with the corresponding HANA type. `abap_type` is not case-sensitive.

## Executable Example

[Access to ABAP Types](abenamdp_abap_types_cs_abexa.md)

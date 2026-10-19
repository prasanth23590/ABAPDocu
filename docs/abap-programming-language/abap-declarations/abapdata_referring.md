---
title: "DATA, TYPE, LIKE"
source_file: abapdata_referring.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, TYPE, LIKE

## Syntax

``` abap
DATA var { {TYPE [LINE OF] type}   
         | {LIKE [LINE OF] dobj} }   
         [VALUE  val|{IS INITIAL}]   
         [READ-ONLY].  
```

[`[VALUE val|{IS INITIAL}]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

When a `type` data type or a `dobj` data object is specified, the data type of variable `var` is already fully defined before the declaration. The syntax and meaning of the additions `TYPE` and `LIKE` are exactly the same as the definition of the data types with [`TYPES`](abaptypes_referring.md), with the following exceptions:

- In the case of `DATA`, a standard table type with [generic primary table key](abaptypes_keydef.md) can be specified after `TYPE`. This creates a bound table type with a [standard key](../../abap-glossary/abenstandard_key_glosry.md).

- In the case of `DATA`, a table type can be specified after `TYPE` that is generic with respect to its [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) because of the explicit addition [`WITH FURTHER SECONDARY KEYS`](abaptypes_keydef.md). This type property is not relevant for the declared data object.

If neither `TYPE` nor `LIKE` is specified, a data object with the bound data type `c` of length 1 is created.

## Hints

- For internal tables, the declaration of the primary table key as a [standard key](../abap-data-types-and-data-objects/abenitab_standard_key.md) can be critical for various reasons. It is best to define the key fields explicitly instead. For this reason, in the case of the statement above, it must be ensured that a table with a standard key is not created by mistake if a generic standard table type is used.

- If an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) is specified after `TYPE` or a data object with this type is specified after `LIKE`, an [enumerated variable](abapdata_enum.md) is created.

- When referring to data types defined in the ABAP Dictionary, the [initial value](../../abap-glossary/abeninitial_value_glosry.md) of elementary data types is not the initial value assigned to the [built-in dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and is the initial value of the mapped [built-in ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) instead.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the `TYPE` addition to declare a work area for a [`SELECT`](../abap-database-access/abapselect.md) statement. Use of the `LIKE` addition to declare a further data object of the same type.

``` abap
DATA wa TYPE scarr. 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'BA' 
       INTO @wa. 
 
DATA buffer LIKE wa. 
buffer = wa.
```

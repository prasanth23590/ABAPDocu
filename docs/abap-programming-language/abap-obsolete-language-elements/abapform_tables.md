---
title: "FORM, table_parameters"
source_file: abapform_tables.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Modularization > Subroutines > FORM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FORM, table_parameters

## Obsolete, deprecated Syntax

``` abap
... t1 [{TYPE itab_type}|{LIKE itab}|{STRUCTURE struc}]   
    t2 [{TYPE itab_type}|{LIKE itab}|{STRUCTURE struc}]   
    ...  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

Defines [table parameters](../../abap-glossary/abentable_parameter_glosry.md) `t1 t2 ...` for subroutines. A table parameter is typed as follows:

- A table type `itab_type` of the table category [standard table](../../abap-glossary/abenstandard_table_glosry.md) can be specified after the addition `TYPE`. Both complete and generic table types are possible, as well as the built-in generic type `STANDARD TABLE`.

- An internal table `itab` of the table category [standard table](../../abap-glossary/abenstandard_table_glosry.md) can be specified after the addition `LIKE`. The technical properties of this internal type are applied completely.

- A [flat structure](../../abap-glossary/abenflat_structure_glosry.md) `struc` can be specified after the obsolete addition [`STRUCTURE`](abapform_structure.md).

- If nothing is specified explicitly, `TYPE STANDARD TABLE` is used implicitly as the typing.

The additions `TYPE` and `LIKE` type the formal parameter either generically or completely. The addition `STRUCTURE` applies the structure `struc` to the line type. The table key remains generic. In generic typings, the formal parameter takes the non-fixed technical type properties from the actual parameter and the usual [typing](../abap-declarations/abentyping.md) rules apply.

## Hints

- The definition of table parameters is obsolete and can be replaced by general [formal parameters](abapform_parameters.md) defined using `USING` and `CHANGING`.

- The table key of a table parameter is either defined completely in the typing or it is taken from the actual parameter in the case of generic typing. This means that the table key of a table parameter is not necessarily the [standard key](../abap-data-types-and-data-objects/abenitab_standard_key.md).

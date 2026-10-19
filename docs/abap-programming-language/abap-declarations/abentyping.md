---
title: "Typing"
source_file: abentyping.html
section: "ABAP Programming Language > ABAP - Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Typing

Typing means specifying a generic or complete data type for a [formal parameter](../../abap-glossary/abenformal_parameter_glosry.md) of a [procedure](../../abap-glossary/abenprocedure_glosry.md) or for a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md). When an actual parameter is assigned to a formal parameter, or a data object to a field symbol, the systems performs a a [check](abentyping_check.md) whether the data type matches the typing.

## Generically Typed

Unlike data objects, where the data type has a specific property and is always completely known, formal parameters and field symbols that are generically typed receive their complete data type only when an actual parameter is passed in a procedure call or when a memory area is assigned using [`ASSIGN`](../abap-processing-internal-data/abapassign.md).

When using generically typed formal parameters or field symbols, a distinction must be made between static and dynamic access.

- In static access to a generically typed formal parameter, field symbol, or their components, the type properties specified by the typing of the formal parameter are used. In static accesses where a complete data type is required, a [standard type](../../abap-glossary/abenstandard_type_glosry.md) is used if possible.

- In dynamic access to a generically typed formal parameter, field symbol, or their components, the type properties of the actual parameter are used.

The properties of the actual parameter, which are not [checked](abentyping_check.md) in calls or assignments, can be different from those of the formal parameter. This can produce different behavior in static and dynamic accesses. A dynamic access to components of generically typed formal parameters will result in a runtime error if the components do not exist in the actual parameter.

## Completely Typed

During compilation and at runtime, formal parameters and field symbols that are completely typed are handled like data objects with completely known data types.

When completely typed formal parameters, or field symbols are used, the properties specified by the typing are used, regardless of whether they are accessed statically or dynamically.

### Hints

- The typing of formal parameters or field symbols defines some or all of the type properties before the actual specification of the type. This allows the use of formal parameters and field symbols in operand positions that require certain type properties.

- If the typing of an existing field symbol or formal parameter is made weaker, note that there may then be fewer options for static accesses and that the associated standard type may change if they are used in [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md).

- The static type of data reference variables is always completely generic (`data`) or completely typed (see [`DATA` - reference variables](abapdata_references.md)).

- An obsolete [table parameter](../../abap-glossary/abentable_parameter_glosry.md) can be typed completely or generically with respect to the table key and the same rules apply as to other formal parameters.

### Executable Example

[Generic Typing and Complete Typing](abentyping_abexa.md)

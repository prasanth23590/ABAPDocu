---
title: "typing Addition, complete_type"
source_file: abentyping_complete.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > typing Addition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# typing Addition, complete_type

## Syntax

``` abap
... { TYPE {[LINE OF] complete_type}   
         | {REF TO type} }   
  | { LIKE {[LINE OF] dobj}   
         | {REF TO dobj} } ...  
```

## Description

To completely type a formal parameter or a field symbol:

- Any non-generic type `complete_type` can be specified after `TYPE`. `complete_type` can be a non-generic data type from the ABAP Dictionary or ABAP CDS, a non-generic public data type from a global class, a non-generic program-local type already defined using [`TYPES`](abaptypes.md), or a non-generic [built-in ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md).

- A data object `dobj` can be specified after `LIKE`. `dobj` according to the rules [`TYPES ... LIKE`](abaptypes_referring.md). The bound type of the data object is transferred. If field symbols and formal parameters are specified for `dobj`, they must be completely typed to create the corresponding complete typing.

If `complete_type` or the data type of `dobj` is table-like, `LINE OF` can be used to refer to the appropriate line type.

`REF TO` types the formal parameter or field symbol as a reference variable, whereby the same rules apply as to the [definition of reference types in `TYPES`](abaptypes_references.md). Typing with `TYPE REF TO data` or `TYPE REF TO object` is also considered a complete typing.

If an actual parameter or a memory area is assigned to completely typed formal parameters or field symbols, the technical properties of the specified data type must match the typing exactly (see [Typing Check](abentyping_check.md)), except when passing literals. Completely typed formal parameters or field symbols can be used in the same operand positions as data objects of the corresponding data type.

Type properties specified by the typing are used during both static and dynamic access to a completely typed formal parameter or field symbol.

## Hints

- The data types that can be referred to with `TYPE` include specifically [CDS types](../../abap-glossary/abencds_type_glosry.md).

- Complete data types, which can be referred to with `TYPE`, or indirectly using `LIKE`, also include [enumerated types](abaptypes_enum.md).

- `LIKE` can be used to refer to data objects, including the public attributes of global classes.

- In a `LIKE` reference to an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), the header line is used. To refer to the table type, `[]` must be appended to the name as per usual. A formal parameter (with the exception of [table parameters](../../abap-glossary/abentable_parameter_glosry.md)) or a field symbol can be typed only with reference to the header line or to the table type.

- The predefined generic data type [`any`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) cannot currently be specified after `REF TO`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, the field symbol `<spfli>` is completely typed with the structured data type `spfli` from the ABAP Dictionary, and can therefore be used like a structure of this data type.

``` abap
FIELD-SYMBOLS <spfli> TYPE spfli. 
... 
<spfli>-carrid = ...
```

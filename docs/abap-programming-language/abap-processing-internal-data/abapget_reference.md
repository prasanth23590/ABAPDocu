---
title: "GET REFERENCE"
source_file: abapget_reference.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET REFERENCE

## Deprecated Syntax

``` abap
GET REFERENCE OF dobj INTO dref.  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

This statement sets the [reference](../../abap-glossary/abenreference_glosry.md) in the reference variable `dref` so that it points to the data object `dobj`. The following can be specified for `dref`:

- An existing [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md). The static type of the data reference variable must be more general than or the same as the data type `dobj`, according to the [assignment rules for reference variables](abenconversion_references.md).

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). This declares a data reference variable whose static type is the data type of `dobj`. The data type of `dobj` must be known statically as a complete type or as the generic type `data`. Field symbols and formal parameters with other generic types, in particular `any`, are not possible.

The data object is specified directly and in accordance with the rules described in the section [Read Positions](../abap-operands/abendata_objects_usage_reading.md). If offsets/lengths ([`+off(len)`](../abap-operands/abenoffset_length.md)) are specified, the data type `dobj` here cannot be `string` or `xstring`.

### Hints

- In addition to the reference operator [`REF`](abenconstructor_expression_ref.md) and the addition [`REFERENCE INTO`](abapread_table_outdesc.md), the statement `GET REFERENCE` is the only option for internal table statements to create [stack references](../../abap-glossary/abenstack_reference_glosry.md). Stack references can become invalid if the referenced data object is deleted.

- When applied to data objects in the [heap](../../abap-glossary/abenheap_glosry.md) `GET REFERENCE` creates memory-retaining [heap references](../../abap-glossary/abenheap_reference_glosry.md).

- The content of two reference variables filled with `GET REFERENCE` is only the same if the remaining administration information is the same, apart from the referenced data objects. For example, a reference that is obtained directly by specifying the data object is not the same as a reference that is obtained by specifying a field symbol if it has a different data type due to a [casting](../../abap-glossary/abencast_casting_glosry.md).

- For an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), a data reference variable can only point to this or the [table body](../../abap-glossary/abentable_body_glosry.md). In the statement `GET REFERENCE`, the name of an internal table with a header line addresses the header line. To address the table body, `[]` must be appended to the name as usual. A dereferenced data reference to which a table body is assigned behaves in the same way in operand positions as a table without a header line.

- If references are set using `GET REFERENCE`, permission to access the corresponding data object is only checked at the position of the statement. The references can then be passed on to any destination and can be used to access the associated data objects from any position using the references. To prevent access to private and read-only attributes using references outside classes, do not publish references to these attributes externally. A constant or read-only input parameter, however, can never be made modifiable by passing its reference.

- The [reference operator](../../abap-glossary/abenreference_operator_glosry.md) [`REF`](abenconstructor_expression_ref.md) works like the statement `GET REFERENCE` and can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

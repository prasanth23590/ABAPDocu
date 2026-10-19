---
title: "Conversion Rules for Structures"
source_file: abenconversion_struc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Structures

In assignments between [structures](../abap-data-types-and-data-objects/abendata_objects_structure.md), it is necessary to distinguish between [flat structures](../../abap-glossary/abenflat_structure_glosry.md) and [deep structures](../../abap-glossary/abendeep_structure_glosry.md):

- Deep structures can only be assigned to each other if they are [compatible](../abap-data-types-and-data-objects/abencompatibility.md). Full compatibility is not required for the following deep components, and the following applies instead:

  - For components that have a [reference type](../../abap-glossary/abenreference_type_glosry.md), [upcasts](../../abap-glossary/abenup_cast_glosry.md) but not [downcasts](../../abap-glossary/abendown_cast_glosry.md) are allowed.

  - For table-like components, it is sufficient if the [line type](../../abap-glossary/abenrow_type_glosry.md) is compatible. This means that full [compatibility](../abap-data-types-and-data-objects/abencompatibility.md) is not required, which also includes [table categories](../../abap-glossary/abentable_category_glosry.md) and [table keys](../../abap-glossary/abentable_key_glosry.md).

- For flat structures, there are conversion rules for the following assignments between incompatible data objects:

  - [Conversion between flat structures](abenconversion_flat_flat.md)

  - [Conversion between flat structures and single fields](abenconversion_flat_elementary.md)

Assignments between structures and data objects that cannot be assigned to structures lead to a syntax error or the runtime error `OBJECTS_MOVE_NOT_SUPPORTED`.

## Hints

- If [substring access](../abap-operands/abenoffset_length.md) is performed on a structure and the substring is shorter than the structure, the substring is handled like an operand of type `c` and the corresponding conversion rules apply. If the substring corresponds exactly to the length of the structure, the substring is handled like the structure itself.

- A [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md) can be used to apply the same assignment rule to flat structures as to deep structures.

- The conversion rules for structures are designed to prevent catchable exceptions from being raised. If an assignment is allowed, it takes place.

- The statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) or the conversion operator [`CORRESPONDING`](abenconstructor_expr_corresponding.md) can be used to assign structures component by component.

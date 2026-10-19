---
title: "ASSIGN, mem_area"
source_file: abapassign_mem_area.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, mem_area

## Syntax

``` abap
... static_dobj   
  | dynamic_dobj   
  | dynamic_components   
  | dynamic_access   
  | writable_exp ...  
```

[`static_dobj`](abapassign_mem_area_static_dobj.md) · [`dynamic_dobj`](abapassign_mem_area_dynamic_dobj.md) · [`dynamic_components`](abapassign_dynamic_components.md) · [`dynamic_access`](abapassign_mem_area_dynamic_access.md) · [`writable_exp`](abapassign_mem_area_writable_exp.md)

### Alternative

**Static Specification**

1\. ... [`static_dobj`](abapassign_mem_area_static_dobj.md)

**Dynamic Specifications**

2\. ... [`dynamic_dobj`](abapassign_mem_area_dynamic_dobj.md)

3\. ... [`dynamic_components`](abapassign_dynamic_components.md)

4\. ... [`dynamic_access`](abapassign_mem_area_dynamic_access.md)

**Specifying an Expression**

5\. ... [`writable_exp`](abapassign_mem_area_writable_exp.md)

## Description

`mem_area` is used to specify the memory area that is assigned to a field symbol with the statement [`ASSIGN`](abapassign.md):

- The first variant [`static_dobj`](abapassign_mem_area_static_dobj.md) is a static variant in which a statically known data object or part of such an object is assigned.

- The second, third and fourth variants are dynamic.

  - The variants [`dynamic_dobj`](abapassign_mem_area_dynamic_dobj.md) are used for general dynamic access to data objects.

  - The variants [`dynamic_components`](abapassign_dynamic_components.md) are used for dynamic access to components of structures.

  - The variants [`dynamic_access`](abapassign_mem_area_dynamic_access.md) are used for dynamic access to the attributes of classes.

- The fifth variant assigns the result of a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md).

For an inline declaration of the field symbol with [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), its typing is done with the data type of `mem_area` for the static variant and when specifying a writable expression. For the dynamic variants the typing is done with the generic type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

The variants differ as to how the system behaves after an unsuccessful assignment:

- For the static variant, the return code `sy-subrc` is not set. The addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) is used implicitly and cannot be specified.

- For the dynamic variants, the statement `ASSIGN` sets the return code `sy-subrc` or can raise an exception. The addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) can be specified.

- When a [table expression](abapassign_mem_area_writable_exp.md) is specified, the statement `ASSIGN` sets the return code `sy-subrc`. The addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) can be specified.

- When assigning constructor operators:

  - For [`NEW`](abapassign_mem_area_writable_exp.md) the return code `sy-subrc` is set by the constructor operator.

  - For [`CASE`](abapassign_mem_area_writable_exp.md) the return code `sy-subrc` is not set.

    The addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) must not be specified because an assignment of a constructor operator is either successful or raises an exception.

## Hints

- In an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), either the header line or the [table body](../../abap-glossary/abentable_body_glosry.md) can be assigned to a field symbol. In the statement `ASSIGN`, the name of an internal table with a header line addresses the header line. To address the table body, `[]` must be appended to the name as usual. A field symbol to which a table body is assigned behaves in the same way in operand positions as a table without a header line.

- Field symbols to which data objects or parts of data objects are assigned in the [heap](../../abap-glossary/abenheap_glosry.md) act in a memory-preserving way, like [heap references](../../abap-glossary/abenheap_reference_glosry.md).

- In an inline declaration of the field symbol with [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), the data type of the assigned memory area determines its typing.

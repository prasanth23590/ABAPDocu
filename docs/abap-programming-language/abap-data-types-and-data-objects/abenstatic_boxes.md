---
title: "Static Boxes"
source_file: abenstatic_boxes.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Structures > Boxed Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Static Boxes

Static boxes are [boxed components](abenboxed_components.md) whose components are known statically, and which are subject to [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md). Declarations of static boxes generally require less memory for structures that occur multiple times but are rarely used.

The following can currently be declared as static boxes:

- Substructures of structured data with the addition [`BOXED`](../abap-declarations/abaptypes_boxed.md) of the statement [`TYPES`](../abap-declarations/abaptypes.md).

- Structured attributes of classes or interfaces with the addition [`BOXED`](../abap-declarations/abapdata_boxed.md) of the statement [`[CLASS-]DATA`](../abap-declarations/abapdata.md).

A static box can have one of two states:

- **Initial value sharing**

  As long as none of the actions named in the following point have been executed, initial value sharing applies to a static box. The internal reference refers to a type-dependent initial value of the structure, which is stored exactly once for each [AS instance](../../abap-glossary/abenas_instance_glosry.md) in its [PXA](../../abap-glossary/abenpxa_glosry.md). The memory requirement in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) is determined only by the internal reference and its [administration](abenmemory_consumption.md).

- **Cancelled initial value sharing**

  The following actions cancel initial value sharing for a static box:

  - Writes to the static box or one of its components.

  - Assigning the static box or one of its components to a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) using [`ASSIGN`](../abap-processing-internal-data/abapassign.md).

  - Addressing the static box or one of its components using a [data reference](../../abap-glossary/abendata_reference_glosry.md).

  - Using a static box or one of its components as an [actual parameter](../../abap-glossary/abenactual_parameter_glosry.md) for procedure calls.

    The internal reference then refers to an instance of the structure in the current internal session. The memory requirement is the same as for a regular structure plus the administration costs for the internal reference.

In initial value sharing, the memory required for the internal session of a static box is not defined at the start of program execution. However, unlike in real [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md), the length of a static box is always known statically. Static boxes can be used in the same way as a regular component of the same type. When a structure that contains a static box is accessed, however, it should be ensured that it is a deep component.

## Hints

- Static boxes can be used to optimize the memory requirement of structures that are used more than once. If, for example, the line structure of an internal table contains substructures, the memory requirement of the substructure accumulates without the use of static boxes for each line, even if the substructure is initial. If static boxes are used, initial substructures do not require multiple memories as long as only reads are performed.

- In addition to the optimized memory requirements, static boxes generally have a positive impact on runtime performance, since assignments between components for which initial value sharing is active only require the internal reference (and no additional data) to be copied.

- The statements `CLEAR` and `FREE` do not affect a static box that has the initial value sharing state like a write statement and the state is retained. On the other hand, once the initial value sharing state is cancelled, these statements do not currently free up any memory and provide the local instance of the static box with type-specific initial values instead.

- Boxes are allocated memory in the following cases:

  - When there is a write access to (one of) their components

  - When a field symbol is assigned or a data reference points to (one of) their components

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a substructure `scarr` as a static box.

``` abap
TYPES: 
  BEGIN OF struct, 
    comp  TYPE c LENGTH 10, 
    scarr TYPE scarr BOXED, 
  END OF struct.
```

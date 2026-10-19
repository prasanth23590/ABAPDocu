---
title: "Assigning Reference Variables"
source_file: abenset_references.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assigning Reference Variables

Special rules apply when setting the reference or pointer of a reference variable:

- [Assignment Rules for Reference Variables](abenconversion_references.md)

A reference is always set as an [upcast](../../abap-glossary/abenup_cast_glosry.md) or as a [downcast](../../abap-glossary/abendown_cast_glosry.md). When a reference variable is assigned to another reference variable, two different assignment operators are used, as well as a constructor operator.

- [`=`, `?=` - Upcast and Downcast](abapmove_cast.md)

- [`CAST` - Casting Operator](abenconstructor_expression_cast.md)

References in data reference variables can point to existing data objects. There is a statement and a constructor operator for this.

- [`GET REFERENCE`](abapget_reference.md)

- [`REF` - Reference Operator](abenconstructor_expression_ref.md)

Like all data objects, reference variables are initialized using the statement [`CLEAR`](abapclear.md). The content of an initial reference variable is the [null reference](../../abap-glossary/abennull_reference_glosry.md), which does not point to an object and can be assigned to every reference variable.&#x3000;

## Hints

- The same rules apply to references set when [objects are created](../abap-creating-objects-and-values/abencreate_objects.md) as to assignments.

- When a reference variable containing a [heap reference](../../abap-glossary/abenheap_reference_glosry.md) is initialized, this affects [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md).

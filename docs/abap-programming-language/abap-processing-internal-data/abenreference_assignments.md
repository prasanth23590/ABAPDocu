---
title: "Assigning References"
source_file: abenreference_assignments.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assigning References

This section discusses the assignments and special statements that set the references (pointers) contained in data references and field symbols.

- [Setting Reference Variables](abenset_references.md)

- [Setting Field Symbols](abenset_field_symbols.md)

When using field symbols and data references that contain references to data objects, the following should be noted:

- In a regular assignment between field symbols, as in an [assignment of data objects](abapmove.md), each field symbol is handled as a dereferenced pointer ([value semantics](../../abap-glossary/abenvalue_semantics_glosry.md)).

- In a regular assignment between data references, as in an [upcast or downcast](abapmove_cast.md), the references are copied ([reference semantics](../../abap-glossary/abenreference_semantics_glosry.md)). The corresponding rules can be found in the [assignment rules for reference variables](abenconversion_references.md).

## Hint

For the [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md) (strings, internal tables) and [boxed components](../../abap-glossary/abenboxed_component_glosry.md) that are also managed internally using references, value semantics apply. This means that the internal administration is not visible for the developers.

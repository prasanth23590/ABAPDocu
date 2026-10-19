---
title: "Initializations"
source_file: abeninitializations.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Initializations

The following statements initialize data objects, which means they set the content of a data object to an initial value:

- [`CLEAR`](abapclear.md)

- [`FREE`](abapfree_dataobject.md)

Initialization does not delete the corresponding data objects. Data objects created by declarative statements are only deleted from the memory when exiting a program, together with the [internal session](../../abap-glossary/abeninternal_session_glosry.md). Objects created dynamically by the statement [`CREATE`](../abap-creating-objects-and-values/abapcreate_object.md) are deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md). The initialization of reference variables can, however, cause the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md) to delete the referenced objects.

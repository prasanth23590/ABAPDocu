---
title: "garbage collector"
source_file: abengarbage_collector_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# garbage collector

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Deletes [objects](abenobject_glosry.md) that are no longer referenced by [heap references](abenheap_reference_glosry.md) or [field symbols](abenfield_symbol_glosry.md) and for which no method is registered as an [event handler](abenevent_handler_glosry.md). The garbage collector is called periodically by the [ABAP runtime framework](abenabap_runtime_frmwk_glosry.md). It tracks the [reference variables](abenreference_variable_glosry.md) of deleted objects.

## The following can be used to call the garbage collector explicitly:

- Static method `COLLECT` of system class `CL_ABAP_GARBAGE_COLLECTOR`

It is generally unnecessary to trigger clearing explicitly. However, it can be beneficial in exceptional cases, such as when very large, unneeded objects consume a significant amount of memory, or when explicitly releasing memory in resource-constrained environments is required. It can also aid in analyzing memory consumption and ensuring proper memory release, or when large objects are created repeatedly in a short period.

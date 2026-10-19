---
title: "ABAP CDS - Entity Buffers"
source_file: abencds_entity_buffers.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Entity Buffers

A [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) is an [ABAP tuning object](../../abap-glossary/abenabap_tuning_object_glosry.md) that defines [table buffering](../../abap-glossary/abentable_buffering_glosry.md) settings for [CDS entities](../../abap-glossary/abencds_entity_glosry.md). The following types of CDS entity buffers are available:

- [CDS view entity buffer](../../abap-glossary/abencds_view_entity_b_glosry.md)

CDS entity buffers are defined with the following special [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) statements in [ADT](../../abap-glossary/abenadt_glosry.md):

- [CDS DDL - `DEFINE VIEW | TABLE ENTITY BUFFER`](abencds_define_view_entity_buffer.md)

## Hints

- The source code of entity buffers has its own editor in [ADT](../../abap-glossary/abenadt_glosry.md), which is documented there.

- Table buffering only takes place when the CDS entity is accessed by ABAP SQL and the same [restrictions](../../abap-programming-language/abap-database-access/abenbuffer_restrictions.md) apply.

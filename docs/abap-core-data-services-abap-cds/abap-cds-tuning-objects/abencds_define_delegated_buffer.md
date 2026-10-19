---
title: "CDS DDL - TYPE DELEGATED"
source_file: abencds_define_delegated_buffer.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects > ABAP CDS - Entity Buffers > CDS DDL - DEFINE VIEW | TABLE ENTITY BUFFER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - TYPE DELEGATED

## Syntax

``` abap
...TYPE DELEGATED...  
```

## Description

Defines a [CDS delegated buffer](../../abap-glossary/abencds_del_buffer_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

A CDS delegated buffer is a [CDS view entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) that delegates the buffer usage of a CDS view entity to the buffer of its base object. This means that the buffer of the base entity is used and there aren't multiple buffers created for the same view stack, saving memory on the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

A delegated buffer is defined as a CDS view entity buffer with the buffering type set to the value `TYPE DELEGATED`. The CDS view entity to be buffered must contain the annotation `@AbapCatalog.entityBuffer.definitionType: [#DELEGATED]`. Further prerequisites and limitations are described in the topic [CDS DDL - `DEFINE VIEW | TABLE ENTITY BUFFER`](abencds_define_view_entity_buffer.md).

The following can be included in the buffered CDS view entity:

- [CDS source fields](../../abap-glossary/abencds_field_glosry.md)

- [Typed literals](../../abap-glossary/abentyped_literal_glosry.md)

- [Session variables](../../abap-glossary/abensession_variable_glosry.md)

- Cast function

- `WHERE` clause with operators `AND`, `OR`, `NOT`, `>`, `<`, `>=`, `<=`, `<>`, `IS [NOT] NULL`, `LIKE`

- Association definition and exposure, including filters

## Restrictions

The following restrictions apply to the delegated buffered CDS view entity:

- Only one base object is allowed

- No `UNION`, no `GROUP-BY`

- All generically-buffered key fields have to be unambiguously bound or exposed

- For single buffered base objects: all key fields have to be bound or exposed

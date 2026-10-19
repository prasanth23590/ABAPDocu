---
title: "ABAP CDS - Table Buffering of CDS Table Entities"
source_file: abencds_table_entity_buffering.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Table Buffering of CDS Table Entities

The following [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) defines whether [table buffering](../../abap-programming-language/abap-database-access/abensap_puffering.md) is allowed for a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md) or not:

[`@AbapCatalog.entityBuffer.definitionAllowed: true|false`](abencds_view_entity_anno.md)

If buffering is allowed, the actual [buffering type](../../abap-programming-language/abap-database-access/abenbuffer_type.md) can be defined by a separate [ABAP tuning object](../../abap-glossary/abenabap_tuning_object_glosry.md) called [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) with the DDL statement:

[`DEFINE TABLE ENTITY BUFFER ON cds_table_entity ...`](../abap-cds-tuning-objects/abencds_define_view_entity_buffer.md)

The CDS entity buffer relates the buffering type to one of the layers core, localization, industry, partner and customer. For each layer, a buffering type can be defined for a CDS table entity.

## Restrictions

If the annotation `@AbapCatalog.entityBuffer.definitionAllowed` is set to `true`, the following restrictions apply to the CDS table entity:

- There must be at least one key element and the combined length of the key elements must not be greater than 900 bytes. Key elements cannot be [LOBs](../../abap-glossary/abenlob_glosry.md).

- The table entity must not have any element of the data type `GEOM_EWKB`.

## Hints

- Buffer delegation using a [CDS delegated buffer](../../abap-glossary/abencds_del_buffer_glosry.md) is not supported for table entities, since table entities do not select data from underlying data sources and there is no base object to delegate to.

- [CDS buffer propagation](../../abap-glossary/abencds_buffer_propagation_glosry.md) is not supported for table entities.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Allowing buffering for a CDS table entity.

``` abap
@EndUserText.label: 'Demo: CDS table entity'
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.entityBuffer.definitionAllowed: true
define table entity DEMO_CDS_TABLE_ENTITY_BUF
{
  key key_field             : abap.int8;
      char_field_not_null   : abap.char(20);
      char_field_null       : abap.char(10) null;
      numc_field            : abap.numc(10);
}
```

Example for buffering of the table entity `DEMO_CDS_TABLE_ENTITY_BUF`:

``` abap
define table entity buffer on DEMO_CDS_TABLE_ENTITY_BUF 
  layer core 
  type full
```

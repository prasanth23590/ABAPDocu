---
title: "CDS DDL - DEFINE VIEW | TABLE ENTITY BUFFER"
source_file: abencds_define_view_entity_buffer.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects > ABAP CDS - Entity Buffers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE VIEW \| TABLE ENTITY BUFFER

## Syntax

``` abap
DEFINE VIEW | TABLE ENTITY BUFFER ON cds_entity 
                   LAYER CORE 
                       | LOCALIZATION 
                       | INDUSTRY 
                       | PARTNER 
                       | CUSTOMER 
                   TYPE SINGLE 
                      | {GENERIC NUMBER OF KEY ELEMENTS number} 
                      | FULL 
                      | DELEGATED 
                      | NONE  
```

[`DELEGATED`](abencds_define_delegated_buffer.md)

## Description

Defines a [CDS view entity buffer](../../abap-glossary/abencds_view_entity_b_glosry.md) or a [CDS table entity buffer](../../abap-glossary/abencds_table_entity_b_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

The following variants are available:

- The syntax `DEFINE VIEW ENTITY BUFFER ON cds_entity ...` can be used to specify buffering settings for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

- The syntax `DEFINE TABLE ENTITY BUFFER ON cds_entity ...` can be used to specify buffering settings for a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md).

View entity buffers and table entity buffers are [ABAP tuning objects](../../abap-glossary/abenabap_tuning_object_glosry.md) that specify a layer dependent [buffering type](../../abap-programming-language/abap-database-access/abenbuffer_type.md) for the [table buffering](../../abap-glossary/abentable_buffering_glosry.md) of a [CDS entity](../../abap-glossary/abencds_v2_view_glosry.md) `cds_entity`. As a prerequisite, the definition of the CDS entity must contain the following annotation:

`@AbapCatalog.entityBuffer.definitionAllowed:true`.

This annotation entails additional syntax checks. It is only allowed if the CDS view entity in question fulfills certain prerequisites. These prerequisites are described in the following topics:

- [ABAP CDS - Table Buffering of CDS View Entities](../abap-cds-data-definitions/abencds_v2_view_buffering.md).

- [ABAP CDS - Table Buffering of CDS Table Entities](../abap-cds-data-definitions/abencds_table_entity_buffering.md).

If a CDS entity buffer is active for a CDS entity, the annotation cannot be removed there.

The [buffering type](../../abap-programming-language/abap-database-access/abenbuffer_type.md) is set as follows:

- `TYPE SINGLE` defines [single record buffering](../../abap-programming-language/abap-database-access/abenbuffer_single_buffering.md).

- `TYPE GENERIC` defines [generic buffering](../../abap-programming-language/abap-database-access/abenbuffer_generic_buffering.md). The number of respected key fields must be set by `number` behind `NUMBER OF KEY ELEMENTS`. `number` must be a positive numeric literal that is not greater than the number of key elements of the CDS entity `cds_entity`.

- `TYPE FULL` defines [complete buffering](../../abap-programming-language/abap-database-access/abenbuffer_complete_buffering.md).

- [`TYPE DELEGATED`](abencds_define_delegated_buffer.md) defines [delegated buffering](../../abap-glossary/abencds_del_buffer_glosry.md).

  **Limitation:** The buffering type `DELEGATED` is available in CDS view entity buffers only. It is not available in CDS table entity buffers.

The addition `LAYER` defines the layer for which the buffering type is valid. The layer determines the priority if there are multiple view entity buffers for one CDS entity. The priority is as follows, where the list starts with the lowest and ends with the highest priority:

1.  `CORE` - SAP basis component

2.  `LOCALIZATION` - SAP application component

3.  `INDUSTRY` - SAP industry solution

4.  `PARTNER` - partner

5.  `CUSTOMER` - customer

It is not possible to define multiple view entity buffers with the same layer for one CDS entity.

The addition `TYPE NONE` can be used to switch off buffering explicitly. This is especially useful for switching off buffering in a higher layer that was defined in a lower layer.

## Hints

- The name of a CDS view entity buffer is not reflected in its definition. It only occurs as the name of the repository object in ADT.

- The layers specified with `LAYER` are the same as in the definition of a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md) with [`ANNOTATE ENTITY`](../abap-cds-annotations/abencds_f1_annotate_view.md).

- Only the explicitly defined key fields of a CDS entity must be respected behind `NUMBER OF KEY ELEMENTS`. Unlike [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), there is no client column to be respected for [client-dependent views](../abap-cds-data-definitions/abencds_v2_view_client_handling.md).

- A CDS entity buffer fulfills the same task as the respective [technical settings](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md) of a DDIC database table. Both can be activated and transported separately from the buffered entity. But compared to buffering DDIC database tables, the buffering type for a CDS entity has the additional feature of being layer-specific.

- Table buffering only takes place if the view entity is accessed by ABAP SQL, and the same [restrictions](../../abap-programming-language/abap-database-access/abenbuffer_restrictions.md) apply.

## More Information

ABAP Data Models guide, section about [CDS View Entity Buffers](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/ddcf02dcfaa344f4a32c9d13dbda167b?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following definitions demonstrate the three kinds of table buffering for three different CDS entities in the layer `core`.

``` abap
define view entity buffer on DEMO_CDS_FULL_BUFFERED_VIEW 
  layer core 
  type full
```abap
define view entity buffer on DEMO_CDS_GEN_BUFFERED_VIEW 
   layer core 
   type generic number of key elements 1
```abap
define view entity buffer on DEMO_CDS_SINGLE_BUFFERED_VIEW 
   layer core 
    type single
```abap
define view entity buffer on DEMO_CDS_DEL_BUFFERED_VIEW 
   layer core 
   type delegated
```

The CDS entities `DEMO_CDS_FULL_BUFFERED_VIEW`, `DEMO_CDS_GEN_BUFFERED_VIEW`, `DEMO_CDS_SINGLE_BUFFERED_VIEW`, and `DEMO_CDS_DEL_BUFFERED_VIEW` all contain the annotation `@AbapCatalog.entityBuffer.definitionAllowed: true`.

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

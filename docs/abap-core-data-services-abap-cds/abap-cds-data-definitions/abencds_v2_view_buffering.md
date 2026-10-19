---
title: "ABAP CDS - Table Buffering of CDS View Entities"
source_file: abencds_v2_view_buffering.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Table Buffering of CDS View Entities

[Table buffering](../../abap-glossary/abentable_buffering_glosry.md) settings for CDS view entities are defined in separate repository objects called [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md). The following types of CDS entity buffer are available:

- [CDS view entity buffer](../../abap-glossary/abencds_view_entity_b_glosry.md): Defines the kind of table buffering for a CDS entity.

The following sections provide information on the different types of CDS entity buffers:

- [CDS View Entity Buffer](abencds_v2_view_buffering.md#cds-view-entity-buffer)

- [CDS Propagated Buffer (Obsolete)](abencds_v2_view_buffering.md#cds-propagated-buffer-obsolete)

## Hints

- The annotations [`@AbapCatalog.buffering.status`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md), [`@AbapCatalog.buffering.type`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md), and [`@AbapCatalog.buffering.numberOfKeyFields`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) are not supported in CDS view entities. They are only valid for [CDS DDIC-based views](../../abap-glossary/abencds_v1_view_glosry.md).

- Other than for [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), where the buffering is defined for the respective [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md), the table buffering of CDS view entities is defined for the CDS entity itself.

- In contrast to [table buffering of CDS DDIC-based views](../abap-cds-obsolete-language-elements/abencds_v1_buffering.md) where ABAP SQL bypasses the table buffer if the prerequisites are not met, the restrictions are checked directly for the view in case of CDS view entities. For a view that does not meet the prerequisites, table buffering cannot be enabled.

- A CDS data model with multiple layers that has buffering defined on multiple layers (for example, [table buffers](../../abap-glossary/abentable_buffer_glosry.md) and [CDS entity buffers](../../abap-glossary/abencds_entity_buffer_glosry.md)) stores data redundantly as soon as the buffers are accessed. For each individual view, the data is stored in a separate table buffer. Non-redundant storage is currently not supported.

- Table buffering only takes place if the view entity is accessed by ABAP SQL and the same [restrictions](../../abap-programming-language/abap-database-access/abenbuffer_restrictions.md) apply.

- The primary key of the buffered CDS view entity, specified using the addition [`KEY`](abencds_select_list_entry_v2.md), is relevant for buffering of CDS entities. A non-unique primary key might lead to unexpected buffer behavior. Therefore, the application developer should ensure that each data record of a buffered entity has a unique primary key.

## CDS View Entity Buffer

The following [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) defines whether [table buffering](../../abap-programming-language/abap-database-access/abensap_puffering.md) using a [CDS view entity buffer](../../abap-glossary/abencds_view_entity_b_glosry.md) is allowed for a [CDS view entity](abencds_view_entity.md) or not:

[`@AbapCatalog.entityBuffer.definitionAllowed: true|false`](abencds_view_entity_anno.md)

If buffering is allowed, the actual [buffering type](../../abap-programming-language/abap-database-access/abenbuffer_type.md) can be defined by a separate [ABAP tuning object](../../abap-glossary/abenabap_tuning_object_glosry.md) called [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) with the DDL statement:

[`DEFINE VIEW ENTITY BUFFER ON cds_view_entity ...`](../abap-cds-tuning-objects/abencds_define_view_entity_buffer.md)

The CDS entity buffer relates the buffering type to one of the layers core, localization, industry, partner and customer. For each layer, one buffering type can be defined for a CDS view entity.

## Restrictions

If the annotation `@AbapCatalog.entityBuffer.definitionAllowed` is set to `true`, the following restrictions apply to the CDS view entity:

- Only the following [data sources](abencds_data_source_v2.md) are possible:

  - [DDIC database tables](../../abap-glossary/abendatabase_table_glosry.md)

  - [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) annotated with the annotation `@AbapCatalog.entityBuffer.definitionAllowed: true`. A CDS view entity used as data source must allow buffering itself and must therefore meet all requirements listed here. In a CDS data model with multiple layers, each CDS view entity must allow buffering as a prerequisite for the upper layer to allow buffering.

- There must be at least one key element and the combined length of the key elements must not be greater than 900 bytes. Key elements cannot be [LOBs](../../abap-glossary/abenlob_glosry.md).

- No [input parameters](abencds_parameter_list_v2.md) are allowed.

- No calculations are allowed that have results that do not depend on database content only, for example [time stamp functions](abencds_timestamp_functions_v2.md) that return or depend on the current time stamp.

- No [session variables](abencds_session_variable_v2.md) other than `$session.client` are allowed.

- No database tables can be accessed where [data aging](../../abap-glossary/abendata_aging_glosry.md) is enabled,

- No customer extensions are allowed. Annotations [`AbapCatalog.extensibility.extensible`](abencds_f1_entity_annotations.md) or [`AbapCatalog.viewEnhancementCategory`](abencds_view_entity_anno.md) cannot be used to enable extensions.

- It is not possible to specify both a view entity buffer and a propagated buffer for a CDS view entity. The annotation `AbapCatalog.entityBuffer.propagationAllowed` must not be used with the value `true`.

- The view entity must not have any element of the data type `GEOM_EWKB`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Allowing buffering for a CDS view entity. The actual buffering is defined with the DDL for an entity buffer as shown under [`DEFINE VIEW ENTITY BUFFER`](../abap-cds-tuning-objects/abencds_define_view_entity_buffer.md).

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.entityBuffer.definitionAllowed: true

define view entity DEMO_CDS_GEN_BUFFERED_VIEW
  as select from sairport
{

  key id        as Id,
  key name      as Name,
      time_zone as Time_Zone
}
```

## CDS Propagated Buffer (Obsolete)

The following [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) defines whether [CDS buffer propagation](../../abap-glossary/abencds_buffer_propagation_glosry.md) using a [CDS propagated buffer](../../abap-glossary/abencds_prop_buffer_glosry.md) is allowed for a [CDS view entity](abencds_view_entity.md) or not:

[`@AbapCatalog.entityBuffer.propagationAllowed: true|false`](abencds_view_entity_anno.md)

If buffer propagation is allowed, the actual [SQL path target fields](../../abap-glossary/abensql_target_field_glosry.md) that are propagated can be defined by a separate [ABAP tuning object](../../abap-glossary/abenabap_tuning_object_glosry.md) called [CDS propagated buffer](../../abap-glossary/abencds_prop_buffer_glosry.md) with the DDL statement:

[`PROPAGATE VIEW ENTITY BUFFER ON cds_entity ...`](../abap-cds-obsolete-language-elements/abencds_propagate_buffer.md)

One or more CDS propagated buffers can be specified for a CDS view entity. In total, a maximum of ten propagated fields can be defined for a CDS view entity.

## Restrictions

If the annotation `@AbapCatalog.entityBuffer.propagationAllowed` is set to `true`, the following restrictions apply to the CDS view entity:

- No [set operators](abencds_set_operators.md) are allowed. This means that the CDS view entity must not contain any of the statements [`UNION`](abencds_union_v2.md), [`EXCEPT`](abencds_except_v2.md), or [`INTERSECT`](abencds_intersect_v2.md).

- It is not possible to specify both a view entity buffer and a propagated buffer for a CDS view entity. The annotation `AbapCatalog.entityBuffer.definitionAllowed` must not be used with the value `true`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Allowing buffer propagation for a CDS transactional query. The actual buffering is defined with the DDL for a propagated buffer as shown under [`PROPAGATE VIEW ENTITY BUFFER`](../abap-cds-obsolete-language-elements/abencds_propagate_buffer.md). The original data source of the SQL path target field is the CDS view `DEMO_SALES_CDS_MAT_TEXT`. This view is fully buffered, so it fulfills the prerequisite for buffer propagation.

``` abap
@EndUserText.label: 'CDS transactional query, material'
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.entityBuffer.propagationAllowed: true
define root view entity DEMO_SALES_PV_MATERIAL
  provider contract transactional_query
  as projection on DEMO_SALES_CDS_MATERIAL
{
  key material,
      material_type,
      material_group,
      /* Associations */
      _Text,
      _Text.material_name as MaterialName : localized
}
```

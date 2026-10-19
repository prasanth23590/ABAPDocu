---
title: "RAP - persistent table"
source_file: abenbdl_persistent_table.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - persistent table

## Syntax

``` abap
... 
persistent table TableName 
 ...  
```

## Description

The [RAP persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md) is the [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) a [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) is based on. The [persistent data](../../abap-glossary/abenrap_persistent_data_glosry.md) on the [persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md) is processed by [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md).

## Availability

- Available for [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) only and for these, it is mandatory to specify a persistent table.

- **Exception:** In a managed RAP BO with an [unmanaged save](../../abap-glossary/abenrap_unman_save_glosry.md), defined using [`with unmanaged save`](abenbdl_saving.md), a persistent table must not be defined.

- In a [projection business object](../../abap-glossary/abenrap_projection_bo_glosry.md), the persistent table is automatically inherited and need not be specified.

Requirements:

- If the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) specifies an [ETag](../../abap-glossary/abenrap_etag_glosry.md) field, the persistent table requires a field that is used to describe the state of the database table. This can be, for example, a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md).

  If this field is annotated in CDS with the relevant annotation, such as [`@Semantics.systemDateTime.localInstanceLastChangedAt: true`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_425922347-_anno.md), then it is automatically updated by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md).

- If the RAP BO is [draft-enabled](abenbdl_with_draft.md) and has a [total ETag field](../../abap-glossary/abenrap_total_etag_glosry.md), the persistent table requires a field that is updated whenever the BO instance is changed. This must be a separate field from the ETag master field. The total ETag field is necessary on the [lock master entity](abenbdl_locking.md).

  If the total ETag field is a time stamp field and if it is annotated in the CDS data model with the annotation `@Semantics.systemDateTime.lastChangedAt`, then this field is updated automatically by the RAP framework.

- If the primary key field is of type [`raw(16)`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) [(UUID)](../../abap-glossary/abenuuid_glosry.md), then it can be filled by the RAP framework using [internal numbering](../../abap-glossary/abenrap_int_numbering_glosry.md). The syntax for this is [`numbering:managed`](abenbdl_field_numbering.md).

- If you decide to use UUIDs as primary keys, the following rules apply:

  - Every entity needs a field for the UUID key.

  - Child entities must have a field for their parent's UUID. This is required to define associations for the [CDS composition](../../abap-glossary/abencds_composition_glosry.md) relationship.

  - Any child entity that has no parent-child relationship with the lock master entity must have a field with the lock master's UUID. This is important to define associations to the lock master entity, which is required for ETag handling.

## Hints

- If the field names of the persistent database table differ from the field names of the CDS views of the underlying data model, then a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) is required in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md). This can be the case, for example, if the fields of the CDS data model have [alias names](../../abap-glossary/abenalias_glosry.md).

- A RAP persistent table is a regular [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) and can be accessed as such. Access with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [AMDP](../../abap-glossary/abenamdp_glosry.md) is technically possible, but not recommended. It is recommended that a persistent table is accessed using the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) only, for example, with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_MANAGED_ROOT`. It specifies persistent database tables for the parent and the child entity.

``` abap
managed implementation in class bp_demo_managed_root unique;
strict ( 2 );

define behavior for DEMO_MANAGED_ROOT
persistent table demo_tab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }

  field ( readonly : update ) key_field;
}

define behavior for DEMO_MANAGED_CHILD alias child
persistent table demo_tab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly : update ) key_field;
  association _parent;
}
```

The class `CL_DEMO_RAP_EML_MODIFY_OP_2` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and performs the following steps:

- Modify operations with `CREATE` and `CREATE BY`

  Two `MODIFY ENTITY` operations are executed to create data sets for the root entity using the `CREATE` statement as well as data sets for the child entity using `CREATE BY`.

- Modify operation with `UPDATE`

  Data sets of the root entity are updated.

- Modify operation with `DELETE`

  Data sets of the root entity are deleted.

- Read operation with `READ` and `READ BY`

  Data sets are read from the root and child entities.

The changes are saved with the statement [`COMMIT ENTITIES`](../abap-for-rap-business-objects/abapcommit_entities.md), and, thus, the changed data is persisted to the database tables. All changes to the persistent table are managed by the RAP framework.

## Executable Example

The example [`MODIFY`: Standard Operations (Managed)](../abap-for-rap-business-objects/abeneml_modify_op_abexa.md) explains the example displayed above in detail.

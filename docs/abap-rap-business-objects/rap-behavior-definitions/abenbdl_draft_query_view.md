---
title: "RAP - query"
source_file: abenbdl_draft_query_view.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics > RAP - draft table"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - query

## Syntax

``` abap
... query DraftQueryView  
```

## Description

Defines a [draft query view](../../abap-glossary/abendraft_query_view_glosry.md) `DraftQueryView` for a [RAP draft table](../../abap-glossary/abendraft_table_glosry.md). `query` is an optional addition that can be specified directly after the RAP draft table [`draft table DraftTableName`](abenbdl_draft_table.md).

The draft query view `DraftQueryView` must be a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) that specifies the RAP draft table as data source after `FROM`. It must contain all fields from the draft table including administrative fields. Otherwise, a syntax check warning occurs.

A draft query view can be used to define read access limitations to the draft data using [data control language (DCL)](../../abap-glossary/abencds_dcl_glosry.md). The DCL access restrictions defined for the CDS view entities selecting from the active database table are not applied to the draft data. A draft query view allows the definition of read access restrictions for draft data.

## Availability

- The syntax addition `query` is available in [draft-enabled RAP business objects](../../abap-glossary/abendraft_rap_bo_glosry.md) of type `managed` or `unmanaged`.

- In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md), the draft query view is automatically inherited from the base BDEF (if specified there). All access restrictions to draft data are reused in the projection BO and interface BO. The syntax `query` is not available there. For details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hint

A draft query view is a prerequisite for classifying a RAP BO with the [C0 contract for extensibility](../../abap-glossary/abenc0_contract_glosry.md) in the context of [RAP extensibility](../../abap-glossary/abenrap_extensibility_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Draft Query Views](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/59365c9790e84014b03c4f042a7a18dd?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed and draft-enabled RAP BO.

- It is based on the CDS view entity `DEMO_RAP_MANAGED_DRAFT_QUERY`. This CDS view entity has read access restrictions defined in the DCL source `DEMO_RAP_DRAFT_QUERY`.

- It specifies the CDS view entity `DEMO_RAP_DRAFT_QUERY_VIEW` as draft query view. This draft query view has read access restrictions defined in the DCL source `DEMO_RAP_DCL_DRAFT`.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) are not implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) here.

``` abap
managed implementation in class bp_demo_rap_managed_draft_quer unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_MANAGED_DRAFT_QUERY alias RootEntity
persistent table demo_dbtab_root
draft table demo_dbtab_draft query DEMO_RAP_DRAFT_QUERY_VIEW
lock master
total etag Timestamp
authorization master ( none )

{
  create;
  update;
  delete;

  field ( readonly : update ) KeyFieldRoot;
  field ( readonly ) Timestamp;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;
  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      Timestamp     = crea_date_time;
      LastChangedAt = lchg_date_time;
    }

}
```

The class `CL_DEMO_RAP_DRAFT_QUERY_VIEW` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and performs the following operations:

- It creates four active entity instances using the EML statement [`MODIFY ENTITIES CREATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md).

- It reads these active instances, first with the EML statement [`READ ENTITIES`](../abap-for-rap-business-objects/abapread_entity_entities.md), and afterwards with ABAP SQL [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md). In the EML read, the DCL access condition is applied and the result set is filtered according to the access condition. Some data sets are filtered out. By contrast, the ABAP SQL `SELECT` displays all instances that were saved on the database.

- It creates four draft instances using the EML statement `MODIFY ENTITIES CREATE`.

- It reads these draft instances, first with the EML statement `READ ENTITIES`, and afterwards with ABAP SQL `SELECT`. In the EML read, the DCL access condition attached to the draft query view is applied and the result set is filtered according to the access condition. Some data sets are filtered out. By contrast, the ABAP SQL `SELECT` displays all instances that were saved in the RAP draft table.

- Finally, the RAP draft table is cleared using the draft action [`Discard`](abenbdl_draft_action.md).

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - RAP BO with DCL Access Control](abenbdl_draft_query_abexa.md).

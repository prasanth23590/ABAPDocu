---
title: "RAP - DraftHandling"
source_file: abenbdl_draft_handling.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - DraftHandling

## Syntax

``` abap
... 
with draft; 
 | with collaborative draft; 
 ...  
```

## Description

[RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) for a [business object](../../abap-glossary/abenbusiness_object_glosry.md) is enabled either with the addition `with draft` or `with collaborative draft`. The corresponding addition is added in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) as it draft-enables the entire business object. It is not possible to implement draft capabilities for individual [entities](../../abap-glossary/abenrap_bo_entity_glosry.md) within a business object.

RAP draft handling is in all scenarios completely managed by the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md). The application developer is not responsible for how draft data is written to the [draft database table](../../abap-glossary/abendraft_table_glosry.md).

- [RAP - `with draft`](abenbdl_with_draft.md)

- [RAP - `with collaborative draft`](abenbdl_with_coll_draft.md)

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In [projection BDEFs](../../abap-glossary/abenrap_projection_bo_glosry.md) and in [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md), draft handling can be reused from the underlying base BO using the syntax addition `use draft` or `use collaborative draft`. For details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

**Dependencies**

The additions with draft or with collaborative draft enable draft handling. There are several related syntax elements in the behavior definition:

- [`draft table`](abenbdl_draft_table.md) \[[`query`](abenbdl_draft_query_view.md)\]:

  A [RAP draft table](../../abap-glossary/abendraft_table_glosry.md) is required for storing [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md). It is defined using the keyword `draft table DraftTableName`. A draft table is mandatory for draft-enabled BOs. A [draft query view](../../abap-glossary/abendraft_query_view_glosry.md) can optionally be specified for a RAP draft table using the addition [`query`](abenbdl_draft_query_view.md).

- [`total etag`](abenbdl_etag.md):

  The [total ETag](../../abap-glossary/abenrap_total_etag_glosry.md) is a designated field in a draft-enabled business object that indicates changes between the active and the draft version. A total ETag is mandatory for draft-enabled implementations.

- [draft actions](abenbdl_draft_action.md):

  [RAP draft actions](../../abap-glossary/abenrap_bo_draft_action_glosry.md) are actions that are available for draft-enabled business objects only. They allow data to be manipulated on the [RAP draft table](../../abap-glossary/abendraft_table_glosry.md). They are implicitly available as soon as a business object is draft-enabled, but can be declared explicitly.

- [draft-enabled associations](abenbdl_association.md):

  A draft-enabled association retrieves active data if it is followed by an [active instance](../../abap-glossary/abenrap_active_instance_glosry.md) and draft data if is followed by a [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md). An association is draft enabled using the syntax addition [`with draft`](abenbdl_association.md). In a draft-enabled RAP BO, it is mandatory that associations are draft-enabled.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Draft](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/a81081f76c904b878443bcdaf7a4eb10?version=sap_cross_product_abap).

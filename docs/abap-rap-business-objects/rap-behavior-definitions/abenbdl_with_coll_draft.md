---
title: "RAP - with collaborative draft"
source_file: abenbdl_with_coll_draft.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader > RAP - DraftHandling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with collaborative draft

## Syntax

``` abap
... 
with collaborative draft; 
 ...  
```

## Description

The addition `with collaborative draft` is added in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and it enables [collaborative draft](../../abap-glossary/abenrap_collaborative_draft_glosry.md) capabilities for the [business object](../../abap-glossary/abenbusiness_object_glosry.md). Additionally, the [draft action](abenbdl_draft_action.md) `Share` needs to be added in the [behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) for collaborative draft capabilities. [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) is in all scenarios completely managed by the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md). The application developer is not responsible for how draft data is written to the [draft database table](../../abap-glossary/abendraft_table_glosry.md).

Collaborative draft also works in [cross-BO](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenarios if both BOs are collaborative draft-enabled and if the cross-BO scenario is fully [draft scope](abenbdl_dependent_draft_abexa.md)-enabled.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Collaborative Draft Handling](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/18d41e2a7be24ff99b43c4c88711e86c?version=sap_cross_product_abap).

---
title: "ABAP behavior pool"
source_file: abenbehavior_pool_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP behavior pool

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

ABP for short. A special [class pool](abenclass_pool_glosry.md) for an [ABAP behavior implementation](abenbehavior_implement_glosry.md). A behavior pool is based on a [RAP behavior definition](abencds_behavior_definition_glosry.md). The name of the [global class](abenglobal_class_glosry.md) of a behavior pool is usually prefixed with `BP_` but does not implement the behavior itself. The [behavior implementation](abenbehavior_implement_glosry.md) is coded in local [ABP handler classes](abenabp_handler_class_glosry.md) and [ABP saver classes](abenabp_saver_class_glosry.md) in the [CCIMP include](abenccimp_glosry.md) of the behavior pool. These classes implement the [unmanaged RAP BO provider](abenunmanaged_rap_bo_prov_glosry.md) that is called by the [RAP runtime engine](abenrap_runtime_engine_glosry.md) when the [RAP BO](abenrap_bo_glosry.md) is accessed.

[***-\>* More about**](../abap-rap-business-objects/abap-for-rap-business-objects/abenabap_behavior_pools.md)

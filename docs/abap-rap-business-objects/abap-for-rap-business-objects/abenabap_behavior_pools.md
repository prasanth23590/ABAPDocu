---
title: "ABAP Behavior Pools (ABP)"
source_file: abenabap_behavior_pools.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Behavior Pools (ABP)

The [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is a special class pool for an ABAP behavior implementation and based on a [RAP behavior definition (BDEF)](../../abap-glossary/abencds_behavior_definition_glosry.md). The [global class](abapclass_for_behavior_of.md) of the behavior pool does not implement the behavior itself. Instead, the behavior implementation is coded in one or more local RAP [handler classes](abenabp_handler_class.md) and one RAP [saver class](abenabp_saver_class.md) in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of the behavior pool. These classes provide the unmanaged parts that are called by the [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md) when the [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) is accessed.

- [`CLASS, FOR BEHAVIOR OF`](abapclass_for_behavior_of.md)

- [RAP Handler Classes and Methods](abenabp_handler_class.md)

- [RAP Saver Class and Methods](abenabp_saver_class.md)

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

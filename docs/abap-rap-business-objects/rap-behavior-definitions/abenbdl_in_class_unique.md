---
title: "RAP - implementation in class unique"
source_file: abenbdl_in_class_unique.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - implementation in class unique

## Syntax

``` abap
... implementation in class ClassName unique  
```

## Description

Specifies an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) for the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). An ABAP behavior pool is a special class pool for an ABAP behavior implementation. The name of the [global class](../../abap-glossary/abenglobal_class_glosry.md) of a behavior pool is usually prefixed with `BP_`. It does not implement the behavior itself. The [behavior implementation](../../abap-glossary/abenbehavior_implement_glosry.md) is coded in local [handler classes](../../abap-glossary/abenabp_handler_class_glosry.md) and [saver classes](../../abap-glossary/abenabp_saver_class_glosry.md). The classes implement the [unmanaged RAP BO provider](../../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) that is called by the [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md) when the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) is accessed.

There exist different options for notation that define how the implementation is distributed:

- The behavior pool can be defined in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md).

  In this case, all implementation-relevant parts of all [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md) that do not have an own implementation class are implemented in the same class. Further behavior pools on entity-level are possible.

- The behavior pool can be defined in the [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) for each CDS entity. Each node of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) can have an own implementation class.

  If there is an additional implementation on header level, this applies to all entities which do not have their own implementation class.

- The behavior pool can be defined within the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) for one or more [implementation groups](abenbdl_grouping.md) specified using the addition [`group`](abenbdl_grouping.md). Each group must have an own implementation class, while entities must not have an implementation class. An additional implementation class on header level is possible.

The behavior for a certain entity or group can only be implemented in the specified behavior pool. Any other class that attempts this will get an error message.

The mandatory addition `unique` defines that each operation can be implemented exactly once.

## Availability

- Managed RAP BO

  In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), certain components are provided by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md), such as [standard operations](abenbdl_standard_operations.md), [operations for associations](abenbdl_association.md), the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), and the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). For these components, no implementation in a behavior pool is necessary. A behavior pool is required for the components that cannot be handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md), such as [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md).

- Unmanaged RAP BO

  In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), an ABAP behavior pool is mandatory. The implementation of an unmanaged RAP BO is fully provided by the [unmanaged RAP BO provider](../../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) in the ABAP behavior pool.

- [Projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md)

  In a projection BDEF, an ABAP behavior pool is not necessary, but possible:

  - Functionality that is [reused](abenbdl_use_projection.md) from the [projected BO](../../abap-glossary/abenrap_projected_bo_glosry.md) does not require its own implementation. The implementation from the projected BO is reused.

  - If the projection BDEF defines [new actions or functions](abenbdl_nonstandard_projection.md), an ABAP behavior pool is required.

## More Information

- For further details on ABAP behavior pools, see the topic [ABAP Behavior Pools (ABP)](../abap-for-rap-business-objects/abenabap_behavior_pools.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Behavior definition with a behavior pool on header level:

``` abap
managed implementation in class ClassName unique; 
  define behavior for CDSEntityName alias AliasName 
   ...
```

Behavior definition with a behavior pool on entity level:

``` abap
managed; 
  define behavior for CDSEntityName alias AliasName 
    implementation in class ClassName unique; 
   ...
```

Behavior definition with implementation groups. Each group has its own implementation class. An implementation class on header level is required to implement the [unmanaged save](../../abap-glossary/abenrap_unman_save_glosry.md).

``` abap
managed implementation in class ClassName unique; 
  define behavior for CDSEntityName alias AliasName 
    with unmanaged save 
{ 
group Group1 implementation in class Class1 unique { ... } 
group Group2 implementation in class Class2 unique { ... } 
... 
} 
   ...
```

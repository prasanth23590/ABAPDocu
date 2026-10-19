---
title: "RAP - lock:none"
source_file: abenbdl_lock_none.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - lock:none

## Syntax

``` abap
... (lock:none) ...  
```

## Description

The RAP BO operation addition `lock:none` prevents the [locking mechanism](../../abap-glossary/abenrap_locking_glosry.md) for the entity instance for which an action is executed. As a prerequisite, the RAP locking mechanism must be defined and implemented.

`lock:none` can be used for the following operations:

- Instance-bound [non-factory actions](abenbdl_action_nonfactory.md)

- Instance-bound [factory actions](abenbdl_action_factory.md)

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

- **Note:** Since static actions are not related to a specific instance, they are non-locking by definition and this syntax element is not applicable.

- **Note:** The locking mechanism is only prevented for the action itself. Possible modify calls in the action implementation are not affected by the non-locking specification in the action definition. Consequently, an instance is locked if it is modified by an action even if the action is defined as non-locking.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In projection and interface BDEFs, the RAP locking settings from the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) are automatically reused and do not need to be explicitly defined. For details, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## More Information

- For details on the RAP locking mechanism, see the topic [RAP - Locking](abenbdl_locking.md).

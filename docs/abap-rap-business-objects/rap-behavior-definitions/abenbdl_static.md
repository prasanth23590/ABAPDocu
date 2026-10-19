---
title: "RAP - static"
source_file: abenbdl_static.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - static

## Syntax

``` abap
... static ...  
```

## Description

Defines a [RAP BO non-standard operation](../../abap-glossary/abenrap_nstandard_operation_glosry.md) as [static](../../abap-glossary/abenrap_static_operation_glosry.md). Static RAP BO operations are not bound to any [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) and relate to the complete [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) instead.

The following non-standard operations can be static:

- [Non-factory actions](../../abap-glossary/abenrap_non_fac_action_glosry.md)

- [Factory actions](../../abap-glossary/abenrap_factory_action_glosry.md)

- [Save actions](../../abap-glossary/abenrap_save_action_glosry.md)

- [Functions](../../abap-glossary/abenrap_function_glosry.md)

Static operations support [global feature control](../../abap-glossary/abenrap_glo_feature_control_glosry.md) ([`features:global`](abenbdl_actions_fc.md)) and global [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) ([`authorization:global`](abenbdl_actions_auth_global.md)).

## Restrictions

- [Repeatable operations](../../abap-glossary/abenrap_repeatable_action_glosry.md) defined using the addition [`repeatable`](abenbdl_action_repeatable.md) cannot be static.

- An [instance feature control](../../abap-glossary/abenrap_ins_feature_control_glosry.md) defined using [`features:instance`](abenbdl_actions_fc.md) is not supported for static operations, because static operations are not bound to any entity instance.

- An instance [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) defined using [`authorization:instance`](abenbdl_actions_auth_instance.md) is not supported for static operations, because static operations are not bound to any entity instance.

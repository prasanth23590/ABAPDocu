---
title: "RAP - EntityBehaviorCharacteristics, Projection BDEF"
source_file: abenbdl_character_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorCharacteristics, Projection BDEF

## Syntax

``` abap
... [use etag] 
    [extensible] 
    [authorization]  ...  
```

[`use etag`](abenbdl_use_projection.md) · [`extensible`](abenbdl_extensible.md) · [`authorization`](abenbdl_authorization_projection.md)

## Description

This topic gives an overview of the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) that can be defined or reused in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md). It also explains which ones of the behavior characteristics from the [projected BO](../../abap-glossary/abenrap_projected_bo_glosry.md) are automatically reused or inherited. These characteristics does not need to be specified explicitly.

Characteristics that must be specified explicitly, if required:

- [`use etag`](abenbdl_use_projection.md)

  An ETag field for [optimistic concurrency control](../../abap-glossary/abenoptimistic_conc_control_glosry.md) can be reused if it is specified in the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md).

  - For details on optimistic concurrency control, see topic [RAP - `etag`](abenbdl_etag.md).

  - For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- [`extensible`](abenbdl_extensible.md)

  To enable [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md), a declaration in the entity behavior definition header is required and the keyword `extensible` must also be declared in the entity behavior characteristics for each individual entity that allows BDEF extensions. In projection BDEFs, only the keyword `extensible` is possible, without any further additions. For details, see topic [RAP - `extensible`](abenbdl_extensible.md).

Characteristic that can be specified explicitly or reused, depending on the context:

- [`authorization`](abenbdl_authorization_projection.md)

  - All [authorization controls](../../abap-glossary/abenrap_auth_control_glosry.md) that are specified in the base BO is automatically and implicitly passed on to the projection BO. For details, see topic [RAP - Authorization](abenbdl_authorization.md).

  - If new [actions](../../abap-glossary/abenrap_action_glosry.md) are specified in a projection BDEF, it is possible to specify authorization control for these new actions in the projection layer. For details, see topic [RAP - `authorization`, Projection BDEF](abenbdl_authorization_projection.md).

Automatic reuse:

- [`persistent table`](abenbdl_persistent_table.md)

  Implementation aspect that is reused automatically.

- [`draft table`](abenbdl_draft_table.md)

  Implementation aspect that is reused automatically.

- [`SavingOptions`](abenbdl_saving.md)

  Implementation aspect that is reused automatically.

- [locking](abenbdl_locking.md)

  Implementation aspect that is reused automatically. Projection BOs inherit the lock master and lock dependent relations. On each [modify operation](../../abap-glossary/abenrap_modify_operation_glosry.md) on a projection BO instance, the method [`FOR LOCK`](../abap-for-rap-business-objects/abaphandler_meth_lock.md) is called and the respective entities are locked.

- [RAP change documents](../../abap-glossary/abenrap_change_documents_glosry.md)

  Implementation aspect that is reused automatically.

- [`early numbering`](abenbdl_early_numb.md)

  Implementation aspect that is reused automatically.

- [`late numbering`](abenbdl_late_numbering.md)

  Implementation aspect that is reused automatically.

---
title: "RAP - RAP BO Operations"
source_file: abenbdl_operations.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - RAP BO Operations

The following types of [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) are available:

- [Standard operations](abenbdl_standard_operations.md): Create, read, update, delete (known as [CRUD operations](../../abap-glossary/abencrud_glosry.md)).

  - In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), these operations are completely handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md)

  - In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), they must be implemented in the ABAP behavior pool in a [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md).

- [Operations for associations](abenbdl_association.md): A RAP BO operation for associations operates along an [association path](../../abap-glossary/abencds_association_path_glosry.md) and affects the [association target](../../abap-glossary/abenassociation_target_glosry.md). There are [standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [non-standard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md).

- [Non-standard operations](abenbdl_nonstandard.md): [RAP actions](../../abap-glossary/abenrap_action_glosry.md) and [RAP functions](../../abap-glossary/abenrap_function_glosry.md). These operations are user-implemented. They allow developers to implement scenario-specific functionality and they can consist of multiple standard operations.

- [Determine actions](abenbdl_determine_action.md): Actions that allow the [business object consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) to call [validations](abenbdl_validations.md) and [determinations](abenbdl_determinations.md) on request.

- [Draft actions](abenbdl_draft_action.md): Actions that allow manipulating the data on the [draft database table](../../abap-glossary/abendraft_table_glosry.md). [Draft actions](../../abap-glossary/abenrap_bo_draft_action_glosry.md) are completely handled by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md), both in a managed and an unmanaged RAP BO.

- [RAP BO operation additions](abenbdl_operations_additions.md) can optionally be used for different types of RAP BO operations.

## Hints

- In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), these RAP BO operations can be reused using the keyword `use`. It is also possible to specify new actions and functions in the projection layer.

  - For further details on reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

  - For further details on new actions and functions in a projection BDEF, see topic [RAP - `action`, Projection BDEF](abenbdl_nonstandard_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), RAP BO operations can be reused using the keyword [`use`](abenbdl_use_projection.md). For further details on reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

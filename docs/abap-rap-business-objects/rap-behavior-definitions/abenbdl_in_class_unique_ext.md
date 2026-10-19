---
title: "RAP - implementation in class unique, Extension"
source_file: abenbdl_in_class_unique_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - ExtensionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - implementation in class unique, Extension

## Syntax

``` abap
... implementation in class ClassName unique;  
```

## Description

Specifies an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) for the extended RAP business object. Valid abbreviations are [extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) ABAP behavior pool or extension ABP. An extension ABP is an optional component of a BDEF extension and only required if the BDEF extension specifies implementation-relevant components.

An extension ABAP behavior pool can be specified in different positions:

- [Extension header](abenbdl_extension_header.md)

- [Entity behavior extension](abenbdl_extend_beh.md)

- [Extension entity behavior definition](abenbdl_define_beh_extend.md)

- [Implementation group](abenbdl_define_beh_extend.md)

The mandatory addition `unique` defines that each operation can be implemented exactly once.

**Original ABPs and Extension ABPs**

An original ABP and an extension ABP are separate artifacts that do not depend on each other. An original ABP and an extension ABP consider each other external consumers. The following rules apply:

- [Internal operations](abenbdl_internal.md):

  RAP BO operations defined as [`internal`](abenbdl_internal.md) can be accessed only from within the same ABP that implements them. An internal operation from the original BDEF cannot be extended, since it is not visible in the extension ABP. In the same way, internal actions from an extension are not visible to the original BO.

- [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md):

  The addition `IN LOCAL MODE` grants privileged access rights only to the particular RAP BO itself. The original BO can be accessed in local mode by its own implementation classes or other classes that are called from its own implementation. The extension BO can be accessed in local mode from its own class implementations. An original BO and an extension BO consider each other external consumers.

- Field usage

  - An extension ABP can use fields from the extended RAP BO.

  - The original RAP BO can use fields from an extension, if the extension is created in the same software component.

  - Field attributes, such as [`readonly`](abenbdl_field_char.md), must be respected between the original ABP and the extension ABP. For example, if an extension ABP tries to update or delete `readonly` fields of the original RAP BO, a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs. **Note:** A runtime error also occurs when trying to modify a read-only field using dynamic EML.

- [Feature control](abenbdl_actions_fc.md):

  - The original ABP implements feature control for original fields and operations.

  - The extension ABP implements feature control for extension fields and extension operations from the same software component.

  - The [`REQUEST` parameter](../abap-for-rap-business-objects/abaphandler_meth_features.md) for the [handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) for [global](../abap-for-rap-business-objects/abaphandler_meth_global_features.md) and [instance feature control](../abap-for-rap-business-objects/abaphandler_meth_features.md) contains the fields and operations from the directly related BDEF, that means, either original or extension. It does not contain operations from both extended and extension BDEF, even if they concern the same RAP BO entity. This means that a strict separation of feature control for original and extension fields and operations is enforced.

- [Authorization control](abenbdl_authorization.md):

  - [RAP authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) can be defined only in the extended RAP BO, but it may be implemented in both the original and the extension ABP, if required.

  - The original BO implements authorization control for actions defined in the original BO.

  - The extension BO implements authorization control for extension actions, if specified.

  - The `REQUEST` parameter for the [handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) for [global](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md) and [instance authorization control](../abap-for-rap-business-objects/abaphandler_meth_auth.md) contains only the operations from the directly related BDEF, that means, either extended or extension. This means that a strict separation of authorization control for original and extension operations is enforced.

  - If an operation, for example [update](abenbdl_standard_operations.md), is protected from unauthorized access and this is implemented in the original RAP BO, then it is checked during all update operations, updates on original nodes as well as updates on extension nodes. That means that the implementation of original and extension components is strictly separated, but the original implementation also applies to operations against extension nodes.

  - The following cases require a separate implementation for authorization control in the extension behavior pool of the master entity and of the authorization-dependent entity: [actions](abenbdl_action.md) of authorization dependent entities, create-enabled [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md), create-enabled associations which are not [CDS compositions](../../abap-glossary/abencds_composition_glosry.md).

**BDEF Derived Types**

- The [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) of a RAP BO includes all original and all extension fields.

- A BDEF extension must not be used as global data type or part of a data type.

## Hint

A BDEF extension can be specified as a [BDEF friend](../../abap-glossary/abenrap_bdef_friend_glosry.md) of an original behavior definition using the syntax [`with friends`](abenbdl_with_friends.md). BDEF friends have unrestricted access to all components of the original RAP BO. For example, a BDEF friend can call [internal RAP BO operations](../../abap-glossary/abenrap_internal_operation_glosry.md) and read or modify RAP BO entities [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md). In this case, the extension ABP can access the original RAP BO without the restrictions described above.

## More Information

- The implementation rules for ABAP behavior pools are described in the topic [ABAP Behavior Pools (ABP)](../abap-for-rap-business-objects/abenabap_behavior_pools.md).

- A complete list of BDEF derived types is provided in the topic [BDEF Derived Types](../abap-for-rap-business-objects/abenrpm_derived_types.md).

## Executable Example

The executable example [Behavior Extension](abenbdl__behavior_ext_abexa.md) implements authorization control, feature control, a validation, a determination and two actions. These implementations are distributed between original ABP and extension ABP.

Further executable examples

- [Node Extension](abenbdl_assoc_ext_abexa.md)

- [Field Extension](abenbdl_field_ext_abexa.md)

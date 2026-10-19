---
title: "RAP - augment"
source_file: abenbdl_augment_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - augment

## Syntax

``` abap
... augment ...  
```

## Description

Optional addition for a [reused](abenbdl_use_projection.md) standard operation that defines [RAP BO augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md) for the operation in question. Augmentation is available for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) only. With [RAP BO augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md), it is possible to modify incoming requests from a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) on the projection layer before data reaches the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md). For example, you can add data to requests reaching the [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) before the request is passed to the [handler method](../../abap-glossary/abenabp_handler_method_glosry.md) of the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md). The operation augmentation must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) of the projection BDEF in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

The following operations can be augmented:

- [create](abenbdl_standard_operations.md)

- [update](abenbdl_standard_operations.md)

- [create by association](../../abap-glossary/abenrap_cba_operation_glosry.md)

It is not possible to set a field in augment which was already set for the original instance. The [RAP runtime](../../abap-glossary/abenrap_runt_framework_glosry.md) discards augment requests for fields that already have values. For example, values set in the original request cannot be changed. Only fields which are unset in the original request can be added.

It is not possible to set fields in augment that are defined as [`readonly`](abenbdl_field_char.md). Augment is handled like an external access and therefore, any attempt to access a `readonly` field leads to a runtime error.

When the augmentation operation is executed, the original base instances have already been locked by the framework. If the augment contains new instances, then the runtime attempts to lock them. Instances for which locking fails are included in the `FAILED` response of the projection request, and are removed from the base request.

## Availability

Augmentation is available in [projection BOs](../../abap-glossary/abenrap_projection_bo_glosry.md) only.

## Hint

It is possible to combine `augment` and [`precheck`](abenbdl_precheck.md). If both the base BO and the projection BO define a precheck method, the execution order is as follows:

1.  Precheck on projection

2.  Augment on projection

3.  Precheck on base

This way, the request including the augmentation can be checked by the base precheck.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Operation Augmentation](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/346c2b7516ce4176bbb4daebaa80c2ca?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that demonstrates how to define and implement the operation augmentation for modify operations. The base BDEF is `DEMO_RAP_MANAGED_ASSOC_ROOT`.

``` abap
projection
implementation in class bp_demo_rap_proj_augment unique;
strict ( 2 );

define behavior for DEMO_RAP_PROJ_AUGMENT alias _Parent
{
  use create ( augment );
  use update ( augment );
  use delete;

  use association _child { create ( augment ); }

  field ( modify ) VirtualElement;
  field ( readonly ) DecFieldRoot;
}

define behavior for DEMO_RAP_PROJ_AUGMENT_CHILD alias _Child
{
  use update;
  use delete;

  use association _parent;
}
```

For the implementation in the ABAP behavior pool, see `BP_DEMO_RAP_PROJ_AUGMENT======CCIMP`.

The ABAP class `CL_DEMO_RAP_PROJ_AUGMENT` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). It performs a create, an update, and a [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md). The augmentations are automatically performed, they add field values and / or add new entity instances.

## Executable Example

The example listed above is displayed an explained in detail in topic [RAP BDL - operation augmentation](abenbdl_augment_abexa.md).

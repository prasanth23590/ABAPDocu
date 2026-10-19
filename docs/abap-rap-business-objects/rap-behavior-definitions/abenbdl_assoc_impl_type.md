---
title: "RAP - AssocImplType"
source_file: abenbdl_assoc_impl_type.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - AssocImplType

## Syntax

``` abap
... [ managed | unmanaged ]  
```

## Description

RAP BDL offers the following statements to define the [association implementation type](../../abap-glossary/abenrap_assoc_impl_type_glosry.md):

- `managed`: Can only be used in business objects with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

  - For [source-resolved associations](../../abap-glossary/abensource_resolved_assoc_glosry.md):

    [Standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). The respective implementation methods do not have to be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). [Nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) for [active instances](../../abap-glossary/abenrap_active_instance_glosry.md) must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) by the application developer. [Nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) for [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) in [draft-enabled RAP business objects](../../abap-glossary/abendraft_rap_bo_glosry.md) with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md). The respective implementation methods do not have to be implemented by the application developer.

  - For [target-resolved associations](../../abap-glossary/abentarget_resolved_assoc_glosry.md):

    [Standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). The respective implementation methods do not have to be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). This holds true for active instances and, in [draft-enabled business objects](../../abap-glossary/abendraft_rap_bo_glosry.md), also for draft instances.

- `unmanaged`: Can only be used in business objects with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and [draft-enabled business objects](../../abap-glossary/abendraft_rap_bo_glosry.md) with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

  [Standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [Nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). This holds true for active and draft instances in [draft-enabled business objects](../../abap-glossary/abendraft_rap_bo_glosry.md).

- No specification of an [association implementation type](../../abap-glossary/abenrap_assoc_impl_type_glosry.md):

  - In business object with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md):

    [Standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). The respective implementation methods do not have to be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). This holds true for active instances and draft instances in [draft-enabled business objects](../../abap-glossary/abendraft_rap_bo_glosry.md). However, it is not guaranteed that transactional enablement works for all associations. [Source-resolved cross-BO associations](../../abap-glossary/abensource_resolved_assoc_glosry.md) are affected by the addition [with cross associations](abenbdl_with_cross_assoc.md) on BDEF header level: without that addition, certain scenarios are not supported, for example the [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md) when the [association target](../../abap-glossary/abenassociation_target_glosry.md) is specified with [RAP late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md). For already supported scenarios, the use of [with cross associations](abenbdl_with_cross_assoc.md) leads to an improved managed runtime implementation with additional syntax checks and error handling.

  - In business objects with [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) [unmanaged](../../abap-glossary/abenmanaged_rap_bo_glosry.md):

    \- [Operations for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) for [active instances](../../abap-glossary/abenrap_active_instance_glosry.md): [Standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [nonstandard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) for [active instances](../../abap-glossary/abenrap_active_instance_glosry.md) must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). - [Operations for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) for [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md): Most of the [operations for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). However, it is not guaranteed that transactional enablement works for all associations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For an example of an unmanaged [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) and [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) for an [intra-BO relationship](../../abap-glossary/abencds_intra_bo_assoc_glosry.md), refer to:

[RAP - Unmanaged Association Implementation](abenbdl_unmanaged_assoc_abexa.md)

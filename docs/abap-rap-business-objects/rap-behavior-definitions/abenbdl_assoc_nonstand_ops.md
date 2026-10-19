---
title: "RAP - NonstandardOperationsForAssoc"
source_file: abenbdl_assoc_nonstand_ops.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - NonstandardOperationsForAssoc

Non-standard operations for [associations](../../abap-glossary/abenassociation_glosry.md) provide noncanonical behavior along an [association path](../../abap-glossary/abencds_association_path_glosry.md) from an [association source](../../abap-glossary/abenassociation_source_glosry.md) to an [association target](../../abap-glossary/abenassociation_target_glosry.md).

The following non-standard operations for associations are available:

- [Link and Unlink Action](abenbdl_link_unlink_action.md):

  A [RAP non-standard operation for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md) that associates a [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) to another RAP BO entity instance by setting the [foreign key](../../abap-glossary/abenforeign_key_glosry.md). The link action can be defined for [intra-BO associations](../../abap-glossary/abencds_intra_bo_assoc_glosry.md) and for [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md). The unlink action disconnects two associated [RAP BO entity instances](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) by removing the value of the [foreign key](../../abap-glossary/abenforeign_key_glosry.md) field.

- [Inverse Function](abenbdl_inverse_funct.md):

  A [RAP non-standard operation for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) that receives the values of the [foreign key fields](../../abap-glossary/abenforeign_key_field_glosry.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) instances as input and provides the corresponding [association source](../../abap-glossary/abenassociation_source_glosry.md) instances as result. It can be used, for example, to enable [read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md) in a[cross-BO](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenario.

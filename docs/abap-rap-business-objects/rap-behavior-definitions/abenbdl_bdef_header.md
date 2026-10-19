---
title: "RAP - BehaviorDefinitionHeader"
source_file: abenbdl_bdef_header.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BehaviorDefinitionHeader

## Syntax

``` abap
managed | unmanaged [SavingOptions] 
      {[implementation in class ClassName unique]}; 
[strict[(version)];] 
[auxiliary class ClassName1[, ClassName2] [, ...];] 
[extensible;] 
[with draft; | with collaborative draft;] 
[with privileged mode disabling ContextName;] 
[with cross associations;] 
[foreign entity EntityName;] 
 EntityBehaviorDefinition1[, EntityBehaviorDefinition2][, ...] 
[AuthorizationContext1][, AuthorizationContext2][, ... ] 
[save after BdefName1[, BdefName2, ...];] 
...  
```

[`managed | unmanaged`](abenbdl_impl_type.md) · [`SavingOptions`](abenbdl_saving.md) · [`implementation in class ClassName unique`](abenbdl_in_class_unique.md) · [`strict[(version)]`](abenbdl_strict.md) · [`auxiliary class ClassName1[, ClassName2] [, ...];`](abenbdl_auxiliary_class.md) · [`extensible`](abenbdl_extensible.md) · [`with draft`](abenbdl_with_draft.md) · [`with collaborative draft`](abenbdl_with_coll_draft.md) · [`with privileged mode disabling ContextName`](abenbdl_privileged_mode.md) · [`with cross associations`](abenbdl_with_cross_assoc.md) · [`foreign entity EntityName`](abenbdl_foreign.md) · [`EntityBehaviorDefinition1`](abenbdl_define_beh.md) · [`EntityBehaviorDefinition2`](abenbdl_define_beh.md) · [`AuthorizationContext1`](abenbdl_authorization_context.md) · [`AuthorizationContext2`](abenbdl_authorization_context.md) · [`save after BdefName1[, BdefName2, ...]`](abenbdl_save_after.md)

## Description

Defines a RAP behavior definition in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). A RAP behavior definition consists of a [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and one or more [entity behavior definitions](../../abap-glossary/abencds_entity_bdef_glosry.md) [`EntityBehaviorDefinition1`](abenbdl_define_beh.md), [`EntityBehaviorDefinition2`](abenbdl_define_beh.md), ... Optionally, one or more [RAP authorization contexts](../../abap-glossary/abencds_auth_con_glosry.md) [`AuthorizationContext1`](abenbdl_authorization_context.md), [`AuthorizationContext2`](abenbdl_authorization_context.md), ... can be specified.

The header can define the following attributes for the entire business object. The implementation type is mandatory, all other attributes are optional.

- [`managed | unmanaged`](abenbdl_impl_type.md): Specifies the [BDEF implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md).

- [`SavingOptions`](abenbdl_saving.md):

  - The default [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) can either be enhanced or switched off and overwritten with a user-defined saving strategy.

  - Can be defined either in the [BDEF header](../../abap-glossary/abencds_bdef_header_glosry.md) and then applies to all entities of the business object. It is also possible to define saving options as an [entity behavior characteristic](abenbdl_character.md).

  - If specified, an implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

  - Only available for [managed implementation scenarios](../../abap-glossary/abenmanaged_rap_bo_glosry.md). In unmanaged implementation scenarios, the save sequence is always user-implemented.

- [`implementation in class ClassName unique`](abenbdl_in_class_unique.md): Specifies one or more classes which allow the behavior implementation of a business object. In a managed scenario, this is optional and required only if unmanaged components are added to the managed implementation.

- [`strict[(version)]`](abenbdl_strict.md): Switches on [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md). Handled by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md).

- [`auxiliary class ClassName1[, ClassName2] [, ...]`](abenbdl_auxiliary_class.md): Specifies one or more additional ABAP classes with enhanced access rights to the referenced RAP BO. The purpose of an [ABP auxiliary class](../../abap-glossary/abenabp_aux_class_glosry.md) is to support the implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

- [`extensible`](abenbdl_extensible.md): Enables [BDEF extensions](abenbdl_extension.md). If this keyword is not specified, BDEF extensions are not allowed for the respective behavior definition.

- [`with draft`](abenbdl_with_draft.md): Enables [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md). This allows users to save their changes as draft and resume editing at a later point in time. Handled by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md).

- [`with collaborative draft`](abenbdl_with_coll_draft.md): Enables [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) and allows multiple users to work concurrently on the same [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md).

- [`with privileged mode disabling ContextName`](abenbdl_privileged_mode.md): Enables [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md). The effect is that the [authorization context](../../abap-glossary/abencds_auth_context_glosry.md) `ContextName` is automatically disabled when a RAP BO consumer accesses the business object in question with a [privileged EML call](../abap-for-rap-business-objects/abapeml_privileged.md).

- [`with cross associations`](abenbdl_with_cross_assoc.md): Enables RAP cross-BO transactional enablement. This keyword effects that the operations for associations in cross-BO scenarios are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

- [`foreign entity`](abenbdl_foreign.md): Defines an entity as [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md). This means, an entity which is not part of the BO structure becomes a component for the response structures, thus enabling message mapping for other BOs.

- [`save after`](abenbdl_save_after.md): Explicitly defines the save order.

The behavior definition header is followed by

- one or more [entity behavior definitions](abenbdl_define_beh.md) that start with `define behavior for`

- or by the definition of one or more [authorization contexts](../../abap-glossary/abencds_auth_con_glosry.md) that start with [`define [own] authorization context`](abenbdl_authorization_context.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_FOREIGN_ENTITY`. The BDEF header consists of the following components:

- the implementation type `managed`

- BDEF strict mode version 2, defined using `strict(2)`

- a RAP foreign entity, in this case `DEMO_SALES_CDS_SO_1`

``` abap
managed implementation in class bp_demo_rap_foreign_entity unique;
strict ( 2 );
//enables MAP_MESSAGES:
foreign entity DEMO_SALES_CDS_SO_1;

define behavior for DEMO_RAP_FOREIGN_ENTITY alias RootEntity
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) key_field;
}
```

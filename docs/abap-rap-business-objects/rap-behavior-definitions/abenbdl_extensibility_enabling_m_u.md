---
title: "RAP - Extensibility Enabling for Base BOs"
source_file: abenbdl_extensibility_enabling_m_u.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Base BOs

## Syntax

``` abap
managed | unmanaged 
strict[(version)]; 
extensible 
[with friends BDEFExtension1 [, BDEFExtension2] [,...] ] 
[{ 
  [with validations on save;] 
  [with determinations on save;] 
  [with determinations on modify;] 
  [with additional save;] 
}]; 
[...] 
define behavior for RootEntity 
  extensible 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
  [determine action Name extensible { ... }] 
  [draft determine action Prepare extensible { ... }] 
  ... 
} 
...  
```

[`managed`](abenbdl_impl_type.md) · [`unmanaged`](abenbdl_impl_type.md) · [`strict[(version)]`](abenbdl_strict.md) · [`extensible`](abenbdl_extensible.md) · [`with friends BDEFExtension1 [, BDEFExtension2] [,...]`](abenbdl_with_friends.md) · [`define behavior for RootEntity`](abenbdl_define_beh.md) · [`extensible`](abenbdl_extensible.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md) · [`determine action Name extensible`](abenbdl_determine_action.md) · [`draft determine action Prepare extensible { ... }`](abenbdl_draft_action.md)

## Prerequisite

To allow [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) to a managed or unmanaged RAP behavior definition, [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be switched on using the keyword [`strict[(version)]`](abenbdl_strict.md).

## Description

The keyword `extensible` can be specified at different places to allow for extensions:

- `extensible` in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md)

  Prerequisite for extensibility. If it is not specified, extensions are not allowed. If specified, at least one [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) must be declared as extensible in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md). Allows the following components to be added to a RAP BO via a BDEF extensions:

  - [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md)

  - Adding a new [RAP authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) and extending an existing [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) from the extended entity.

  - Defining behavior for an extension node by means of a [RAP extension entity behavior](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md).

In the header declaration, the following optional additions are available:

- [`with friends`](abenbdl_with_friends.md): Can be used to declare one or more BDEF extensions `BDEFExtension1`, `BDEFExtension2`, ... as friends of the current behavior definition `RootEntity`. At least one BDEF extension must be specified. The friends of a BDEF have enhanced access rights to the behavior definition in question. Further details are described in the topic [RAP - `with friends`](abenbdl_with_friends.md).

- Within curly brackets, one or more of the following additions are possible:

  - `with validations on save`

  - `with determinations on save`

  - `with determinations on modify`

  - `with additional save`

    These additions explicitly allow [validations](abenbdl_validations.md), [determinations](abenbdl_determinations.md), or a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) in a [RAP entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md). If not declared explicitly, the respective type of determination, validation, or the additional save must not be defined in an extension to an existing RAP BO entity. **Note:** This declaration refers only to extensions of existing RAP BO entities ([`extend behavior for`](abenbdl_extend_beh.md)). In extension nodes ([`define behavior for`](abenbdl_define_beh_extend.md)), validations, determinations, and an additional save are always possible and no explicit permission is required.

- `extensible` in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md)

  Mandatory for each individual [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) that allows extensions. Allows the following behavior extensions to be added via a BDEF extension for the RAP BO entity in question:

  - [RAP determinations](../../abap-glossary/abenrap_determination_glosry.md) and [RAP validations](../../abap-glossary/abenrap_validation_glosry.md) can be defined for the RAP BO entity in question, under the precondition that the particular kind of determination and validation is allowed in the header definition.

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to [extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) fields.

  - [RAP actions](../../abap-glossary/abenrap_action_glosry.md) including [RAP feature control](../../abap-glossary/abenrap_feature_control_glosry.md).

  - [RAP functions](../../abap-glossary/abenrap_function_glosry.md).

  - [RAP BO determine actions](../../abap-glossary/abenrap_bo_det_action_glosry.md).

  - Behavior-enabling of [associations](../../abap-glossary/abenassociation_glosry.md) that have an extension node as association target.

  - [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md).

  - [RAP foreign entities](../../abap-glossary/abenrap_foreign_entity_glosry.md).

  - [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md).

- `extensible` can be specified in different places in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md):

  - [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the extended RAP business object can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

  - [`determine action Name extensible { ... }`](abenbdl_determine_action.md): only allowed for [draft-enabled BOs](../../abap-glossary/abendraft_rap_bo_glosry.md). Allows validations or determinations to be added to the [determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md) in question.

    `Internal` determine actions must not be declared as extensible.

  - [`draft determine action Prepare extensible { ... }`](abenbdl_draft_action.md): only allowed for draft-enabled BOs. Allows validations or determinations to be added to the [draft determine action Prepare](../../abap-glossary/abenrap_bo_draft_action_glosry.md) in question.

    `Internal` draft determine actions must not be declared as extensible.

## &ABAP_LIMITATION&

In unmanaged RAP BOs, there are the following limitations:

- Determinations and validations cannot be specified in BDEF extensions to unmanaged RAP BOs. Therefore, the following additions are not available:

  `with validations on save;` `with determinations on modify;` `with determinations on save;`

- A RAP additional save is not available in BDEF extensions to unmanaged RAP BOs. Therefore, the addition `with additional save;` is not available.

- Determine actions and the draft determine action `Prepare` are not available in BDEF extensions to unmanaged RAP BOs. Therefore, determine actions and the draft determine action `Prepare` cannot be specified as `extensible`.

- Node extensibility is not available for unmanaged RAP BOs.

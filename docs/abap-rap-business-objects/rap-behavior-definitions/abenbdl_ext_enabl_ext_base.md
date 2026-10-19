---
title: "RAP - Extensibility Enabling for Base BDEF Extensions"
source_file: abenbdl_ext_enabl_ext_base.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling > RAP - Extensibility Enabling for BDEF Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Base BDEF Extensions

## Syntax

``` abap
extension [using interface]; 
extensible [with friends BDEFExtension1 [, BDEFExtension2] [,...]] [{ 
  [with validations on save;] 
  [with determinations on save;] 
  [with determinations on modify;] 
  [with additional save;] 
}]; 
[...] 
extend behavior for EntityName 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
  [determine action Name extensible { ... }] 
   ... 
} 
 
define behavior for ExtNode 
  extensible 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
  [determine action Name extensible { ... }] 
  [draft determine action Prepare extensible { ... }] 
  ... 
} 
[...] 
...  
```

[`extension`](abenbdl_extension_syntax.md) · [`extensible`](abenbdl_extensible.md) · [`with friends BDEFExtension1 [, BDEFExtension2] [,...]]`](abenbdl_with_friends.html) · [`extend behavior for EntityName`](abenbdl_extend_beh.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md) · [`determine action Name extensible`](abenbdl_determine_action.md) · [`define behavior for ExtNode`](abenbdl_define_beh_extend.md) · [`extensible`](abenbdl_extensible.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md) · [`determine action Name extensible`](abenbdl_determine_action.md) · [`draft determine action Prepare extensible { ... }`](abenbdl_draft_action.md)

## Description

To extend a [base BDEF extension](../../abap-glossary/abenrap_base_bdef_ext_glosry.md), the keyword `extensible` can be specified in the following places:

- `extensible` in the BDEF header:

  Prerequisite for extensibility. If it is not specified, extensions are not allowed. If specified, at least one component of the [RAP BO extension](../../abap-glossary/abenrap_bo_extension_glosry.md) must be declared as `extensible`.

In the header declaration, the following optional additions are available:

- [`with friends`](abenbdl_with_friends.md): Can be used to declare one or more BDEF extensions `BDEFExtension1`, `BDEFExtension2`, ... as friends of the current BDEF extension. At least one BDEF extension must be specified. The friends of a BDEF have enhanced access rights to the behavior definition in question. Further details are described in the topic [RAP - `with friends`](abenbdl_with_friends.md).

- Within curly brackets, one or more of the following additions are possible:

  - `with validations on save`

  - `with determinations on save`

  - `with determinations on modify`

  - `with additional save`

    These additions explicitly allow [validations](abenbdl_validations.md), [determinations](abenbdl_determinations.md), or a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) in a [RAP entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md). If not declared explicitly, the respective type of determination, validation, or the additional save must not be defined in an extension to an existing RAP BO entity. **Note:** This declaration refers only to extensions of existing RAP BO entities ([`extend behavior for`](abenbdl_extend_beh.md)). In extension nodes ([`define behavior for`](abenbdl_define_beh_extend.md)), validations, determinations, and an additional save are always possible and no explicit permission is required.

- `extensible` in the body of an [entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md):

  - [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

  - [`determine action Name extensible { ... }`](abenbdl_determine_action.md): only allowed for [draft-enabled BOs](../../abap-glossary/abendraft_rap_bo_glosry.md). Allows validations or determinations to be added to the [determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md) in question.

    `Internal` determine actions must not be declared as extensible.

- `extensible` in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) of an [extension entity behavior definition](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) (extension node):

  Mandatory for each individual extension node that allows extensions. Allows the following behavior extensions to be added via a BDEF extension:

  - [RAP determinations](../../abap-glossary/abenrap_determination_glosry.md) and [RAP validations](../../abap-glossary/abenrap_validation_glosry.md) can be defined for the RAP BO entity in question, under the precondition that the particular kind of determination and validation is allowed in the header definition.

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to [extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) fields.

  - [RAP actions](../../abap-glossary/abenrap_action_glosry.md) including [RAP feature control](../../abap-glossary/abenrap_feature_control_glosry.md).

  - [RAP functions](../../abap-glossary/abenrap_function_glosry.md).

  - [RAP BO determine actions](../../abap-glossary/abenrap_bo_det_action_glosry.md).

  - Behavior-enabling of [associations](../../abap-glossary/abenassociation_glosry.md) that have an extension node as association target.

  - [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md).

  - [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md).

- `extensible` can be specified in different places in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of an extension node:

  - [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the extended RAP business object can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

  - [`determine action Name extensible { ... }`](abenbdl_determine_action.md): only allowed for [draft-enabled BOs](../../abap-glossary/abendraft_rap_bo_glosry.md). Allows validations or determinations to be added to the [determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md) in question.

    `Internal` determine actions must not be declared as extensible.

  - [`draft determine action Prepare extensible { ... }`](abenbdl_draft_action.md): only allowed for draft-enabled BOs. Allows validations or determinations to be added to the [draft determine action Prepare](../../abap-glossary/abenrap_bo_draft_action_glosry.md) in question.

    `Internal` draft determine actions must not be declared as extensible.

## &ABAP_LIMITATION&

In BDEF extensions to unmanaged RAP BOs, there are the following limitations:

- Determinations and validations cannot be specified in BDEF extensions to unmanaged RAP BOs. Therefore, the following additions are not available:

  `with validations on save;` `with determinations on modify;` `with determinations on save;`

- A RAP additional save is not available in BDEF extensions to unmanaged RAP BOs. Therefore, the addition `with additional save;` is not available.

- Determine actions and the draft determine action `Prepare` are not available in BDEF extensions to unmanaged RAP BOs. Therefore, determine actions and the draft determine action `Prepare` cannot be specified as `extensible`.

- Node extensibility is not available for unmanaged RAP BOs. Therefore, extension nodes cannot be specified as `extensible`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXTEND2` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE`. It is declared as `extensible` and therefore allows for extension layering.

``` abap
extension implementation in class bp_demo_rap_extend2 unique;
extensible {
with determinations on save;
with validations on save; }

extend behavior for DEMO_RAP_EXTENSIBLE
{
 association _child {create; with draft;}
}

define behavior for DEMO_RAP_EXTENSIBLE_CH
authorization dependent
lock dependent
persistent table demo_dbtab_child
draft table demo_dbtab_dr2
extensible
{
update;
delete;
action(authorization:global) MyExtAction;

association _to_parent{with draft;}

field(readonly:update) key_field, key_field_child;
}
```

The BDEF extension `DEMO_RAP_BASE_EXT_LAYER` extends the BDEF extension `DEMO_RAP_EXTEND2`.

``` abap
extension implementation in class bp_demo_rap_base_ext_layer unique;

extend behavior for DEMO_RAP_EXTENSIBLE
{

}

extend behavior for DEMO_RAP_EXTENSIBLE_CH
{
  action(authorization:global) Action_X;
  validation Validation_X on save { create; }
  determination Determination_X on save { create; }
  determine action (authorization:none) DetAct_X {
    validation Validation_X; determination Determination_X;}
}
```

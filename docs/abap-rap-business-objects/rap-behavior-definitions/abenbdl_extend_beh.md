---
title: "RAP - EntityBehaviorExtension"
source_file: abenbdl_extend_beh.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorExtension

## Syntax

``` abap
extend behavior for EntityName 
[implementation in class ClassName unique] 
[with additional save [with full data]] 
{ 
    ExtensionBody 
  |[group] 
} 
...  
```

[`implementation in class ClassName unique`](abenbdl_in_class_unique_ext.md) · [`with additional save [with full data]`](abenbdl_saving.md) · [`ExtensionBody`](abenbdl_entity_beh_extension.md) · [`group`](abenbdl_group_extension.md)

## Description

Extends the behavior of an existing RAP BO entity.

Syntax additions and components:

- [`implementation in class ClassName unique`](abenbdl_in_class_unique_ext.md): Specifies an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) for the [extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) behavior of the particular entity.

- [`with additional save [with full data]`](abenbdl_saving.md):

  - Adds additional steps to the default [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

  - As a prerequisite, the extended BDEF must explicitly allow extensions with additional save (see the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md)).

  - Possible only if the underlying BO has implementation type [`managed`](../../abap-glossary/abenmanaged_rap_bo_glosry.md). Currently not supported for unmanaged RAP BOs.

  - The saving options [`SavingOptions`](abenbdl_saving.md) specified in the original BO do not affect the additional save of the extension. The original BO can specify an [additional save](../../abap-glossary/abenrap_add_save_glosry.md), an [unmanaged save](../../abap-glossary/abenrap_unman_save_glosry.md), or use the default save sequence. The original saving option is applied to original behavior and the additional save specified in the extension is applied to extension behavior.

  - In an extension, an additional save can be specified per entity in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md). Notation in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md), like in the extended BDEF, is not allowed.

  - The implementation takes place in the [`save_modified`](../abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md) method of the [RAP saver class](../abap-for-rap-business-objects/abenabp_saver_class.md) in the respective extension [ABP](../../abap-glossary/abenbehavior_pool_glosry.md). The method parameters of this `save_modified` method are typed according to the particular BDEF extension that enables the additional save. In other words, the ABP reflects exactly the BDEF components of the BDEF it belongs to and not the entire RAP BO. Furthermore, the rules for [extension ABPs](abenbdl_in_class_unique_ext.md) apply. Data is passed to the `save_modified` method. It works as described in topic [RAP - `SavingOptions`](abenbdl_saving.md). If this addition is specified either in the original RAP BO or in an extension, then it is enabled each time an additional save is implemented. Multiple extensions may exist and all of them may specify an additional save, but only one of them may specify `with full data`. In this case, full instance data is passed each time the `save_modified` method is called, even for extensions which do not specify this addition.

  - The addition `with additional save [with full data]` in a BDEF extension works as described in topic [RAP - `SavingOptions`](abenbdl_saving.md).

- [`ExtensionBody`](abenbdl_entity_beh_extension.md): Extends the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md).

- [`group`](abenbdl_group_extension.md): Divides the implementation-relevant parts of an extended RAP BO's business logic into multiple groups for behavior implementation, each with its own [implementation class](abenbdl_in_class_unique_ext.md).

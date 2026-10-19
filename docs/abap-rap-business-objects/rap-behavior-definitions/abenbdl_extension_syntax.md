---
title: "RAP - extension"
source_file: abenbdl_extension_syntax.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extension

## Syntax

``` abap
extension [using interface InterfaceBdef][;] 
  [ExtensionHeader] 
  [foreign entity] 
  [EntityBehaviorExtension] 
  [ExtensionEntityBehavior] 
  [extend own authorization context] 
  [define authorization context] 
...  
```

[`using interface InterfaceBdef`](abenbdl_using_interface.md) · [`ExtensionHeader`](abenbdl_extension_header.md) · [`foreign entity`](abenbdl_foreign.md) · [`EntityBehaviorExtension`](abenbdl_extend_beh.md) · [`ExtensionEntityBehavior`](abenbdl_define_beh_extend.md) · [`extend own authorization context`](abenbdl_extend_own_auth_context.md) · [`define authorization context`](abenbdl_def_auth_context.md)

## Description

Extends an existing [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) of type [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) using a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). An existing RAP behavior definition can have one or more BDEF extensions. The number of extensions is not limited.

Naming: BDEF extensions themselves and each single extension element should use a separate [namespace](../../abap-glossary/abennamespace_glosry.md) to avoid naming conflicts with the original BDEF and its elements. BDEF extensions created in non-SAP and non-partner development systems should use the [customer namespace](../../abap-glossary/abencustomer_namespace_glosry.md) prefix `Z` or `ZZ`.

A BDEF extension can have the following components:

- [`using interface`](abenbdl_using_interface.md): It is strongly recommended that a RAP BO is extended via an interface layer. For details, see the topic [RAP - `using interface`, Extension](abenbdl_using_interface.md).

- [`ExtensionHeader`](abenbdl_extension_header.md): Mandatory component of a BDEF extension. Similar to the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) but offers fewer options.

  The semicolon after the keyword `extension` is either mandatory or not allowed, depending on the components of the `ExtensionHeader`. See examples.

- [`foreign entity`](abenbdl_foreign.md): Defines a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) which is not part of the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the current RAP BO as part of the response structures. A foreign entity can be defined before, after, or between the other components. Only entities that belong to the same software component can be added as [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) to a BDEF extension.

- [`EntityBehaviorExtension`](abenbdl_extend_beh.md): Behavior extension of an existing RAP BO entity.

- [`ExtensionEntityBehavior`](abenbdl_define_beh_extend.md): Defines the behavior for an extension node. Node extensibility is currently not supported for unmanaged RAP BOs.

- [`extend own authorization context`](abenbdl_extend_own_auth_context.md): If the extended BO defines a [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md), this context can be extended. If the extended BO does not define an own authorization context, it must not be added via an extension.

- [`define authorization context`](abenbdl_def_auth_context.md): A new [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) can be defined in a BDEF extension. The syntax is similar to the syntax for RAP BOs with the following difference: The addition `for disable` is not supported. For details, see topic [RAP - `define authorization context`](abenbdl_def_auth_context.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows BDEF extension `DEMO_RAP_EXTENSION_1`. It extends BDEF `DEMO_RAP_EXTENSIBLE_ROOT`. The extension contains the following components:

- BDEF extension header

- Entity behavior extension

- Extension entity behavior

``` abap
extension using interface demo_rap_ext_using_interface;
foreign entity demo_rap_factory_ACTION;
extend behavior for GrandChildInterface
{
  association _Children4Ext { create; with draft; }
}

define behavior for DEMO_RAP_EXTENSIBLE_EXT alias ExtNode
  using DEMO_RAP_EXT_USING_INT_EXT
persistent table demo_ggchl_ex_ba
draft table demo_ggrch_ext
etag master Timestamp
( lock, authorization ) dependent

{
  update;
  delete;
  field ( readonly )
  KeyField, KeyFieldchild, Keyfieldgrchld;

  field ( readonly : update ) Keyfieldggchld;
  field ( readonly ) Timestamp;

  association _parent { with draft; }
  association _Sibling4 { with draft; }
  ancestor association _GrandParent2 { with draft; }
  ancestor association _GreatGrandParent1 { with draft; }

  mapping for demo_ggchl_ex_ba
  {
    Keyfield = key_field;
    Keyfieldchild = key_field_child;
    Keyfieldgrchld = key_field_grchld;
    Keyfieldggchld = key_field_ggchld;
    Datafield = data_field;
    Charfield = char_field;
    Timestamp = timestamp;
  }
}
```

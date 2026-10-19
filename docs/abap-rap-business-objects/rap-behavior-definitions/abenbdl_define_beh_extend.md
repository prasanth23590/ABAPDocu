---
title: "RAP - Extension Entity Behavior Definition"
source_file: abenbdl_define_beh_extend.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extension Entity Behavior Definition

## Syntax

``` abap
... define behavior for ExtNode [using]   ...  
```

[`define behavior for ExtNode [using] `](abenbdl_define_beh.md)

## Prerequisite

As a prerequisite, the extended [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) must explicitly allow BDEF extensions as described in the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

## Description

Defines the behavior for an [extension node](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) in a BDEF extension using the statement `define behavior for`. As a prerequisite, the node must be added to the RAP data model via [RAP data model extensions](../../abap-glossary/abenrap_data_model_ext_glosry.md). The BDEF extension can add behavior for this extension node.

The behavior for the extension node is defined in the same way as for RAP BOs, see [`EntityBehaviorDefinition`](abenbdl_define_beh.md), with the following differences:

- A [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) can be specified with the syntax addition [`using`](abenbdl_using_interface.md) (instead of [`using interface`](abenbdl_using_interface.md), which is used for RAP BO extensions).

- No explicit pointing to a [RAP authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md).

  Use `authorization dependent` instead of [`authorization dependent by _Assoc`](abenbdl_authorization.md).

- No explicit pointing to a [RAP lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md).

  Use `lock dependent` instead of [`lock dependent by _Assoc`](abenbdl_locking.md).

- No explicit pointing to a [RAP ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md).

  Use `etag dependent` instead of [`etag dependent by _Assoc`](abenbdl_etag.md). **Note:** As a best practice, SAP recommends that an ETag master field is defined for each individual entity. As a consequence, the syntax `etag dependent` should not be used at all.

- No explicit pointing to a [RAP change documents master entity](../../abap-glossary/abenrap_change_doc_master_glosry.md).

  Use `changedocuments dependent` instead of [`changedocuments dependent by _Assoc`](abenbdl_change_documents.md).

- Declare [ancestor associations](abenbdl_ancestor_ext.md), so that the path to the authorization master, lock master, and ETag master entities can be derived.

If an ABAP behavior pool is specified, the rules for extension ABPs apply. See the topic [RAP - `implementation in class unique`, Extension](abenbdl_in_class_unique_ext.md).

**Limitation:** Node extensibility is currently not supported in unmanaged RAP BOs. Defining new associations in node extensions is currently only partially supported. The following scenarios are supported:

- Defining a source-resolved association to an early-numbered target for an extension of a non-draft managed core behavior definition.

- Defining a source-resolved association to an early-numbered target for an extension of a draft-enabled managed core behavior definition.

- Defining a source-resolved association to a late-numbered target for an extension of a managed non-draft core behavior definition.

## Hints

- A short syntax form is available: `( lock, authorization, etag ) dependent`. Each of the three components `lock`, `authorization`, and `etag` is optional but at least one of them must be specified within the parentheses.

- Currently, only root entities can be defined as authorization master and lock master entity. An extension node can therefore not be specified as authorization master or as lock master entity.

- Currently, [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) can only be defined in [RAP BO root entities](../../abap-glossary/abenrap_bo_root_entity_glosry.md). Since extension nodes are usually below the root node, they cannot define any new RAP business events.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXTENSION_1` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE_ROOT`. It behavior-enables an extension node using the syntax `define behavior for`. It defines behavior and multiple ancestor associations. Lock, authorization, and ETag master are not specified explicitly, but derived implicitly.

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

## Executable Example

The executable example [Node extension](abenbdl_assoc_ext_abexa.md) explains the example above in detail.

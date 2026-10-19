---
title: "RAP - using interface, Extension"
source_file: abenbdl_using_interface.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - using interface, Extension

## Syntax Forms

**General Specification on Header Level**

``` abap
... using interface InterfaceBdef;
```

**Specification for Extension Nodes on Entity Level**

``` abap
... using CDSInterface;
```

### Variant

[1. `... using interface InterfaceBdef;`](abenbdl_using_interface.md#variant-1)

[2. `... using CDSInterface;`](abenbdl_using_interface.md#variant-2)

## Overview

### Description

[RAP business objects](../../abap-glossary/abenrap_bo_glosry.md) can be extended via [RAP BO interfaces](../../abap-glossary/abenrap_bo_interface_glosry.md) using the optional addition `using interface`. A RAP BO interface is a layer on top of the base BO that is an interface for stable consumption and is usually [released as API](../../abap-glossary/abenreleased_api_glosry.md). In a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) with the addition `using interface`, only entities that are part of the RAP BO interface can be extended.

- In general, the RAP BO interface is specified in the [BDEF extension header](../../abap-glossary/abenrap_bdef_ext_header_glosry.md), directly after the keyword `extension`, using the syntax addition `using interface`. All entities that are part of the RAP BO interface can be extended then. Further details are provided under Variant 1.

- In a node extensibility scenario, the extension node is not part of the RAP BO interface. An interface for the extension node can be specified using the keyword `using` in the [RAP extension entity behavior](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) on entity level. Further details are provided under Variant 2.

Extensions can be created directly for managed or unmanaged RAP BOs. However, SAP recommends that you always extend a RAP BO via an interface and to always use the addition `using interface`. In case of [C0](../../abap-glossary/abenc0_contract_glosry.md) [developer extensibility](../../abap-glossary/abendev_extensibility_glosry.md), an interface is mandatory. In some other scenarios, `using interface` is mandatory and this is enforced by a syntax check error.

## More Information

- Topic [RAP - Interface Behavior Definition](abenbdl_rap_bo_interface.md).

- Development guide for the ABAP RESTful Application Programming Model, topic [Business Object Interface](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/7caa146ddc4b4f24a58efd33f0f789b4?version=sap_cross_product_abap).

- Topic [Contract Checks for Released APIs](../../abap-apis/release-contracts/abenrestricted_apis_atc_checks.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows two BDEF extensions:

- The first one directly extends the base BDEF, without interface.

- The second one extends the base BDEF via a BDEF interface.

The base BDEF is the managed BDEF `DEMO_RAP_EXTENSIBLE_ROOT`.

BDEF extension `DEMO_RAP_EXT_WO_INT` without an interface:

``` abap
extension;

extend behavior for Root
{
event myEvent;
}
```

BDEF extension `DEMO_RAP_EXT_USING_INTERF` using an interface.

``` abap
extension using interface DEMO_RAP_EXT_USING_INTERFACE
 implementation in class bp_demo_rap_ext_using_interf unique;

extend behavior for RootInterface {

action (authorization : instance) SetValue_ext;

}

extend behavior for ChildInterface {
}

extend behavior for GrandChildInterface {
}

extend behavior for GreatGrandChildInterface {
}
```

## Variant 1

`... using interface InterfaceBdef`

## Prerequisite

As a prerequisite for `using interface`, the [RAP interface behavior definition](../../abap-glossary/abencds_interface_bdef_glosry.md) `InterfaceBdef` must explicitly allow extensions. It must be declared as `extensible` in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) as described in topic [RAP - Behavior Definition Header, Interface BDEF](abenbdl_bo_interface_header.md).

### Description

Using the optional addition `using interface`, a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) is extended via a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). A RAP BO interface is a layer on top of the base BO that is an interface for stable consumption and is usually [released as API](../../abap-glossary/abenreleased_api_glosry.md). In a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) with the addition `using interface`, only entities that are part of the RAP BO interface can be extended.

An extension `using interface` produces simultaneous extensions of the base RAP BO and of the interface. For example, an extension action is part of the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) of the base RAP BO and of the interface RAP BO.

The extension BDEF must reference [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md), [RAP BO fields](../../abap-glossary/abenrap_bo_field_glosry.md), and other elements by their interface names, not by their base names (which may be different). The only exceptions are elements which are not reflected in the interface, such as determinations and validations.

In its implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md), the extension may use any released interface existing for the base RAP BO to perform [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) operations. It is an EML consumer like any other and there might be multiple released interfaces for a RAP BO. But it is most common that it uses the very same interface which it extends.

### Hint

An extension `using interface` is created for a BDEF of type `managed` or `unmanaged`. It is not created directly for the interface. In [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md), you select the base BDEF as basis for an extension.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Base BDEF: RAP BO with four nodes.

``` abap
managed implementation in class bp_demo_rap_extensible_root unique;
strict(2);
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

with draft;
define behavior for DEMO_RAP_EXTENSIBLE_ROOT alias Root
persistent table demo_dbtab_root
draft table demo_dbtab_exdrf
lock master
total etag Timestamp
authorization master ( instance, global )
extensible

etag master LastChangedAt
{
  create;
  update;
  delete;
  association _child { create; with draft; }

  draft action ( authorization : none ) Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare extensible;

  field(readonly:update) KeyField;
  field(readonly) Timestamp;

  mapping for demo_dbtab_root corresponding extensible
  {
    KeyField = key_field;
    DataField = data_field;
    CharField = char_field;
    CharField2 = char_field_2;
    DecField = dec_field;
    Timestamp = crea_date_time;
    LastChangedAt = lchg_date_time;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_CHILD alias Child
persistent table demo_dbtab_child
draft table demo_dbtab_exchl
(lock, etag, authorization) dependent by _parent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField;
  association _parent { with draft; }
  association _grchld { create; with draft; }

  field(readonly:update) KeyFieldChild;

  mapping for demo_dbtab_child corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    DataField = data_field;
    CharField = char_field;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_GRCHLD alias GrandChild
persistent table demo_dbtab_grchl
draft table demo_dbtab_grch
(lock,authorization,etag) dependent by _GrandParent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField, KeyFieldChild;
  association _GrandParent { with draft; }
  association _parent { with draft; }
  association _child { create; with draft; }

  field(readonly:update) KeyFieldGrchld;

  mapping for demo_dbtab_grchl corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    KeyFieldGrchld = key_field_grchld;
    DataField = data_field;
    CharField = char_field;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_GGCHLD alias GreatGrandChild
persistent table demo_dbtab_ggchl
draft table demo_dbtab_ggrch
(lock, authorization, etag) dependent by _GreatGrandParent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField, KeyFieldChild, KeyFieldGrChld;
  association _GrandParent { with draft; }
  association _parent { with draft; }
  association _GreatGrandParent { with draft; }

  field(readonly:update) KeyFieldGgchld;

  mapping for demo_dbtab_ggchl corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    KeyFieldGrchld = key_field_grchld;
    KeyFieldGgchld = key_field_ggchld;
    DataField = data_field;
    CharField = char_field;
  }
}
```

Interface BDEF: renames the RAP BO entities.

``` abap
interface;
use draft;
extensible;
use side effects;

define behavior for DEMO_RAP_EXT_USING_INTERFACE alias RootInterface
{
  use create;
  use update;
  use delete;

  use action Edit;
  use action Activate;
  use action Discard;
  use action Resume;
  use action Prepare;

  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_CHILD alias ChildInterface
{
  use update;
  use delete;

  use association _parent { with draft; }
  use association _grchld { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_GRCHLD alias GrandChildInterface
{
  use update;
  use delete;

  use association _GrandParent { with draft; }
  use association _parent { with draft; }
  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_GGCHLD alias GreatGrandChildInterface
{
  use update;
  use delete;

  use association _GrandParent { with draft; }
  use association _parent { with draft; }
  use association _GreatGrandParent { with draft; }
}
```

Extension using interface: Extends the root node, which it refers to by its interface name.

``` abap
extension using interface DEMO_RAP_EXT_USING_INTERFACE
 implementation in class bp_demo_rap_ext_using_interf unique;

extend behavior for RootInterface {

action (authorization : instance) SetValue_ext;

}

extend behavior for ChildInterface {
}

extend behavior for GrandChildInterface {
}

extend behavior for GreatGrandChildInterface {
}
```

### Executable Example

The executable example [RAP - RAP BO Extension Using Interface](abenbdl_using_interface_abexa.md) explains the example above in detail.

## Variant 2

`... using CDSInterface`

### Description

In a node extensibility scenario, an interface for the extension node can be specified using the keyword `using` in the [RAP extension entity behavior](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) on entity level. `CDSInterface` is the name of a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) that projects the extension node.

**Caution**

Node extensibility is currently not supported for unmanaged RAP BOs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following BDEF extension `DEMO_RAP_EXTENSION_1` adds an extension node to an existing RAP business object. It uses the RAP BO interface `DEMO_RAP_EXT_USING_INTERFACE` and the [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) `DEMO_RAP_EXT_USING_INT_EXT`.

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

---
title: "RAP - extension for abstract"
source_file: abenbdl_extension_for_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Abstract BDEF Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extension for abstract

## Syntax

``` abap
extension for abstract; 
  [extensible;] 
  [define behavior for ...] 
  [extend behavior for ...] 
  [scalar entity ...] 
...  
```

[`extensible`](abenbdl_ext_enabl_ext_abs.md)

### Alternative

[1. `... define behavior for`](abenbdl_extension_for_abstract.md#alternative-1)

[2. `... extend behavior for`](abenbdl_extension_for_abstract.md#alternative-2)

[3. `... scalar entity`](abenbdl_extension_for_abstract.md#alternative-3)

## Overview

### Description

Extends an existing [abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md) using an [abstract BDEF extension](../../abap-glossary/abenrap_abs_bdef_ext_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). An abstract behavior definition can have one or more abstract BDEF extensions. The number of extensions is not limited.

An abstract BDEF extension can have the following components:

- [`extensible`](abenbdl_ext_enabl_ext_abs.md): if specified, [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md) is allowed. For details, see [RAP - Extensibility Enabling for Abstract BDEF Extensions](abenbdl_ext_enabl_ext_abs.md).

- `define behavior for`: Adds a new node to the hierarchical type of the abstract BDEF using the statement `define behavior for`.

- `extend behavior for`: Extends an existing node using the statement `extend behavior for`.

- `scalar entity`: Adds a new scalar entity to the hierarchical type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The abstract BDEF extension `DEMO_RAP_ABSTRACT_X` extends the abstract behavior definition `DEMO_RAP_ABSTRACT_ROOT`.

- It extends the behavior of the root node.

- It adds the scalar entity `DEMO_RAP_ABSTRACT_5`.

- It adds the extension node `DEMO_RAP_ABSTRACT_4` using the syntax `define behavior for`.

``` abap
extension for abstract;
extensible;

extend behavior for DEMO_RAP_ABSTRACT_ROOT
{
  association _item3;
  extend deep mapping for demo_rap_struc_x
    {
      sub _Item3 = sub_3;
    }
}

scalar entity DEMO_RAP_ABSTRACT_5 field comp3;

extend behavior for DEMO_RAP_ABSTRACT_1
{
  association _x1;
}

define behavior for DEMO_RAP_ABSTRACT_4
with control
extensible
{
  field ( suppress ) comp1, comp2;
}
```

## Alternative 1

`... define behavior for ...`

## Prerequisites

- As a prerequisite, the original abstract behavior definition must explicitly allow BDEF extensions as described in topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

- The extension node must be added to the RAP data model via [RAP data model extensions](../../abap-glossary/abenrap_data_model_ext_glosry.md).

### Description

An extension node adds a new node to the hierarchical type of the abstract BDEF using the statement `define behavior for`. [Field characteristics](abenbdl_field_abstract.md), [associations](abenbdl_association_abstract.md), and [type mappings](abenbdl_type_mapping_abstract.md) can be specified for the extension node in the same way as for abstract BDEFs. There is only one difference: the attribute `mandatory:execute` is not available in abstract BDEF extensions, neither for fields, nor for associations.

For details, see the topic [RAP - Entity Behavior Body, Abstract BDEF](abenbdl_body_abstract.md).

## Alternative 2

`... extend behavior for ...`

### Description

Extends an existing node of an abstract BDEF. As a prerequisite, extensions must be explicitly enabling as described in the topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

Options:

- The field characteristic `suppress` can be specified for extension fields.

- Associations that have an extension node as association target can be added.

- An existing type mapping can be extended. As a prerequisite, the original type mapping must explicitly allow extensions as described in the topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

- A new RAP type mapping to a partner type can be added. This type mapping can only contain extension fields. It must not contain any fields from the original data model. The syntax is exactly the same as for abstract BDEFs, see topic [RAP - Mapping, Abstract BDEF](abenbdl_type_mapping_abstract.md).

## Alternative 3

`... scalar entity ...`

### Description

A new scalar entity can be integrated into the hierarchical type as scalar type. This scalar entity must be an extension node, which means it must be added to the data model via [RAP data model extensions](../../abap-glossary/abenrap_data_model_ext_glosry.md). The syntax is exactly the same as for abstract BDEFs, see the topic [RAP - Entity Behavior Definition, Abstract BDEF](abenbdl_define_beh_abstract.md).

---
title: "RAP - Entity Behavior Definition, Abstract BDEF"
source_file: abenbdl_define_beh_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Entity Behavior Definition, Abstract BDEF

## Syntax

``` abap
{{ define behavior for AbstractEntity [alias AliasName] 
  [extensible] 
  [with control] 
  { 
   entity behavior body 
  } 
} 
| scalar entity AbstractEntity field FieldName } 
 
[behavior for ChildEntity1][, behavior for ChildEntity2][, ... 
]  
```

[`extensible`](abenbdl_extensible.md) · [`entity behavior body`](abenbdl_body_projection.md)

### Alternative

[1. `... define behavior for`](abenbdl_define_beh_abstract.md#alternative-1)

[2. `... scalar entity ...`](abenbdl_define_beh_abstract.md#alternative-2)

## Overview

### Description

Defines the behavior for a [RAP abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). The abstract behavior definition must be based on a root [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) `AbstractEntity` and it can define the behavior for one or more of the nodes of the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md).

For each node of the CDS composition tree, there are two possibilities how to include them in the behavior definition:

- A node can be integrated into the hierarchical type as a structured type using the syntax `define behavior for`. In this case, an [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) is mandatory.

- A node can be integrated into the hierarchical type as a scalar type using the syntax `scalar entity`.

Both alternatives are described with their additions below.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an abstract BDEF with two nodes, one of them being a scalar entity.

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_CDS_SCALAR_ROOT_1 alias Root
{
mapping for demo_cds_scalar_1 corresponding
  {
    field1 = r_fd1;
    field2 = r_fd2;
    field3  = r_sib;
  }

    association _item1;
}

scalar entity demo_cds_scalar_child_1 field i1fd2;
```

## Alternative 1

`... define behavior for ...`

### Description

[Entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) for a CDS abstract entity. It can consist of the following additions and components:

- `alias`: an alias name can be specified using the keyword `alias`. The length of an alias name `AliasName` is restricted to 30 characters.

- [`extensible`](abenbdl_extensible.md): To enable [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md), a declaration in the abstract BDEF header is required and the keyword `extensible` must also be declared after the statement `define behavior for` for each entity that allows BDEF extensions. For details, see the topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

- `with control` is an optional addition that adds a [`%control`](../abap-for-rap-business-objects/abapderived_types_comp.md) structure to the corresponding derived type structure. That means that for each component of the hierarchical type, stemming either from an entity field or from an association, an identically named component of the [built-in ABAP type `x(1)`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) is added as part of the structure `%control` which is appended at the end. As a result, all or some levels of the hierarchical types contain `%control` components which may be used by applications to indicate the provisioning of the equally named payload components.

  As a prerequisite to use `with control`, the abstract BDEF must use the addition [`with hierarchy`](abenbdl_bdef_abstract_header.md).

- An [entity behavior body](abenbdl_body_abstract.md) is mandatory and it can define field characteristics, associations, or type mapping. Transactional behavior is not possible in an abstract BDEF.

### Hint

[Entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) cannot be specified for abstract BDEFs.

## Alternative 2

`... scalar entity ...`

### Description

An entity in the CDS composition tree can be integrated into the hierarchical type not as a structured type, but as a scalar type, for example, an integer or a character. This is often defined for [leaf entities](../../abap-glossary/abenleaf_entity_glosry.md). For a scalar type, the following syntax must be used instead of the usual `define behavior for` syntax:

`... scalar entity AbstractEntity field FieldName;`

The specified field `FieldName` of the scalar entity `AbstractEntity` is taken for the scalar type. All other entity fields are ignored. Suppressing unwanted fields and type mappings are irrelevant.

It is also possible to declare the root node as scalar entity. Then the complete hierarchical type turns into one scalar type. This enables entity-based action parameter types which are [elementary](../../abap-glossary/abenelementary_data_type_glosry.md) or [internal tables](../../abap-glossary/abeninternal_table_glosry.md) with elementary [line types](../../abap-glossary/abenrow_type_glosry.md).

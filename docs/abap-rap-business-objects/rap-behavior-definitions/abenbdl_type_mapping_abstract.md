---
title: "RAP - Mapping, Abstract BDEF"
source_file: abenbdl_type_mapping_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions > RAP - Entity Behavior Definition, Abstract BDEF > RAP - Entity Behavior Body, Abstract BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Mapping, Abstract BDEF

## Syntax Forms

**Type Mapping**

``` abap
... mapping for PartnerType ...
```

**Deep Mapping**

``` abap
... deep mapping for NestedDeepDDICType [corresponding [extensible]] 
   { 
      EntityComp1 = PartnerComp1 
     [...] 
     [sub _Compos1 = Partnersub1][, 
      sub _Compos2 = Partnersub2] 
     [...] 
    } 
...
```

[`mapping for PartnerType`](abenbdl_type_mapping.md) · [`extensible`](abenbdl_extensible.md)

### Alternative

[1. `mapping for PartnerType ...`](abenbdl_type_mapping_abstract.md#alternative-1)

[2. `deep mapping for NestedDeepDDICType ...`](abenbdl_type_mapping_abstract.md#alternative-2)

## Overview

### Description

[RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) maps data types of the abstract BDEF to DDIC partner types. If the DDIC partner type is a [flat structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) and only elementary data types are mapped, flat type mapping can be used. If the DDIC partner type is a [nested or deep structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md), deep mapping can be used. It defines a mapping for nested table components or substructures.

## Alternative 1

`mapping for PartnerType ...`

### Description

To map elements to flat DDIC structures, type mapping using the syntax `mapping for PartnerType` can be used. The syntax is the same as for [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and it is described in topic [RAP BDL - type mapping](abenbdl_type_mapping.md).

## Alternative 2

`deep mapping for NestedDeepDDICType ...`

### Description

In an abstract BDEF `with hierarchy`, mappings can be defined between the generated hierarchical derived types and nested or deep DDIC types. These mappings must be introduced with the keyword `deep`.

The optional addition `sub` can be used for `sub` specifications. Child entities with a composition cardinality \> 1 can be mapped to nested table components. If the composition cardinality is \<= 1, a mapping to a substructure can be defined.

Syntax for `sub` specification:

`sub _Compos1 = Partnersub1`

The left-hand side of a `sub` equation `sub _Compos1` contains the name of a composition association of the entity. The right-hand side contains the name of a component `PartnerComp1` of the nested or deep partner type `NestedDeepDDICType`. The components that are mapped onto each other must match, both must be either tables or structures. To cover the full hierarchical derived type, such a mapping must be defined for every entity in the abstract composition hierarchy and its corresponding partner type, with `sub` specifications for child entities at each level.

The optional addition `extensible` enables [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) for the type mapping in question. That means that [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) are allowed to add extension fields to that particular type mapping. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

Example: `deep mapping for NestedDeepDDICType corresponding extensible;`.

For details on extensibility enabling, see topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following abstract BDEF defines the behavior for three nodes of a CDS composition tree. For each entity, a mapping to a partner type is defined.

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_CDS_ABSTRACT_ROOT alias Root
{
  field ( suppress ) Dummy;

  deep mapping for DEMO_CDS_ABSTRACT_STRUC
  {
    char10 = char_10;
    Integer4 = integer_4;
    sub _itemStructure = struktur;
    sub _itemTable = tabelle;
  }

  association _itemTable;
  association _itemStructure;
}

define behavior for DEMO_CDS_ABSTRACT_ITEMSTRUCT alias ItemStructure
{
  field ( suppress ) Dummy, ToRoot;

  deep mapping for DEMO_ABSTRACT_ITEMSTRUCT
  {
    Char10 = char_10;
    Integer4 = integer_4;
  }

  association _parent;
}

define behavior for DEMO_CDS_ABSTRACT_ITEMTABLE alias ItemTable
{
  field ( suppress ) Dummy, ToRoot;

  deep mapping for DEMO_ABSTRACT_ITEMTABLE corresponding
  {
    Char10 = char_10;
    Integer4 = integer_4;
  }

  association _parent;
}
```

---
title: "RAP - Behavior Definition Header, Abstract BDEF"
source_file: abenbdl_bdef_abstract_header.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Behavior Definition Header, Abstract BDEF

## Syntax

``` abap
abstract; 
[strict[(version)];] 
[extensible;] 
[with hierarchy [like entity];] 
 entity behavior definition ...  
```

[`abstract;`](abenbdl_impl_type.md) · [`strict[(version)];`](abenbdl_strict.md) · [`extensible;`](abenbdl_extensible.md) · [`entity behavior definition`](abenbdl_define_beh_abstract.md)

## Description

The [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) of an [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) can define the attributes listed below. The [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) is mandatory; `strict[(version)]` and `with hierarchy` are strongly recommended for the following reasons: [strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) ensures that no outdated syntax can be used. When leaving out `with hierarchy`, the abstract BDEF represents the same [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) as a single [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) and does not offer any additional value.

- [`abstract`](abenbdl_impl_type.md): An abstract BDEF must have the [implementation type](abenbdl_impl_type.md) `abstract`.

- [`strict[(version)]`](abenbdl_strict.md): It is strongly recommended that the most recent version of [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) is used.

- [extensible](abenbdl_extensible.md): If specified, [BDEF extensions](abenbdl_extension.md) are allowed. As a prerequisite, [BDEF strict mode](abenbdl_strict.md) must be switched on using the keyword `extensible`. For more details, see the topic [RAP - `extensible`](abenbdl_extensible.md).

- `with hierarchy [like entity]`:

  - The optional addition `with hierarchy` causes the construction of a new kind of [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) for the entities that are part of the BDEF: starting from the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md), such a type contains all entity fields, plus a component for each [CDS composition](../../abap-glossary/abencds_composition_glosry.md). For a composition with a unique [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md), i.e. `TO ONE` or `TO EXACT ONE`, this component is a structure; otherwise, the component is a table. The type of the component (or its line type) is defined recursively in the same way, down to the [leaf level](../../abap-glossary/abenleaf_entity_glosry.md) in the [CDS composition hierarchy](../../abap-glossary/abencds_composition_tree_glosry.md).

  - The addition `like entity` can optionally be used in combination with `with hierarchy`. It guarantees that the hierarchical BDEF derived type that is constructed from the abstract BDEF is equivalent to the underlying CDS type that is derived from the abstract entity. The addition `with hierarchy like entity` enforces the following additional syntax rules:

    \- The abstract BDEF in question must not contain any [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) in its BDEF derived type. - The field attribute [`suppress`](abenbdl_field_abstract.md) is not allowed, as this would create a difference in BDEF derived types between the underlying abstract entity and the abstract BDEF. - The field attribute [`mandatory:execute`](abenbdl_field_abstract.md) is not allowed. - The optional addition [`with control`](abenbdl_define_beh_abstract.md) is not allowed.

The behavior definition header is followed by an [entity behavior definition](abenbdl_define_beh_abstract.md).

## Hints

- The addition `with hierarchy` is a precondition for the following components of an abstract BDEF:

  - [`with control`](abenbdl_define_beh_abstract.md)

  - [`deep mapping`](abenbdl_type_mapping_abstract.md)

  - [`scalar entity`](abenbdl_define_beh_abstract.md)

  - [`association _Assoc with hierarchy`](abenbdl_association_abstract.md)

- The addition `with hierarchy like entity` ensures that the derived type of the behavior definition is equivalent to the structure type of the underlying abstract entity. This ensures compatibility between the BDEF type and the CDS type. The advantage of the BDEF (over using the CDS type) is that it allows additional [type mappings](abenbdl_type_mapping_abstract.md) to be defined.

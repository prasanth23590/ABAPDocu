---
title: "DDIC DDL - DEFINE STRUCTURE, structure_annos"
source_file: abenddicddl_define_struct_props.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, structure_annos

## Syntax

``` abap
@EndUserText.label : '...' 
@AbapCatalog.enhancement.category : enh_cat  
```

## Description

Mandatory annotations for specifying structure properties in the definition of a DDIC structure using the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md).

- `@EndUserText.label` defines the [short text of the structure](abenddic_structures_sema.md) in its original language in quotation marks.

- `@AbapCatalog.enhancement.category` defines the [enhancement category of the structure](abenddic_structures_enh_cat.md). The following can be specified for `enh_cat`:

  - `#NOT_CLASSIFIED` - [Not classified](abenddic_structures_enh_cat.md)

  - `#NOT_EXTENSIBLE` - [Cannot be enhanced](abenddic_structures_enh_cat.md)

  - `#EXTENSIBLE_CHARACTER` - [Can be enhanced (character-like)](abenddic_structures_enh_cat.md)

  - `#EXTENSIBLE_CHARACTER_NUMERIC` - [Can be enhanced (character-like or numeric)](abenddic_structures_enh_cat.md)

  - `#EXTENSIBLE_ANY` - [Can be enhanced (deep)](abenddic_structures_enh_cat.md)

## Hints

- The specification `#NOT_CLASSIFIED` is only intended for displaying existing structures of this property. Any new or modified structures should always have an enhancement category.

- The syntax used to specify the properties is similar to [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). There are, however, no associated [annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md).

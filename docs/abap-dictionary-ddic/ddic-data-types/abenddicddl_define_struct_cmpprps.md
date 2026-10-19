---
title: "DDIC DDL - DEFINE STRUCTURE, component_annos"
source_file: abenddicddl_define_struct_cmpprps.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE > DDIC DDL - DEFINE STRUCTURE, component"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, component_annos

## Syntax

``` abap
[@EndUserText.label : '...'] 
[@AbapCatalog.decfloat.outputStyle : style ] 
[@AbapCatalog.textLanguage ] 
[@Semantics.amount.currencyCode : 'struct.comp'] 
[@Semantics.quantity.unitOfMeasure : 'struct.comp']  
```

## Description

Annotation for specifying optional properties of a [component](abenddicddl_define_struct_comps.md) in the definition of a DDIC structure using the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md).

- In quotation marks, `@EndUserText.label` defines the [short text of the component](abenddic_structures_sema.md) in the original language of the structure.

- `@AbapCatalog.decfloat.outputStyle` defines the [output style](../ddic-built-in-data-types/abenddic_decimal_floating_point.md) of a decimal floating point number. `style` can be specified as:

  - `#NORMAL` - default, mathematical or scientific, depending on space

  - `#SIGN_RIGHT`

  - `#SCALE_PRESERVING`

  - `#SCIENTIFIC`

  - `#SCIENTIFIC_WITH_LEADING_ZERO`

  - `#SCALE_PRESERVING_SCIENTIFIC`

  - `#ENGINEERING`

- `@AbapCatalog.textLanguage` - Flags a component of type `LANG` as text language

- `@Semantics.amount.currencyCode` - Definition of a [reference field](abenddic_structures_sema.md) for a [currency field](../ddic-built-in-data-types/abenddic_currency_field.md). A component `comp` with the built-in dictionary type `CUKY` from the same or from a different structure `struc` must be specified in quotation marks.

- `@Semantics.quantity.unitOfMeasure` - Definition of a [reference field](abenddic_structures_sema.md) for a [quantity field](../ddic-built-in-data-types/abenddic_quantity_field.md). A component `comp` with the built-in dictionary type `UNIT` from the same or from a different structure `struc` must be specified in quotation marks.

## Hint

The syntax used to specify the properties is based on [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). There are, however, no visible associated [annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of the component `weight_unit` as a reference field for the quantity field `weight` in the same structure.

``` abap
... 
define structure struct { 
  ... 
  @Semantics.quantity.unitOfMeasure : 'struct.weight_unit' 
  weight :      abap.quan(2); 
  weight_unit : abap.unit(2); 
  ... 
  }
```

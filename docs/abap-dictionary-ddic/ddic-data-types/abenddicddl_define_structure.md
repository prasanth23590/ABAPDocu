---
title: "DDIC DDL - DEFINE STRUCTURE"
source_file: abenddicddl_define_structure.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE

## Syntax

``` abap
structure_annos 
ext_annos 
DEFINE STRUCTURE struct { 
  ... 
  component; 
  ... 
  include; 
  ... 
 }  
```

[`structure_annos`](abenddicddl_define_struct_props.md) · [`ext_annos`](abenddicddl_define_ext_annos.md) · [`component;`](abenddicddl_define_struct_comps.md) · [`include;`](abenddicddl_define_struct_incl.md)

## Description

[Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement for defining an ABAP Dictionary [DDIC structure](abenddic_structures.md) `struct` in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md).

- A structure is defined using the statement `DEFINE STRUCTURE`. The name `struct` is subject to the [naming rules for DDIC data types](abenddic_types_names.md).

- [Annotations](../../abap-glossary/abenddic_annotation_glosry.md) [`structure_annos`](abenddicddl_define_struct_props.md) in front of the statement `DEFINE STRUCTURE` define the mandatory structure properties.

- Optionally, extensibility annotations [`ext_annos`](abenddicddl_define_ext_annos.md) can be specified in front of the statement `DEFINE STRUCTURE`. These annotations are a prerequisite for [C0 release](../../abap-glossary/abenc0_contract_glosry.md) of a DDIC structure.

- The structure components are defined in a semicolon-separated list in curly brackets `{ }` by one of the following methods:

  - Defining individual components [`component`](abenddicddl_define_struct_comps.md)

  - Including include structures [`include`](abenddicddl_define_struct_incl.md)

## Hints

- As in the [CDS syntax](../../abap-core-data-services-abap-cds/abap-cds-syntax/abencds_general_syntax_rules.md), an ABAP Dictionary structure definition can contain comments after `//` and between `/* ... */`.

- A more detailed description of the syntax is available in the `ADT` documentation [Syntax of ABAP Dictionary Objects](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/fc6cd6f7d02f4546a33feb3f5fc9dd66).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of the structure `DEMOFLI` in ADT.

``` abap
@EndUserText.label : 'Structure for ALV Demo'
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE
define structure demofli {

  fldate   : s_date;
  seatsmax : s_seatsmax;
  seatsocc : s_seatsocc;

}
```

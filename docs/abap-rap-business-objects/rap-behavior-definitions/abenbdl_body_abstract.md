---
title: "RAP - Entity Behavior Body, Abstract BDEF"
source_file: abenbdl_body_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions > RAP - Entity Behavior Definition, Abstract BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Entity Behavior Body, Abstract BDEF

## Syntax

``` abap
 
... {[field characteristics]; 
     [associations]; 
     [mapping];} 
...  
```

[`field characteristics`](abenbdl_field_abstract.md) · [`associations`](abenbdl_association_abstract.md) · [`mapping`](abenbdl_type_mapping_abstract.md)

## Description

In the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of an [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md), the following elements can be specified:

- [field characteristics](abenbdl_field_abstract.md): [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) are available to define field attributes for the fields of an abstract BDEF.

- [Associations](abenbdl_association_abstract.md) can be included in the hierarchical BDEF derived type.

- [Mapping](abenbdl_type_mapping_abstract.md): Data types of the abstract BDEF can be mapped to DDIC partner types. There are two possibilities: type mapping or deep mapping.

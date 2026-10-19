---
title: "CDS DDL - CDS View Entity, ROOT"
source_file: abencds_define_root_view_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, ROOT

## Syntax

``` abap
... ROOT ...  
```

## Description

The addition `ROOT` defines the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in question as the root entity of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). The [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) is the top node of the hierarchical structure of a business object and represents the business object.

The following applies to a root entity:

- There is exactly one root entity in the structure of a business object.

- A root entity does not have a [parent entity](../../abap-glossary/abenparent_entity_glosry.md).

- A root entity can specify [to-child associations](../../abap-glossary/abento_child_association_glosry.md) to [child entities](../../abap-glossary/abenchild_entity_glosry.md) of the business object using the keyword [`COMPOSITION`](abencds_composition_v2.md). This is not mandatory, a root node can also be a [leaf entity](../../abap-glossary/abenleaf_entity_glosry.md).

## Hints

- For more information about the ABAP RESTful Application Programming Model, see [ABAP RAP Business Objects](../../abap-rap-business-objects/abenabap_rap.md).

- The statement [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md) can add to a root entity but cannot turn a regular view entity into a root entity.

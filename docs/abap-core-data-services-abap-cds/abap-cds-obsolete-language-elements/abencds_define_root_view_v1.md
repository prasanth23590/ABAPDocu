---
title: "CDS DDL - DDIC-Based View, ROOT"
source_file: abencds_define_root_view_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, ROOT

## Syntax

``` abap
... ROOT ...  
```

## Description

The addition `ROOT` defines the CDS view `ddic_based_view` as the root entity of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). The [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) is the top node of the hierarchical structure of a business object and represents the business object.

The following applies to a root entity:

- There is exactly one root entity in the structure of a business object.

- The definition of a root entity can use [`COMPOSITION`](abencds_composition_v1.md) to specify [to-child associations](../../abap-glossary/abento_child_association_glosry.md) to [child entities](../../abap-glossary/abenchild_entity_glosry.md) of the business object.

- A root entity does not have a [parent entity](../../abap-glossary/abenparent_entity_glosry.md).

## Hints

- For more information about the ABAP RESTful Application Programming Model, see [ABAP RAP Business Objects](../../abap-rap-business-objects/abenabap_rap.md).

- The statement [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md) can add to a root entity but cannot make a regular view into a root entity.

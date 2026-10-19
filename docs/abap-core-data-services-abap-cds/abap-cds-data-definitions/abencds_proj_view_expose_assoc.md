---
title: "CDS DDL - expose_assoc, Transactional Query"
source_file: abencds_proj_view_expose_assoc.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - expose_assoc, Transactional Query

## Syntax

``` abap
 ... association[[filter]] [AS alias] [: redirection   ]
```

[`filter`](abencds_pv_assoc_modified.md) · [`redirection`](abencds_pv_assoc_redirected.md)

## Description

CDS associations from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) can be exposed in the projection list of a CDS projection view. Note that only an association from the projected entity can be exposed, path expressions are not valid to expose an association.

All elements included in the `ON` clause of an exposed [CDS association](../../abap-glossary/abencds_association_glosry.md) must also be included in the projection list of the CDS projection view.

The following additions are possible:

- [`filter`](abencds_pv_assoc_modified.md)

  An exposed association in a CDS projection view can be modified. That means that you can add a filter condition and in this way implicitly change the [cardinality](../../abap-glossary/abencardinality_glosry.md).

- `AS alias`

  The names of the elements of a `SELECT` list must be unique. There must be no other element with this name. If necessary, `AS` must be used to define an alternative element name `alias` for the CDS association. If no alternative element name `alias` is defined, the element name is defined by the name of the CDS association used in the path expression. When a CDS association with a [filter condition](abencds_pv_assoc_modified.md) `cds_cond` is exposed, an alternative element name `alias` using `AS` is mandatory.

- [`redirection`](abencds_pv_assoc_redirected.md)

  If the original [association target](../../abap-glossary/abenassociation_target_glosry.md) is also projected, you can redirect the association to the new target using the keyword `REDIRECTED TO`. Find details in the topic [CDS DDL - `projection_view`, `REDIRECTED TO`](abencds_pv_assoc_redirected.md) below.

A CDS association can be exposed multiple times with various alternative element names. This makes it possible to use different filter conditions.

An exposed CDS association is part of the projection list. It is not, however, part of the result set, nor a component of the type defined in ABAP with respect to the CDS projection view.

## Hints

- As alternative to exposing an association with a filter and redirection described in this topic, it is also possible to redefine an association on header level using the keyword [`REDEFINE ASSOCIATION`](abencds_proj_view_redefined_assoc.md). The filter and redirection is then automatically applied to all fields exposed via path expression.

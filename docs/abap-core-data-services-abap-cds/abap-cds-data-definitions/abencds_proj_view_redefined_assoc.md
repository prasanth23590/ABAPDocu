---
title: "CDS DDL - REDEFINE ASSOCIATION, Transactional Query"
source_file: abencds_proj_view_redefined_assoc.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - REDEFINE ASSOCIATION, Transactional Query

## Syntax

``` abap
 ... REDEFINE ASSOCIATION [source.]_ProjAssoc [filter] [AS _RedefinedName] redirection  ...  
```

[`filter`](abencds_pv_assoc_modified.md) · [`redirection`](abencds_pv_assoc_redirected.md)

## Description

A CDS association from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) can be redefined in the header part, that means in front of the projection list, of a CDS projection view. In this way, it is possible to modify an association from the underlying view. The modified association can be used locally and it can be exposed in the projection list for usage in, for example, [CDS view entity extensions](../../abap-glossary/abencds_view_entity_extend_glosry.md).

The syntax consists of the following elements:

- `_ProjAssoc`: the association from the projected entity which should be redefined must be identified by its original name. The [association source](../../abap-glossary/abenassociation_source_glosry.md) `source` can optionally be specified as prefix.

- [`filter`](abencds_pv_assoc_modified.md): A filter, consisting of a [filter condition](../../abap-glossary/abenfilter_condition_glosry.md) and, optionally, a [cardinality](../../abap-glossary/abencardinality_glosry.md), can be specified. See topic [CDS Projection View, filter](abencds_pv_assoc_modified.md) for details.

  The following rules apply in addition to the rules described in topic [CDS Projection View, filter](abencds_pv_assoc_modified.md):

  If the numeric syntax variant is used, the `min` cardinality can be 0 or 1. The `max` cardinality can be 1 or \*. The `min` and `max` cardinality of redefined to-parent redirects must not be changed.

- `AS alias`: A new alias name `AS alias` can be assigned.

- [`redirection`](abencds_pv_assoc_redirected.md): This addition is mandatory for redefined associations. As a prerequisite, the original [association target](../../abap-glossary/abenassociation_target_glosry.md) must also have a CDS projection view. Redirection using the keyword `REDIRECTED TO [...]` means to direct an association to a new association target, which is also a CDS projection view, in this way moving the complete data model to the projection layer.

  See topic [`CDS Projection View, redirection`](abencds_pv_assoc_redirected.md) for further details.

Exposure in the projection list:

- The redefined association can be exposed, but exposure is not mandatory, as it can also be done in [CDS view entity extensions](../../abap-glossary/abencds_view_entity_extend_glosry.md) later on.

- Even if an association has been redefined, it is still possible to expose the original association by using the source as prefix.

  Example:

  Expose redefined association: `_assoc`.

  Expose original association: `source._assoc`

- The redefined association can be used in [path expressions](abencds_proj_view_path_expr.md) to expose fields from the association target in the projection list. If a filter condition was added to the redefined association in the header, this is automatically applied to all fields exposed via a path expression.

- A new alias name can be assigned when exposing a redefined association, even if an alias has already been defined in the context of the redefinition.

- A new filter condition with a new cardinality can be specified when exposing a redefined association, even if a filter condition with a cardinality has already been defined in the context of the redefinition. In this case, a new alias name is mandatory.

All elements included in the `ON` clause of an exposed redefined association must also be included in the projection list.

Limitations

- It is not possible to redefine [locally defined associations](abencds_proj_view_association.md).

- `_ProjAssoc` cannot be specified as path expression.

## Hints

- As alternative to the redefinition described in this topic, a filter condition and redirection can also be specified in the projection list when exposing the association. See topic [CDS Projection View, `expose_assoc`](abencds_proj_view_expose_assoc.md) for details.

- The syntax described in this topic can also be used in a CDS view entity extension using [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md).

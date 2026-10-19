---
title: "AbapCatalog.viewEnhancementCategory"
source_file: abencds_801468554-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.viewEnhancementCategory

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.viewEnhancementCategory[ ]`                      |
| **Scope**   | `#VIEW`                                                       |
| **Type**    | `String(20)`                                                  |
| **Enums**   | `#GROUP_BY, #NONE, #PROJECTION_LIST, #UNION`                  |
| **Default** | `-`                                                           |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## viewEnhancementCategory

Specifies how a CDS object can be extended using CDS object extensions. A comma-separated list of values can be specified in the square brackets of the annotation array.

If the annotation is not sepecified, the value \#PROJECTION_LIST is used.

## Enums

## \#NONE

No extensions allowed. Cannot be specified together with other values.

## \#PROJECTION_LIST

## In CDS View Entities

Extensions of the SELECT list and additional CDS associations are allowed. Extensions of CDS views whose SELECT lists contain aggregate expressions or which contain a set operator clause (UNION, INTERSECT, EXCEPT) are not allowed.

## In CDS Projection Views

Extensions of the SELECT list and additional CDS associations are allowed; extensions of CDS views whose SELECT lists contain aggregate expressions or have a UNION clause must be allowed using further values

## \#GROUP_BY

Can only be specified together with \#PROJECTION_LIST. Allows views to be extended that have aggregate expressions in the SELECT list. Aggregated or non-aggregated elements can be added to the SELECT list by the extension. The GROUP-BY clause must be extended accordingly using the addition GROUP BY.

## \#UNION

Can only be specified together with \#PROJECTION_LIST. Allows views to be extended that use a clause with a set operator (UNION, INTERSECT, EXCEPT).

## Further Information

- The annotation`AbapCatalog.viewEnhancementCategory` specifies how a CDS view can be extended. `AbapCatalog.viewEnhancementCategory` and `AbapCatalog.extensibility.extensible` can optionally be specified together in the same CDS view. In this case, the annotation values must fit to each other. They must both either allow or forbid extensions.

- In the [annotation array](../../abap-glossary/abenannotation_array_glosry.md) `AbapCatalog.viewEnhancementCategory[ ]`, `#GROUP_BY` and `#UNION` can only be specified together with the default value `#PROJECTION_LIST`. The value `#NONE` excludes any other values.

- `AbapCatalog.viewEnhancementCategory[#NONE]` is mandatory for views that contain an element of data type `LRAW` or `LCHR`. The reason is that elements of data type `LRAW` or `LCHR` must always be in the last position in the `SELECT` list and therefore, no extensions are allowed.

- Extensions of a view with aggregate expressions or with a set operator clause ([`EXCEPT`](../abap-cds-data-definitions/abencds_except_v2.md), [`INTERSECT`](../abap-cds-data-definitions/abencds_intersect_v2.md), or [`UNION`](../abap-cds-data-definitions/abencds_union_v2.md)) modify the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the result set. This means that these extensions must have special permission in the view to enable consumers of the view to handle any changes to cardinalities.

- ` AbapCatalog.viewEnhancementCategory[#UNION]` allows extensions not only for union views, but for views including any set operator (also [`EXCEPT`](../abap-cds-data-definitions/abencds_except_v2.md) and [`INTERSECT`](../abap-cds-data-definitions/abencds_intersect_v2.md)). The annotation array value `#UNION` is a known misnomer.

---
title: "Analytics.settings.dataRetrieval"
source_file: abencds_1374018734_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.dataRetrieval

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.dataRetrieval`                                 |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `#ALL_AT_ONCE, #ON_HIERARCHY_DRILLDOWN, #ON_NAVIGATION`            |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## dataRetrieval

This annotation enables Analytical Engine to read data from the data base with different detailed levels when a user runs an analytical CDS query.

For example, when a CDS analytical query with active hierarchy is executed, data is retrieved at leaf level or at node level. This can impact the query performance in different navigation steps when a huge amount of data is selected. If the data is retrieved with all the details at leaf level and stored in the memory, the initial query result will take longer time, but open hierarchy nodes will be fast. If the data is retrieved at node level, the initial query result is faster, additional data is read from DB when expanding a hierarchy node. The annotation provides user the flexibility to choose a data retrieval mode which fits to the application requirement.

This annotation can be set in analytical Provider View ( Analytics.Datacategory \#CUBE or Analytics.Datacategory \#DIMENSION ) or analytical Query View ( Analytics.Query: true or Projection View with provider contract analytical query ). The setting in the query view overwrites the setting in the provider view. When it is not set in a CDS analytical query view, the setting in the CDS provider view takes effect.

Without this annotation, by default the dataRetrieval = \#ON_HIERARCHY_DRILLDOWN.

## Enums

## \#ALL_AT_ONCE

When run a CDS analytical query, the data required for all possible navigation steps for this query is read in one go. When navigating further (add more drill down, expanding hierarchy, etc), all new navigation statuses are aggregated and calculated from the main memory data.

No further data is read from the data base .

This corresponds to ReadMode = A in Analytical Engine.

Note: `@Analytics.settings.dataRetrieval`: \#ALL_AT_ONCE can't be used together with `@Analytics.settings.olapPushdown`: \#MAX

## \#ON_NAVIGATION

When run a CDS analytical query, at the beginning only data for necessary fields for the initial query result are selected from DB. When a field has hierarchy active, all values for the whole hierarchy tree are selected. In this way, the query is open faster. Later if additional drill down is added, a new data read will be triggered.

This corresponds to ReadMode = X in Analytical Engine.

## \#ON_HIERARCHY_DRILLDOWN

When run a CDS analytical query, at the beginning the smallest data necessary for initial query result are selected from DB. When a hierarchy is active on the field, only the aggregated value to the node level is read. Later when add a new drill down, or expand a hierarchy node, a new data read is triggered.

This corresponds to ReadMode = H in Analytical Engine.

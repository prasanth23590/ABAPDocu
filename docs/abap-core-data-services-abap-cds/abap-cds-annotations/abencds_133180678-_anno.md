---
title: "UI.chart.chartType"
source_file: abencds_133180678-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.chart.chartType

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `UI.chart[ ].chartType`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Scope**   | `#ENTITY`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Type**    | `String(40)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Enums**   | `#AREA, #AREA_STACKED, #AREA_STACKED_100, #BAR, #BAR_DUAL, #BAR_STACKED, #BAR_STACKED_100, #BAR_STACKED_DUAL, #BAR_STACKED_DUAL_100, #BUBBLE, #BULLET, #COLUMN, #COLUMN_DUAL, #COLUMN_STACKED, #COLUMN_STACKED_100, #COLUMN_STACKED_DUAL, #COLUMN_STACKED_DUAL_100, #COMBINATION, #COMBINATION_DUAL, #COMBINATION_STACKED, #COMBINATION_STACKED_DUAL, #DONUT, #DONUT_100, #HEAT_MAP, #HORIZONTAL_AREA, #HORIZONTAL_AREA_STACKED, #HORIZONTAL_AREA_STACKED_100, #HORIZONTAL_COMBINATION_DUAL, #HORIZONTAL_COMBINATION_STACKED, #HORIZONTAL_COMBINATION_STACKED_DUAL, #HORIZONTAL_WATERFALL, #LINE, #LINE_DUAL, #PIE, #RADAR, #SCATTER, #TREE_MAP, #VERTICAL_BULLET, #WATERFALL` |
| **Default** | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Text**    | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **MDE**     | `X`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## chart

### Short Description

Annotations belonging to UI.chart are used to show a visual representation of aggregated data.

Evaluation Runtime (Engine): SADL: Translates CDS annotations into the corresponding OData annotations

### More Information

[Micro Chart Facet](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#micro-chart-facet)

## chartType

### Short Description

This annotation specifies the type of graphical representation most appropriate for the data in the annotated view or entity.

### Use case

You want to display specific types of charts.

## Enums

## \#COLUMN

### Short Description

This annotation specifies the type of graphical representation as a column chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

## \#COLUMN_STACKED

### Short Description

This annotation specifies the type of graphical representation as a column chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. These values are stacked.

## \#COLUMN_STACKED_100

### Short Description

This annotation specifies the type of graphical representation as a 100% stacked column chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

## \#COLUMN_DUAL

## \#COLUMN_STACKED_DUAL

## \#COLUMN_STACKED_DUAL_100

## \#BAR

### Short Description

This annotation specifies the type of graphical representation as a bar chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

## \#BAR_STACKED

### Short Description

This annotation specifies the type of graphical representation as a bar chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. These values are stacked.

## \#BAR_STACKED_100

### Short Description

This annotation specifies the type of graphical representation as a 100% stacked bar chart. This type of graph presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

## \#BAR_DUAL

## \#BAR_STACKED_DUAL

## \#BAR_STACKED_DUAL_100

## \#AREA

### Short Description

This annotation specifies the type of graphical representation as an area chart. This type of graph presents graphically quantitive data emphasized through colors, textures and hatchings.

## \#AREA_STACKED

### Short Description

This annotation specifies the type of graphical representation as an stacked area chart. This type of graph presents graphically quantitive data emphasized through colors, textures and hatchings.

## \#AREA_STACKED_100

### Short Description

This annotation specifies the type of graphical representation as an 100% stacked area chart. This type of graph presents graphically quantitive data emphasized through colors, textures and hatchings.

## \#HORIZONTAL_AREA

### Short Description

This annotation represents one dimension on the y-axis, and one or more measures on the x-axis ("horizontal bar").

## \#HORIZONTAL_AREA_STACKED

### Short Description

This annotation represents one dimension on the y-axis, and one or more measures on the x-axis ("horizontal bar"). The values within are stacked.

## \#HORIZONTAL_AREA_STACKED_100

### Short Description

This annotation represents one dimension on the y-axis, and one or more measures on the x-axis ("horizontal bar"). The values within are 100% stacked.

## \#LINE

### Short Description

This annotation specifies the type of graphical representation as a line chart. This type of graph presents a series of data points connected by straight line segments.

## \#LINE_DUAL

## \#COMBINATION

## \#COMBINATION_DUAL

## \#COMBINATION_STACKED

## \#COMBINATION_STACKED_DUAL

## \#HORIZONTAL_COMBINATION_STACKED

## \#HORIZONTAL_COMBINATION_STACKED_DUAL

## \#PIE

### Short Description

This annotation specifies the type of graphical representation as a pie chart. This type of graph presents data in a circular statistical graphic which is divided into slices demonstrating its numerical proportions.

## \#DONUT

### Short Description

This annotation specifies the type of graphical representation as a donut chart. The visualization is similar to a pie chart, with an empty middle section.

## \#SCATTER

### Short Description

This annotation specifies the type of graphical representation as a scatter chart.

This type of graph has one dimension for x-axis, one measure for y-axis. Data is displayed as a collection of points, having the value of one variable determining the position on the horizontal axis and another determining the position on the vertical axis.

## \#BUBBLE

### Short Description

This annotation specifies the type of graphical representation as a bubble chart.

This type of graph displays three dimensions of data.

## \#RADAR

### Short Description

This annotation specifies the type of graphical representation as a radar chart.

This type of graph has three or more dimensions for the axes of the spider web.

## \#HEAT_MAP

### Short Description

This annotation specifies the type of graphical representation as a heat map chart.

This type of graph has two dimensions for x- and y-axis, one measure mapped into a color code

## \#TREE_MAP

### Short Description

This annotation specifies the type of graphical representation as a tree map chart.

This type of graph has one or more hierarchical dimensions, one measure for the rectangle size, optional second measure mapped into color code.

## \#WATERFALL

### Short Description

This annotation specifies the type of graphical representation as a waterfall chart.

This type of graph has one dimension for x-axis, one measure for y-axis.

## \#BULLET

### Short Description

This annotation specifies the type of graphical representation as a bullet chart.

This type of graph has one dimension for x-axis, one measure for y-axis. It is a variation of the bar graph.

## \#VERTICAL_BULLET

## \#HORIZONTAL_WATERFALL

## \#HORIZONTAL_COMBINATION_DUAL

## \#DONUT_100

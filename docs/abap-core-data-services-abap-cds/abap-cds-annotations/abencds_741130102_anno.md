---
title: "Aggregation.default"
source_file: abencds_741130102_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Aggregation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Aggregation.default

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)               |
|-------------|------------------------------------------------------------------|
| **Syntax**  | `Aggregation.default`                                            |
| **Scope**   | `#ELEMENT`                                                       |
| **Type**    | `String(30)`                                                     |
| **Enums**   | `#AVG, #COUNT_DISTINCT, #FORMULA, #MAX, #MIN, #NONE, #NOP, #SUM` |
| **Default** | `-`                                                              |
| **Text**    | `-`                                                              |
| **MDE**     | `-`                                                              |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`    |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Aggregation

## default

Specifies a measure element in an analytical scenario.

Measures are elements with numerical values that can be aggregated in analytical scenarios.

All other elements in the CDS entity that are not annotated with this annotation are dimensions, which provide structured labeling information about the numeric measures.

As soon as one element in a CDS entity is annotated with this annotation, the CDS entity is considered an analytical entity.

**Use all values for this annotation only for fields of numeric and date type. This is only allowed in views with dataCategory: \#CUBE, \#FACT, \#DIMENSION: Aggregation should not be used for all character like fields**

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

## Value

The following values are only available for analytic manager

- NOP

- FORMULA

## Required Annotations

The following values can only be used with other required annotations

- AVG

The analytic manager allows AVG only together with Aggregation.referenceElement and exactly one element in this list. `Aggregation: { default: #AVG , referenceElement: <element> }` behaves like `Aggregation: { default: #SUM, exception: #AVG , referenceElement: <element> }`

- COUNT_DISTINCT

The analytic manager allows COUNT only together with Aggregation.referenceElement and exactly one element in this list. behaves like `Aggregation: { default: #SUM, exception: #COUNT_DISTINCT , referenceElement: <element> }`

- FORMULA

This value can only be used with Analytics.query:true

### More Information

<https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#chart>

### Enums

### \#NONE

*not evaluated by SADL*

*Analytical Engine*

This value indicates that the element is not a measure. Usually these elements are used in filters and GROUP BY statements.

### \#SUM

This enumeration value is used for elements whose sum is displayed on the analytical UI.

/

Use this enumeration value ... whose sum should be displayed/ you want to display ...

Only elements with numerical data types can be annotated with this annotation.

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

### \#MIN

This enumeration value is used for elements whose lowest value is displayed on the analytical UI.

Only elements with numerical data types or date types can be annotated with this annotation.

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

### \#MAX

This enumeration value is used for elements whose highest value is displayed on the analytical UI.

Only elements with numerical data types or date types can be annotated with this annotation.

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

### \#AVG

This enumeration value is used for elements whose average value is displayed on the analytical UI.

Only elements with numerical data types can be annotated with this annotation.

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

The analytic manager allows AVG only together with Aggregation.referenceElement and exactly one element in this list. `Aggregation: { default: #AVG , referenceElement: <element> }` behaves like `Aggregation: { default: #SUM, exception: #AVG , referenceElement: <element> }`

### \#COUNT_DISTINCT

This enumeration value is used for elements whose distinct value are counted and displayed on the analytical UI.

In combination with the annotation @Aggregation.ReferenceElement: \['elementRef'\], you can count the number of distinct values of another element that is referenced.

### \#NOP

*not evaluated by SADL*

NOP returns a value if all values are equal. Otherwise, it returns a special error value. It is the default in views with and dataCategory: \#CUBE, \#FACT,#DIMENSION if the data type of the element is numeric.

### \#FORMULA

*not evaluated by SADL*

*Analytical Engine*

The value FORMULA indicates that the element is a formula. This has to be calculated after the operands have been determined by aggregation or calculation. It should never be aggregated.

Note that it can only be used in views with Analytics.query: true.

Example:

Margin : = Revenue / Cost. If Margin should be shown per OrgUnit in a report, the aggregates of Revenue and Cost have to be determined per OrgUnit first, and then the Margin has to be calculated per OrgUnit.

### Further Information

- The annotation `Aggregation.default` replaces the obsolete annotation `DefaultAggregation`.

- This annotation is evaluated by both [SADL](../../abap-glossary/abensadl_glosry.md) and analytic manager.

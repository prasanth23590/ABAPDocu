---
title: "Aggregation.exception"
source_file: abencds_1540548770_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Aggregation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Aggregation.exception

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                              |
|-------------|-----------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `Aggregation.exception`                                                                                         |
| **Scope**   | `#ELEMENT`                                                                                                      |
| **Type**    | `String(30)`                                                                                                    |
| **Enums**   | `#AVG, #COUNT, #COUNT_DISTINCT, #FIRST, #LAST, #MAX, #MEDIAN, #MIN, #NHA, #STANDARD_DEVIATION, #SUM, #VARIANCE` |
| **Default** | `-`                                                                                                             |
| **Text**    | `-`                                                                                                             |
| **MDE**     | `-`                                                                                                             |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                   |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Aggregation

## exception

*not evaluated by SADL*

*Analytical Engine*:

Exception aggregation is always performed in addition to default aggregation, which must not be be equal to \#NONE. This is not an alternative to default aggregation. This means that data is first aggregated through the default aggregation grouped by the reference elements, and then aggregated with the exception aggregation.

Note

If you want to use Aggregation.exception, you have to define Aggregation.default (not equal to NONE) and Aggregation.referenceElement in order to define the granularity with which the aggregation rule is applied.

## Value

The following values determine the aggregation of teh measure in the same way as in Aggregation.default

- SUM

- MAX

- MIN

- AVG

- COUNT

- COUNT_I

### Enums

### \#SUM

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#MIN

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#MAX

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#AVG

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#COUNT

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#COUNT_DISTINCT

*Analytical Engine*

This value determines the aggregation of the measure in the same way as SUM, MAX, MIN, AVG, COUNT, COUNT_DISTINCT in Aggregation.default.

### \#FIRST

*Analytical Engine*

This value indicates that the first value in relation to the reference characteristic is shown in the result line.

### \#LAST

*Analytical Engine*

This value indicates that the last value in relation to the reference characteristic is shown in the result line.

### \#STANDARD_DEVIATION

*Analytical Engine*

This value indicates that, after aggregating with the reference characteristic, the standard deviation of the calculated values is shown in the results row.

### \#VARIANCE

*Analytical Engine*

This value indicates that, after aggregating with the reference characteristic, the variance of the calculated values is shown in the results row.

### \#MEDIAN

*Analytical Engine*

This value indicates that the middle value (central value) of a set sorted in ascending order is calculated:

For a set with an uneven number of elements, the result is the middle value.

Example 1:

For a set of five elements, the result is the value of the third element. Suppose you have the following values: 1, 12, 2, 4, 24. When the values are sorted in ascending order (1, 2, 4, 12, 24), the median is the third middle value, which is 4.

For a set with an even number of elements, the result is the average of the two middle values.

Example 2:

For a set of six elements, the result is the average of the third and fourth elements. Suppose you have the following values: 1, 12, 2, 4, 24, 6. When the values are sorted in ascending order (1, 2, 4, 6, 12, 24), the median is the average of the values 4 and 6, which is 5.

### \#NHA

*Analytical Engine*

No aggregation along the hierarchy. This value ensures that nodes with a postable value part, and which only aggregate the values of their children, are calculated as NULL. This means they have no value if they are not postable nodes.

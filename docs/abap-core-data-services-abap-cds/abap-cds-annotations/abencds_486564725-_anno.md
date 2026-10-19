---
title: "ObjectModel.unitConversionRate.association"
source_file: abencds_486564725-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.unitConversionRate.association

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.unitConversionRate.association`                       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `AssociationRef`                                                   |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## unitConversionRate

### Short Description

This annotation and the related modeling pattern resemble the pattern for language-dependent texts: The annotation `@ObjectModel.text.association` at the dimension key leads to a unique entity with supported capability LANGUAGE_DEPENDENT_TEXT, which is then used at runtime to lookup the text.

### Use Case

The Analytic Engine supports unit conversion with dimension-specific rates. Overall the entities containing unit conversion rates can be found via the corresponding supported capability (see \[2023-08-01\] `@ObjectModel`.\[modelingPattern\|supportedCapabilities\]: \#UNIT_CONVERSION_RATE).

However, in an Analytical Dimension (i.e. an entity with the capability ANALYTICAL_DIMENSION), maximum one entity can be used for the dimension-specific unit conversion.

For a simple and explicit declaration of this relation, the dimension entity shall contain an association to the applicable unit conversion rate entity, and the representative key element of the dimension shall be annotated with the appropriate association.

The annotation then serves two purposes: (1) indicate that dimension-specific unit conversion rates shall be supported at runtime, (2) find the (unique) entity to look up the unit conversion rates (which is the target of the unitConversionRate.association).

## association

### Short Description

The annotated association leads to a target entity which contains unit conversion rates. In an Analytical Dimension the annotation indicates that these rates shall be used to offer dimension-specific unit conversion in analytical queries at runtime.

### Constraints

The target entity of the annotated association must support the capability UNIT_CONVERSION_RATE. All keys of the (source) entity must be mapped to keys of the target entity in the on-condition of the association.

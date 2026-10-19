---
title: "Semantics.largeObject.acceptableMimeTypes"
source_file: abencds_514907485_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.largeObject.acceptableMimeTypes

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Semantics.largeObject.acceptableMimeTypes[ ]`                     |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(255)`                                                      |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Semantics

Semantic annotations complement the concept of semantic data types, while semantic data types always introduce specific behavior in the provider/core infrastructure (through dedicated operations or conversion functions).

Semantic annotations allow the standardizing of semantics that only have an impact on the consumption side (such as currency code representation together with the amount).

Evaluation Runtime (Engine): Interpreted by the RAP runtime engine (SADL): Translates CDS annotations into the corresponding OData annotations.

## largeObject

### Short Description

You can enable your RAP application for maintaining large objects (LOBs). By doing so, you provide end users the option to incorporate external binary files or text files when editing entity instances. First the appropriate fields should be added into the database table and the CDS view, and also the annotations `@Semantics.largeObject` and `@Semantics.mimeType`. To show it in a table, you will need annotation `@UI.lineItem`. Lastly, you should also update the mapping and the draft table in your behaviour definition.

### More Information

[Adding Large Object/Stream Property to a Table](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#adding-large-objectstream-property-to-a-table)

## acceptableMimeTypes

### Short Description

Provides a list of acceptable mime types for the related stream property to restrict or verify the user entry accordingly. If any subtype is accepted, this can be indicated by .

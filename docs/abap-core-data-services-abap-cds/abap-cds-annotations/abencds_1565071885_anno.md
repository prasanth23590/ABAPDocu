---
title: "UI.connectedFields.label"
source_file: abencds_1565071885_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.connectedFields.label

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `UI.connectedFields[ ].label`                                      |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(60)`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `X`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## connectedFields

### Short Description

Connected fields have a read-only representation that resembles a single field value, only on edit they are visually disassembled into several input controls.

Connected fields can appear in forms and tables. A set of connected fields is identified by its qualifier and can be referenced in data fields for annotation similar to data points and charts.

Its language-dependent template specifies how to render the connected fields. The template consists of placeholders for values (must be valid OData simple identifiers - think: variable names) enclosed in curly braces, plus printable characters and white-space outside of the curly braces. The example template {rate}% ({amount}) consists of two placeholders rate and amount. The value to be inserted for rate will be followed by a percent sign, the value to be inserted for amount will be enclosed in parentheses. Note that the ""values"" to be inserted are themselves data fields and thus can have advanced formatting, here a currency amount with currency for amount. Other possibilities include micro-charts and data points, making this rather powerful.

The first occurrence of groupLabel for a given qualifier wins, same for template. Other occurrences for the same qualifier are redundant and should be avoided.

### More Infomation

<https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#connected-fields>

## label

### Short Description

This annotation contains a language-dependent text that can be used for column titles in tables headers.

If omitted, the label of the annotated element, or the label of the element referenced via the value is used.

### Use case

You want to create human readable labels for data fields so you add a label annotation for `@UI.connectedFields`.

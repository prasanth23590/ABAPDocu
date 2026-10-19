---
title: "Workflow.enabledFor"
source_file: abencds_1985209549_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Workflow"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Workflow.enabledFor

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Workflow.enabledFor[ ]`                                           |
| **Scope**   | `#VIEW`                                                            |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `#CUSTOM_TASK_ATTRIBUTES, #RESPONSIBILITY_MANAGEMENT`              |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Workflow

## Short Description

The @Workflow annotation is designed to configure the linkage between a CDS view and a business object within SAP Workflow Management. It facilitates the integration of workflow components by specifying areas where the CDS view can be utilized.

## Required Annotations

- `@ObjectModel.sapObjectNodeType.name`: Specifies the name of the SAP Object Node Type for the workflow.

### enabledFor

Contains areas within the workflow component, where this CDS view can be used

### Enums

### \#RESPONSIBILITY_MANAGEMENT

Usage in Responsibility Management (REM)

### \#CUSTOM_TASK_ATTRIBUTES

CDS entities annotated with this annotation become available for selection in configuration UIs where custom task attributes are defined.

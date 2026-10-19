---
title: "AccessControl.auditing.specification"
source_file: abencds_956586857-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AccessControl"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AccessControl.auditing.specification

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AccessControl.auditing.specification`                             |
| **Scope**   | `#TABLE_ENTITY`, `#VIEW`                                           |
| **Type**    | `String(1000)`                                                     |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AccessControl

Defines access control for a CDS object.

## auditing

A CDS entity (in the following called aspect entity) used as data source by a self defined aspect must have set this annotation.

The content of the aspect entity has a particular relevance for audits by being used in a self defined aspect in access control.

To determine which user had access to particular data at a particular time in a system, it must be possible to reconstruct the state of the data of the aspect entity. Existing mechanisms (such as version management or change documents) cover this requirement in the case of development objects or PFCG roles. Aspect entities do not specify their data sources and whether these sources are themselves auditable.

The development and runtime systems for CDS access control cannot check whether data sources are auditable. To highlight this requirement, however, the aspect entity must have set the following annotations:

`@AccessControl.auditing.type`

`@AccessControl.auditing.specification`

If auditing cannot be ensured, the CDS entity cannot be used in a self defined aspect.

## specification

Specifies (as text) how the content of the aspect entity is audited.

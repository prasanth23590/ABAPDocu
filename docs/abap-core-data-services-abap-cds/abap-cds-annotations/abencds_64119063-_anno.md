---
title: "AccessControl.authorizationCheckMandatory"
source_file: abencds_64119063-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AccessControl"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AccessControl.authorizationCheckMandatory

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)            |
|-------------|-------------------------------------------------------------------------------|
| **Syntax**  | `AccessControl.authorizationCheckMandatory[ ]`                                |
| **Scope**   | `#EXTERNAL_ENTITY`, `#HIERARCHY`, `#TABLE_ENTITY`, `#TABLE_FUNCTION`, `#VIEW` |
| **Type**    | `String(20)`                                                                  |
| **Enums**   | `#DELETE, #INSERT, #SELECT, #UPDATE`                                          |
| **Default** | `-`                                                                           |
| **Text**    | `-`                                                                           |
| **MDE**     | `-`                                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                 |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AccessControl

Defines access control for a CDS object.

## authorizationCheckMandatory

For the operations specified in the annotation, access control is enforced at runtime. For operations that are not specified, access control is disabled, with the exception of the SELECT operation. In the case of the SELECT operation, the system falls back to the value stored in the '`@AccessControl.authorizationCheck`' annotation.

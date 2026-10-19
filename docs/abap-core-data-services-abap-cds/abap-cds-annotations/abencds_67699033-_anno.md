---
title: "AbapCatalog.dataMaintenance"
source_file: abencds_67699033-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.dataMaintenance

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.dataMaintenance`                                 |
| **Scope**   | `#HIERARCHY`, `#TABLE_FUNCTION`, `#VIEW`                      |
| **Type**    | `String(20)`                                                  |
| **Enums**   | `#ALLOWED, #DISPLAY_ONLY, #NOT_ALLOWED, #RESTRICTED`          |
| **Default** | `#RESTRICTED`                                                 |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## dataMaintenance

Can be used to restrict data preview for a CDS object by specifying one of the allowed Enum values.

If the annotation is not specified, the value \#RESTRICTED is used.

## Enums

## \#ALLOWED

Data preview is allowed.

## \#NOT_ALLOWED

Data preview not allowed.

## \#RESTRICTED

Data preview allowed with restrictions.

## \#DISPLAY_ONLY

Data preview is allowed as display only.

## Further Information

The annotation `AbapCatalog.dataMaintenance` defines whether the CDS object can be displayed or maintained by certain tools such as Data Preview in [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). The annotation is evaluated by these tools. Restrictions imposed by that annotation are user-independent and they are evaluated before accessing the data. Additional restrictions imposed by [CDS roles](../../abap-glossary/abencds_role_glosry.md) are evaluated during the actual data access, if this is done by ABAP SQL.

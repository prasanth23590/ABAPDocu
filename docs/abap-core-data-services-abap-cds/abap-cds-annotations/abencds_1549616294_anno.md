---
title: "ClientHandling.clientSafe"
source_file: abencds_1549616294_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ClientHandling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ClientHandling.clientSafe

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `ClientHandling.clientSafe`                                   |
| **Scope**   | `#HIERARCHY`, `#TABLE_FUNCTION`, `#VIEW`                      |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ClientHandling

Specifies the client handling of certain CDS objects.

## Note

An annotation `@ClientHandling` cannot be specified together with the obsolete annotation `@ClientDependent`.

## clientSafe

Enables or disables client safety checks for a CDS object.

Annotation Values

true: Client safety is ensured by stricter checks.

false: Client safety is not ensured.

If the annotation is not specified, the value false is used.

## Further Information

For more information about [client safe](../../abap-glossary/abenclient_safe_glosry.md) CDS entities, refer to:

- [Client Safety of CDS View Entities](../abap-cds-data-definitions/abencds_v2_view_client_safety.md)

- [Client Safety of CDS Table Functions](../abap-cds-data-definitions/abencds_func_client_safety.md)

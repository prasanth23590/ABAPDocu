---
title: "ClientHandling.algorithm"
source_file: abencds_1114072352_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ClientHandling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ClientHandling.algorithm

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `ClientHandling.algorithm`                                    |
| **Scope**   | `#TABLE_FUNCTION`, `#VIEW`                                    |
| **Type**    | `String(20)`                                                  |
| **Enums**   | `#AUTOMATED, #NONE, #SESSION_VARIABLE`                        |
| **Default** | `-`                                                           |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ClientHandling

Specifies the client handling of certain CDS objects.

## Note

An annotation `@ClientHandling` cannot be specified together with the obsolete annotation `@ClientDependent`.

## algorithm

Defines client handling when ABAP SQL is used to access the CDS object.

If the annotation is not specified, the value \#AUTOMATED is used for CDS views and the value \#NONE is used for CDS table functions.

## Enums

## \#NONE

No implicit client handling takes place

## \#AUTOMATED

The joins of the CDS object are modified implicitly.

## \#SESSION_VARIABLE

The joins of the CDS object are modified implicitly and the session variable \$session.client is used implicitly to improve performance.

## Further Information

- For more information about client handling in CDS DDIC-based views, refer to [Client Handling in CDS DDIC-based views](../abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md).

- For more information about client handling in CDS table functions, refer to [Client Handling in CDS Table Functions](../abap-cds-data-definitions/abencds_func_client_handling.md).

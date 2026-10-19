---
title: "ClientHandling.type"
source_file: abencds_613831553_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ClientHandling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ClientHandling.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `ClientHandling.type`                                         |
| **Scope**   | `#TABLE_ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                   |
| **Type**    | `String(20)`                                                  |
| **Enums**   | `#CLIENT_DEPENDENT, #CLIENT_INDEPENDENT, #INHERITED`          |
| **Default** | `#INHERITED`                                                  |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ClientHandling

Specifies the client handling of certain CDS objects.

## Note

An annotation `@ClientHandling` cannot be specified together with the obsolete annotation `@ClientDependent`.

## type

Defines the client dependency when ABAP SQL is used to access the CDS object.

If the annotation is not specified, the value \#CLIENT_DEPENDENT is used.

## Enums

## \#CLIENT_DEPENDENT

The CDS object is client-dependent. When accessed using ABAP SQL SELECT, implicit client handling is applied.

## \#CLIENT_INDEPENDENT

The CDS object is client-independent. No implicit client handling is applied.

## \#INHERITED

The client dependency of the CDS object is determined by the data sources used. If a data source is client-dependent, the CDS object is too.

## Further Information

- For more information about client handling in CDS DDIC-based views, refer to [Client Handling in CDS DDIC-based views](../abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md).

- For more information about client handling in CDS table functions, refer to [Client Handling in CDS Table Functions](../abap-cds-data-definitions/abencds_func_client_handling.md).

- For more information about client handling in CDS hierarchies, refer to [Client Handling in CDS Hierarchies](../abap-cds-data-definitions/abencds_hiera_client_handling.md).

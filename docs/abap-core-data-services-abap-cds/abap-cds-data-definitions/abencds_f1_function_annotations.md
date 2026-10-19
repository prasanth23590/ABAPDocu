---
title: "CDS DDL - DEFINE TABLE FUNCTION, function_annot"
source_file: abencds_f1_function_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > CDS DDL - DEFINE TABLE FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE FUNCTION, function_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) in front of the statement [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md) as a function notation. The character `@` must be placed in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#TABLE_FUNCTION`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.dataMaintenance`](../abap-cds-annotations/abencds_67699033-_anno.md)

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

- ClientHandling Annotations

  - [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md)

  - [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md)

  - [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md)

- ObjectModel Annotations

  - [`ObjectModel.usageType.dataClass`](../abap-cds-annotations/abencds_1091668137-_anno.md)

  - [`ObjectModel.usageType.serviceQuality`](../abap-cds-annotations/abencds_1255374604-_anno.md)

  - [`ObjectModel.usageType.sizeCategory`](../abap-cds-annotations/abencds_1163152301_anno.md)

## Hints

- Alongside the function annotations shown here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for a table function.

- The annotations `AccessControl` and `ObjectModel` have further [framework-specific subannotations](../abap-cds-annotations/abencds_annotations_frmwrk.md).

- Special rules for [Client Handling in CDS Table Functions](abencds_func_client_handling.md):

  - For the annotation `ClientHandling.type` only the enumeration values `#CLIENT_DEPENDENT` and `#CLIENT_INDEPENDENT` can be specified in table function definitions. Especially, `#INHERITED` cannot be used.

  - For the annotation `ClientHandling.algorithm` only the enumeration values `#NONE` and `#SESSION_VARIABLE` can be specified in table function definitions and the latter can be used only together with `ClientHandling.type: #CLIENT_INDEPENDENT`.

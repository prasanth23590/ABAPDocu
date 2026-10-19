---
title: "CDS DDL - CDS Simple Type, type_annot"
source_file: abencds_simple_type_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Simple Types > CDS DDL - DEFINE TYPE simple_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Simple Type, type_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a simple type annotation in the definition of a CDS simple type in front of the statement [`DEFINE TYPE`](abencds_define_simple_type.md). The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation must be defined as a [CDS object](../../abap-glossary/abencds_object_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs. In the annotation definition, the annotation `@Scope` should be used with the value `#SIMPLE_TYPE`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.typeSpec.changeDocumentRelevant`](../abap-cds-annotations/abencds_2016919924-_anno.md)

  - [`AbapCatalog.typeSpec.conversionExit`](../abap-cds-annotations/abencds_58258031_anno.md)

  - [`AbapCatalog.typeSpec.outputLength`](../abap-cds-annotations/abencds_1569826112_anno.md)

- EndUserText Annotations

  - [`EndUserText.heading`](../abap-cds-annotations/abencds_92083118_anno.md)

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

  - [`EndUserText.quickInfo`](../abap-cds-annotations/abencds_26162021_anno.md)

If a CDS simple type is based on another CDS simple type, it inherits the annotations of the underlying simple type. If required, these annotations can be overwritten using locally defined annotations in the overlying simple type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS simple type is based on a built-in data type in ABAP Dictionary.

``` abap
@EndUserText.heading: 'abc' 
@EndUserText.label: 'myLabel' 
@EndUserText.quickInfo: 'lala'  
define type demo_simple_type : abap.int4;
```

The following CDS simple type reuses the simple type `DEMO_SIMPLE_TYPE`. It inherits its properties and metadata.

`define type DEMO_SIMPLE_TYPE_2 : DEMO_SIMPLE_TYPE;`

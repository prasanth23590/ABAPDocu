---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, element_annot"
source_file: abencds_f1_absent_list_annotation.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY > CDS DDL - DEFINE ABSTRACT ENTITY, element_list > CDS DDL - DEFINE ABSTRACT ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, element_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_f1_absent_list_element.md) or CDS association of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) as element annotation. The character `@` must be placed directly in front of the name `annotation` of the annotation. In a CDS abstract entity, element annotations can only be specified in front of an element or a CDS association and not specified after it using `@<`.

The elements and CDS associations of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) can be assigned to the element annotations grouped under [`element_annot`](abencds_f1_element_annotation.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity with element annotations:

``` abap
@Metadata.allowExtensions : true

define abstract entity demo_cds_abstract_entity_elem
  {
        @EndUserText.label: 'Key field'
    key col1 : abap.char(3);
        @EndUserText.label: 'Integer field'
        col2 : abap.int4;
        @EndUserText.label: 'String field'
        col3 : abap.string;
        @EndUserText.label: 'Simple type field'
        col4 : DEMO_BT_CHAR_TEXT;
  }
```

The class `CL_DEMO_CDS_ABSTRACT_ENTITY_EL` shows that the element annotations of the CDS abstract entity can be evaluated using the class `CL_DD_DDL_ANNOTATION_SERVICE`. In this case, there are also derived annotations for the data element used for typing and annotations from a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md). The metadata extension is specified as an example for [`ANNOTATE ENTITY`](../abap-cds-annotations/abencds_f1_annotate_view.md).

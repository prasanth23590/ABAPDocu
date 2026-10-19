---
title: "CDS DDL - DEFINE CUSTOM ENTITY, element_annot"
source_file: abencds_f1_custom_element_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, element_list > CDS DDL - DEFINE CUSTOM ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, element_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_f1_absent_list_element.md) or CDS association of an [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) as element annotation. The character `@` must be placed directly in front of the name `annotation` of the annotation. In a CDS custom entity, element annotations can only be specified in front of an element or a CDS association.

All element annotations described in topic [`CDS DDL - element_annot`](abencds_f1_element_annotation.md) can be used to annotate elements and associations in a CDS custom entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity with element annotations:

``` abap
define custom entity demo_cds_custom_entity_elem 
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

The class `CL_DEMO_CDS_CUSTOM_ENTITY_ELEM` shows that the element annotations of the CDS custom entity can be evaluated using the class `CL_DD_DDL_ANNOTATION_SERVICE`. The result set contains not only the direct element annotations, but also derived annotations which are defined for the simple type used for typing.

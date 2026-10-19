---
title: "CDS DDL - ANNOTATE, element_list"
source_file: abencds_f1_annotate_view_sele_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions > ABAP CDS - DDL for Metadata Extensions > CDS DDL - ANNOTATE ENTITY, VIEW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - ANNOTATE, element_list

## Syntax

``` abap
... @element_annot1 
   [@element_annot2 
    ...] 
    element1[; 
    @element_annot1 
   [@element_annot2 
    ...] 
    element2; 
    ...;]  
```

[`@element_annot1`](../abap-cds-data-definitions/abencds_f1_element_annotation.md) · [`@element_annot2`](../abap-cds-data-definitions/abencds_f1_element_annotation.md) · [`@element_annot1`](../abap-cds-data-definitions/abencds_f1_element_annotation.md) · [`@element_annot2`](../abap-cds-data-definitions/abencds_f1_element_annotation.md)

## Description

Specifies annotations in a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md) introduced with [`ANNOTATE`](abencds_f1_annotate_view.md) for the following:

- [Elements](../abap-cds-data-definitions/abencds_f1_absent_list_element.md) in the [element list](../abap-cds-data-definitions/abencds_f1_absent_element_list.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [Elements](../abap-cds-data-definitions/abencds_select_list_entry_v2.md) in the [`SELECT` list](../abap-cds-data-definitions/abencds_select_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [Elements](../abap-cds-obsolete-language-elements/abencds_select_list_entry_v1.md) in the [`SELECT` list](../abap-cds-obsolete-language-elements/abencds_select_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

A semicolon-separated list `element1`; `element2`; ...; prefixed with annotations `element_annot` can be specified in the curly brackets of the statement `ANNOTATE`. There must be a semicolon after the last element of the list.

Each specified element `element` should appear in the `SELECT` list of the entity that is annotated using `ANNOTATE`. If not, the syntax check produces a warning. An externally visible element name must be used. For [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), this is either the direct name, an alternative element name defined with [`AS`](../abap-cds-obsolete-language-elements/abencds_select_list_entry_v1.md), or the name defined in a [name list](../abap-cds-obsolete-language-elements/abencds_name_list_v1.md). For [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), this is either the direct name, or an alternative element name defined with [`AS`](../abap-cds-data-definitions/abencds_select_list_entry_v2.md).

All elements of the `SELECT` list can be used exactly once. Valid [SAP annotations](abencds_annotations_sap.md) `@element_annot` can be specified before these as [element annotations](../abap-cds-data-definitions/abencds_f1_element_annotation.md). It is not possible here to specify annotations after the name of an element `element` with the syntax `@<element_annot`.

At least one element annotation`@element_annot` must be specified before each element of the list. However, the curly brackets of the `ANNOTATE` statement can also be empty.

## Hints

- An element must be specified directly with its name. It cannot be specified using names with multiple parts separated by periods, which can be used within the entity for its definition.

- The program `ABAP_DOCU_MDE_ANNOS` shows all annotations that can be specified in metadata extensions.

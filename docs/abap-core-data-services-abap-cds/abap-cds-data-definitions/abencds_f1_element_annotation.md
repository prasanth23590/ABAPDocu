---
title: "CDS DDL - element_annot"
source_file: abencds_f1_element_annotation.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Common DDL Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - element_annot

## Syntax

``` abap
... @annotation ...   
... @<annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) · [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as an element annotation for the following [CDS entities](../../abap-glossary/abencds_entity_glosry.md):

- [Elements](abencds_table_entity_element.md) in the [element list](abencds_table_entity_element_list.md) of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md)

- [Elements](abencds_select_list_entry_v2.md) in the [`SELECT` list](abencds_select_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [Elements](abencds_proj_view_element.md) in the [element list](abencds_proj_view_element_list.md) of a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md)

- [Elements](abencds_f1_return_list_element.md) in an [element list](abencds_f1_return_list.md) of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md)

- [Elements](abencds_ee_element.md) in an [element list](abencds_ee_elem_list.md) of a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md)

- [Elements](abencds_f1_hiera_element.md) in an [element list](abencds_f1_hiera_element_list.md) of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md)

- [Elements](abencds_f1_custom_element.md) in an [element list](abencds_f1_custom_element_list.md) of a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md)

- [Elements](abencds_f1_absent_list_element.md) in an [element list](abencds_f1_absent_element_list.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [Elements](../abap-cds-obsolete-language-elements/abencds_select_list_entry_v1.md) in the [`SELECT` list](../abap-cds-obsolete-language-elements/abencds_select_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

The elements of the `SELECT` list or element list of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) define the components of the result set of database accesses using [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) and of structured data types in ABAP. The annotations enrich these components with additional semantic properties. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) In the annotation definition, the annotation `@Scope` should be specified using the value `#ELEMENT`.

Element annotations can be specified before and after the element:

- In front of the element, the character `@` must be placed before the name `annotation` of the annotation.

- After the element, the characters `@<` must be placed before the name `annotation` of the annotation.

  This notation is possible for all CDS entities listed above, except for CDS view entities. For CDS view entities, all annotations, including element annotations, are possible only in front of the element they refer to.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.typeSpec.conversionExit`](../abap-cds-annotations/abencds_58258031_anno.md)

  - [`AbapCatalog.typeSpec.outputLength`](../abap-cds-annotations/abencds_1569826112_anno.md)

- Aggregation Annotations

  - [`Aggregation.default`](../abap-cds-annotations/abencds_741130102_anno.md)

- API Annotations

  - [`API.element.decommissioningPlannedForYearMonth`](../abap-cds-annotations/abencds_1318352950-_anno.md)

  - [`API.element.releaseState`](../abap-cds-annotations/abencds_1839662893-_anno.md)

  - [`API.element.successor`](../abap-cds-annotations/abencds_1922632877-_anno.md)

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

  - [`EndUserText.quickInfo`](../abap-cds-annotations/abencds_26162021_anno.md)

- Environment Annotations

  - [`Environment.sql.passValue`](../abap-cds-annotations/abencds_1000560355-_anno.md)

- Semantics Annotations

  - [`Semantics.amount.currencyCode`](../abap-cds-annotations/abencds_689127610-_anno.md)

  - [`Semantics.currencyCode`](../abap-cds-annotations/abencds_1954553685-_anno.md)

  - [`Semantics.quantity.unitOfMeasure`](../abap-cds-annotations/abencds_653082254-_anno.md)

  - [`Semantics.unitOfMeasure`](../abap-cds-annotations/abencds_772720932-_anno.md)

- ObjectModel Annotations

  - [`ObjectModel.virtualElementCalculatedBy`](../abap-cds-annotations/abencds_1555784333_anno.md)

## Hints

- The semantics annotations are used to define the [currency fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) and [quantity fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_quantity_field.md) of [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md), [CDS views](../../abap-glossary/abencds_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md), and [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md).

- If a CDS entity selects from a DDIC database table or from another CDS entity, the above semantics annotations are propagated and they do not have to be defined again explicitly.

  **Exception:** in CDS views with [set operators](../../abap-glossary/abencds_set_operators_glosry.md), the annotation [`Metadata.ignorePropagatedAnnotations: true`](abencds_view_entity_anno.md) is mandatory, propagation is switched off and therefore, reference annotations must be redefined explicitly.

- In addition to the [ABAP annotations](../abap-cds-annotations/abencds_annotations_abap.md) shown here, there are also [framework-specific](../abap-cds-annotations/abencds_annotations_frmwrk.md) semantics and object model annotations.

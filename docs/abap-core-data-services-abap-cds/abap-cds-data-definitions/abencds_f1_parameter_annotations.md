---
title: "CDS DDL - parameter_annot"
source_file: abencds_f1_parameter_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Common DDL Elements > CDS DDL - parameter"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - parameter_annot

## Syntax

``` abap
... @annotation ...   
... @<annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) · [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a parameter annotation in the definition of an [CDS parameter](../../abap-glossary/abencds_parameter_glosry.md) [`parameter`](abencds_f1_param.md) in one of the following:

- [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md)

- [CDS table function](../../abap-glossary/abencds_table_function_glosry.md)

- [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md)

- [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md)

- [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

Parameter annotations can be specified before and after the parameter:

- In front of the parameter, the character `@` must be placed before the name `annotation` of the annotation.

- After the parameter, the characters `@<` must be placed before the name `annotation` of the annotation.

  This notation is possible for all CDS entities listed above, except for CDS view entities. For CDS view entities, all annotations, including parameter annotations, are possible only in front of the element they refer to.

The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be specified using the value `#PARAMETER`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

  - [`EndUserText.quickInfo`](../abap-cds-annotations/abencds_26162021_anno.md)

- Environment Annotations

  - [`Environment.sql.passValue`](../abap-cds-annotations/abencds_1000560355-_anno.md)

  - [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md)

## Hint

A tooltip defined with `EndUserText.quickInfo` is not translated for parameters. The text specified after `EndUserText.quickInfo` for a parameter is not saved in the table for translatable texts. This is only the case for parameters and is an exception. If specified in any other position, tooltips are translated.

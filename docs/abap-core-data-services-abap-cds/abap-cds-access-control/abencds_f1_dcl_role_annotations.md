---
title: "CDS DCL - DEFINE ROLE, role_annot"
source_file: abencds_f1_dcl_role_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, role_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a role annotation in front of the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in the definition of a [CDS role](../../abap-glossary/abencds_role_glosry.md). The character `@` must be placed in front of the name `annotation` of the annotation. The annotation must be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` must be specified using the value `#ROLE`.

The following [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) can be specified for `annotation`. No other annotations can be specified.

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

- MappingRole Annotations

  - [`MappingRole`](../abap-cds-annotations/abencds_984551930-_anno.md)

## Hint

Every definition of a CDS role must contain the ABAP annotation `MappingRole` with the value `true`.

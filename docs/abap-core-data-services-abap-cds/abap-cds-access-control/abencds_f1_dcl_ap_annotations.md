---
title: "CDS DCL - DEFINE ACCESSPOLICY, access_policy_annot"
source_file: abencds_f1_dcl_ap_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ACCESSPOLICY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ACCESSPOLICY, access_policy_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as an access policy annotation in the definition of a [CDS access policy](../../abap-glossary/abencds_access_policy_glosry.md) in front of the statement [`DEFINE ACCESSPOLICY`](abencds_f1_define_accesspolicy.md). The character `@` must be placed directly in front of the name `annotation` of the annotation.

The following [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) can be specified for `annotation`. No other annotations can be specified.

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

## Hint

The `EndUserText.label` annotation is not recommended for CDS access policies, since its value is overwritten by the identically named annotation of the [PFCG mapping](abencds_f1_dcl_pm_annotations.md) or [aspect](abencds_f1_dcl_as_annotations.md) in question.

This means that the short text for these objects should be entered there directly and not in the CDS access policy.

---
title: "CDS DCL - DEFINE ACCESSPOLICY"
source_file: abencds_f1_define_accesspolicy.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ACCESSPOLICY

## Syntax

``` abap
[@access_policy_annot] 
[DEFINE] ACCESSPOLICY access_policy { 
  pfcg_mapping_definition | aspect_definition 
}  
```

[`@access_policy_annot`](abencds_f1_dcl_ap_annotations.md) · [`pfcg_mapping_definition`](abencds_f1_define_pfcg_mapping.md) · [`aspect_definition`](abencds_f1_define_generic_aspect.md)

## Description

Defines a [CDS access policy](../../abap-glossary/abencds_access_policy_glosry.md) `access_policy` in the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) to be used as a medium for further definitions.

An `ACCESSPOLICY` contains the definition of one of the following objects (which must have the same name as the access policy):

- A [PFCG mapping](../../abap-glossary/abencds_pfcg_mapping_glosry.md) [`DEFINE PFCG_MAPPING`](abencds_f1_define_pfcg_mapping.md)

- A user-defined aspect [`DEFINE ASPECT`](abencds_f1_define_generic_aspect.md).

`DEFINE ACCESSPOLICY` can be used to specify the optional annotation [`@access_policy_annot`](abencds_f1_dcl_ap_annotations.md) in front of the actual definition of the access policy.

## Hints

- Separate [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) must be created for each CDS access policy.

- The [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) of a CDS access policy must have the same name as this policy.

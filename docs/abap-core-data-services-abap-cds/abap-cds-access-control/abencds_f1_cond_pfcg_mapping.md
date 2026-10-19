---
title: "CDS DCL - DEFINE ROLE, pfcg_mapping"
source_file: abencds_f1_cond_pfcg_mapping.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition > CDS DCL - DEFINE ROLE, pfcg_condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, pfcg_mapping

## Syntax

``` abap
... ( ... { element1[, element2 ...] } ... ) 
        =|?= ASPECT pfcg_auth 
               ( ... PFCG_MAPPING = pfcg_mapping ...  ) ...  
```

## Description

Assigns an element list specified in curly brackets `{ element1[, element2 ...] }` to a [PFCG mapping](../../abap-glossary/abencds_pfcg_mapping_glosry.md) `pfcg_mapping` in the definition of a [PFCG condition](abencds_f1_cond_pfcg.md).

- The element list of the left side is a comma-separated list of one or more directly specified [CDS elements](../../abap-glossary/abencds_element_glosry.md) of the CDS entity for which the access condition is defined. An element `element` can also be specified using a path expression [`path_expr`](../../abap-glossary/abensql_path_expression_glosry.md) and must have one of the valid [data types](abencds_f1_dcl_cond_data_types.md).

- After `PFCG_MAPPING =`, the right side must specify a PFCG mapping `pfcg_mapping` defined using [`DEFINE PFCG_MAPPING`](abencds_f1_define_pfcg_mapping.md) as part of a [CDS access policy](../../abap-glossary/abencds_access_policy_glosry.md).

When the PFCG condition is transformed into specific conditions, the PFCG mappings are handled as follows by CDS access control:

- The authorization fields specified in the comma-separated list of the definition of the [PFCG mapping](abencds_f1_define_pfcg_mapping.md) are used as input fields of the mapping `pfcg_mapping`.

- The output fields of the [PFCG mapping](abencds_f1_define_pfcg_mapping.md) are compared with the CDS elements of the element list assigned to the PFCG mapping in the PFCG condition.

The other conditions of the [PFCG condition](abencds_f1_cond_pfcg.md) are created as described there. The PFCG condition is true if the conditions for the individually specified CDS elements and the PFCG mapping are met. If multiple authorizations exist for a single authorization field and there are individually specified CDS elements alongside the PFCG mapping, the PFCG mapping is resolved for each individual authorization.

## Hints

- PFCG mappings enable those entries in a CDS entity allowed for a particular user to be specified using high-order structural characteristics.

- Using PFCG mappings can negatively affect performance, particularly if individual CDS elements are specified simultaneously and if multiple authorizations exist for a single authorization field.

- If the PFCG condition has the addition [`IN SCENARIO`](abencds_f1_cond_pfcg.md), the PFCG mapping used in this place must also have this addition and name the same scenario.

- Optional elements with `DEFAULT TRUE` are removed from the element list of the PFCG mapping. If this applies to all elements, a PFCG mapping with empty element list emerges (such cannot be created literally in an access control yet). The runtime result will be an SQL `EXISTS` on the mapping entity which is supplied from the PFCG role data, but without relation to the protected entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following role uses the PFCG mapping `demo_cds_pfcg_mapping` defined in the example for [`DEFINE PFCG_MAPPING`](abencds_f1_define_pfcg_mapping.md) in a [PFCG condition](../../abap-glossary/abenpfcg_condition_glosry.md):

``` abap
CDS or DDIC source code was not found
```

The class `CL_DEMO_CDS_AUTH_PFCG_MAPPING` accesses the view `DEMO_CDS_AUTH_PFCG_MAPPING` and an SQL trace demonstrates how the PFCG mapping works.

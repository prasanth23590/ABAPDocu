---
title: "CDS DDL - path_expr, Transactional Query"
source_file: abencds_proj_view_path_expr.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - path_expr, Transactional Query

## Syntax

``` abap
... [source.]_assoc1[parameters][filter] ...  
```

[`parameters`](abencds_select_parameters_v2.md) · [`filter`](abencds_pv_assoc_modified.md)

## Description

A path expression in the CDS DDL is a sequence of CDS associations separated by periods (.) whose names are specified using `assoc1, assoc2,` and so on. The rules for path expressions in CDS projection views are similar to path expressions in CDS view entities, see topic [CDS DDL - CDS View Entity, `path_expr`](abencds_path_expression_v2.md) with the following differences:

- The filter of a path expression of a CDS projection view cannot define a join type. It can only define a cardinality and a filter condition as described in topic [CDS DDL - CDS Projection View, filter](abencds_pv_assoc_modified.md).

- The result set of the CDS projection view must be the same as the result set of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Therefore, the [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md) of each traversed association must be *one*. This can be achieved by using a [filter condition](../../abap-glossary/abenfilter_condition_glosry.md).

- The keyword [`LOCALIZED`](abencds_proj_view_element.md) can be used to display text elements in the user's logon language. All previous association paths must be filtered to *one*.

- It is possible to pass parameters in association paths. This works in the same way as parameter passing in CDS view entities, see topic [CDS DDL - CDS View Entity, `path_expr`](abencds_path_expression_v2.md).

---
title: "CDS DDL - CDS View Entity, Set Operators"
source_file: abencds_set_operators.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Set Operators

[Set operators](../../abap-glossary/abencds_set_operators_glosry.md) merge the result sets of multiple queries into a single result set. In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), the following set operators are available:

- [`EXCEPT`](abencds_except_v2.md) returns all distinct rows of the first result set that are not part of the following result sets.

- [`INTERSECT`](abencds_intersect_v2.md) returns all distinct rows that are part of all result sets.

- [`UNION`](abencds_union_v2.md) merges the result sets of all queries.

The following image illustrates how each set operator merges several result sets: ![figure](images_abdoc_set_operators.jpg)

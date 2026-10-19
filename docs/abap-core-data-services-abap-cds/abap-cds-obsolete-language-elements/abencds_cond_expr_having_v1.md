---
title: "CDS DDL - DDIC-Based View, cds_cond, HAVING"
source_file: abencds_cond_expr_having_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, clauses > CDS DDL - DDIC-Based View, SELECT, HAVING"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, HAVING

Rules for conditions [`cds_cond`](abencds_conditional_expression_v1.md) in a [`HAVING` condition](abencds_having_clause_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- The relational operator `BETWEEN` is not allowed. All other relational operators are allowed.

- A [field](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) or an [aggregate expression](abencds_aggregate_functions_v1.md) for this kind of field can be specified for `lhs`.

- An [element](abencds_select_list_entry_v1.md) of the [`SELECT` list](abencds_select_list_v1.md), an [aggregate expression](abencds_aggregate_functions_v1.md), a [literal](abencds_literal_v1.md) with an optional domain prefix, or a [parameter](abencds_parameter_v1.md) can be specified for `rhs` (with the exception of the operator [`LIKE`](abencds_cond_expr_like_v1.md)). If `lhs` is an [aggregate expression](abencds_aggregate_functions_v1.md), a [literal](abencds_literal_v1.md) must be specified.

- A field of a data source can be specified using a path expression [`path_expr`](abencds_path_expression_v1.md).element, as long as the CDS associations of the expression do not have any [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) as [association targets](../../abap-glossary/abenassociation_target_glosry.md) and the expression is unique:

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) of the contained [CDS associations](../../abap-glossary/abencds_association_glosry.md) is to-one.

  - The path expression only contains

  - [filter conditions](abencds_path_expression_filter_v1.md) with addition `1:`.

    `element` can be used to specify an element of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path.

- Other expressions and function calls are not allowed.

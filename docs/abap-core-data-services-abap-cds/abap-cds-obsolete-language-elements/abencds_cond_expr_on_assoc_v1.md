---
title: "CDS DDL - DDIC-Based View, cds_cond, ON, CDS Association"
source_file: abencds_cond_expr_on_assoc_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, ON, CDS Association

Rules for conditions [`cds_cond`](abencds_conditional_expression_v1.md) in an [`ON` condition](abencds_association_v1.md) of a [CDS association](../../abap-glossary/abencds_association_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- All relational operators are allowed.

- A [field](abencds_field_v1.md) of one of the two data sources [`data_source`](abencds_data_source_v1.md) of the CDS association can be specified for `lhs`.

- A [field](abencds_field_v1.md) of both data sources [`data_source`](abencds_data_source_v1.md) of the CDS association, a [literal](abencds_literal_v1.md) with optional domain prefix, a [parameter](abencds_parameter_v1.md), or a [session variable](abencds_session_variable_v1.md) can be specified for `rhs` (with the exception of the operator [`LIKE`](abencds_cond_expr_like_v1.md)).

  **Note:** As of ABAP release 7.92, [typed literals](../abap-cds-data-definitions/abencds_typed_literal_v2.md) are also supported for `rhs`.

- A field of the [association source](../../abap-glossary/abenassociation_source_glosry.md) can also be specified by an alternative element name (defined using [`AS`](abencds_select_list_entry_v1.md)) of the current CDS view.

- At least one comparison for equality between a field of the initial data source and a field of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the CDS association must be performed.

- No path expressions or other expressions or function calls can be specified.

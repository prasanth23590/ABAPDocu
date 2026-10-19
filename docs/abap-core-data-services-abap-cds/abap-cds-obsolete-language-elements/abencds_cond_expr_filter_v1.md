---
title: "CDS DDL - DDIC-Based View, cds_cond, Filter"
source_file: abencds_cond_expr_filter_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, path_expr > CDS DDL - DDIC-Based View, path_expr, attributes > CDS DDL - DDIC-Based View, path_expr, Filter"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, Filter

Rules for conditions [`cds_cond`](abencds_conditional_expression_v1.md) in a

[filter condition](abencds_path_expression_filter_v1.md) of a [path expression](abencds_path_expression_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- All relational operators are allowed.

- `lhs` expects a [field](abencds_field_v1.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the current [CDS association](../../abap-glossary/abencds_association_glosry.md).

- A [field](abencds_field_v1.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the current [CDS association](abencds_association_v1.md), a [literal](abencds_literal_v1.md) with optional domain prefix, a [parameter](abencds_parameter_v1.md), a [session variable](abencds_session_variable_v1.md), or a [built-in function](abencds_builtin_functions_v1.md) can be specified for `rhs` (with the exception of the operator [`LIKE`](abencds_cond_expr_like_v1.md)).

- No path expressions or other expressions or function calls can be specified.

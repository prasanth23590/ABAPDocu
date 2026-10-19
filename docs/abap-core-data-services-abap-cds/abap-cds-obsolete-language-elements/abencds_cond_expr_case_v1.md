---
title: "CDS DDL - DDIC-Based View, cds_cond, CASE"
source_file: abencds_cond_expr_case_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, case_expr > CDS DDL - DDIC-Based View, searched_case_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, CASE

Rules for conditions [`cds_cond`](abencds_conditional_expression_v1.md) in a [complex case distinction](abencds_searched_case_expr_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) view:

- All relational operators are allowed.

- `lhs` expects a [field](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md).

- A [field](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md), a [literal](abencds_literal_v1.md) with optional domain prefix, a [parameter](abencds_parameter_v1.md), a [session variable](abencds_session_variable_v1.md), or a [built-in function](abencds_builtin_functions_v1.md) can be specified for `rhs` (with the exception of the operator [`LIKE`](abencds_cond_expr_like_v1.md)).

- A field of a data source can be specified using a path expression [`path_expr`](abencds_path_expression_v1.md).element, as long as the CDS associations of the expression do not have any [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) as [association targets](../../abap-glossary/abenassociation_target_glosry.md) and the expression is unique:

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) of the contained [CDS associations](../../abap-glossary/abencds_association_glosry.md) is to-one.

  - The path expression only contains

  - [filter conditions](abencds_path_expression_filter_v1.md) with addition `1:`.

    `element` can be used to specify an element of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path.

- Other expressions and function calls are not allowed.

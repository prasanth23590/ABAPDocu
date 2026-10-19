---
title: "CDS DDL - DDIC-Based View, cds_cond, Operands"
source_file: abencds_cond_expr_operands_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, Operands

The following rules apply to the operands `lhs` and `rhs` in relational expressions of the `SELECT` statement in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- General Rules

  - [Character literals](abencds_literal_v1.md) cannot be used in comparisons with numeric values.

  - [Numeric literals](abencds_literal_v1.md) that represent a value outside the value range of [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) must be specified as floating point literals with a decimal point.

- Special Context-Specific Rules:

  - [Rules](abencds_cond_expr_where_v1.md) for use in a `WHERE` condition

  - [Rules](abencds_cond_expr_having_v1.md) for use in a `HAVING` condition

  - [Rules](abencds_joined_data_source_v1.md) for use in an `ON` condition of a join expression

  - [Rules](abencds_cond_expr_on_assoc_v1.md) for use in an `ON` condition of a CDS association

  - [Rules](abencds_cond_expr_filter_v1.md) for use in a filter condition of a path expression

  - [Rules](abencds_cond_expr_case_v1.md) for use in a complex case distinction.

## Hint

For [comparisons](abencds_cond_expr_comp_v1.md), the tables of [comparable types](abencds_cond_expr_types_v1.md) show which data types can be compared with each other.

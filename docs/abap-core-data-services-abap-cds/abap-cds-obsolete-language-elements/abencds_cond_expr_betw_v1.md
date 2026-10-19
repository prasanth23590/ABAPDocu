---
title: "CDS DDL - DDIC-Based View, cds_cond, BETWEEN"
source_file: abencds_cond_expr_betw_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, BETWEEN

## Syntax

``` abap
... lhs BETWEEN rhs1 AND rhs2 ...  
```

## Description

Compares an interval in a [condition](abencds_conditional_expression_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The relational expression is true if the value of `lhs` is between the values of `rhs1` and `rhs2`. The expression has the same meaning as the following combination of two [comparisons](abencds_cond_expr_comp_v1.md):

`... lhs >= rhs1 AND lhs <= rhs2 ...`

The corresponding context-dependent rules apply to the [operands](abencds_cond_expr_operands_v1.md) `lhs`, `rhs1`, and `rhs2` as well as the same [conditions](abencds_cond_expr_types_v1.md) for the data types.

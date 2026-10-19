---
title: "CDS DDL - CDS View Entity, cds_cond, BETWEEN"
source_file: abencds_cond_expr_betw_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cds_cond, BETWEEN

## Syntax

``` abap
... lhs [NOT] BETWEEN rhs1 AND rhs2 ...  
```

## Description

Compares an interval in a [condition](abencds_conditional_expression_v2.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The relational expression is true if the value of `lhs` is between the values of `rhs1` and `rhs2`. The expression has the same meaning as the following join of two [comparisons](abencds_cond_expr_comp_v2.md): `... lhs >= rhs1 AND lhs <= rhs2 ...`

The operands `lhs`, `rhs1`, and `rhs2` must stick to the context-dependent rules listed in topic [CDS DDL - View Entity, `cds_cond`, Operands](abencds_cond_expr_operands_v2.md). Moreover, the data types of the operands must be comparable as described in topic [CDS DDL - View Entity, `cds_cond`, Comparable Types](abencds_cond_expr_types_v2.md).

---
title: "CDS DDL - CDS View Entity, cds_cond, Comparison Operators"
source_file: abencds_cond_expr_comp_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cds_cond, Comparison Operators

## Syntax

``` abap
... lhs operator rhs ...  
```

## Description

Comparison operators can be used to specify a comparison in a [condition](abencds_conditional_expression_v2.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The following table shows relational expressions `rel_exp` that are constructed with comparison operators:

| **rel_expr** | **True if**                                                   |
|--------------|---------------------------------------------------------------|
| `lhs = rhs`  | Value of `lhs` is equal to the value of `rhs`                 |
| `lhs <> rhs` | Value of `lhs` is not equal to the value of `rhs`             |
| `lhs < rhs`  | Value of `lhs` is less than the value of `rhs`                |
| `lhs > rhs`  | Value of `lhs` is greater than the value of `rhs`             |
| `lhs <= rhs` | Value of `lhs` is less than or equal to the value of `rhs`    |
| `lhs >= rhs` | Value of `lhs` is greater than or equal to the value of `rhs` |

- Context-dependent rules apply when specifying the operands `lhs` and `rhs`. For further details, see topic [CDS DDL - CDS View Entity, `cds_cond`, Operands](abencds_cond_expr_operands_v2.md).

- The tables of [comparable types](abencds_cond_expr_types_v2.md) show which data types can be compared with each other.

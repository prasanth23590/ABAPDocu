---
title: "CDS DDL - DDIC-Based View, cds_cond, Comparison Operators"
source_file: abencds_cond_expr_comp_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, Comparison Operators

## Syntax

``` abap
... lhs operator rhs ...  
```

## Description

Comparison operators can be used to specify a comparison in a [condition](abencds_conditional_expression_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The following table shows relational expressions `rel_exp` that are constructed with comparison operators:

| **rel_expr** | **True if**                                                   |
|--------------|---------------------------------------------------------------|
| `lhs = rhs`  | Value of `lhs` is equal to the value of `rhs`                 |
| `lhs <> rhs` | Value of `lhs` is not equal to the value of `rhs`             |
| `lhs < rhs`  | Value of `lhs` is less than the value of `rhs`                |
| `lhs > rhs`  | Value of `lhs` is greater than the value of `rhs`             |
| `lhs <= rhs` | Value of `lhs` is less than or equal to the value of `rhs`    |
| `lhs >= rhs` | Value of `lhs` is greater than or equal to the value of `rhs` |

- Context-dependent rules apply when specifying the [operands](abencds_cond_expr_operands_v1.md) `lhs` and `rhs`.

- The tables of [comparable types](abencds_cond_expr_types_v1.md) show which data types can be compared with each other.

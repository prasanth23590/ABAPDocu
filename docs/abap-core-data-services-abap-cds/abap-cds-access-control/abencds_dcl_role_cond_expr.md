---
title: "CDS DCL - DEFINE ROLE, cds_cond"
source_file: abencds_dcl_role_cond_expr.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, access_rules > CDS DCL - DEFINE ROLE, conditional_rule"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, cds_cond

## Syntax

``` abap
... condition 
  | [NOT] cds_cond [AND|OR cds_cond] ...  
```

[`condition`](abencds_dcl_role_conditions.md)

## Description

Formulates an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) in the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). The result of an access condition is true or false.

An access condition is either a single condition, [`condition`](abencds_dcl_role_conditions.md), or an expression constructed from the Boolean operators `NOT`, `AND`, and `OR` in which parenthesized full conditions `cds_cond` using parentheses `( ... )` are possible. The Boolean operators work as follows:

- `NOT` negates the result of the following condition. It cannot be used if `cds_cond` is one of the following conditions:

  - A PFCG condition [`pfcg_condition`](abencds_f1_cond_pfcg.md) whose left side specifies CDS elements that themselves are assigned authorization fields on the right side after `ASPECT pfcg_auth` using `mapped_field1`, `mapped_field2`, ...

  - A user-defined aspect [`aspect`](abencds_f1_cond_aspect.md).

  - An inheritance condition [`inherit_condition`](abencds_f1_cond_inherit.md).

- An `AND` combination is true if both combined conditions are true.

- An `OR` combination is true if at least one of the combined conditions is true.

The operator `NOT` is a stronger binding than `AND`, which itself is a strong binding than `OR`. This produces implicit parentheses, which can be overridden by explicit parentheses.

When an access condition is evaluated using CDS access control, only those lines are selected for which the access condition is true.

## Hint

Inside of the `NOT` operator (also in nested subconditions), some constituents of access conditions cannot be used:

- PFCG conditions with left side elements.

- User-defined aspects.

- Literal conditions using optional elements.

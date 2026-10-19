---
title: "CDS DCL - DEFINE ROLE, access_rules"
source_file: abencds_dcl_role_rules.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, access_rules

## Syntax

``` abap
1. ... conditional_rule|grant_rule 
     [conditional_rule|grant_rule] 
      ...   
 
2. ... inherited_rule 
     [conditional_rule|grant_rule] 
     [conditional_rule|grant_rule] 
      ...   
 
3. ... projection_rule ...  
```

[`conditional_rule`](abencds_dcl_role_cond_rule.md) · [`grant_rule`](abencds_dcl_role_grant_rule.md) · [`conditional_rule`](abencds_dcl_role_cond_rule.md) · [`grant_rule`](abencds_dcl_role_grant_rule.md) · [`conditional_rule`](abencds_dcl_role_cond_rule.md) · [`grant_rule`](abencds_dcl_role_grant_rule.md) · [`conditional_rule`](abencds_dcl_role_cond_rule.md) · [`grant_rule`](abencds_dcl_role_grant_rule.md) · [`projection_rule`](abencds_dcl_role_proj_rule.md)

## Description

Access rules that can be specified in curly brackets in the statement [`DEFINE ROLE`](abencds_f1_define_role.md) to define a [CDS role](../../abap-glossary/abencds_role_glosry.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). Each access rule defines access to a [CDS](../../abap-glossary/abencds_entity_glosry.md) entity. There are the following types of access rule:

- Conditional access rules [`conditional_rule`](abencds_dcl_role_cond_rule.md), which control access using [access conditions](abencds_dcl_role_conditions.md).

- Full access rules [`grant_rule`](abencds_dcl_role_grant_rule.md) that grant unrestricted access.

- A projection rule [`projection_rule`](abencds_dcl_role_proj_rule.md) for transactional projection views.

Multiple access rules can be combined in a single CDS role, but an inherited access rule `inherited_rule` can only occur once.

The access conditions defined by the individual access rules are joined with a logical *or*. In the same way, the access rules defined by different CDS roles for a CDS entity are joined by a logical *or*.

## Hint

It is advisable to use only one access rule in a CDS role.

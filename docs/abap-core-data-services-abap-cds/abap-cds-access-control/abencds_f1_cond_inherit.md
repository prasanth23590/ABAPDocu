---
title: "CDS DCL - DEFINE ROLE, inherit_condition"
source_file: abencds_f1_cond_inherit.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, inherit_condition

## Syntax

``` abap
... { { INHERIT parent_role FOR GRANT SELECT ON cds_entity } 
  | { INHERITING CONDITIONS FROM 
       { ENTITY cds_entity [DEFAULT TRUE|FALSE] } 
       | SUPER } } 
    [ replacing ] ...  
```

[`replacing`](abencds_f1_cond_inherit_replacing.md)

### Variant

[1. `... INHERIT parent_role FOR GRANT SELECT ON cds_entity`](abencds_f1_cond_inherit.md#variant-1)

[2. `... INHERITING CONDITIONS FROM ENTITY cds_entity ...`](abencds_f1_cond_inherit.md#variant-2)

[3. `... INHERITING CONDITIONS FROM SUPER`](abencds_f1_cond_inherit.md#variant-3)

## Overview

### Description

Inheritance condition as part of an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md) in an [access rule](abencds_dcl_role_rules.md) of the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). There are three variants:

- The variant `INHERIT FOR GRANT` applies the access conditions from a different CDS role.

- The variant `INHERITING CONDITIONS FROM ENTITY` applies the access conditions from a CDS entity.

- The variant `INHERITING CONDITIONS FROM SUPER` applies the access conditions from roles that are redefined by the current role.

In all variants, the inherited conditions can be altered by [`replacing`](abencds_f1_cond_inherit_replacing.md) before they are applied to the CDS entity of the current access control.

### Hints

- Multiple inheritance conditions can be specified within a single access condition and these can be combined with [literal conditions](abencds_f1_cond_literal.md), [PFCG conditions](abencds_f1_cond_pfcg.md), and [user conditions](abencds_f1_cond_user.md).

- The inherited access conditions are parenthesized implicitly. It is not necessary to set parentheses explicitly.

- An inheritance condition cannot be negated using [`NOT`](abencds_dcl_role_cond_expr.md).

- Full access rules can be inherited and are represented in the resulting conditions as the Boolean predicate `TRUE`.

- Using inheritance can cause cycles which result in syntax errors.

- Both inheritance flavors respect access rules that are declared in the same access role as the inheritance statement. The access rule which contains the inheritance statement is excluded. This feature allows the demonstration of inheritance within a single access control document for test purposes.

## Variant 1

`... INHERIT parent_role FOR GRANT SELECT ON cds_entity`

### Description

This syntax is not available in the current ABAP language version.

## Variant 2

`... INHERITING CONDITIONS FROM ENTITY cds_entity [DEFAULT TRUE|FALSE] [REPLACING ...]`

### Addition

[`... DEFAULT TRUE|FALSE`](abencds_f1_cond_inherit.md#addition)

### Description

From a CDS entity `cds_entity`, this variant of an inheritance condition inherits the access roles defined for it using CDS roles and inserts them at the location of the inheritance condition. This joins the access rules of multiple CDS roles using the same algorithm which also applies to access to the CDS entity `cds_entity`, that is, `COMBINATION MODE` and `REDEFINITION` are respected.

If the CDS entity does not have any access conditions yet, a syntax warning occurs and the expression is replaced with the Boolean predicate `TRUE`. You can avoid this warning by the `DEFAULT` addition.

The inherited access conditions must match the CDS entity for which the current access rule is defined.

- If an inherited access condition does not match the current CDS entity, for example because the wrong field or path is specified, all access rules of the parent CDS role are ignored.

  - If there is no [full access rule](abencds_dcl_role_grant_rule.md) for the entity in this case, the current CDS role cannot be activated.

  - If there is a [full access rule](abencds_dcl_role_grant_rule.md) for the entity, the CDS role can be activated but a syntax check warning occurs.

### Hint

An annotation `@AccessControl.authorizationCheck` in the source code of the parent CDS entity `cds_entity` is ignored by `INHERITING CONDITIONS`. The access rules are passed to the current CDS role even if the value `#NOT_ALLOWED` is specified.

## Addition

`... DEFAULT TRUE|FALSE`

### Description

If the source CDS entity does not have a CDS role, this addition replaces the expression `INHERITING CONDITIONS ...` with the Boolean predicate [`TRUE`](abencds_dcl_role_conditions.md) or [`FALSE`](abencds_dcl_role_conditions.md).

### Hints

- If specified for the variant `INHERITING CONDITIONS`, `DEFAULT TRUE` is designed to inherit access conditions from other CDS entities regardless of whether a CDS role is already defined for them or not.

- If the variant `INHERITING CONDITIONS` is the only access condition of an access rule and no CDS role is defined for the CDS entity `cds_entity`, the rule is applied like a [full access rule](abencds_dcl_role_grant_rule.md) if `DEFAULT TRUE` is specified and like a rule that generally blocks access if `DEFAULT FALSE` is specified.

## Variant 3

`... INHERITING CONDITIONS FROM SUPER`

### Description

This variant is possible only if the access rule has the addition [`REDEFINITION`](abencds_dcl_role_cond_rule.md) and only if the inherited CDS entity has access controls.

Instead of this condition, those conditions are used that would have been applied by the access controls disabled by `REDEFINITION`.

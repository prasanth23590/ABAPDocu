---
title: "CDS DCL - DEFINE ROLE, conditional_rule"
source_file: abencds_dcl_role_cond_rule.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, access_rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, conditional_rule

## Syntax

``` abap
GRANT SELECT ON cds_entity 
     [WITH OPTIONAL ELEMENTS ( element1 DEFAULT  { TRUE | FALSE }, ...  ) ] 
     [COMBINATION MODE OR | COMBINATION MODE AND | REDEFINITION] 
      WHERE cds_cond;  
```

[`cds_cond`](abencds_dcl_role_cond_expr.md)

### Addition

[1. `... WITH OPTIONAL ELEMENTS`](abencds_dcl_role_cond_rule.md#addition-1)

[2. `... COMBINATION MODE AND|OR`](abencds_dcl_role_cond_rule.md#addition-2)

[3. `... REDEFINITION`](abencds_dcl_role_cond_rule.md#addition-3)

[4. `....WHERE`](abencds_dcl_role_cond_rule.md#addition-4)

## Overview

### Description

Conditional access rule in the statement [`DEFINE ROLE`](abencds_f1_define_role.md) of the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). A conditional access rule `GRANT SELECT ON` with the addition `WHERE` restricts access to a CDS entity `cds_entity` using [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md).

A single CDS entity can be specified in multiple access rules of a CDS role and multiple CDS roles can contain access rules for a single CDS entity.

If a CDS entity is specified in multiple access rules of a CDS role or in multiple CDS roles, the resulting access conditions are combined using the method specified by the addition `COMBINATION MODE`.

### Hint

No [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md) or [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md) can be specified for `cds_entity`.

## Addition 1

`... WITH OPTIONAL ELEMENTS ...`

### Description

When you use condition inheritance to apply the access conditions of a CDS entity to another CDS entity, subsequent changes to the inheritance source conditions may invalidate the inheritance target because newly introduced elements are not present.

By declaring elements of an access control as optional you specify that these elements may be missing in inheritance targets of the access conditions using those elements.

The syntax check of the inheriting access controls will then report a warning instead of an error and at runtime, conditions using those elements are processed according to the declared default value (specific details are provided in the documentation of the respective conditions).

### Hints

- Optionality can only be declared for a directly specified field or the first association of a path expression. In the latter case, all path expressions starting with this association are considered optional and are handled with the default value when this association does not exist at runtime. However, when the association exists but any of the following path components is missing, this is considered an error and results in a syntax error of the inheriting access control and potential runtime error at entity access.

- In the access control where the optionality is declared, the element must exist. It is not possible to create access controls for non-existing elements.

- Optionality can get lost in condition inheritance by application of certain replacement steps. This is documented in the respective steps.

- Optionality is only applied to left side CDS elements which are written in the current access control. It does not apply to left side CDS elements which are inherited from other access controls.

- Optionality shall bridge a short time-gap between the modification of access conditions acting as inheritance source and the necessary adoptions of CDS entities protected by inheriting access controls. It is not recommended that it used as a permanent constituent of an access control design.

- The default value must be chosen carefully. *Secure by default* implies using `DEFAULT FALSE`, by using `DEFAULT TRUE` you declare that it is temporarily acceptable that access control may ignore this element. This situation may be on hand when an established authorization concept is refined by additional fields.

- Optional elements cannot be used inside of `NOT` conditions, to avoid that a secure `DEFAULT FALSE` is accidentally flipped to the Boolean predicate `TRUE`.

## Addition 2

`... COMBINATION MODE AND|OR`

### Description

The optional addition `COMBINATION MODE AND|OR` can be used to define how the access conditions of multiple access rules for the same CDS entity `cds_entity` are combined. This addition can be applied regardless of whether other access rules already exist for the CDS entity.

`COMBINATION MODE OR` is used to combine the access conditions using the logical operator *or*. If created, these access rules make the restrictions less strong.

`COMBINATION MODE AND` combines the current access rule with the logical operator *and* and the other access rules. This means the restrictions are made stronger.

If multiple access rules with the combination methods *AND* (`cond_and_1`, `cond_and_2`, ...), and *OR* (`cond_or_1`, `cond_or_2`, ...) exist, the following expression produces the full condition:

`( cond_or_1 OR cond_or_2 OR ... ) AND cond_and_1 AND cond_and_2 AND ...`

A full access rule overrides the construction above, however, and produces a full access rule as the end result, even if there are rules with the mode `COMBINATION MODE AND`.

The following applies to the addition `COMBINATION MODE OR`:

- The addition `COMBINATION MODE OR` does not need to be specified explicitly. If there are multiple access rules for a CDS entity, they are combined implicitly using the logical operator *or*. For reasons of consistency, however, the addition `COMBINATION MODE OR` is recommended.

- Any existing access controls without the explicit addition `COMBINATION MODE OR` are valid.

- In roles with the [`SWITCHABLE`](abencds_f1_define_role.md) addition, the `COMBINATION MODE` addition is mandatory, including for the mode `OR`.

## Addition 3

`... REDEFINITION`

### Description

The optional addition `REDEFINITION` is used to indicate that the access rule in question is the only existing access rule for the CDS entity and any other access rules are ignored. The addition makes it possible for customers and partners to replace all access rules delivered by SAP for CDS entity with their own access rules without making modifications. The language element `INHERITING CONDITIONS FROM SUPER` can, however, be used to incorporate conditions delivered by SAP in customer or partner access rules.

The following applies to the addition `REDEFINITION`:

- This addition can be used in customer systems only. SAP does not deliver access rules of this type.

- The addition can also be applied if there are no other access rules for an entity. It ensures that the conditions defined here are not disabled by any later access rules.

- The addition can be used for a maximum of one access rule for a CDS entity. If used more than once, an activation error or import error occurs.

- This addition also disables existing full access rules for a CDS entity. SAP does not deliver full access rules, which means that this statement applies only to customer full access rules that are themselves overridden by customer `REDEFINITION` rules.

- In roles with the [`SWITCHABLE`](abencds_f1_define_role.md) addition, `REDEFINITION` is not allowed.

## Addition 4

`... WHERE`

### Description

A `WHERE` clause is used to define an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md) for the CDS entity `cds_entity`. When a CDS entity is accessed using ABAP SQL, and an access rule is configured for this entity in a role, the access conditions are evaluated implicitly. This means their selection is restricted accordingly and hence any [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) reads use a logical *and* to add the access condition to the select condition of the statement passed to the database by the database interface.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS role `DEMO_CDS_ROLE_LIT_PFCG_VE` defines an access condition for the CDS view entity `demo_cds_authority_lit_pfcg_ve` in an access rule. Both a [PFCG condition](abencds_f1_cond_pfcg.md) for the [authorization object](../../abap-glossary/abenauthorization_object_glosry.md) `S_CARRID` and a [literal condition](abencds_f1_cond_literal.md) for the currency field are specified.

``` abap
CDS or DDIC source code was not found
```

The CDS view entity is as follows:

``` abap
@AccessControl.authorizationCheck: #CHECK
define view entity DEMO_CDS_AUTHORITY_LIT_PFCG_VE
  as select from
    scarr
    {
      key carrid,
          carrname,
          currcode,
          url
    }
```

The class `CL_DEMO_CDS_AUTH_LIT_PFCG_VE` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view entity. CDS access control restricts the selections to data for which the current user has authorization according to classic role maintenance (transaction PFCG) and that meets the literal condition.

---
title: "CDS DCL - DEFINE ROLE, user_condition"
source_file: abencds_f1_cond_user.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, user_condition

## Syntax

``` abap
...[ALL|EXISTS] element =|<>|?= ASPECT user ...  
```

[`=|<>|?=`](abencds_f1_dcl_cond_expression.md)

### Variant

[1. `... ( element ) = ASPECT user_alias ...`](abencds_f1_cond_user.md#variant-1)

[2. `... ( element ) = ASPECT user_business_partner_number ...`](abencds_f1_cond_user.md#variant-2)

### Addition

[`... ALL|EXISTS`](abencds_f1_cond_user.md#addition)

## Overview

### Description

User condition as part of an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md) in an [access rule](abencds_dcl_role_rules.md) of the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). In a user condition, the predefined [aspect](../../abap-glossary/abencds_aspect_glosry.md) `user` is specified on the right side introduced with `ASPECT`.

The left side is compared with the [user name](../../abap-glossary/abenuser_name_glosry.md) of the user currently logged on to AS ABAP by using one of the three operators [`=`](abencds_f1_dcl_cond_expression.md), [`<>`](abencds_f1_dcl_cond_expression.md), [`?=`](abencds_f1_dcl_cond_expression.md), as in a [literal condition](abencds_f1_dcl_cond_expression.md).

The behavior when `element` is declared as optional element and missing at runtime is the same as for literal conditions.

### Hints

- The base syntax `ASPECT_USER` is deprecated and should be replaced by `$session.user.`

  In the syntax check, the new syntax validates that `element` is compatible with all possible user names. The deprecated syntax emitted a warning only and a runtime error was possible.

- User conditions can be combined within an access rule using [literal conditions](abencds_f1_cond_literal.md) and [PFCG conditions](abencds_f1_cond_pfcg.md), and [inheritance conditions](abencds_f1_cond_inherit.md).

- A user condition acts like a comparison with the session variable [`$session.user`](../abap-cds-data-definitions/abencds_session_variable_v2.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). It is not currently possible to use session variables on the right side of conditions in DCL.

- The behavior when an element is declared as optional element and is missing at runtime matches the one for literal conditions.

## Variant 1

`... ( element ) = ASPECT user_alias ...`

### Description

The value of the alias can be checked instead of the user name.

If the user does not have an alias, the condition behaves like the Boolean predicate `FALSE`.

## Variant 2

`... ( element ) = ASPECT user_business_partner_number ...`

### Description

The number of the business partner assigned to the user can be checked instead of the user name.

If the user does not have an assigned business partner, the condition behaves like the Boolean predicate `FALSE`.

## Addition

`... ALL|EXISTS`

### Description

The `ALL` or `EXISTS` quantifiers can be specified for user conditions and behave as for literal conditions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity contains an element `uname`, which contains a user name:

``` abap
@AccessControl.authorizationCheck: #CHECK
define view entity demo_cds_auth_user
  as select from
    abdocmode
    {
      key uname,
      key langu,
          flag
    }
```

The following role can be defined for the view:

``` abap
CDS or DDIC source code was not found
```

The role grants a user AS ABAP access to his or her own entries in the DDIC database table `ABDOCMODE`, as well as to entries in which the `UNAME` column is initial or contains a [null value](../../abap-glossary/abennull_value_glosry.md).

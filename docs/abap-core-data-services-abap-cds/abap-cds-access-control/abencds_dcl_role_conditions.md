---
title: "CDS DCL - DEFINE ROLE, condition"
source_file: abencds_dcl_role_conditions.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, condition

## Syntax

``` abap
... literal_condition 
  | pfcg_condition 
  | aspect_condition 
  | user_condition 
  | inherit_condition 
  | dcl_function 
  | TRUE 
  | FALSE 
  | VOID 
  | if_then_else ...  
```

[`literal_condition`](abencds_f1_cond_literal.md) · [`pfcg_condition`](abencds_f1_cond_pfcg.md) · [`aspect_condition`](abencds_f1_cond_aspect.md) · [`user_condition`](abencds_f1_cond_user.md) · [`inherit_condition`](abencds_f1_cond_inherit.md) · [`dcl_function`](abencds_f1_dcl_function.md) · [`if_then_else`](abencds_f1_dcl_ifthenelse.md)

## Description

Part of an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) [`cds_cond`](abencds_dcl_role_cond_expr.md) in an [access rule](../../abap-glossary/abenaccess_rule_glosry.md) of the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). The following categories of conditions can be specified, which can be combined using `AND` or `OR`:

- Literal conditions [`literal_condition`](abencds_f1_cond_literal.md) that compare an element of a CDS entity with fixed values.

- PFCG conditions [`pfcg_condition`](abencds_f1_cond_pfcg.md) that associate an element of a CDS entity with [authorizations](../../abap-glossary/abenauthorization_glosry.md) in the [SAP authorization concept](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) (which are based on [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md)).

- User-defined aspects [`aspect_condition`](abencds_f1_cond_aspect.md) that join elements in a CDS entity with value sets of any other entity that can itself be addressed using the current user name as a selection condition.

- User conditions [`user_condition`](abencds_f1_cond_user.md) as a special case of a literal condition on whose right side the user name of the current user is used as an operand.

- Inheritance conditions [`inherit_condition`](abencds_f1_cond_inherit.md) that apply conditions from other CDS roles.

- DCL functions [`dcl_function`](abencds_f1_dcl_function.md) are evaluated in the application server before the statement is sent to the database. The currently existing DCL functions return a Boolean predicate and in combination with `AND` and `OR` conditions allow enabling or disabling parts of the access conditions based on the function result.

- Boolean predicates `TRUE` and `FALSE`. These conditions are either always met or not met. They are usually not needed in a role definition, but can be created implicitly in the [inheritance of conditions](abencds_f1_cond_inherit.md).

- The predicate `VOID`. A condition with the value `VOID` is handled as nonexistent.

  ` VOID` conditions are not required in the definition of a role and can be created implicitly in inheritances. The following rules apply in combination with other conditions:

  - `X AND VOID = VOID AND X = X`

  - `X OR VOID = VOID OR X = X`

  - `NOT VOID = VOID`

  - An access rule cannot consist solely of `VOID` conditions.

- Control structures [`if_then_else`](abencds_f1_dcl_ifthenelse.md).

On the left side of a condition of this type, it is possible to specify elements of the CDS entity for which the access condition is defined directly or using [path expressions](../../abap-glossary/abenpath_expression_glosry.md). The following restrictions apply:

- Only certain [data types](abencds_f1_dcl_cond_data_types.md) are allowed.

- Path expressions `path_expr` in CDS DCL have the same syntax as [path expressions](../abap-cds-data-definitions/abencds_path_expression_v2.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

## Hints

- It is advisable to specify an `element` in a CDS entity directly in the CDS DCL and to only use path expressions in exceptional cases. More specifically, path expressions with multiple values can have a negative effect on the runtime of a [query](../../abap-glossary/abenasql_query_glosry.md).

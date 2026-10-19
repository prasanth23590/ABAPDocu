---
title: "CDS DCL - DEFINE ASPECT"
source_file: abencds_f1_define_generic_aspect.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ACCESSPOLICY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ASPECT

## Syntax

``` abap
 
[aspect_annot] 
[DEFINE] ASPECT aspect AS SELECT FROM aspect_entity 
  WITH USER ELEMENT user_element 
  [WITH FILTER ELEMENTS ( filter_element1 [AS filter_alias1], 
        filter_element2... ) ] 
{ 
    output1 [BYPASS WHEN aspect_bypass_condition] 
    [, ... ] 
}  
```

[`aspect_annot`](abencds_f1_dcl_as_annotations.md)

## Description

Defines a user-defined aspect `aspect` as part of a [CDS access policy](../../abap-glossary/abencds_access_policy_glosry.md) defined using [`DEFINE ACCESSPOLICY`](abencds_f1_define_accesspolicy.md). The name of the user-defined aspect must be the same as the name of the CDS access policy.

The definition of a user-defined aspect contains the following:

- An aspect entity `aspect_entity`, specified after the name `aspect`, which is used as a data source.

- An element `user_element` of the aspect entity that is used as the input field for the user name of the logged on user.

- An optional list of elements `filter_element` of the aspect entity. Using filter elements, the rows of the aspect entity can be reduced specifically for a usage location in an access role `( ( ...) = ASPECT ... FILTER BY` `condition>)`. Filter elements are addressed in the filter condition using the last component of their path expression. Optionally an alias can be specified by the ` AS` addition. Adding filter elements is a compatible change from the perspective of access roles using the aspect, that is, they offer a filtering possibility, but do not mandate that filtering is in fact done.

- A comma-separated list that specifies the output elements `output1, output2, ...` of the generic aspect. The specified order applies.

- Any number of the output fields can be tagged with a condition using the addition `BYPASS WHEN aspect_bypass_condition`. Typical bypass values are `*` or an empty value.

The following are possible as bypass conditions `aspect_bypass_condition`:

- [`IS [NOT] NULL`](../abap-cds-data-definitions/abencds_cond_expr_null_v2.md)

- [`IS [NOT] INITIAL`](../abap-cds-data-definitions/abencds_cond_expr_initial_v2.md)

- `IS INITIAL OR NULL`

  Is met if the value of the aspect is `NULL` or the type-compliant initial value.

- = [`literal`](../abap-cds-data-definitions/abencds_literal_v2.md)

At runtime, the field `user_element` is filled with the user name of the current user. The rows produced in the aspect entity are matched with their output fields in the specified order and with the elements on the left side of the access condition to which the user-defined aspect is assigned. This means those rows in the protected entity meet the condition for which a row exists for the current user in the aspect entity.

When the bypass condition is used, the match with this field is not used if this condition exists in a row of the aspect entity. A specified value, therefore, (such as an asterisk `*`) can be used to indicate that any values of the protected entity are allowed.

**Special Requirements in the Aspect Entity**

The content of the aspect entity has a particular relevance for audits by being used in a user-defined aspect in access control.

To determine which user had access to particular data at a particular time in a system, it must be possible to reconstruct the state of the data of the aspect entity. Existing mechanisms (such as version management or change documents) cover this requirement in the case of development objects or PFCG roles, whereas aspect entities may freely specify their data sources and cannot control whether these sources are themselves auditable.

The development and runtime systems for CDS access control cannot check whether data sources are auditable. To emphasize this requirement, however, the aspect entity must have the following annotations:

- An auditing type with the annotation `@AccessControl.auditing.type`. Currently only the value `#CUSTOM` is possible.

- A component with the annotation `@AccessControl.auditing.specification` specifying (as text) how the content of the entity is audited.

## Hints

- Just adding the annotations, however, does not activate auditing. This annotation should only be set if it is ensured that auditing takes place.

- Auditing must respect all data sources of the aspect entity.

- If auditing cannot be ensured, the aspect entity cannot be used in a user-defined aspect.

- In ABAP SQL access to a CDS entity assigned a role of this type, user-defined aspects are defined internally using a [subquery](../../abap-glossary/abensubquery_glosry.md) after `EXISTS`.

---
title: "CDS DCL - DEFINE ROLE"
source_file: abencds_f1_define_role.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE

## Syntax

``` abap
@MappingRole: true 
[@role_annot1] 
[@role_annot2] 
... 
[DEFINE] ROLE role_name [SWITCHABLE] { access_rules }  
```

[`@MappingRole: true`](abencds_f1_dcl_role_annotations.md) · [`@role_annot1`](abencds_f1_dcl_role_annotations.md) · [`@role_annot2`](abencds_f1_dcl_role_annotations.md) · [`access_rules`](abencds_dcl_role_rules.md)

### Addition

[1. `... SWITCHABLE ...`](abencds_f1_define_role.md#addition-1)

## Overview

### Description

Defines a [CDS role](../../abap-glossary/abencds_role_glosry.md) called `role_name` in the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). A CDS role consists of one or more access rules [`access_rules`](abencds_dcl_role_rules.md) specified within the curly brackets. Each access rule defines access to a [CDS](../../abap-glossary/abencds_entity_glosry.md) entity. A CDS role can contain access rules for different CDS entities. An access rule either defines an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) for the CDS entity or grants full access. When a CDS entity of this type is accessed using ABAP SQL, an access condition is evaluated as an additional selection condition.

Before the role is defined using `DEFINE ROLE`, the annotation [`@MappingRole`](abencds_f1_dcl_role_annotations.md) must be specified with the value `true`. The annotation [`@MappingRole`](abencds_f1_dcl_role_annotations.md) is used to assign the CDS role to every user regardless of the client. Further optional annotations [`role_annot1`](abencds_f1_dcl_role_annotations.md), [`role_annot2`](abencds_f1_dcl_role_annotations.md), ... can also be specified.

### Hints

- Every CDS role defined using `DEFINE ROLE` is assigned to every user implicitly, which means that the associated access control is applied to every user. User-specific checks are applied using [PFCG conditions](../../abap-glossary/abenpfcg_condition_glosry.md) and [user conditions](../../abap-glossary/abenuser_condition_glosry.md).

- A CDS role can be defined for a CDS entity in every package and in every system and specifies that implicit access control applies.

- Access control can be disabled for a CDS entity as follows:

  - Specify the annotation `@AccessControl.authorizationCheck` with the value `#NOT_ALLOWED` in the definition of the entity. In this case, the definition of a role for the CDS entity produces a syntax check warning in the DCL editor.

  - Use the addition [`[WITH] PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in ABAP SQL when the entity is accessed.

- Separate [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) must be created for each CDS role. The DCL source code of a CDS role is edited in a different editor from the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) (a [CDS view](../../abap-glossary/abencds_view_glosry.md) or [CDS table function](../../abap-glossary/abencds_table_function_glosry.md)) or a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md). The ADT documentation describes how the different types of source code are created.

## Addition 1

`... SWITCHABLE ...`

### Description

With this addition, the content of the role reacts to status changes in the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md) with respect to the package of the access control:

- If the package has no switch assigned or when it has a switch assigned with state *On*, the role content is generated.

- If a switch is assigned to the package and that switch has a state other than *On*, the role is generated with empty content, in particular, all rules in the role are no longer present at runtime.

### Hints

- The keyword `SWITCHABLE` can be applied to roles even if they are not in a switchable package. The keyword then has no function.

- Roles without the keyword `SWITCHABLE` can be in switchable packages. The role then does not react to the switch state and its content is always generated.

- If a switchable role is not generated due to the current switch state, the syntax check does not detect all errors in the rule content. It is possible to deliver access roles from a system where the role is not generated, causing import errors in a system where the role is generated.

- In a switchable role, you can use elements of the protected entity itself and of [CDS entity extensions](../../abap-glossary/abencds_entity_extend_glosry.md) of that entity, as long as they are located in the same package as the access control. The access control syntax checker issues an error message if an access rule violates this constraint.

- In a non-switchable role, you should only use elements of the protected entity itself and avoid using elements that are in switchable [CDS entity extensions](../../abap-glossary/abencds_entity_extend_glosry.md), because importing this role may cause syntax errors in systems where the package of the extension is switched off. The access control syntax checker issues a warning message for this constellation.

- In switchable roles, the addition [`COMBINATION MODE`](abencds_dcl_role_cond_rule.md) is mandatory, even if the chosen combination mode is [`OR`](abencds_dcl_role_cond_rule.md).

- In switchable roles, the addition [`REDEFINITION`](abencds_dcl_role_cond_rule.md) is not allowed.

- In switchable roles, using inheritance statements is not allowed.

- Switchable roles cannot be the source for role-based inheritance in another access control.

- Switchable roles can be part of entity-based inheritance in other access controls. The switch state is respected when the inheritance is resolved. This means that, in a system where the role is not generated, it is not part of the access conditions of the inheritance source because the access rule for the entity inside the role does not exist.

- Switchable roles respect the switchability of packages on a structural level and thus allow the use of elements of switched [CDS entity extensions](../../abap-glossary/abencds_entity_extend_glosry.md). In contrast to this, the DCL functions [`SWITCH_RUNTIME_STATE`](abencds_f1_dcl_function.md) and [`TOGGLE_RUNTIME_STATE`](abencds_f1_dcl_function.md) allow querying a switch state as a runtime-only check and are the preferred way to implement switch dependency if this need does not exist.

- A switchable role for a CDS entity can exist as the only access control for a CDS entity. For a switch state other than *On*, the entity then behaves as if no access control is defined. In conjunction with the entity annotation `@AccessControl.authorizationCheck: #MANDATORY`, this can lead to a runtime error when the entity is accessed.

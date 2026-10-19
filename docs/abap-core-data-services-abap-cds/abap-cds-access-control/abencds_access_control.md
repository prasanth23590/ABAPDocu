---
title: "ABAP CDS - Access Control"
source_file: abencds_access_control.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Access Control

ABAP CDS enables access control based on a [data control language (CDS DCL)](abencds_f1_dcl_syntax.md). Access control in ABAP CDS further restricts the data returned from a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in ABAP CDS. CDS access control is based on the following aspects:

- [CDS roles](../../abap-glossary/abencds_role_glosry.md) defined using the CDS DCL statement [`DEFINE ROLE`](abencds_f1_define_role.md). A CDS role is not assigned to individual users and is evaluated for every user instead.

- [Access rules](../../abap-glossary/abenaccess_rule_glosry.md) defined for [CDS entities](../../abap-glossary/abencds_entity_glosry.md) in a CDS role. [Access rules](abencds_dcl_role_rules.md) can define conditions, but also provide full access. In a CDS role, access rules can be inherited from another CDS entity or rule.

- [Access conditions](../../abap-glossary/abenaccess_condition_glosry.md) defined in an access rule for the elements of [CDS entities](../../abap-glossary/abencds_entity_glosry.md). Access conditions are based primarily on literal values, on classic [authorizations](../../abap-glossary/abenauthorization_glosry.md) of the current users, or on data from other CDS entities defined by a selection with the current user ([user-defined aspects](abencds_f1_define_generic_aspect.md)).

If a CDS role with access rules is defined for a [CDS entity](../../abap-glossary/abencds_non_sql_entity_glosry.md), the access conditions are evaluated implicitly in each [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) read, unless access control is switched off using the value `#NOT_ALLOWED` for the annotation `@AccessControl.authorizationCheck` or using the addition [`[WITH] PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in ABAP SQL. If access control is enabled, only that data is read that meets the access conditions.

Every CDS role is defined in its own separate piece of [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md). These pieces of DCL source code can only be edited in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). The DCL source code of a CDS role is edited in a different editor than [DDL](../../abap-glossary/abenddl_source_code_glosry.md), [DDLA](../../abap-glossary/abenddla_source_code_glosry.md), and [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md). The [ADT](../../abap-glossary/abenadt_glosry.md) documentation describes how the different types of source code are created.

## Hints

- When a CDS entity is used as a data source in another CDS entity, its access controls are not considered when the wrapping entity is accessed. CDS access control only applies to the entry level entities accessed by ABAP SQL. In other words, there is no automatic inheritance of CDS access control to higher layers of a CDS data model.

- It is advisable to continue to use classic authorization checks for start authorizations (used to check whether a user can start an application in the first place). CDS access control can be used within an application to perform authorization checks (used to check the authorization of a user as defined by the data model and the data in question).

- When CDS entities are accessed using ABAP SQL, ABAP programs cannot distinguish whether data is not read because it does not exist or because they are not allowed by CDS access control.

- CDS access control modifies the database selection performed by the application code. Although the amount of data returned is reduced, the additional filter work may have an affect on the statement performance. The effect depends on the complexity of the access control, the complexity of the protected CDS entity, the amount of data in the PFCG role data assigned to the user and the position of the protected entity in the concrete database statement.

- CDS roles can be defined for [CDS views](../../abap-glossary/abencds_view_glosry.md), [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md), [CDS transactional queries](../../abap-glossary/abencds_transactional_pv_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) and [CDS static external entities](../../abap-glossary/abencds_static_ee_glosry.md). Implicit access control is applied only when a CDS entity of this type is accessed directly using ABAP SQL.

- In emergency mode (user `SAP*`), CDS access control is disabled. This not only affects PFCG conditions but also literal access conditions and user-defined aspect conditions.

- The CDS entity annotation `@AccessControl.authorizationCheck` affects access control by its value:

  - `#NOT_REQUIRED` (default): When no access control exists, all users have full access to the entity. When an access control exists, it is evaluated.

  - `#CHECK`: The runtime behavior is identical to `#NOT_REQUIRED`, but there is a syntax check warning in the CDS entity if no access control object exists.

  - `#MANDATORY`: An access control must exist. If no access control has been created for the entity, a runtime error will occur when the entity is accessed in ABAP SQL. Use this for entities where access control is critical and accidental removal of the access control must not remain unnoticed.

  - `#NOT_ALLOWED`: No access control is allowed to exist. When an access control exists, it is ignored at runtime. Use this for technical entities where access control would be harmful. This value does not prevent the creation of access controls, but a warning message is issued that the access control is not applied at runtime.

  - `#PRIVILEGED_ONLY`: This special value is only evaluated by dedicated frameworks, such as [SADL](../../abap-glossary/abensadl_glosry.md). For ABAP SQL, the actual behavior is the same as `#CHECK`. Customers should not use this value unless explicitly requested by the documentation.

- Access control can be disabled in particular in the following ways:

  - If access control is not applicable in general (for example because the unit in question is a technical unit), the annotation `@AccessControl.authorizationCheck` with the value `#NOT_ALLOWED` can be specified in its CDS data definition.

  - If access control is not applicable only in specific places, the addition `WITH PRIVILEGED ACCESS` can be used in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of an ABAP SQL query to disable access control for the particular entity in use.

  - It is also possible to disable access control for an entire statement with the addition `PRIVILEGED ACCESS` as last position. This syntax variant in addition to the direct entity usage in the statement also covers usage by association traversal in ABAP SQL based on [path expressions](../../abap-glossary/abensql_path_expression_glosry.md) (introduced by the *\\* character).

  - Access control can be disabled for an entity (without making modifications) by creating a full access rule for the entity in a customer CDS role.

  - A CDS entity can also be used as a data source in another CDS entity for which access control is disabled.

- CDS access control provides an additional method for checking authorizations in the [SAP authorization concept](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md). Authorizations in the SAP authorization concept are based on [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) and are granted in the classic role maintenance (transaction PFCG). CDS access control expands these checks to include implicit evaluations of [access conditions](../../abap-glossary/abenaccess_condition_glosry.md).

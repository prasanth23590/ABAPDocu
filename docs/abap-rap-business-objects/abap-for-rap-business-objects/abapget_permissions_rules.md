---
title: "GET PERMISSIONS, Guidelines"
source_file: abapget_permissions_rules.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET PERMISSIONS, Guidelines

When using `GET PERMISSIONS` statements, the following aspects must be taken into consideration:

- Permission result consolidation and best practices

- RAP BO provider guidelines

- RAP BO consumer guidelines

- Best practices for authorization

**Permission Result Consolidation and Best Practices**

- The sequence of the implementation method (i. e. handler) calls is as follows: First, the method for global authorization is called followed by the methods for instance authorization, global features and instance features. This sequence has an impact on the permission result:

  - If global authorization fails for an element, this element is removed from the request for the following handler calls.

  - If global features disable an element, this element is removed from the request for the following handler calls.

  - If instance authorization fails for an instance, no further handlers are called for this instance.

- The result of the permission request can show merged information and follows specific principles:

  - Dynamic feature control is merged with authorization.

  - Global results for instance-based elements are merged with instance results. The following mapping of static features to instance results is applied:

    \- `readonly` is mapped to instance result `readonly`

    \- `readonly:update` is mapped to instance result `readonly`

    \- static `mandatory` is ignored in instance results

    \- static `mandatory:create` is ignored in instance results

    `mandatory` and `mandatory:create` are ignored because they are only relevant for create operations, and not for existing instances.

  - Global results contain only global and static information.

  - Static features results are always merged with global feature results.

  - Static feature control in projections overrides dynamic feature control of their bases.

  - Projections inherit static features from their [bases](../../abap-glossary/abenrap_projected_bo_glosry.md).

  - Static feature control that is not related to permissions, for example, [virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md) or fields with the notation [`numbering:managed`](../rap-behavior-definitions/abenbdl_field_numbering.md) in the BDEF, is not returned by the `GET PERMISSIONS` statement.

- The result contains only instances for which non-empty data has been returned by the relevant [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) implementations for the requested operations. That is, instances with no relevant restrictions are not contained in the permission result.

- If an instance has been reported as failed by any of the provider implementations, the result contains no entry for this instance even if other provider implementations may have returned valid results.

- There is at most one entry for each instance in the permission result (not taking the responses for `FAILED` and `REPORTED` into account here), even if `keys` contains duplicates.

- The result and the entries in the responses (that is, the response parameters for `FAILED` and `REPORTED`) can have a different order than the keys that are input.

- The responses may contain multiple entries for the same instance, for example, originating from different provider implementations, or specifying different fail causes.

**RAP BO Provider Guidelines**

- Authorization handlers or feature handlers must not assume that the key values they receive are verified, i.e. that they actually correspond to existing instances.

- The implementation should not return duplicate entries in the result.

- The result and the entries in the responses (that is, the response parameters for `FAILED` and `REPORTED`) should only contain instances from the provided keys, i. e. the implementation should not add other instances that are not related to the provided keys.

- The result should not contain empty entries, that is, entries where all fields except the key values are initial.

- The value range - as it is specified for the constants in interface `IF_ABAP_BEHV` - for the flags in the result and response parameters should be respected.

- As a rule, the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) should use certain constants that are available in the interface `IF_ABAP_BEHV`. Note that permissions are the result of merging authorization and feature control information, i. e. there are no permission handlers and, thus, no constants for permissions on provider side.

  - Authorization provider: `IF_ABAP_BEHV=>AUTH`

  - Feature provider: `IF_ABAP_BEHV=>FC`

  - Example: If the consumer receives a result for the permissions retrieval, the interpretation of the result must be done with care. For example, the result shows the value *'02'* for field permissions that stands for `read_only` (`IF_ABAP_BEHV=>PERM-F`). If the value `00` is returned in the result in this context, it can mean that there are no restrictions for the particular field. However, it can also mean the field is not enabled in the `request` parameter or the request has failed (in that case, the `responses` should be checked).

**RAP BO Consumer Guidelines**

- For results of operations and associations (global and instance), [`BIT-AND`](../../abap-programming-language/abap-processing-internal-data/abenbit_operators.md) can be used with the constants `PERM-O-UNAUTHORIZED` and `PERM-O-DISABLED` of interface `IF_ABAP_BEHV` to distinguish between missing authorization and disabled feature.

- For querying results of fields, [`BIT-AND`](../../abap-programming-language/abap-processing-internal-data/abenbit_operators.md) with the constants `PERM-F-...` of interface `IF_ABAP_BEHV` should be used. The static feature control `mandatory` is ignored.

- As a rule, the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) should use certain constants that are available in the interface `IF_ABAP_BEHV`:

  - `IF_ABAP_BEHV=>PERM`

**Best Practices for Authorization**

- The authorization for the standard operations `create`, `update`, and `delete` of a dependent entity specified in the BDEF are implemented by the handler for the standard operation update of its `authorization master`. For more information on the BDEF part for authorization, see the topic [RAP BDL - authorization](../rap-behavior-definitions/abenbdl_authorization.md).

- The authorization for the standard operations of `authorization master`, `create`, `update`, and `delete` are implemented by the handler of `authorization master`.

- For [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md), the authorization is implemented by handlers of the source entity.

- For [compositions](../../abap-glossary/abencds_composition_glosry.md), the authorization checking for create-by-association operations is handled like the authorization checking for `update` of the source entity. If the source entity is an authorization-dependent entity, the authorization checking happens on the `authorization master` (as `update` authorization). Authorizations for compositions can also be implemented. Hence, the authorization result for an update and these additional compositions are linked using [`OR`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_or.md).

- [Read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md) are handled by the provider internally and are not part of the permission concept.

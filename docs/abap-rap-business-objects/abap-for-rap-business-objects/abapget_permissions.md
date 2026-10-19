---
title: "GET PERMISSIONS"
source_file: abapget_permissions.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET PERMISSIONS

## Syntax Forms

**[`GET PERMISSIONS`, Short Form](abapget_permissions_short.md)**

``` abap
1. GET PERMISSIONS [[FORWARDING] PRIVILEGED] [only_clause] 
      ENTITY entity [FROM keys] REQUEST request RESULT result_tab [response_param].
```

**[`GET PERMISSIONS`, Long Form](abapget_permissions_long.md)**

``` abap
2. GET PERMISSIONS [[FORWARDING] PRIVILEGED] [only_clause] OF bdef 
     ENTITY entity1 [FROM keys] REQUEST request RESULT result_tab 
    [ENTITY entity2 [FROM keys] REQUEST request RESULT result_tab] 
    [...] 
    [response_param]. 
```

**[`GET PERMISSIONS`, Dynamic Form](abapget_permissions_dyn.md)**

``` abap
3. GET PERMISSIONS [[FORWARDING] PRIVILEGED] [only_clause] OPERATIONS perm_tab [response_param].
```

[`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`only_clause`](abapget_permissions_only_clause.md) · [`RESULT result_tab`](abapeml_result.md) · [`response_param`](abapeml_response.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`only_clause`](abapget_permissions_only_clause.md) · [`RESULT result_tab`](abapeml_result.md) · [`RESULT result_tab`](abapeml_result.md) · [`response_param`](abapeml_response.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`only_clause`](abapget_permissions_only_clause.md) · [`response_param`](abapeml_response.md)

## Description

Gets information about the permissions of RAP BOs. Permissions are defined at the operation and field level, for example, operations can be disabled and fields can be set to read-only. Permissions are checked when EML requests are processed by the RAP runtime but they can also be requested in advance by the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) using a `GET PERMISSIONS` statement. The permissions cover multiple aspects:

- [Global authorization and instance authorization](../rap-behavior-definitions/abenbdl_authorization.md)

  - Global authorization: Checks whether the current user is allowed to execute an operation in general, i. e. independent of the data to be processed, for example, a user must not change data.

  - Instance authorization: Authorization checks that can be defined based on a concrete value of an instance's field.

- [Global feature control and instance feature control](../rap-behavior-definitions/abenbdl_actions_fc.md)

  - [Global feature control](../../abap-glossary/abenrap_glo_feature_control_glosry.md): Feature controls that depend on external factors like specific user settings or the business scope.

  - [Instance feature control](../../abap-glossary/abenrap_ins_feature_control_glosry.md): Checks depending on the state of an entity instance.

- [Static feature control](../rap-behavior-definitions/abenbdl_field_char.md): Specifies individual fields of an entity that have certain access restrictions, for example, fields that are marked as `readonly` in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md).

For all characteristics, the permission retrieval must be user-implemented in RAP BO provider implementations except for static feature controls. In latter case, the access restriction is directly defined in the BDEF. One example is when a field is marked as `readonly`. Depending on the context, `GET PERMISSIONS` statements in [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) trigger the calling of the [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR [INSTANCE] AUTHORIZATION`](abaphandler_meth_auth.md), [`FOR [INSTANCE] FEATURES`](abaphandler_meth_features.md), [`FOR GLOBAL AUTHORIZATION`](abaphandler_meth_global_auth.md), or [`FOR GLOBAL FEATURES`](abaphandler_meth_global_features.md).

The handling and consolidation of the permission result as well as general best practices are outlined in the topic [`GET PERMISSIONS`, Guidelines](abapget_permissions_rules.md). One example is when the permission result contains merged information. Among others, static feature controls are merged with global feature controls.

Permissions can be retrieved for the following:

- Create, update and delete operations

- Associations with [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md)

- Fields

- Actions

- Functions

**Note:** Permissions cannot be retrieved for [internal](../rap-behavior-definitions/abenbdl_internal.md) elements like internal associations and internal actions. For [virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md) in projections, there are only static features available.

The following variants of the `GET PERMISSIONS` statement can be used:

- [`GET PERMISSIONS`, Short Form](abapget_permissions_short.md)

  Used to retrieve information on permissions for instances of a single entity.

- [`GET PERMISSIONS`, Long Form](abapget_permissions_long.md)

  Used for collecting multiple queries on multiple entities of a RAP BO.

- [`GET PERMISSIONS OPERATIONS`, Dynamic Form](abapget_permissions_dyn.md)

  Collects permission queries of multiple RAP BO entities in one `GET PERMISSIONS` statement.

## Hints

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

- CDS projection views of the type [transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) can define a `WHERE` clause to filter the result set. By default, this `WHERE` clause in the projection layer is ignored when a BDEF is accessed with the `GET PERMISSIONS` statement. This means that it is possible to read and modify entity instances that are not part of the projection BDEF's or interface BDEF's result set. This behavior may pose a security risk.

  To mitigate this risk, a dedicated BDEF syntax is available to enforce evaluation of the `WHERE` clause defined in the projection layer: [`with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md). For further details, see [RAP - `with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md).

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

## Executable Example

- The example [ABAP EML - `GET PERMISSIONS`, Variants](abenget_perm_forms_abexa.md) demonstrates the different variants with a simple managed RAP BO.

- The example [ABAP EML - `GET PERMISSIONS`, `only_clause`](abenget_perm_only_abexa.md) demonstrates the different variants of the `only_clause` with a simple managed RAP BO.

- The example [ABAP EML - RAP Calculator (Unmanaged)](abeneml_calculator_abexa.md) uses a `GET PERMISSIONS` statement with a simple unmanaged RAP BO. In this case, permissions are requested if a calculation based on entries provided is possible or not. For example, it is disallowed if a division by 0 should be executed.

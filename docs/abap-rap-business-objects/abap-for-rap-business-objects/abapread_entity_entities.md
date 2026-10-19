---
title: "READ ENTITY, ENTITIES"
source_file: abapread_entity_entities.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITY, ENTITIES

## Syntax Forms

**[`READ ENTITY`, Short Form](abapread_entity_short.md)**

``` abap
1. READ ENTITY [IN LOCAL MODE [WITH CHANGES]|[FORWARDING] PRIVILEGED] 
    entity operations [response_param].
```

**[`READ ENTITIES`, Long Form](abapread_entities_long.md)**

``` abap
2. READ ENTITIES OF bdef[IN LOCAL MODE|[FORWARDING] PRIVILEGED] 
    ENTITY entity1 operations 
    [ENTITY entity2 operations] 
    [...] 
    [WITH CHANGES] 
    [response_param].
```

**[`READ ENTITIES OPERATIONS`, Dynamic Form](abapread_entities_operations.md)**

``` abap
3. READ ENTITIES [IN LOCAL MODE|[FORWARDING] PRIVILEGED] OPERATIONS op_tab [response_param].
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`WITH CHANGES`](abapeml_read_with_changes.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`operations`](abapread_entity_entities_op.md) · [`response_param`](abapeml_response.md) · [`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`operations`](abapread_entity_entities_op.md) · [`operations`](abapread_entity_entities_op.md) · [`WITH CHANGES`](abapeml_read_with_changes.md) · [`response_param`](abapeml_response.md) · [`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`response_param`](abapeml_response.md)

## Description

Used to perform read-only operations on [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). Read operations always return a result and can be performed on RAP BO entities by default (except for the [abstract](../rap-behavior-definitions/abenbdl_abstract.md) implementation type) provided that the entities are part of a [behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) after a declaration using [`define behavior for`](../rap-behavior-definitions/abenbdl_define_beh.md).

The following variants of the `READ` statement can be used to read from RAP BO entities:

- [`READ ENTITY`, Short Form](abapread_entity_short.md)

  The short form of the `READ` statement allows reading multiple instances of a single entity.

- [`READ ENTITIES`, Long Form](abapread_entities_long.md)

  The long form of the `READ` statement allows reading multiple instances of multiple entities.

- [`READ ENTITIES OPERATIONS`, Dynamic Form](abapread_entities_operations.md)

  The dynamic form of the `READ` statement allows collecting multiple instances to be read in multiple entities in one `READ` statement.

## Hints

- ABAP EML is used to read RAP BO node instances. From a RAP BO consumer perspective, the returned data of read operations include the current transactional image, i. e. the currently persisted values in the database and, additionally, the still unsaved changes from the current [LUW](../../abap-glossary/abenluw_glosry.md).

- ABAP EML `READ` statements in [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) trigger the calling of [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR READ`](abaphandler_meth_read.md).

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

- CDS projection views of the type [transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) can define a `WHERE` clause to filter the result set. By default, this `WHERE` clause in the projection layer is ignored when a BDEF is accessed with EML `READ` requests. This means that it is possible to read and modify entity instances that are not part of the projection BDEF's or interface BDEF's result set. This behavior may pose a security risk.

  To mitigate this risk, a dedicated BDEF syntax is available to enforce evaluation of the `WHERE` clause defined in the projection layer: [`with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md). For further details, see [RAP - `with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md).

- [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) may contain [CDS virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md). For these, ABAP EML read operations are not supported.

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

## Executable Example

- The example [ABAP EML - `READ`, Variants](abeneml_read_alternatives_abexa.md) demonstrates the different variants with a simple managed RAP BO.

- For more examples, see [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).

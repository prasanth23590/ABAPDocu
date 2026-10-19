---
title: "MODIFY ENTITY, ENTITIES"
source_file: abapmodify_entity_entities.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITY, ENTITIES

## Syntax Forms

**[`MODIFY ENTITY`, Short Form](abapmodify_entity_short.md)**

``` abap
1. MODIFY ENTITY [IN LOCAL MODE|[FORWARDING] PRIVILEGED] entity operations [response_param].
```

**[`MODIFY ENTITIES`, Long Form](abapmodify_entities_long.md)**

``` abap
2. MODIFY ENTITIES OF bdef [IN LOCAL MODE|[FORWARDING] PRIVILEGED] 
           ENTITY entity1 operations 
          [ENTITY entity2 operations] 
          [...] 
          [response_param]. 
```

**[`MODIFY ENTITIES OPERATIONS`, Dynamic Form](abapmodify_entities_operations_dyn.md)**

``` abap
3. MODIFY ENTITIES [IN LOCAL MODE|[FORWARDING] PRIVILEGED] OPERATIONS op_tab [response_param].
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`operations`](abapmodify_entity_entities_op.md) · [`response_param`](abapeml_response.md) · [`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`operations`](abapmodify_entity_entities_op.md) · [`operations`](abapmodify_entity_entities_op.md) · [`response_param`](abapeml_response.md) · [`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING`](abapeml_privileged.md) · [`PRIVILEGED`](abapeml_privileged.md) · [`response_param`](abapeml_response.md)

## Description

Used to perform [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) on [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). This includes [standard operations](../../abap-glossary/abencrud_glosry.md) (`CREATE`, `CREATE BY`, `UPDATE`, `DELETE`) and nonstandard operations (actions) using the keyword `EXECUTE`.

The following variants of the `MODIFY` statement can be used to modify RAP BO entities:

- [`MODIFY ENTITY`, Short Form](abapmodify_entity_short.md)

  The short form of the `MODIFY` statement allows modifying instances of a single entity.

- [`MODIFY ENTITIES`, Long Form](abapmodify_entities_long.md)

  The long form of the `MODIFY` statement allows modifying instances of multiple entities.

- [`MODIFY ENTITIES OPERATIONS`, Dynamic Form](abapmodify_entities_operations_dyn.md)

  The dynamic form of the `MODIFY` statement allows collecting multiple instances to be modified in multiple entities in one `MODIFY` statement.

## Hints

- A [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) must not use ABAP EML `MODIFY` statements in the [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) [`check_before_save`](abensaver_check_before_save.md), [`adjust_numbers`](abensaver_adjust_numbers.md), [`save`](abensaver_method_save.md), [`save_modified`](abaprap_saver_meth_save_modified.md) and [`cleanup`](abensaver_method_cleanup.md). The statements can only be used in the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and in the [`finalize`](abensaver_finalize.md) saver method in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). Furthermore, ABAP EML `MODIFY` statements are not allowed in read-only [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md).

- ABAP EML `MODIFY` statements in [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) trigger the calling of [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](abaphandler_meth_modify.md).

- RAP modify [standard operations](../../abap-glossary/abenrap_standard_operation_glosry.md) do not return [result](abapeml_result.md) parameters, whereas [non-standard operations](../../abap-glossary/abenrap_nstandard_operation_glosry.md) do so. The changed data can be read via a subsequent ABAP EML `READ` statement.

- RAP BO instances can only be modified if several conditions are met. For example, a modification can be prevented depending on certain specifications in the BDEF, among them control characteristics like (global or instance) [authorization](../rap-behavior-definitions/abenbdl_authorization.md) and [feature control](../rap-behavior-definitions/abenbdl_actions_fc.md), [locking](../rap-behavior-definitions/abenbdl_locking.md), [ETag](../rap-behavior-definitions/abenbdl_etag.md) or [prechecks](../rap-behavior-definitions/abenbdl_precheck.md). See more detailed information on the mentioned topics in the Development guide for the ABAP RESTful Application Programming Model, section [Business Object](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/a3ff9dcdb25a4f1a9408422b8ba5fa00?version=sap_cross_product_abap).

- If ABAP EML modify statements are used outside of behavior pools, for example, in ABAP programs, a [`COMMIT ENTITIES`](abapcommit_entities.md) statement is necessary to persist data to the database. If the statement is not provided, there would not be any effect on the database because the modify operations are only performed on the transactional buffer. Hence, a manual triggering of the save sequence is required. This is valid for all modify operations. Note that RAP supports the established [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) concept that incorporates [`COMMIT WORK`](../../abap-programming-language/abap-database-access/abapcommit.md). In RAP, `COMMIT ENTITIES` basically includes `COMMIT WORK` and provides additional information.

- When executing independent modify requests, there is no dedicated processing sequence. However, the processing sequence is relevant if the modify requests are dependent, for example, when using [`%cid`](abapderived_types_comp.md) or [`%cid_ref`](abapderived_types_comp.md) or in case of [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md) that can be dependent on a previous operation. To ensure the processing sequence when executing independent modify requests, it is recommended that separate EML statements are used. In the interest of a better performance, requests should preferably be executed in a bundled way.

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

- A special `MODIFY ENTITY`/`MODIFY ENTITIES` variant exists that includes the keyword `AUGMENTING` with which incoming requests can be modified on the projection layer before data reaches the transactional buffer. The variant can currently only be used for projections. See the details in the documentation for [`MODIFY AUGMENTING ENTITY, ENTITIES`](abapmodify_aug_entity_entities.md).

- In case of a non-dynamic ABAP EML `MODIFY` statement without the addition `IN LOCAL MODE` and without specifying the `FAILED` response parameter, it is recommended that the `FAILED` response parameter is specified and that proper error handling on the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) side is implemented. Otherwise, a syntax warning occurs, which can be suppressed using the pragma `##EML_FAILED_MISSING_OK`.

- CDS projection views of the type [transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) can define a `WHERE` clause to filter the result set. By default, this `WHERE` clause in the projection layer is ignored when a BDEF is accessed with EML `MODIFY` requests. This means that it is possible to read and modify entity instances that are not part of the projection BDEF's or interface BDEF's result set. This behavior may pose a security risk.

  To mitigate this risk, a dedicated BDEF syntax is available to enforce evaluation of the `WHERE` clause defined in the projection layer: [`with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md). For further details, see [RAP - `with managed instance filter`](../rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md).

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

## Executable Examples

- The example [ABAP EML - `MODIFY`, Variants](abeneml_modify_alternatives_abexa.md) demonstrates the different variants with a simple managed RAP BO.

- For more examples, see [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).

- The example [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md) demonstrates various RAP handler methods within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled. It includes ABAP EML requests with `MODIFY` in a RAP consumer and provider.

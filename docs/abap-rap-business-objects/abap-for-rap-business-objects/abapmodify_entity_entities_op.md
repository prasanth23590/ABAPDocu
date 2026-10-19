---
title: "MODIFY ENTITY, ENTITIES, operations"
source_file: abapmodify_entity_entities_op.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITY, ENTITIES, operations

## Syntax

``` abap
... [CREATE field_spec] 
    [CREATE BY \_assoc field_spec] 
    [UPDATE field_spec] 
    [DELETE field_spec] 
    [EXECUTE action field_spec [REQUEST request] [RESULT result_tab]] ...  
```

[`field_spec`](abapmodify_entity_entities_fields.md) · [`field_spec`](abapmodify_entity_entities_fields.md) · [`field_spec`](abapmodify_entity_entities_fields.md) · [`field_spec`](abapmodify_entity_entities_fields.md) · [`field_spec`](abapmodify_entity_entities_fields.md) · [`RESULT result_tab`](abapeml_result.md)

### Variant

[1. `... CREATE field_spec`](abapmodify_entity_entities_op.md#variant-1)

[2. `... CREATE BY \_assoc field_spec`](abapmodify_entity_entities_op.md#variant-2)

[3. `... UPDATE field_spec`](abapmodify_entity_entities_op.md#variant-3)

[4. `... DELETE field_spec`](abapmodify_entity_entities_op.md#variant-4)

[5. `... EXECUTE action field_spec`](abapmodify_entity_entities_op.md#variant-5)

## Overview

### Description

The EML `MODIFY` statement supports the following operations:

- `CREATE`: Create new RAP BO node instances for root or child entities.

- `CREATE BY`: Create target instances for associated entities for which `create` must be enabled in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). The creation is not restricted to compositions.

- `UPDATE`: Update existing RAP BO node instances.

- `DELETE`: Delete existing RAP BO node instances. Note that the deletion also affects node instances along the composition.

- `EXECUTE` [actions](../rap-behavior-definitions/abenbdl_action.md): Carry out user-defined modify operations.

In both, managed and unmanaged implementations, all modify operations must be specified in the [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md). See more details in the BDL documentation: [`Define Behavior, Standard Operations`](../rap-behavior-definitions/abenbdl_standard_operations.md). All nonstandard operations (actions) must be user-implemented in the [ABP](../../abap-glossary/abenbehavior_pool_glosry.md).

Each modify operation requires an internal table (`field_spec`) of instances as input parameters after the respective keyword to specify the fields that should be modified.

### Hints

- After the keyword `BY` for create-by-association operations, a backslash (`\`) must be inserted in front of the associations are displayed via the code completion.

- Updating and deleting instances via associations is not possible.

- In [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios, draft instances are created if the draft indicator [`%is_draft`](abapderived_types_is_draft.md) is set to true. If it is set to false, active instances are created.

## More Information

See further information and rules for using ABAP EML statements in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and [consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) in the Development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

## Variant 1

`... CREATE field_spec`

### Description

Used to create new node instances of a [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) entity.

For the keywords that must follow the keyword `CREATE`, see the documentation for [`field_spec`](abapmodify_entity_entities_fields.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OP_2` demonstrates a `CREATE` operation.

``` abap
MODIFY ENTITY demo_managed_root 
CREATE FIELDS ( key_field data_field1_root data_field2_root ) 
WITH VALUE #( 
    ( %cid = 'cid1' key_field = 1 
      data_field1_root = 'aaa' data_field2_root = 'bbb' ) 
    ( %cid = 'cid2' key_field = 2 
      data_field1_root = 'ccc' data_field2_root = 'ddd' ) 
    ( %cid = 'cid3' key_field = 3 
      data_field1_root = 'eee' data_field2_root = 'fff' ) 
    ( %cid = 'cid4' key_field = 4 
      data_field1_root = 'ggg' data_field2_root = 'hhh' ) 
          ).
```

## Variant 2

`... CREATE BY \_assoc field_spec`

### Description

Used to create new node instances for associated entities for which `create` must be enabled in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). The creation is not restricted to compositions. `_assoc` is the name of the association as it is specified in the underlying CDS view.

For the keywords that must follow the keyword `CREATE`, see the documentation for [`field_spec`](abapmodify_entity_entities_fields.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OP_2` demonstrates a create-by-association operation.

``` abap
MODIFY ENTITY demo_managed_root 
CREATE BY \_child 
FIELDS ( data_field1_child data_field2_child ) 
WITH VALUE #( 
  ( key_field = 1 
    %target = VALUE #( ( %cid = 'cid3' 
                         data_field1_child = 'iii' 
                         data_field2_child = 'jjj' ) ) ) 
  ( key_field = 2 
    %target = VALUE #( ( %cid = 'cid4' 
                         data_field1_child = 'kkk' 
                         data_field2_child = 'lll' ) ) ) ).
```

## Variant 3

`... UPDATE field_spec`

### Description

Used to update node instances of a RAP BO. The `UPDATE` statement allows delta updates on [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) side to be triggered where only key fields and the fields with new values must be provided. On [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) side, the fields to be overwritten and kept are identified.

For the keywords that must follow the keyword `UPDATE`, see the documentation for [`field_spec`](abapmodify_entity_entities_fields.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OP_2` demonstrates an `UPDATE` operation.

``` abap
MODIFY ENTITY demo_managed_root 
UPDATE FIELDS ( data_field1_root data_field2_root ) 
WITH VALUE #( 
    ( key_field = 3 
      data_field1_root = 'qqq' 
      data_field2_root = 'rrr' ) 
    ( key_field = 4 
      data_field1_root = 'sss' 
      data_field2_root = 'ttt' ) ).
```

## Variant 4

`... DELETE field_spec`

### Description

Used to delete instances of a RAP BO. Only key field values or [`%cid_ref`](abapderived_types_comp.md) are needed to identify which instances are to be deleted.

For the keywords that must follow the keyword `DELETE`, see the documentation for [`field_spec`](abapmodify_entity_entities_fields.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OP_2` demonstrates a `DELETE` operation.

``` abap
MODIFY ENTITY demo_managed_root 
DELETE FROM VALUE #( ( key_field = 4  ) ).
```

## Variant 5

`... EXECUTE action field_spec [REQUEST request] [RESULT result_tab]`

### Addition

[1. `... REQUEST request`](abapmodify_entity_entities_op.md#addition-1)

[2. `... RESULT result_tab`](abapmodify_entity_entities_op.md#addition-2)

### Description

Used to trigger custom actions that are defined to modify data in a user-implemented way. The syntax for executing an `action` allows requested data (`REQUEST request`) to be specified and result data (`RESULT result_tab`) to be exported, each action specified in target variables.

For the keywords that must follow the keyword `EXECUTE` and the action name, see the documentation for [`field_spec`](abapmodify_entity_entities_fields.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_CDS_PURCHASE` demonstrates a modify operation executing an action.

``` abap
MODIFY ENTITIES OF demo_cds_purch_doc_m 
  ENTITY PurchaseDocument 
  EXECUTE approve_order 
  FROM VALUE #( ( PurchaseDocument = 'a' ) ) 
  RESULT FINAL(result) 
  FAILED FINAL(failed) 
  REPORTED FINAL(reported).
```

## Addition 1

`... REQUEST request`

### Description

Used to specify whether the result should be returned completely or only parts of it (for example, only the keys) for the purpose of improving performance. `request` must be typed with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR ACTION REQUEST`](abaptype_structure_for.md). The components of the structure are all key and data fields of the RAP BO entity. They are of type `ABP_BEHV_FLAG` and can be flagged to specify whether the respective fields are included or not.

This is optional and can only be used for actions specified in the BDEF with the addition [`result selective`](../rap-behavior-definitions/abenbdl_action_output_para.md).

## Addition 2

`... RESULT result_tab`

### Description

Actions can optionally return a result. This can only be used for actions specified in the BDEF with the addition [`result`](../rap-behavior-definitions/abenbdl_action_output_para.md). The internal table `result_tab` must be of type `TABLE FOR ACTION RESULT bdef~action`. See more details in [`RESULT result_tab`](abapeml_result.md).

### Executable Example

- The example [`MODIFY`: Standard Operations (Managed)](abeneml_modify_op_abexa.md) demonstrates various standard operations with `MODIFY`.

- The example [`MODIFY`: Nonstandard Operations](abeneml_modify_custom_op_abexa.md) shows the implementation of an action in the context of a managed RAP BO. See more examples of actions in the [documentation about RAP actions](../rap-behavior-definitions/abenbdl_action_abexas.md).

- The example [`MODIFY`: Standard Operations (Unmanaged)](abeneml_modify_op_u_abexa.md) demonstrates all standard operations with `MODIFY` with a simple unmanaged RAP BO.

- The example [Example for RAP Handler Methods (Unmanaged BO with draft)](abenrap_handler_methods_abexa.md) includes various standard and nonstandard ABAP EML `MODIFY` operations in both a [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and a [consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md).

- For more examples on `MODIFY` operations in general, see [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).

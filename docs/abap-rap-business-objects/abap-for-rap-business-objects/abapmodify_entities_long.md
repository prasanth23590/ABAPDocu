---
title: "MODIFY ENTITIES, Long Form"
source_file: abapmodify_entities_long.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITIES, Long Form

## Syntax

``` abap
MODIFY ENTITIES OF bdef [IN LOCAL MODE|[FORWARDING  ] PRIVILEGED  ] 
           ENTITY entity1 operations 
          [ENTITY entity2 operations] 
          [...] 
          [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`operations`](abapmodify_entity_entities_op.md) · [`operations`](abapmodify_entity_entities_op.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapmodify_entities_long.md#addition-1)

[2. `... [FORWARDING] PRIVILEGED ...`](abapmodify_entities_long.md#addition-2)

[3. `... response_param.`](abapmodify_entities_long.md#addition-3)

## Overview

### Description

The long form of the `MODIFY` statement is used for executing multiple modify operations ([`operations`](abapmodify_entity_entities_op.md)) on multiple entities of a RAP BO. However, it can also be used for a single operation on a single RAP BO.

`bdef` must be a [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) followed by a list of operations grouped by individual entities. `entity1`, `entity2`, and so on, must be entities contained in the [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the root entity `bdef`. If specified in the BDEF, alias names should be used for `entity1`, `entity2`, and so on. The root entity itself can also be inserted in the position of `bdef1`, for example. Each part of the list of operations specified after `MODIFY ENTITIES OF bdef` has the same syntax as the short form. At least one entry (`ENTITY bdef/entity1/...` with an operation) must be specified. The same entity can be specified after `ENTITY` repeatedly, however, the same operation in that combination is allowed only once.

### Hint

A [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) must not use ABAP EML `MODIFY` statements in the [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) [`check_before_save`](abensaver_check_before_save.md), [`adjust_numbers`](abensaver_adjust_numbers.md), [`save`](abensaver_method_save.md), [`save_modified`](abaprap_saver_meth_save_modified.md) and [`cleanup`](abensaver_method_cleanup.md). The statements can only be used in the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and in the [`finalize`](abensaver_finalize.md) saver method in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). Furthermore, ABAP EML `MODIFY` statements are not allowed in read-only [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md).

## Addition 1

`... IN LOCAL MODE ...`

### Description

The addition [`IN LOCAL MODE`](abapin_local_mode.md) is used to exclude [feature controls](../rap-behavior-definitions/abenbdl_actions_fc.md) and [authorization checks](../rap-behavior-definitions/abenbdl_authorization.md). It can only be used within the RAP BO runtime implementation.

### Hint

In case of a non-dynamic ABAP EML `MODIFY` statement without the addition `IN LOCAL MODE` and without specifying the `FAILED` response parameter, it is recommended that the `FAILED` response parameter is specified and that proper error handling on the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) side is implemented. Otherwise, a syntax warning occurs, which can be suppressed using the pragma `##EML_FAILED_MISSING_OK`.

## Addition 2

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 3

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY` demonstrates an EML `MODIFY ENTITIES OF` statement that includes `CREATE`, `UPDATE` and create-by-association operations.

``` abap
MODIFY ENTITIES OF demo_managed_root 
    ENTITY demo_managed_root 
        CREATE FIELDS ( key_field data_field1_root 
          data_field2_root ) WITH VALUE #( 
          ( %cid = 'cid5' 
            key_field = 3 
            data_field1_root = 'iii' 
            data_field2_root = 'jjj' ) 
          ( %cid = 'cid6' 
            key_field = 4 
            data_field1_root = 'kkk' 
            data_field2_root = 'lll' ) ) 
    ENTITY demo_managed_root 
        UPDATE FIELDS ( data_field1_root 
          data_field2_root ) WITH VALUE #( 
          ( %cid_ref = 'cid6' 
            data_field1_root = 'mmm' 
            data_field2_root = 'nnn' ) ) 
    ENTITY demo_managed_root 
        CREATE BY \_child FIELDS ( data_field1_child 
          data_field2_child ) WITH VALUE #( 
          ( %cid_ref = 'cid5' 
            %target = VALUE #( ( %cid = 'cid7' 
                                 data_field1_child = 'eee' 
                                 data_field2_child = 'fff' ) 
                             ) ) 
          ( %cid_ref = 'cid6' 
            %target = VALUE #( ( %cid = 'cid8' 
                                 data_field1_child = 'ggg' 
                                 data_field2_child = 'hhh' ) 
                             ) ) ) 
    ENTITY child 
        UPDATE FIELDS ( data_field1_child 
            data_field2_child ) WITH VALUE #( 
          ( %cid_ref = 'cid8' 
            data_field1_child = 'ooo' 
            data_field2_child = 'ppp' ) ) 
        FAILED   FINAL(fail_mod) 
        REPORTED FINAL(rep_mod) 
        MAPPED   FINAL(map_mod).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The root entity name in the position of the first statement, `MODIFY ENTITIES OF bdef`, must be the full entity name. `entity1`, and so on, should be the entity alias names if provided in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). Using the full entity name will cause a warning. If the root entity is used in the list of operations, its alias name, if defined in the BDEF, should be used as well.

For example, an alias name is specified for root and child entity as in the BDEF `DEMO_RAP_MANAGED_GROUP`. A statement with `MODIFY ENTITIES OF` could be as follows:

``` abap
MODIFY ENTITIES OF demo_rap_managed_group 
  ENTITY RootEntity 
    CREATE FIELDS ( keyfieldroot charfieldroot datafieldroot ) 
    WITH VALUE #( 
        (  %cid = 'cid1' keyfieldroot = 1 
           datafieldroot = 'aaa' charfieldroot = 'bbb' ) 
        (  %cid = 'cid2' keyfieldroot = 2 
           datafieldroot = 'ccc' charfieldroot = 'ddd' ) 
              ) 
  ENTITY ChildEntity 
    DELETE FROM VALUE #( 
        ( keyfield = 3 keyfieldchild = 4 ) 
        ( keyfield = 5 keyfieldchild = 6 ) 
              ).
```

### Executable Example

- The example [ABAP EML - `MODIFY`, Variants](abeneml_modify_alternatives_abexa.md) demonstrates this `MODIFY` variant with a simple managed RAP BO.

- For more examples on `MODIFY` operations in general, see [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).

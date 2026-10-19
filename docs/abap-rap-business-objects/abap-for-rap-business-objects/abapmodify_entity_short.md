---
title: "MODIFY ENTITY, Short Form"
source_file: abapmodify_entity_short.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITY, Short Form

## Syntax

``` abap
MODIFY ENTITY [IN LOCAL MODE|[FORWARDING  ] PRIVILEGED  ] entity operations [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`operations`](abapmodify_entity_entities_op.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapmodify_entity_short.md#addition-1)

[2. `... [FORWARDING] PRIVILEGED ...`](abapmodify_entity_short.md#addition-2)

[3. `... response_param.`](abapmodify_entity_short.md#addition-3)

## Overview

### Description

The short form of the `MODIFY` statement is used to perform transactional modify operations ([`operations`](abapmodify_entity_entities_op.md)) for a single RAP BO node.

`entity` can be any node of the RAP BO when the statement is used within the implementation class. If the statement is used outside of the implementation class, `entity` can only be the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md). `entity` must be the full entity name and cannot be an alias name. It is also possible to specify any node of the RAP BO following the root entity name and `\\`:

``` abap
MODIFY ENTITY root_entity\\bdef_node1 ... 
MODIFY ENTITY root_entity\\bdef_node2 ... 
...
```

`bdef_node1`, `bdef_node2`, and so on, must be the alias names if provided in the BDEF. Otherwise, the full names must be inserted.

Multiple operations can be inserted for `operations` within a single `MODIFY` statement.

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

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY` demonstrates an EML `MODIFY ENTITY` statement that includes a `CREATE` and create-by-association operation.

``` abap
MODIFY ENTITY demo_managed_root 
      CREATE FIELDS ( key_field data_field1_root 
          data_field2_root ) WITH VALUE #( 
        ( %cid = 'cid1' key_field = 1 
          data_field1_root = 'aaa' data_field2_root = 'bbb' ) 
        ( %cid = 'cid2' key_field = 2 
          data_field1_root = 'ccc' data_field2_root = 'ddd' ) ) 
      CREATE BY \_child FIELDS ( data_field1_child 
          data_field2_child ) WITH VALUE #( 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( ( %cid = 'cid3' 
                               data_field1_child = 'eee' 
                               data_field2_child = 'fff' ) 
                           ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( ( %cid = 'cid4' 
                               data_field1_child = 'ggg' 
                               data_field2_child = 'hhh' ) 
                           ) ) 
        ) 
        FAILED   FINAL(fail_mod) 
        REPORTED FINAL(rep_mod) 
        MAPPED FINAL(map_mod).
```

## Executable Examples

- The example [ABAP EML - `MODIFY`, Variants](abeneml_modify_alternatives_abexa.md) demonstrates this `MODIFY` variant with a simple managed RAP BO.

- For more examples on `MODIFY` operations in general, see [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).

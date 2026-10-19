---
title: "COMMIT ENTITIES RESPONSES, Dynamic Form"
source_file: abapemlcommit_entities_dyn.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES RESPONSES, Dynamic Form

## Syntax

``` abap
COMMIT ENTITIES [IN SIMULATION MODE] RESPONSES OF dyn_tab response_param  .  
```

[`response_param `](abapeml_response.md)

### Addition

[`... IN SIMULATION MODE`](abapemlcommit_entities_dyn.md#addition)

## Overview

### Description

Triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and completes the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). All transactional changes in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), that is, [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) created, modified, or deleted within the RAP transaction, are persisted to the database.

The `RESPONSES OF` addition to the `COMMIT ENTITIES` statement allows you to retrieve [`FAILED`](abapeml_response.md) and [`REPORTED`](abapeml_response.md) responses from the [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) by dynamically specifying one or more [RAP BO root entities](../../abap-glossary/abenrap_bo_root_entity_glosry.md) in `dyn_tab`.

Notes on the syntax:

- `dyn_tab` must be of type `ABP_ENTITY_NAME_TAB`. The components are the names of the root entities. They must be typed with `ABP_ROOT_ENTITY_NAME`.

- The parameters following `FAILED` and `REPORTED` must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`. For more information on `response_param`, see [here](abapeml_response.md).

For general hints on using the statement see the topic [`COMMIT ENTITIES`](abapcommit_entities.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_COMMIT_2` demonstrates the dynamic form of the `COMMIT ENTITIES` statement.

``` abap
DATA: root_name1 TYPE abp_root_entity_name 
                 VALUE 'DEMO_MANAGED_ASSOC_CUSTOM', 
      root_name2 TYPE abp_root_entity_name 
                 VALUE 'DEMO_MANAGED_ROOT_2'. 
 
FINAL(dyn_tab) = VALUE abp_entity_name_tab( ( root_name1 ) 
                                            ( root_name2 ) ). 
 
COMMIT ENTITIES 
 RESPONSES OF dyn_tab 
  FAILED   FINAL(failed) 
  REPORTED FINAL(reported).
```

### Hints

- `COMMIT ENTITIES` statements are not allowed in [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md).

- When using `COMMIT ENTITIES` statements, a check of `sy-subrc` should be included to avoid syntax warnings. If responses are retrieved, it is recommended that the response parameter `failed` is checked so as to react accordingly. See the topic [`COMMIT ENTITIES`](abapcommit_entities.md) for more information.

## Addition

`... IN SIMULATION MODE`

### Description

Used to process a save in simulation mode. See more information in topic [`COMMIT ENTITIES`, `IN SIMULATION MODE`](abapcommit_entities_simulation.md).

### Executable Example

The example [`COMMIT ENTITIES`, Dynamic Form](abeneml_commit_dyn_abexa.md) demonstrates the use of the dynamic form of the `COMMIT ENTITIES` statement.

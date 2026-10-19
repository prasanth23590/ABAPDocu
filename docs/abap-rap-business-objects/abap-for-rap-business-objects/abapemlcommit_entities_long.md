---
title: "COMMIT ENTITIES RESPONSE OF, Long Form"
source_file: abapemlcommit_entities_long.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES RESPONSE OF, Long Form

## Syntax

``` abap
COMMIT ENTITIES [IN SIMULATION MODE] RESPONSE OF bdef1 response_param   
                                    [RESPONSE OF bdef2 response_param  ] 
                                    [...].  
```

[`response_param `](abapeml_response.md) · [`response_param `](abapeml_response.md)

### Addition

[`... IN SIMULATION MODE`](abapemlcommit_entities_long.md#addition)

## Overview

### Description

Triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and completes the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). All transactional changes in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), that is, [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) created, modified, or deleted within the RAP transaction, are persisted to the database.

The long syntax form of the `COMMIT ENTITIES` statement includes the retrieval of information returned by the `FAILED` and `REPORTED` response parameters of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) for multiple [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md). [`FAILED`](abapeml_response.md) and [`REPORTED`](abapeml_response.md) responses can be retrieved for one or more RAP BOs that have been modified beforehand. `bdef1`, `bdef2`, etc., must be the names of root entities.

The responses of each involved BO must be requested separately. The operands following the additions `FAILED` and `REPORTED` must be of type [`TYPE RESPONSE FOR FAILED LATE`](abaptype_response_for.md) or [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md) respectively. For more information on `response_param`, see [here](abapeml_response.md).

For general hints on using the statement see the topic [`COMMIT ENTITIES`](abapcommit_entities.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_COMMIT_1` demonstrates the long form of the `COMMIT ENTITIES` statement.

``` abap
COMMIT ENTITIES 
  RESPONSE OF demo_managed_root_2 
    FAILED   FINAL(failed) 
    REPORTED FINAL(reported) 
  RESPONSE OF demo_managed_assoc_custom 
    FAILED   FINAL(failed2) 
    REPORTED FINAL(reported2).
```

## Addition

`... IN SIMULATION MODE`

### Description

Used to process a save in simulation mode. See more information in topic [`COMMIT ENTITIES`, `IN SIMULATION MODE`](abapcommit_entities_simulation.md).

### Executable Example

The example [`COMMIT ENTITIES`, Short and Long Form](abencommit_entities_sh_lo_abexa.md) demonstrates the use of the long (and short) form of the `COMMIT ENTITIES` statement.

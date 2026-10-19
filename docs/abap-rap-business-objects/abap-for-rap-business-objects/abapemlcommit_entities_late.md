---
title: "COMMIT ENTITIES BEGIN, END"
source_file: abapemlcommit_entities_late.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES BEGIN, END

## Syntax

``` abap
COMMIT ENTITIES BEGIN [IN SIMULATION MODE] 
                      [{RESPONSES response_param  } 
                       | {RESPONSE OF ... response_param  } 
                       | {RESPONSES OF ... response_param  }]. 
  ... 
  [CONVERT KEY OF bdef 
    FROM [TEMPORARY] pre_key 
    TO final_key.] 
  ... 
COMMIT ENTITIES END.  
```

[`response_param `](abapeml_response.md) · [`response_param `](abapeml_response.md) · [`response_param `](abapeml_response.md) · [`[CONVERT KEY OF bdef`](abapconvert_key.html) · [`FROM [TEMPORARY] pre_key`](abapconvert_key.md) · [`TO final_key.`](abapconvert_key.md)

### Addition

[1. `... IN SIMULATION MODE`](abapemlcommit_entities_late.md#addition-1)

[2. `... RESPONSES response_param.`](abapemlcommit_entities_late.md#addition-2)

[3. `... RESPONSE OF ... response_param.`](abapemlcommit_entities_late.md#addition-3)

[4. `... RESPONSES OF ... response_param.`](abapemlcommit_entities_late.md#addition-4)

## Overview

### Description

Triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and completes the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). All transactional changes in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), that is, [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) created, modified, or deleted within the RAP transaction, are persisted to the database. This variant is relevant for [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) on entities for which [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) has been enabled. It is used to get the final keys from the preliminary keys.

For [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) on entities for which [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) has been enabled, only preliminary identifiers have been assigned, for example [`%pid`](abapderived_types_pid.md) or temporary keys. Those preliminary identifiers are converted to final keys when calling the [`adjust_numbers`](abensaver_adjust_numbers.md) [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) as part of the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). If your use case is to retrieve the final keys of the new instances, this `COMMIT ENTITIES` variant defines a scope in which the EML statement [`CONVERT KEY OF`](abapconvert_key.md) can be used to retrieve the final keys from the preliminary keys.

The purpose of the syntax parts is the following:

| **Syntax Part**             | **Purpose**                                                                                                                        |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `COMMIT ENTITIES BEGIN ...` | Opens the commit scope.                                                                                                            |
| `COMMIT ENTITIES END.`      | Closes the commit scope. With the closing, all information on keys that are relevant for operations performed beforehand are lost. |

### Hints

- For general hints on using the statement see the topic [`COMMIT ENTITIES`](abapcommit_entities.md).

- `COMMIT ENTITIES` statements are not allowed in [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md).

- When using `COMMIT ENTITIES` statements, a check of `sy-subrc` should be included to avoid syntax warnings. If responses are retrieved, it is recommended that the response parameter `failed` is checked so as to react accordingly. See the topic [`COMMIT ENTITIES`](abapcommit_entities.md) for more information. If this variant is used, `sy-subrc` should be checked after the statement with the addition `BEGIN`.

## Addition 1

`... IN SIMULATION MODE`

### Description

Used to process a save in simulation mode. See more information in topic [`COMMIT ENTITIES`, `IN SIMULATION MODE`](abapcommit_entities_simulation.md).

## Addition 2

`... RESPONSES response_param.`

### Description

Used for retrieving information returned by the response parameters of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). For more information on `response_param`, see [here](abapeml_response.md).

## Addition 3

`... RESPONSE OF ... response_param.`

### Description

Used for retrieving information returned by the response parameters of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). For more information on `response_param`, see [here](abapeml_response.md).

In this case, it is the [long form](abapemlcommit_entities_long.md) with which multiple root entities can be specified.

## Addition 4

`... RESPONSES OF ... response_param.`

### Description

Used for retrieving information returned by the response parameters of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). For more information on `response_param`, see [here](abapeml_response.md).

In this case, it is the [dynamic form](abapemlcommit_entities_dyn.md).

### Executable Example

The example [`COMMIT ENTITIES BEGIN`, `END` with `CONVERT KEY OF`](abencommit_entities_beginend_abexa.md) demonstrates the use of this `COMMIT ENTITIES` statement including `CONVERT KEY OF`.

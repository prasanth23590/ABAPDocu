---
title: "COMMIT ENTITIES, Short Form"
source_file: abapemlcommit_entities_short.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES, Short Form

## Syntax

``` abap
COMMIT ENTITIES [IN SIMULATION MODE] [RESPONSES response_param  ].  
```

[`response_param `](abapeml_response.md)

### Addition

[1. `... IN SIMULATION MODE`](abapemlcommit_entities_short.md#addition-1)

[2. `... RESPONSES response_param.`](abapemlcommit_entities_short.md#addition-2)

## Overview

### Description

Triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and completes the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). All transactional changes in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), that is, [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) created, modified, or deleted within the RAP transaction, are persisted to the database. For general hints on using the statement, see the topic [`COMMIT ENTITIES`](abapcommit_entities.md).

## Addition 1

`... IN SIMULATION MODE`

### Description

Used to process a save in simulation mode. See more information in topic [`COMMIT ENTITIES`, `IN SIMULATION MODE`](abapcommit_entities_simulation.md).

## Addition 2

`... RESPONSES response_param.`

### Description

You can optionally retrieve information returned by the response parameters of [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). The operands following `FAILED` and `REPORTED` must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`. For more information on `response_param`, see [here](abapeml_response.md).

### Executable Example

The example [`COMMIT ENTITIES`, Short and Long Form](abencommit_entities_sh_lo_abexa.md) demonstrates the use of the short (and long) form of the `COMMIT ENTITIES` statement.

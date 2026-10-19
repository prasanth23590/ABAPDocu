---
title: "READ ENTITY, Short Form"
source_file: abapread_entity_short.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITY, Short Form

## Syntax

``` abap
READ ENTITY [IN LOCAL MODE [WITH CHANGES  ]|[FORWARDING  ] PRIVILEGED  ] 
    entity operations [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`WITH CHANGES `](abapeml_read_with_changes.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`operations`](abapread_entity_entities_op.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapread_entity_short.md#addition-1)

[2. `... WITH CHANGES ...`](abapread_entity_short.md#addition-2)

[3. `... [FORWARDING] PRIVILEGED ...`](abapread_entity_short.md#addition-3)

[4. `... response_param.`](abapread_entity_short.md#addition-4)

## Overview

### Description

The short form of the `READ` statement is used for read operations ([`operations`](abapread_entity_entities_op.md)) from a single RAP BO entity only. The entity name (`entity`) can be specified directly, that is, reading from a child entity can also be done directly and not via the [root entity](../../abap-glossary/abenroot_entity_glosry.md) of a RAP BO. In this case, `entity` must be the full entity name and cannot be an alias name because the context of a RAP BO is unknown. It is possible to include all three read options in one operation per entity `entity`: [read operation](../../abap-glossary/abenrap_read_operation_glosry.md), [read-by-association operation](../../abap-glossary/abenrap_rba_operation_glosry.md) and an operation executing a function, but only one of each kind within the same `READ ENTITY` statement.

## Addition 1

`... IN LOCAL MODE ...`

### Description

The addition [`IN LOCAL MODE`](abapin_local_mode.md) is used to exclude [feature controls](../rap-behavior-definitions/abenbdl_actions_fc.md) and [authorization checks](../rap-behavior-definitions/abenbdl_authorization.md). It can only be used within the RAP BO runtime implementation.

## Addition 2

`... WITH CHANGES ...`

### Description

The [`WITH CHANGES`](abapeml_read_with_changes.md) addition is used to access accumulated change operation information for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md).

## Addition 3

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 4

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ` demonstrates an EML `READ ENTITY` statement.

``` abap
READ ENTITY demo_spfli_flights 
ALL FIELDS WITH VALUE #( ( %key-carrid = 'LH' 
                           %key-connid = 2407 ) ) 
 RESULT FINAL(read_entity) 
 FAILED FINAL(read_failed). 
IF read_failed-demo_spfli_flights IS NOT INITIAL. 
  "... 
  RETURN. 
ENDIF.
```

### Executable Example

- The example [ABAP EML - `READ`, Variants](abeneml_read_alternatives_abexa.md) demonstrates this `READ` variant with a simple managed RAP BO.

- For more examples on `READ` operations, refer to [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).

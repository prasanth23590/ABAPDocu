---
title: "READ ENTITIES, Long Form"
source_file: abapread_entities_long.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITIES, Long Form

## Syntax

``` abap
READ ENTITIES OF bdef[IN LOCAL MODE|[FORWARDING  ] PRIVILEGED  ] 
    ENTITY entity1 operations 
    [ENTITY entity2 operations] 
    [...] 
    [WITH CHANGES  ] 
    [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`operations`](abapread_entity_entities_op.md) · [`operations`](abapread_entity_entities_op.md) · [`WITH CHANGES `](abapeml_read_with_changes.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapread_entities_long.md#addition-1)

[2. `... [FORWARDING] PRIVILEGED ...`](abapread_entities_long.md#addition-2)

[3. `... WITH CHANGES ...`](abapread_entities_long.md#addition-3)

[4. `... response_param.`](abapread_entities_long.md#addition-4)

## Overview

### Description

The long syntax form of the `READ` statement is used to collect multiple read operations ([`operations`](abapread_entity_entities_op.md)) on multiple entities of a RAP BO. Yet, it can also be used to just read from a single entity of a RAP BO.

``` abap
`bdef` must be a root entity followed by a list of operations grouped by individual entities\. `entity1`, `entity2`, and so on, must be entities contained in the composition tree of the root entity `bdef`\. The root entity itself can also be inserted in the position of `entity1`, for example\. Each part of the list of operations specified after `READ ENTITIES OF bdef` has the same syntax as the short form\. At least one entry \(`ENTITY entity1` with the operation\) must be specified\. The same entity can be specified after `ENTITY` only once for a read operation\. The root entity name can be used more than once but only in the context of read\-by\-association operations or executing actions, for example as follows: 
`READ ENTITIES OF bdef` 
    `   ENTITY bdef ...` 
    `   ENTITY bdef BY \_assoc1 ...` 
    `   ENTITY bdef BY \_assoc2 ...` 
`...`
```

The root entity name in the position of the first statement, `READ ENTITIES OF bdef`, must be the full entity name. `entity1`, and so on, should be the entity alias names if provided in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). Using the full entity name will cause a warning. If the root entity is used in the list of operations, its alias name, if defined in the BDEF, should be used as well.

## Addition 1

`... IN LOCAL MODE ...`

### Description

The addition [`IN LOCAL MODE`](abapin_local_mode.md) is used to exclude [feature controls](../rap-behavior-definitions/abenbdl_actions_fc.md) and [authorization checks](../rap-behavior-definitions/abenbdl_authorization.md). It can only be used within the RAP BO runtime implementation.

## Addition 2

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 3

`... WITH CHANGES ...`

### Description

The [`WITH CHANGES`](abapeml_read_with_changes.md) addition is used to access accumulated change operation information for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md).

## Addition 4

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ` demonstrates an EML `READ ENTITIES` statement.

``` abap
READ ENTITIES OF demo_spfli_flights 
  ENTITY demo_spfli_flights 
    ALL FIELDS WITH VALUE #( ( %key-Carrid = 'SQ' 
                               %key-connid = 67 ) ) 
    RESULT FINAL(read_entities_of) 
  ENTITY sflight 
    ALL FIELDS WITH 
       VALUE #( ( %key-Carrid = 'AA' 
                  %key-connid = 17 Fldate = '20170125'  ) ) 
    RESULT FINAL(read_entities_child) 
  ENTITY demo_spfli_flights 
    BY \_Flights 
    ALL FIELDS WITH 
        VALUE #( ( %key-Carrid = 'AZ' 
                   %key-connid = 791 ) ) 
    RESULT FINAL(rba2) 
    FAILED FINAL(read_entities_failed). 
IF read_entities_failed-demo_spfli_flights IS NOT INITIAL. 
  ... 
ENDIF.
```

### Executable Example

- The example [ABAP EML - `READ`, Variants](abeneml_read_alternatives_abexa.md) demonstrates this `READ` variant with a simple managed RAP BO.

- For more examples on `READ` operations in general, see [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).

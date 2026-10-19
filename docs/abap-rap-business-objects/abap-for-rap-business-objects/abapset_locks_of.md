---
title: "SET LOCKS OF, Long Form"
source_file: abapset_locks_of.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > SET LOCKS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET LOCKS OF, Long Form

## Syntax

``` abap
SET LOCKS OF bdef   
   ENTITY entity1 FROM inst1   
  [ENTITY entity2 FROM inst2]   
  [...]   
  [response_param  ].  
```

[`response_param `](abapeml_response.md)

### Addition

[`... response_param.`](abapset_locks_of.md#addition)

## Overview

### Description

The long form of the `SET LOCKS` statement is used to exclusively lock instances of multiple RAP BO entities.

`bdef` must be a root entity followed by a list of locks grouped by individual entities. `entity1`, `entity2`, and so on, must be entities contained in the [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the root entity `bdef`. The root entity itself can also be inserted in the position of `entity1`, for example. Each part of the list specified after `SET LOCKS OF bdef` has the same syntax as the [short form](abapset_locks_entity.md). At least one entry (`ENTITY bdef1 FROM inst`) must be specified. The root entity name in the position of the first statement, `SET LOCKS OF bdef`, must be the full entity name. `entity1`, and so on, should be the entity alias names if provided in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). Using the full entity name will cause a warning. If the root entity is used in the list of operations, its alias name, if defined in the BDEF, should be used as well.

`inst1`, `inst2`, and so on, are internal tables specifying the instances that are to be locked. The tables must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR KEY OF`](abaptype_table_for.md). They can be constructed in an operand position using [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), for example with the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) (`VALUE`) and other [constructor operators](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) to fill the internal tables with instances as input parameters after the keyword `FROM`.

## Addition

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Hint

The internal tables `inst1`, `inst2`, and so on, can also be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR LOCK`](abaptype_table_for.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_RAP_EML_SET_LOCKS` covers all forms of the `SET LOCKS` statement. It accesses a RAP BO using [EML](../../abap-glossary/abeneml_glosry.md) and creates multiple BO instances. A `SET LOCKS` statement follows that exclusively locks instances via the keys. The following `SET LOCKS` statement (long form) is used in the middle of the example:

``` abap
SET LOCKS OF demo_managed_root 
 ENTITY demo_managed_root 
  FROM VALUE #( ( key_field = 4 ) ) 
 ENTITY child 
  FROM VALUE #( ( key_field = 6 ) ) 
   FAILED   FINAL(lt_failed2) 
   REPORTED FINAL(lt_reported2).
```

The following image shows the global lock table (transaction `SM12`) during the transaction, before the `ROLLBACK ENTITIES` statement is executed. The newly created instances are locked, and they are automatically removed from the lock table after the `ROLLBACK ENTITIES` statement is executed. ![figure](images_abdoc_set_locks_2.png)

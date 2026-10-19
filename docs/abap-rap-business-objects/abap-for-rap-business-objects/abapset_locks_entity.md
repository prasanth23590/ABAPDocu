---
title: "SET LOCKS ENTITY, Short Form"
source_file: abapset_locks_entity.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > SET LOCKS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET LOCKS ENTITY, Short Form

## Syntax

``` abap
SET LOCKS ENTITY entity FROM inst [response_param  ].  
```

[`response_param `](abapeml_response.md)

### Addition

[`... response_param.`](abapset_locks_entity.md#addition)

## Overview

### Description

Used to exclusively lock instances of a single RAP BO entity.

The entity name `entity` can be specified directly. The entity name must be the full entity name and cannot be an alias name because the context of a RAP BO is unknown.

`inst` is an internal table specifying the instances that are to be locked. The table must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR KEY OF`](abaptype_table_for.md). It can be constructed in an operand position using [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), for example with the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) (`VALUE`) and other [constructor operators](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) to fill the internal table with instances as input parameters after the keyword `FROM`.

## Addition

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Hint

The internal table `inst` can also be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR LOCK`](abaptype_table_for.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_RAP_EML_SET_LOCKS` covers all forms of the `SET LOCKS` statement. It accesses a RAP BO using [EML](../../abap-glossary/abeneml_glosry.md) and creates several BO instances. A `SET LOCKS` statement follows that exclusively locks instances via the keys. The following `SET LOCKS` statement (short form) is used at the beginning of the example:

``` abap
SET LOCKS ENTITY demo_managed_root 
   FROM VALUE #( ( key_field = 1 ) 
                 ( key_field = 2 ) ) 
    FAILED   FINAL(lt_failed1) 
    REPORTED FINAL(lt_reported1).
```

The following image shows the global lock table (transaction `SM12`) during the transaction, before the `ROLLBACK ENTITIES` statement is executed. The newly created instances are locked. After the `ROLLBACK ENTITIES` statement is executed, the entries are automatically deleted from the lock table. ![figure](images_abdoc_set_locks_1.png)

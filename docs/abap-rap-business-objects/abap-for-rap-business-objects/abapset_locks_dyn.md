---
title: "SET LOCKS lock_tab, Dynamic Form"
source_file: abapset_locks_dyn.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > SET LOCKS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET LOCKS lock_tab, Dynamic Form

## Syntax

``` abap
SET LOCKS lock_tab [response_param  ].  
```

[`response_param `](abapeml_response.md)

### Addition

[`... response_param`](abapset_locks_dyn.md#addition)

## Overview

### Description

The dynamic form of the `SET LOCKS` statement is used to collect instances of multiple RAP BO entities that are to be locked exclusively in one single `SET LOCKS` statement.

`lock_tab` must be an internal table of type `ABP_BEHV_LOCKS_TAB`. This table has specific components:

| **Component** | **Details**                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `entity_name` | Specifies the name of the RAP BO entity for which exclusive locking is intended. The name must be provided using capital letters.                                           |
| `instances`   | Specifies a reference to an internal table that is typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR KEY OF`](abaptype_table_for.md). |

## Addition

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified. When used in the context of the dynamic form of the ABAP EML statement, the parameters must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`.

### Hint

The internal tables that are referenced to within `lock_tab` as parameters of `INSTANCES` can also be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR LOCK`](abaptype_table_for.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_RAP_EML_SET_LOCKS` covers all forms of the `SET LOCKS` statement. It accesses a RAP BO using [EML](../../abap-glossary/abeneml_glosry.md) and creates multiple BO instances. A `SET LOCKS` statement follows that exclusively locks instances via the keys. The following `SET LOCKS` statement (dynamic form) is used at the end of the example:

``` abap
DATA inst TYPE TABLE FOR KEY OF demo_managed_root. 
DATA inst2 TYPE TABLE FOR KEY OF demo_managed_child. 
 
inst  = VALUE #( ( key_field = 7 ) ). 
inst2 = VALUE #( ( key_field = 9 ) 
                 ( key_field = 10 ) ). 
 
FINAL(lt_lock) = VALUE abp_behv_locks_tab( 
 ( entity_name = 'DEMO_MANAGED_ROOT' instances = REF #( inst ) ) 
 ( entity_name = 'DEMO_MANAGED_CHILD' instances = REF #( inst2 ) ) ). 
 
SET LOCKS lt_lock FAILED   FINAL(lt_failed3) 
                  REPORTED FINAL(lt_reported3).
```

The following image shows the global lock table (transaction `SM12`) during the transaction, before the `ROLLBACK ENTITIES` statement is executed. The newly created instances are locked. After the `ROLLBACK ENTITIES` statement is executed, the entries are automatically deleted from the lock table. ![figure](images_abdoc_set_locks_3.png)

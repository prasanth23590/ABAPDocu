---
title: "TYPE REQUEST FOR"
source_file: abaptype_request_for.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPE REQUEST FOR

## Syntax

``` abap
... REQUEST FOR { { CHANGE 
                  | DELETE } 
                    bdef } ...  
```

### Alternative

[1. `... CHANGE bdef`](abaptype_request_for.md#alternative-1)

[2. `... DELETE bdef`](abaptype_request_for.md#alternative-2)

## Overview

### Description

A structured data type that is only used in the context of managed implementations [`with additional save`](../rap-behavior-definitions/abenbdl_saving.md) and [`with unmanaged save`](../rap-behavior-definitions/abenbdl_saving.md). In these cases, the [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) contains the `save_modified` method that is part of a local saver class that inherits from the base saver class `CL_ABAP_BEHAVIOR_SAVER`. Within the `save_modified` method, the following predefined parameters can be addressed:

- `create`: structure typed with `TYPE REQUEST FOR CHANGE`

- `update`: structure typed with `TYPE REQUEST FOR CHANGE`

- `delete`: structure typed `TYPE REQUEST FOR DELETE`

## Alternative 1

`... CHANGE bdef`

### Description

Used for the predefined `create` and `update` parameters that are only available in local saver classes of the [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) that inherit from the base saver class `CL_ABAP_BEHAVIOR_SAVER`. `create` and `update` that are typed with `TYPE REQUEST FOR CHANGE` contain nested tables that are named according to those entities for which the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) has specifications `with additional save` or `with unmanaged save` respectively and for which `CREATE` and/or `UPDATE` operations are allowed. The nested tables are of type [`TYPE TABLE FOR CHANGE`](abaptype_table_for.md). The tables include those [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) that are to be created (or updated) and saved.

## Alternative 2

`... DELETE bdef`

### Description

Used for the predefined `delete` parameter that is only available in local saver classes of the [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) that inherit from the base saver class `CL_ABAP_BEHAVIOR_SAVER`. `delete` is typed with `TYPE REQUEST FOR DELETE`. It contains nested tables that are named according to those entities for which the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) has specifications `with additional save`, or `with unmanaged save` respectively; and for which `DELETE` operations are allowed. The nested tables are of type [`TYPE TABLE FOR KEY OF`](abaptype_table_for.md). The table includes those [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) that are to be deleted.

### Executable Example

- The example [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Additional Save](abenrap_additional_save_abexa.md) shows the types `TYPE REQUEST FOR CHANGE` and `TYPE REQUEST FOR DELETE` in the context of a simple managed RAP BO whose BDEF is specified with `with additional save`.

- The example [ABAP EML - `TYPE REQUEST FOR` in a managed RAP BO with unmanaged save](abenrap_managed_unm_save_abexa.md) shows the types `TYPE REQUEST FOR CHANGE` and `TYPE REQUEST FOR DELETE` in the context of a simple managed RAP BO whose BDEF is specified with `with unmanaged save`.

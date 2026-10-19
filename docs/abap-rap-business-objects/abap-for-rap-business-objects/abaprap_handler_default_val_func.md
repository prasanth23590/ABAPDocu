---
title: "Handler Methods for RAP Default Values Functions"
source_file: abaprap_handler_default_val_func.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods > FOR READ, RAP Handler Method"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Handler Methods for RAP Default Values Functions

## Syntax

``` abap
**Handler method definition:**

METHODS [getdefaultsforcreate | getdefaultsforname] 
   FOR READ [IMPORTING  ] imp_param 
   FUNCTION [bdef~getdefaultsforcreate | bdef~getdefaultsforname] 
   RESULT res_func.  

**Note:** The syntax above only covers the definition as it is created by the quick fix in the ABAP development tools for Eclipse. For all options, see here.
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`ABAP development tools for Eclipse`](../../abap-glossary/abenadt_glosry.md) · [`here`](abaphandler_meth_read.md)

## Description

If RAP BO operations are defined with [RAP default values functions](../../abap-glossary/abenrap_bo_defaulting_glosry.md), [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) must be implemented in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

The names of the methods are predefined

- `getdefaultsforcreate`: For [create operations](../../abap-glossary/abenrap_create_operation_glosry.md); cannot be a custom name

- `getdefaultsforname`: A custom name `name` following the mandatory `getdefaultsfor` for a [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md), [function](../../abap-glossary/abenrap_function_glosry.md) or [action](../../abap-glossary/abenrap_action_glosry.md) as specified in the [behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md)

The type of the importing parameter `imp_param` is [`TYPE TABLE FOR FUNCTION IMPORT`](abaptype_table_for.md) and automatically derived. The type for ...

- create operations contains [`%cid`](abapderived_types_cid.md).

- create-by-association operations contains [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) key values.

- static functions and actions contains `%cid`.

- instance functions and actions contains RAP BO instance key values.

Note that, depending on the context, more components can be included. For example, in case of a draft-enabled RAP BO, the draft indicator [`%is_draft`](abapderived_types_is_draft.md) is available as type component.

The type of the output parameter `res_func` is [`TYPE TABLE FOR FUNCTION RESULT`](abaptype_table_for.md) and automatically derived. The type for ...

- create and create-by-association operations contains a table for mapping the instance identifiers (key field values or `%cid`) to the fields of the related (target) entity (contained in the [`%param`](abapderived_types_param.md) component).

- functions and actions contains a table for mapping the instance identifiers (key field values or `%cid`) to the input parameter field values of the related operation (contained in the [`%param`](abapderived_types_param.md) component).

## More Information

Topic [RAP - `default function`](../rap-behavior-definitions/abenbdl_default_function.md)

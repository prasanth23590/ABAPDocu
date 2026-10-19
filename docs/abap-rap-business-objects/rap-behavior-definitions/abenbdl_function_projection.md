---
title: "RAP - function, Projection BDEF"
source_file: abenbdl_function_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - function, Projection BDEF

## Syntax

``` abap
[internal] [static] function 
           [( 
           [features: {instance | global}] 
           [authorization:none] 
           [authorization:global] 
           [authorization:instance] 
           )] 
           FunctionName 
           [external 'ExternalName'] 
           [InputParameter] 
            OutputParameter 
           [{default function GetDefaultsForFuncName [external 'GetDefaultsForExtName'];}] 
           [key (AlternativeKey) function FunctionName ...;]  
```

[`features: {instance | global}`](abenbdl_actions_fc.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`external`](abenbdl_external.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForFuncName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md) · [`key (AlternativeKey) function FunctionName ...;`](abenbdl_keyfunction.md)

## Description

It is possible to define a [RAP function](../../abap-glossary/abenrap_function_glosry.md), a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md), or a [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md) for a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) in the projection layer. This works in the same way as defining functions in a [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md); see the topic [RAP - `function`](abenbdl_function.md) for details.

There is a difference however regarding the [authorization concept](abenbdl_authorization.md) of a function defined in a projection BDEF: In a projection BDEF, no authorization master from the base BDEF is available. If an authorization concept is required, this must be specified for each node of a BO node as described in topic [RAP BDL - authorization, projection BDEF](abenbdl_authorization_projection.md).

In the case of a RAP key function, the [BDEF alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) from the underlying [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) must be reused using the syntax [`use key AltKeyName`](abenbdl_use_projection.md). This reused key can be used as the basis of a key function. Defining new alternative keys in a projection behavior definition is not possible.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [Function Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/30708173550d4a358f87f38bcc77f6d2?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that defines a new function in the projection layer. It is based on the underlying base BO `DEMO_RAP_STRICT`. It defines the new function `getDetails` in the projection layer.

``` abap
projection implementation in class bp_demo_rap_proj_new_function unique;
strict;

define behavior for DEMO_RAP_PROJ_NEW_FUNCTION alias Root
{
  use create;
  use update;
  use delete;

  function getDetails result [0..*] $self;
}
```

The ABAP behavior pool implements the new function `getDetails`. This function reads the values of the fields `key_field` and `data_field` and returns them in its result structure.

``` abap
METHOD getDetails. 
  DATA(lt_keys) = keys. 
  CHECK lt_keys IS NOT INITIAL. 
 
  READ ENTITIES OF demo_rap_proj_new_function IN LOCAL MODE 
    ENTITY Root 
      FIELDS ( key_field data_field ) 
      WITH CORRESPONDING #( lt_keys ) 
    RESULT DATA(lt_item) 
    FAILED DATA(read_failed). 
 
  failed = CORRESPONDING #( DEEP read_failed ). 
 
  LOOP AT lt_item ASSIGNING FIELD-SYMBOL(<fs_item>). 
    APPEND VALUE #( %tky   = <fs_item>-%tky 
                    %param = CORRESPONDING #( <fs_item> ) ) TO result. 
  ENDLOOP. 
ENDMETHOD.
```

The ABAP class `CL_DEMO_RAP_PROJ_NEW_FUNCTION` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to RAP business object. It first creates two new entity instances and then executes the function `getDetails` for both of them.

Result: The content of the fields `key_field` and `data_field` is returned in the result structure. ![figure](images_abdoc_new_function.jpg)

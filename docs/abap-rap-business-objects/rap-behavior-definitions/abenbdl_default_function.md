---
title: "RAP - default function"
source_file: abenbdl_default_function.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - default function

## Syntax

``` abap
... {default function [DefaultValuesFunctionName] [ external 'GetDefaultsForExtName'];}  
```

[`external 'GetDefaultsForExtName'`](abenbdl_external.md)

## Description

RAP BO operation addition that defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for a RAP BO operation. A default values function defaults field values or input parameters for a RAP BO operation on the user interface. An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR READ ... FOR FUNCTION ...`](../abap-for-rap-business-objects/abaprap_handler_default_val_func.md) is required. `default function` can be used for the [standard operation](abenbdl_standard_operations.md) `create`, the [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md), [actions](abenbdl_action.md), and [functions](abenbdl_function.md).

The name `DefaultValuesFunctionName` and the optional external name `GetDefaultsForExtName` of the default values function must start with `GetDefaultsFor`. The name of the default values function must be unique within the current BDEF. The external name does not have to be unique. If specified, it is exposed in the OData metadata.

Default values functions are defined by adding the keywords `{default function GetDefaultsForOperation;}` behind the respective operation and parameter definition.

Special rules apply to this addition for each operation:

[**create**](abenbdl_standard_operations.md)

- A dedicated name after `default function` is optional. If specified, the name must be `GetDefaultsForCreate`.

- An external name `GetDefaultsForExtName` is not possible.

- A syntax diagram is available in the topic [RAP - Standard Operations](abenbdl_standard_operations.md).

[**create by association**](abenbdl_association.md)

- `default function` must be specified in combination with `create` within curly brackets.

- An external name `GetDefaultsForExtName` is possible.

- A syntax diagram is available in the topic [RAP - Operations for Associations](abenbdl_association.md).

[**RAP action**](abenbdl_action.md)

- The default values function can default values for the input parameter for the action. As a prerequisite, the action must specify an input parameter [`InputParameter`](abenbdl_action_input_param.md). Flat, deep, and deep table parameters are supported.

- An external name `GetDefaultsForExtName` is possible.

- A syntax diagram is available in the topic [RAP - `action`](abenbdl_action.md).

[**RAP function**](abenbdl_function.md)

- The default values function can default values for the input parameter for the function. As a prerequisite, the function must specify an input parameter [`InputParameter`](abenbdl_action_input_param.md). Flat, deep, and deep table parameters are supported.

- An external name `GetDefaultsForExtName` is possible.

- A syntax diagram is available in the topic [RAP - `function`](abenbdl_function.md).

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), default values functions can be defined for [actions and functions](abenbdl_nonstandard_projection.md) defined in the projection layer. See the topic [RAP - `action`, Projection BDEF](abenbdl_nonstandard_projection.md) for details.

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), default values functions can be reused with the addition [`use`](abenbdl_use_default_function.md). The operation in question and the default values function must be reused separately. For details, see the topic [RAP - `use DefaultValuesFunction`](abenbdl_use_default_function.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), default values functions can be reused with the addition [`use`](abenbdl_use_default_function.md). The operation in question and the default values function must be reused separately. For details, see the topic [RAP - `use DefaultValuesFunction`](abenbdl_use_default_function.md).

## Hints

- The defaulting of values takes place in an OData service only. When accessing an operation that has a default values function attached using ABAP EML, the default values function is not accessed and no default values are provided.

- The RAP default values function can be triggered in ABAP EML like other [RAP functions](../../abap-glossary/abenrap_function_glosry.md), using the [`READ ENTITIES ... EXECUTE`](../abap-for-rap-business-objects/abapread_entity_entities_op.md) statement.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Operation Defaulting](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/59a29c74b40c4e7d8f2651e77a193af9?version=sap_cross_product_abap).

- Topic [Handler Methods for RAP Default Values Functions](../abap-for-rap-business-objects/abaprap_handler_default_val_func.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following managed BDEF defines a default values function for the operations create, create-by-association, the RAP action `InstanceAction`, and the RAP function `StaticFunction`.

``` abap
managed implementation in class bp_demo_rap_default_values_fun unique;
strict ( 2 );

define behavior for DEMO_RAP_DEFAULT_VALUES_FUNC alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  //Default values function for create
  create { default function GetDefaultsForCreate; }
  update;
  delete;
  field ( readonly : update ) key_field;

  //Default values function for create-by-association
  association _to_child
  { create { default function GetDefaultsForChild; } }

    //Default values function for action
    action InstanceAction parameter demo_cds_abstract_entity
      { default function GetDefaultsForAction; }

    //Default values function for static function
    static function (authorization:none) StaticFunction
      parameter demo_cds_abstract_entity
      result [0..*] $self
      { default function GetDefaultsForStaticFunction; }
  }

  define behavior for DEMO_RAP_DEFAULT_VALUES_CHLD alias Child
  persistent table demo_dbtab_child
  lock dependent by _to_parent
  authorization dependent by _to_parent
  {
    update;
    delete;
    field ( readonly ) key_field;
    field ( readonly : update ) key_field_child;
    association _to_parent;
  }
```

The default values function for the operation create is implemented in the ABAP behavior pool `BP_DEMO_RAP_DEFAULT_VALUES_FUN`. The RAP handler method `GetDefaultsForCreate` provides default values for the fields `char_field` and `lchg_date_time`.

``` abap
METHOD GetDefaultsForCreate. 
 LOOP AT df_create ASSIGNING FIELD-SYMBOL(<df_create>). 
    INSERT INITIAL LINE INTO TABLE df_create_result 
    ASSIGNING FIELD-SYMBOL(<df_create_result>). 
 
    GET TIME STAMP FIELD DATA(lv_timestamp). 
 
    <df_create_result> = VALUE #( 
                         %cid   = <df_create>-%cid 
                         %param = VALUE 
                             #( char_field   = 'Default Value' 
                                lchg_date_time = lv_timestamp ) ). 
  ENDLOOP. 
ENDMETHOD.
```

The effect is that in an OData service, when creating a new entity instance, the fields `char_field` and `lchg_date_time` are filled with default values.

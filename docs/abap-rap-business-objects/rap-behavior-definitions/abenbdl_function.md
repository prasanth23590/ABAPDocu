---
title: "RAP - function"
source_file: abenbdl_function.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - function

## Syntax

``` abap
[internal] [static] [repeatable] function 
                [( 
                [features: {instance | global}] 
                [authorization:none] 
                [authorization:global] 
                [authorization:instance] 
                 )] 
                FunctionName [external'ExternalName'] 
                [InputParameter] 
                 OutputParameter; 
                [{default function GetDefaultsForFuncName [external 'GetDefaultsForExtName'];}] 
                [key (AlternativeKey) function FunctionName ...;]  
```

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`repeatable`](abenbdl_action_repeatable.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`external`](abenbdl_external.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForFuncName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md) · [`key (AlternativeKey) function FunctionName ...;`](abenbdl_keyfunction.md)

## Description

A [RAP function](../../abap-glossary/abenrap_function_glosry.md) is a user-implemented operation that returns information without any side effects. A function performs calculations or [read operations](../../abap-glossary/abenrap_read_operation_glosry.md) on business objects without issuing [locks](abenbdl_locking.md) or modifying data. An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR READ ... FUNCTION`](../abap-for-rap-business-objects/abaphandler_meth_read.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

**Note:** A function must not modify any data. [`MODIFY ENTITIES`](../abap-for-rap-business-objects/abapmodify_entity_entities.md) operations are not valid in the implementation in the ABAP behavior pool. A `MODIFY ENTITIES` statement in a function implementation leads to a runtime error when a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) tries to access the function in question.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`static`](abenbdl_static.md): A function per default relates to a RAP BO entity instance and changes the state of the instance. [Static functions](../../abap-glossary/abenrap_static_operation_glosry.md) are not bound to any instance of a RAP BO entity but relate to the complete entity.

- [`repeatable`](abenbdl_action_repeatable.md): Per default, a function must not be executed multiple times on the same [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) within the same [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) request. Any attempt to do so leads to a contract check violation if the respective contract checks are switched on. The optional addition `repeatable` enables multiple executions of the same function on the same RAP BO entity instance within the same ABAP EML or OData request. For further details, see topic [RAP - `repeatable`](abenbdl_action_repeatable.md).

- Dynamic feature control with [`(features:instance)`](abenbdl_actions_fc.md). This enables or disables the function depending on preconditions within the business object.

- Global feature control with [`(features:global)`](abenbdl_actions_fc.md) enables or disables the function depending on BO-external preconditions.

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:global`](abenbdl_actions_auth_global.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies instance authorization checks instead.

- [`external`](abenbdl_external.md): Can be used to provide an alias name for the function for external usage. This external name is exposed in the OData metadata, but it is not known by ABAP. It can be much longer than the actual action name.

- [`internal`](abenbdl_internal.md): An internal function is accessible only from within the business object implementation.

- An input parameter [`InputParameter`](abenbdl_action_input_param.md) can optionally be added to the function signature.

- An output parameter [`OutputParameter`](abenbdl_action_output_para.md) is mandatory.

- [`default function`](abenbdl_default_function.md) defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for the function in question. It is an optional addition that can be used to default values for the input parameter of the function. As a prerequisite, the function must specify an input parameter.

- [`key (AlternativeKey) function ...`](abenbdl_keyfunction.md) defines a [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md) for an [alternative BDEF key](../../abap-glossary/abenrap_alternative_key_glosry.md). For details, see the topic [RAP - `key function`](abenbdl_keyfunction.md).

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), functions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md). It is also possible to specify new functions as described in topic [RAP BDL - actions and functions, projection BDEF](abenbdl_nonstandard_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), functions from the base BDEF can be reused. For details on the reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Functions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d401150cfdb1454d9f55d80aead9579a?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) based on the CDS root view entity `DEMO_CDS_FUNCTION_1`. The business object represents a purchase order. Three functions are defined:

- `getDetails` is an instance function that reads the values of the fields `PurchaseDocument`, `Price`, and `Status` for the specified entity instances and returns them in the result structure.

- `calculateTotal` is a static function that sums up the prices of all entity instances with status 'O' and returns the total in its result structure.

  **Note:** This function uses a DDIC data element as output parameter. Note that the recommended procedure is to use only CDS abstract entities as BDEF parameters.

- `calculateDiscount` has an input parameter for the discount percentage. It subtracts the discount from the initial price and returns a reduced price in its result structure.

``` abap
managed implementation in class bp_demo_cds_function_1 unique;
strict ( 2 );

define behavior for DEMO_CDS_FUNCTION_1 alias PurchaseDocument
persistent table demo_purch_doc
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  // instance function
  function (authorization:none) getDetails result [0..*] $self;

  // static function
  static function (authorization:none) calculateTotal
    result [1] demo_sales_total_price;

  //function with input parameter
  function (authorization:none) calculateDiscount
    parameter DEMO_CDS_DEDUCT_DISCOUNT
    result [1] $self;

  field ( readonly : update ) Purchasedocument;

  mapping for demo_purch_doc corresponding
    {
      CreaDateTime = crea_date_time;
      CreaUname    = crea_uname;
      LchgDateTime = lchg_date_time;
      LchgUname    = lchg_uname;
    }
}
```

The class `CL_DEMO_CDS_FUNCTION` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md), executes all three functions, and displays the content of their result structures. No modify operations are carried out, the functions merely deliver information in their result structure without changing database entries. ![figure](images_abdoc_function.png)

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - function](abenbdl_function_abexa.md).

---
title: "RAP - repeatable"
source_file: abenbdl_action_repeatable.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action > RAP - action, Non-Factory"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - repeatable

## Syntax

``` abap
... repeatable ...  
```

## Description

Defines a non-factory [RAP action](../../abap-glossary/abenrap_action_glosry.md) or a [RAP function](../../abap-glossary/abenrap_function_glosry.md) as [repeatable RAP BO operation](../../abap-glossary/abenrap_repeatable_action_glosry.md). A repeatable RAP BO operation can be executed multiple times on the same [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) within the same [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) request. The [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) of a repeatable RAP BO operation contains a [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md) component and the [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) are filled for each execution individually.

**Repeatable Actions**

- Only non-factory, instance-bound RAP actions can be declared as `repeatable`. Other kinds of RAP actions must not be declared as repeatable for the following reasons:

  - [RAP factory actions](../../abap-glossary/abenrap_factory_action_glosry.md) are always repeatable and an explicit declaration is not necessary. The BDEF derived type of a RAP factory action contains the `%cid` component and multiple executions are possible.

  - [Static](abenbdl_static.md) RAP actions are always repeatable and an explicit declaration is not necessary. Static RAP actions are identified by means of a `%cid` component and multiple executions are possible.

  - [Draft actions](../../abap-glossary/abenrap_bo_draft_action_glosry.md) must not be executed multiple times on the same [RAP draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md) within one request. This is not useful and not supported.

- The same rules apply and the same [RAP BDL operation additions](abenbdl_operations_additions.md) are available as for non-factory actions, see topic [RAP - `action`, Non-Factory](abenbdl_action_nonfactory.md). There is only one exception: the syntax addition `static` is not available for repeatable actions.

**Repeatable Functions**

- Only instance-bound functions can be declared as `repeatable`. Static RAP functions are always repeatable and they are identified by means of a `%cid` component. Therefore, an explicit declaration of the repeatable characteristic is not required and not supported.

- The same rules apply and the same [RAP BDL operation additions](abenbdl_operations_additions.md) are available as for functions, see topic [RAP - `function`](abenbdl_function.md). There is only one exception: the syntax addition `static` is not available for repeatable functions.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md): Reuse of repeatable RAP BO operations as well as definition of new repeatable RAP BO operations. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md). For details on action definition, see topic [RAP - `action`, Projection BDEF](abenbdl_nonstandard_projection.md).

- [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md): Reuse of repeatable RAP BO operations For details on reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hint

When executing a RAP repeatable action or function, the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) component [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md) must be provided. This can be done using the optional addition [`AUTO FILL CID`](../abap-for-rap-business-objects/abapmodify_entity_entities_fields.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section about [Actions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/83bad707a5a241a2ae93953d81d17a6b?version=sap_cross_product_abap).

- Development guide for the ABAP RESTful Application Programming Model, section about [Functions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d401150cfdb1454d9f55d80aead9579a?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF with multiple actions and functions.

**Note:** This example is intentionally kept short and simple and focuses on specific RAP aspects. It does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md).

``` abap
managed implementation in class bp_demo_rap_repeatable_action unique;
strict ( 2 );

define behavior for DEMO_RAP_REPEATABLE_ACTION alias Root
persistent table demo_cs_rap_tab1
lock master
authorization master ( none )

{
  field ( readonly : update ) key_field;
  create;
  update;
  delete;

 // dup-key check
  action Action;

  // no dup-key check
  repeatable action RepeatAction;

  // no dup-key check (implicitly "repeatable")
  factory action FactoryAction [1];

 // no dup-key check (implicitly "repeatable")
  static action StaticAction;

  function (authorization:none) Function result [1] $self;

  repeatable function (authorization:none) RepeatFunction result [1] $self;
}
```

The BDEF derived type of the non-factory instance-bound action `Action` does not have a `%cid` component. It looks as follows: ![figure](images_derived_type_action.jpg)

The BDEF derived type of the repeatable action `RepeatAction` has a `%cid` component. It looks as follows: ![figure](images_repeat_action.jpg)

The non-factory instance-bound action `Action` must not be executed multiple times on the same RAP BO entity instance. The following execution results in a runtime error.

``` abap
DELETE FROM demo_cs_rap_tab1. 
MODIFY ENTITIES OF demo_rap_repeatable_action 
      ENTITY Root 
      CREATE FIELDS ( key_field field3 ) 
      WITH VALUE #( ( %cid = 'cid1' key_field = 3 field3 = 77 ) ) 
    EXECUTE Action 
FROM VALUE #( ( %cid_ref = 'cid1'  ) ( %cid_ref = 'cid1'  ) ). 
COMMIT ENTITIES.
```

The repeatable action `RepeatAction` can be executed multiple times on the same RAP BO entity instance as follows:

**Note:** `RepeatAction` is not implemented in this example.

``` abap
DELETE FROM demo_cs_rap_tab1. 
MODIFY ENTITIES OF demo_rap_repeatable_action 
      ENTITY Root 
      CREATE FIELDS ( key_field field3 ) 
      WITH VALUE #( ( %cid = 'cid1' key_field = 3 field3 = 77 ) ) 
    EXECUTE RepeatAction 
FROM VALUE #( ( %cid = 'cid3' %cid_ref = 'cid1'  ) 
              ( %cid = 'cid4' %cid_ref = 'cid1'  ) ). 
COMMIT ENTITIES.
```

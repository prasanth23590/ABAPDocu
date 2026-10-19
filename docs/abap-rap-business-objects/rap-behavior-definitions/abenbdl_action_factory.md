---
title: "RAP - action, factory"
source_file: abenbdl_action_factory.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - action, factory

## Syntax

``` abap
[internal][static [default]] factory action 
                  [( 
                  [features: {instance | global}] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:update] 
                  [authorization:global] 
                  [authorization:instance] 
                  [lock:none] 
                   )] 
                   ActionName [external 'ExternalName'] 
                  [InputParameter] 
                   [cardinality] 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]  
```

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`default`](abenbdl_action_default_factory.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md)

## Description

[Factory actions](../../abap-glossary/abenrap_factory_action_glosry.md) are used to create [RAP BO entity instances](../../abap-glossary/abenrap_bo_entity_inst_glosry.md). Factory actions can be instance-bound or [static](abenbdl_static.md). Instance-bound factory actions can copy specific values of an instance. Static factory actions can be used to create instances with prefilled default values. Factory actions may also create child entity instances.

For factory actions, the same rules apply as for [non-factory actions](abenbdl_action_nonfactory.md) with the following differences:

- Output parameters [`OutputParameter`](abenbdl_action_output_para.md) are not allowed. A factory action always creates one or more new BO entity instances of the RAP BO entity for which it is declared. Therefore, it is not necessary to specify the result in the BDL.

- It is mandatory to specify a cardinality. The cardinality can be one of the following values:

  - `[1]`: Exactly one entity instance is created.

  - `[0..1]`: None or exactly one entity instance is created.

  - `[0..*]`: None or any number of instances are created.

  - `[1..*]`: Any number of instances is created, but at least one.

For each unique [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) `%cid` (for static factory actions) or `%key` (for instance-bound factory actions) passed to the action, the number of newly created instances (none, one, or multiple) are added to the [response parameter](../abap-for-rap-business-objects/abapeml_response.md) `MAPPED` (success) or `FAILED`.

Exactly one static factory action can be defined as default factory action using the syntax addition [default](abenbdl_action_default_factory.md). This definition of default factory actions has an effect on consuming frameworks, such as OData. For further details, see topic [RAP - Default Factory Action](abenbdl_action_default_factory.md).

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), factory actions from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md) can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md). It is also possible to specify new factory actions as described in topic [RAP BDL - actions and functions, projection BDEF](abenbdl_nonstandard_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), factory actions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hint

For factory actions, the optional addition [`AUTO FILL CID`](../abap-for-rap-business-objects/abapmodify_entity_entities_fields.md) can be used to automatically fill the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) component [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) which defines two factory actions:

- `copy_instance`: All values of the requested entity instance are copied and a new key value is assigned.

- `new_instance`: A new entity instance is created with default values.

``` abap
managed implementation in class bp_demo_rap_factory_action unique;
strict(2);

define behavior for demo_rap_factory_action
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;

  // copy instance, assign new unique key value
  factory action copy_instance [1];

  // create new instance with default values
  static factory action new_instance [1];
}
```

The actions are implemented in behavior pool `BP_DEMO_RAP_FACTORY_ACTION`. The class `CL_DEMO_RAP_FACTORY_ACTION` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and executes both actions.

Result: the entity instance with key field *1* is copied and a new entity instance with default values is created.

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - factory action](abenbdl_action3_abexa.md).

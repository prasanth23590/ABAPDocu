---
title: "RAP - feature control"
source_file: abenbdl_actions_fc.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - feature control

## Syntax

``` abap
... (features:instance) 
  | (features:global) ...  
```

### Variant

[1. `... (features:instance)`](abenbdl_actions_fc.md#variant-1)

[2. `... (features:global)`](abenbdl_actions_fc.md#variant-2)

## Overview

### Description

Defines [feature control](../../abap-glossary/abenrap_feature_control_glosry.md) for a [RAP BO operation](../../abap-glossary/abenrap_bo_operation_glosry.md). With feature control, operations can be enabled or disabled.

There are two variants available:

- [Instance feature control](../../abap-glossary/abenrap_ins_feature_control_glosry.md)

  Operations of a business object can be enabled or disabled depending on instance-specific criteria, for example on the value of a specific field or the value of referenced data. For example, if the status of a BO instance is set to *archived*, all modifying operations can be disabled by means of instance feature control. An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE FEATURES`](../abap-for-rap-business-objects/abaphandler_meth_features.md) is mandatory.

- [Global feature control](../../abap-glossary/abenrap_glo_feature_control_glosry.md)

  Operations of a business object can be enabled or disabled globally. That means, the decision is independent of the state of the individual entity instance. An operation can be globally enabled or disabled, for example, by interpreting a feature toggle state. An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR GLOBAL FEATURES`](../abap-for-rap-business-objects/abaphandler_meth_global_features.md) is mandatory.

If an operation is disabled by means of instance feature control, it is grayed out on the user interface of an OData application. If an external [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) tries to execute a disabled operation with EML, the operation fails and an entry is returned in the [`failed`](../abap-for-rap-business-objects/abapeml_response.md) structure.

### Hints

- Feature control cannot be used for [internal operations](abenbdl_internal.md).

- For [static RAP BO operations](../../abap-glossary/abenrap_static_operation_glosry.md), only global feature control is available. Instance feature control is not available.

- Feature control runtime checks are not evaluated for EML calls with the addition [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md).

- The EML statement [`GET PERMISSIONS`](../abap-for-rap-business-objects/abapget_permissions.md) can be used to get information about disabled operations.

- In UI scenarios, feature control is displayed as [RAP consumer hint](../../abap-glossary/abenrap_consumer_hint_glosry.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Feature Control](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/a5055eef86fa492d99a29b3a9c7c2b88?version=sap_cross_product_abap).

## Variant 1

`... features:instance`

### Description

Instance feature control enables or disables operations depending on the state of the BO entity instance. Instance feature control can be defined for the following operations:

- The [standard operations](abenbdl_standard_operations.md) `update` and `delete`

- [Operations for associations](abenbdl_association.md)

- [Actions](abenbdl_action.md)

- The [draft action `Edit`](abenbdl_draft_action.md).

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

- [Functions](abenbdl_function.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines dynamic feature control for the standard operation `update`.

``` abap
managed implementation in class bp_demo_rap_operation_fc unique;
strict ( 2 );

define behavior for DEMO_RAP_OPERATION_FC
persistent table demo_dbtab_field
lock master
authorization master ( none )
{
  create;
  update ( features : instance );
  delete;
  field ( readonly : update ) key_field;
}
```

In the ABAP behavior pool, the following is specified: if field `int_field1` \> 50, then the update operation is disabled.

``` abap
METHOD get_instance_features. 
  READ ENTITIES OF demo_rap_operation_fc IN LOCAL MODE 
   ENTITY demo_rap_operation_fc 
   FIELDS ( int_field1 int_field2 ) WITH CORRESPONDING #( keys ) 
   RESULT DATA(lt_result) 
   FAILED failed. 
 
  result = VALUE #( FOR ls_result IN lt_result 
   ( %key = ls_result-%key 
     %features-%update = COND #( WHEN ls_result-int_field1 > 50 
                                 THEN if_abap_behv=>fc-o-disabled 
                                 ELSE if_abap_behv=>fc-o-enabled 
                               ) ) ). 
 
ENDMETHOD.
```

For the complete implementation, see `BP_DEMO_RAP_OPERATION_FC======CCIMP`

The ABAP class `CL_DEMO_RAP_FC_OPERATION` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object.

- First, it inserts two entity instances directly onto the database using ABAP SQL `INSERT`:

  - One of them has the value '1' for field `int_field1`.

  - The second one has value '55' for field `int_field1`. Therefore, it fulfills the condition that triggers feature control: for this instance, the update operation is disabled.

- An EML [`UPDATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md) operation is executed on both instances, which updates field `int_field2`.

- Using the ABAP SQL [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement, the content of the underlying database table is displayed.

Result: the first entity instance is updated successfully. For the second entity instance, the update operation fails and an entry is returned in the `failed` structure. The update was prevented by the dynamic feature control runtime check.

  
![figure](images_abdoc_fc_op.png)  

## Variant 2

`... features:global`

### Description

Global feature control enables or disables operations depending on the state of an entity instance. Global feature control can be defined for the following operations:

- The [standard operations](abenbdl_standard_operations.md) `create`, `update`, and `delete`

- [Operations for associations](abenbdl_association.md)

- [Actions](abenbdl_action.md)

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

- [Functions](abenbdl_function.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF that defines global feature control for the standard operation `delete`.

``` abap
unmanaged implementation in class bp_demo_rap_unmanaged_fc unique;
strict(2);

define behavior for DEMO_RAP_UNMANAGED_FC
lock master
authorization master ( none )
{
  create;
  update;
  delete ( features : global );
  field ( readonly:update ) key_field;
}
```

In the ABAP behavior pool, the following is specified: delete operations are allowed only in the time period between 10 pm and 6 am.

``` abap
METHOD get_global_features. 
  DATA(time1) = CONV t( '060000' ). 
  DATA(time2) = CONV t( '220000' ). 
 
  result = VALUE #( %delete = COND #( 
              WHEN cl_demo_date_time=>get_system_time( ) 
                BETWEEN time1 AND time2 
              THEN if_abap_behv=>fc-o-disabled 
              ELSE if_abap_behv=>fc-o-enabled ) 
                  ). 
 
  IF result-%delete = if_abap_behv=>fc-o-disabled. 
    APPEND VALUE #( %msg  = new_message_with_text( 
          text     = 'Delete is only allowed between 10 pm and 6 am.' 
          severity = if_abap_behv_message=>severity-error ) 
          %global = if_abap_behv=>mk-on ) 
          TO reported-demo_rap_unmanaged_fc. 
  ENDIF. 
ENDMETHOD.
```

For the complete implementation, see `BP_DEMO_RAP_UNMANAGED_FC======CCIMP`

The ABAP class `CL_DEMO_RAP_UNMANAGED_FC` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object.

- Three entity instances are created.

- An attempt is made to delete one of the entity instances.

  - In the time period between 10 pm and 6 am (night shift), the delete operation is successful.

  - In the time period between 6 am and 10 pm (day shift), the delete operation is disabled and an error message is returned.

Result: In this example, the delete operation is not allowed and an error message is returned. ![figure](images_abdoc_global_fc.jpg)

---
title: "RAP - action, Projection BDEF"
source_file: abenbdl_nonstandard_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - action, Projection BDEF

## Syntax

``` abap
[internal][static][factory][{static [default] factory}] action 
                  [( 
                  [features: {instance | global}] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:update] 
                  [lock:none] 
                   )] 
                   ActionName [external 'ExternalName'] 
                  [InputParameter] 
                  [OutputParameter] 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]  
```

[`internal`](abenbdl_internal.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_authorization_projection.md) · [`authorization:update`](abenbdl_authorization_projection.md) · [`lock:none`](abenbdl_lock_none.md) · [`external 'ExternalName'`](abenbdl_external.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md)

## Description

Defines a [RAP action](../../abap-glossary/abenrap_action_glosry.md) in the projection layer of a RAP BO. This works similar to defining actions in a base BDEF; see the topic [RAP - `action`](abenbdl_action.md).

There is a difference however regarding the [authorization concept](abenbdl_authorization.md) of an action defined in a projection BDEF: In a projection BDEF, no authorization master from the base BDEF is available. If an authorization concept is required, this must be specified for each node of a BO node as described in topic [RAP BDL - authorization, projection BDEF](abenbdl_authorization_projection.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [Action Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14ddc6b2442b4b97842af9158a1c9c44?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that defines a new action in the projection layer. It is based on the underlying base BO `DEMO_RAP_UNMANAGED_AUTH`. It defines the new action `deductDiscount` in the projection layer. For this action, global [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) is specified.

``` abap
projection implementation in class bp_demo_rap_proj_new_action unique;
strict(2);

define behavior for DEMO_RAP_PROJ_NEW_ACTION alias Root
authorization ( global )
{
  use create;
  use update;
  use delete;

  action deductDiscount parameter DEMO_CDS_ABSTRACT_DISCOUNT result [1] $self;
}
```

The ABAP behavior pool implements the global authorization control and the new action.

Global authorization control: In this simple example, the condition for global authorization control is always true.

``` abap
METHOD get_global_auth. 
  IF requested_authorizations-%action-deductDiscount EQ if_abap_behv=>mk-on. 
    "full access granted 
    IF sy-uname = sy-uname. 
      result-%action-deductDiscount = if_abap_behv=>auth-allowed. 
    ELSE. 
      result-%action-deductDiscount = if_abap_behv=>auth-unauthorized. 
      APPEND VALUE #( %msg    = new_message_with_text( 
                      text     = 'Operation not authorized.' 
                      severity = if_abap_behv_message=>severity-error ) 
                      %global = if_abap_behv=>mk-on ) TO reported-root. 
    ENDIF. 
  ENDIF. 
ENDMETHOD.
```

Action `deductDiscount`: The user can specify a discount percentage. This discount percentage is subtracted from the initial value of field `dec_field`.

``` abap
METHOD deductDiscount. 
  DATA lt_update_item 
         TYPE TABLE FOR UPDATE demo_rap_proj_new_action. 
  DATA(lt_keys) = keys. 
 
  LOOP AT lt_keys ASSIGNING FIELD-SYMBOL(<fs_key>) 
       WHERE %param-discount_percent IS INITIAL 
       OR %param-discount_percent > 100 
       OR %param-discount_percent <= 0. 
 
    APPEND VALUE #( %tky = <fs_key>-%tky ) TO failed-root. 
 
    DELETE lt_keys. 
  ENDLOOP. 
 
  CHECK lt_keys IS NOT INITIAL. 
 
  "get total price 
  READ ENTITIES OF demo_rap_proj_new_action IN LOCAL MODE 
    ENTITY Root 
      FIELDS ( DecFieldRoot ) 
      WITH CORRESPONDING #( lt_keys ) 
    RESULT DATA(lt_item) 
    FAILED DATA(read_failed). 
 
  failed = CORRESPONDING #( DEEP read_failed ). 
 
  LOOP AT lt_item ASSIGNING FIELD-SYMBOL(<fs_item>). 
    DATA lv_percentage TYPE decfloat16. 
    DATA(lv_discount_percent) = 
         lt_keys[ KEY entity %tky = <fs_item>-%tky ]-%param-discount_percent. 
    lv_percentage =  lv_discount_percent / 100 . 
    DATA(lv_reduced_fee) = <fs_item>-DecFieldRoot * ( 1 - lv_percentage ). 
 
    APPEND VALUE #( %tky       = <fs_item>-%tky 
                    DecFieldRoot = lv_reduced_fee  ) TO lt_update_item. 
  ENDLOOP. 
 
  "update total price with reduced price 
  MODIFY ENTITIES OF demo_rap_proj_new_action IN LOCAL MODE 
    ENTITY Root 
     UPDATE FIELDS ( DecFieldRoot ) 
     WITH lt_update_item 
  FAILED DATA(update_failed) 
  REPORTED DATA(update_reported). 
 
  "Read changed data for action result 
  READ ENTITIES OF demo_rap_proj_new_action IN LOCAL MODE 
    ENTITY Root 
      ALL FIELDS WITH 
      CORRESPONDING #( lt_item ) 
    RESULT DATA(lt_item_with_discount). 
 
  result = VALUE #( FOR item IN lt_item_with_discount ( %tky   = item-%tky 
                                              %param = item ) ). 
ENDMETHOD.
```

The ABAP class `CL_DEMO_RAP_PROJ_NEW_ACTION` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). It first creates two new entity instances and then executes the action `deductDiscount` for both of them.

Result: The specified discount percentage is subtracted from the initial value. ![figure](images_abdoc_new_action.jpg)

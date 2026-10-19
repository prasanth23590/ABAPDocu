---
title: "%global"
source_file: abapderived_types_global.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Information Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %global

## Use

`%global` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is used as a component of the `REPORTED` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) and indicates whether a message is to be retrieved for [global feature control](../rap-behavior-definitions/abenbdl_actions_fc.md) and [global authorization](../rap-behavior-definitions/abenbdl_authorization.md). These messages do not belong to a specific instance.

**Type**

The component has the following type: `ABP_BEHV_FLAG`

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `REPORTED [EARLY|LATE]`

## More Information

See more details on message handling in the Development Guide for the ABAP RESTful Application Programming Model, section [Messages](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ac74189b5cae49c1b091f04393bac069?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_REPORTED=CCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_MANAGED_ROOT_REPORTED`. The code example demonstrates the component `%global` in the context of an implementation for the `get_global_authorizations` method. See the executable program for this example further down.

``` abap
METHOD get_global_authorizations. 
 
  "The variable auth_flag represents the authorization that is 
  "granted or not. 
  "The demo avoids an authorization object. In this case, the 
  "permission is always granted. 
  DATA(auth_flag) = abap_true. 
 
  IF auth_flag =  abap_true. 
    IF requested_authorizations-%create EQ if_abap_behv=>mk-on. 
      result-%create = if_abap_behv=>auth-allowed. 
      APPEND VALUE #( 
        %msg = new_message_with_text( 
                text = 'Authorization granted.' 
                severity = if_abap_behv_message=>severity-success ) 
        %create = if_abap_behv=>mk-on 
        %global = if_abap_behv=>mk-on ) 
        TO reported-demo_managed_root_reported. 
 
    ENDIF. 
    IF requested_authorizations-%delete EQ if_abap_behv=>mk-on. 
      result-%delete = if_abap_behv=>auth-allowed. 
      APPEND VALUE #( 
        %msg = new_message_with_text( 
          text = 'Authorization granted.' 
          severity = if_abap_behv_message=>severity-success ) 
        %delete = if_abap_behv=>mk-on 
        %global = if_abap_behv=>mk-on ) 
        TO reported-demo_managed_root_reported. 
 
    ENDIF. 
 
    IF requested_authorizations-%update EQ if_abap_behv=>mk-on. 
      result-%update = if_abap_behv=>auth-allowed. 
      APPEND VALUE #( 
        %msg = new_message_with_text( 
          text = 'Authorization granted.' 
          severity = if_abap_behv_message=>severity-success ) 
        %update = if_abap_behv=>mk-on 
        %global = if_abap_behv=>mk-on ) 
        TO reported-demo_managed_root_reported. 
 
    ENDIF. 
 
  ELSE. 
    result-%create = if_abap_behv=>auth-unauthorized. 
    result-%delete = if_abap_behv=>auth-unauthorized. 
    result-%update = if_abap_behv=>auth-unauthorized. 
    APPEND VALUE #( 
      %msg = new_message_with_text( 
        text = 'Authorization denied.' 
        severity = if_abap_behv_message=>severity-error ) 
      %create = if_abap_behv=>mk-off 
      %update = if_abap_behv=>mk-off 
      %delete = if_abap_behv=>mk-off 
      %global = if_abap_behv=>mk-on ) 
      TO reported-demo_managed_root_reported. 
  ENDIF. 
 
  "Get time stamp 
  DATA: ts2 TYPE timestampl. 
  GET TIME STAMP FIELD ts2. 
 
  "Fill %OTHER 
  reported-%other = VALUE #( ( 
    new_message_with_text( 
      severity = if_abap_behv_message=>severity-information 
      text   = |a) Unbound message set at { ts2 TIMESTAMP = ISO }.| 
     ) ) ). 
 
ENDMETHOD.
```

## Executable Example

The example [Example for Message-Related BDEF Derived Type Components](abenderived_types_reported_abexa.md) demonstrates the use of various BDEF derived type components including `%global` with a managed RAP BO.

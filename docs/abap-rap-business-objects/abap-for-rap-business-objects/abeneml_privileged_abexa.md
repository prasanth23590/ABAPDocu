---
title: "Using the PRIVILEGED Addition with an ABAP EML Statement"
source_file: abeneml_privileged_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - PRIVILEGED"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using the PRIVILEGED Addition with an ABAP EML Statement

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates ABAP EML `MODIFY` statements executing an [action](../../abap-glossary/abenrap_action_glosry.md) with and without the addition `PRIVILEGED` using a managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_PRIVILEGED`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_PRIVILEGED
  as select from demo_tab_root_3
  {
    key key_field,
        field1,
        field2,
        field3,
        field4
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_PRIVILEGED` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_privileged unique;
strict ( 2 );
extensible;
with privileged mode disabling ac;

define authorization context ac
{
  'AUTHOBJ1';
  'AUTHOBJ2';
  'AUTHOBJ3';
}

define own authorization context by privileged mode;

define behavior for DEMO_MANAGED_PRIVILEGED
persistent table demo_tab_root_3
lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;
  action check_privileged;
  action forwarding_privileged;
  action forwarding_privileged_aux;
  field ( readonly : update ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, there is an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) available. The global class of the behavior pool is `BP_DEMO_MANAGED_PRIVILEGED`. This global class implements the local handler class `LHC_DEMO_MANAGED_PRIVILEGED`. The actual implementation takes place in the `BP_DEMO_MANAGED_PRIVILEGED====CCIMP`. The following method is relevant for the example:

- `check_privileged`

  First, the privileged mode is checked. The privileged mode can be queried by the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) using the method `GET_CURRENT_CONTEXT` of the class `CL_ABAP_BEHV_AUX`. If the privileged mode is active, a flag is set appropriately. For demonstration purposes in this implementation, the flag for the privileged mode is stored in a variable of the global class of the behavior pool so that the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) (another class or program) can access it. As a next step, an authority check for demonstrating the privileged mode is carried out using the statement [`AUTHORITY-CHECK OBJECT`](../../abap-programming-language/abap-authorizations/abapauthority-check.md). Like the flag for the privileged mode, the value of `sy-subrc` is stored in a variable in the global class. After the check, a loop is run across the imported key fields. In this implementation, only the RAP response parameters are manually filled (`failed` and `reported`). In case the authorization is not granted, both `failed` and `reported` are filled. In the other case, only the `reported` structure is filled with a success message.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_eml_privileged DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS: 
      constructor, 
      fill_dbtab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_privileged IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: ABAP EML Statements with ` && 
                        `and without the Addition PRIVILEGED` 
    )->write_doc( `<b>ABAP EML MODIFY Statement without PRIVILEGED</b>` 
    )->begin_code( `priv1` ). 
    MODIFY ENTITY demo_managed_privileged 
        EXECUTE check_privileged 
            FROM VALUE #( ( key_field = 1 ) 
                          ( key_field = 2 ) ) 
        FAILED FINAL(fail_no_priv) 
        REPORTED FINAL(reported_no_priv). 
    out->end_code( `priv1` 
      )->write_doc( |sy-subrc after carrying out the authority| && 
                    | check: { bp_demo_managed_privileged=>subrc }.| ). 
 
    IF bp_demo_managed_privileged=>priv_flag IS INITIAL. 
      out->write_html( `<span style="color:red;">` && 
                       `We are not in privileged mode.</span>` ). 
    ELSE. 
      out->write_html( `<span style="color:green;">` && 
                       `We are in privileged mode.</span>` ). 
    ENDIF. 
 
    out->write( fail_no_priv 
      )->write( reported_no_priv 
      )->line( 
      )->write_doc( `<b>ABAP EML MODIFY Statement with PRIVILEGED</b>` 
      )->begin_code( `priv2` ). 
    MODIFY ENTITY PRIVILEGED demo_managed_privileged 
        EXECUTE check_privileged 
            FROM VALUE #( ( key_field = 1 ) 
                          ( key_field = 2 ) ) 
            FAILED FINAL(failed_with_priv) 
            REPORTED FINAL(reported_with_priv). 
    out->end_code( `priv2` 
      )->write_doc( |sy-subrc after carrying out the authority| && 
                    | check: { bp_demo_managed_privileged=>subrc }.| ). 
 
    IF bp_demo_managed_privileged=>priv_flag IS INITIAL. 
      out->write_html( `<span style="color:red;">` && 
                       `We are not in privileged mode.</span>` ). 
    ELSE. 
      out->write_html( `<span style="color:green;">` && 
                       `We are in privileged mode.</span>` ). 
    ENDIF. 
 
    out->write( reported_with_priv ). 
 
  ENDMETHOD. 
  METHOD fill_dbtab. 
    DELETE FROM demo_tab_root_3. 
    MODIFY demo_tab_root_3 FROM TABLE @( VALUE #( 
      ( key_field = 1 
        field1 = 'a' 
        field2 = 'b' 
        field3 = 1 
        field4 = 2 ) 
      ( key_field = 2 
        field1 = 'c' 
        field2 = 'd' 
        field3 = 3 
        field4 = 4 ) ) ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    fill_dbtab( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The source code above uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class. There are two ABAP EML modify requests:

1.  ABAP EML modify request without using the addition `PRIVILEGED`

    The action `check_privileged` is executed based on two key fields. The output includes the `sy-subrc` value that is set when calling the method and carrying out the authority check. Here, it shows the value *12* indicating that the authorization has not been granted. It also shows a phrase indicating whether the privileged mode is active or not based on a flag that has been set during the method call. For the modify request, the response parameters for `failed` and `reported` are filled and are output too. In this case, they include all instances for which the authorization has not been granted and a failure message.

2.  ABAP EML modify request with using the addition `PRIVILEGED`

    Same as above, the action `check_privileged` is executed based on two key fields. The output demonstrates the effect of the addition `PRIVILEGED` that circumvents authority checks. Here, the `sy-subrc` value is *0* indicating that the authorization has been granted. For this request, only the response parameter for `reported` is filled with a success message.

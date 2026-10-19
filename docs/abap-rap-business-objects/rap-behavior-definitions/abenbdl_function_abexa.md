---
title: "RAP - function"
source_file: abenbdl_function_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - function"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a function is defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_CDS_FUNCTION_1`, which represents a purchase order.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, function'

define root view entity DEMO_CDS_FUNCTION_1
  as select from demo_purch_doc
{
  key purchasedocument         as Purchasedocument,
      description              as Description,
      status                   as Status,
      priority                 as Priority,
      price                    as Price,
      currency                 as Currency,
      purchasingorganization   as Purchasingorganization,
      purchasedocumentimageurl as Purchasedocumentimageurl,
      crea_date_time           as CreaDateTime,
      crea_uname               as CreaUname,
      lchg_date_time           as LchgDateTime,
      lchg_uname               as LchgUname
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CDS_FUNCTION_1` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

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

**Function definition**

Three functions are defined:

- `getDetails`: instance function that reads the values of the fields `PurchaseDocument`, `Price`, and `Status` for the specified entity instances and returns them in the result structure.

- `calculateTotal`: static function that sums up the prices of all entity instances with status 'O' and returns the total in its result structure.

  **Note:** This function uses a DDIC data element as output parameter. Note that the recommended procedure is to use only CDS abstract entities as BDEF parameters.

- `calculateDiscount`: function with an input parameter for a discount percentage. It subtracts the discount in percent from the initial price of an entity instance and returns the reduced price in its result structure.

All three functions merely deliver information in their result structure. No modify operation is carried out and no data is changed on the database.

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. It can be accessed under `BP_DEMO_CDS_FUNCTION_1========CCIMP`.

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
CLASS cl_demo_cds_function DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_function IMPLEMENTATION. 
  METHOD main. 
 
    fill_table(  ). 
 
    "Read operation executing a function 
    READ ENTITIES OF demo_cds_function_1 
     ENTITY PurchaseDocument 
      EXECUTE getDetails 
      FROM VALUE #( ( %tky-PurchaseDocument =  '1' ) 
                    ( %tky-PurchaseDocument =  '2' ) ) 
     RESULT FINAL(result) 
     FAILED FINAL(failed) 
     REPORTED FINAL(reported). 
 
    "Set up internal table to output 
    "the result of the function execution 
    TYPES: BEGIN OF result_structure, 
             purchasedocument TYPE purchdocde, 
             price            TYPE p LENGTH 15 DECIMALS 2, 
             status           TYPE c LENGTH 1, 
           END OF result_structure. 
 
    TYPES result_table_type TYPE TABLE OF result_structure. 
    DATA instance_function TYPE result_table_type. 
 
    LOOP AT result   ASSIGNING FIELD-SYMBOL(<result>). 
      APPEND VALUE #( purchasedocument = 
                      <result>-%param-purchasedocument 
                      price =  <result>-%param-price 
                      status =  <result>-%param-status 
                    ) TO instance_function. 
    ENDLOOP. 
 
    out->next_section( 
        'Instance function that reads data' 
        )->write( instance_function ). 
 
*      Read operation executing a static function 
    READ ENTITIES OF demo_cds_function_1 
   ENTITY PurchaseDocument 
    EXECUTE calculateTotal 
    FROM VALUE #( ( %cid = 'myCid' ) ) 
   RESULT FINAL(static_result) 
   FAILED FINAL(static_failed) 
   REPORTED FINAL(static_reported). 
 
    TYPES: BEGIN OF result_static, 
             cid   TYPE c LENGTH 20, 
             price TYPE p LENGTH 15 DECIMALS 2, 
           END OF result_static. 
 
    TYPES result_table_type_1 TYPE TABLE OF result_static. 
    DATA static_function TYPE result_table_type_1. 
 
    LOOP AT static_result ASSIGNING FIELD-SYMBOL(<static_result>). 
      APPEND VALUE #( cid = <static_result>-%cid 
                     price =  <static_result>-%param 
                    ) TO static_function. 
    ENDLOOP. 
 
    out->next_section( 
     'Static function that calculates the total price' 
     )->write( static_function ). 
 
    READ ENTITIES OF demo_cds_function_1 
         ENTITY PurchaseDocument 
          EXECUTE calculateDiscount 
          FROM VALUE #( (  %tky-purchasedocument   = '1' 
                           %param-discount_percent = 30 ) ) 
         RESULT FINAL(param_result) 
         FAILED FINAL(param_failed) 
         REPORTED FINAL(param_reported). 
 
    TYPES: BEGIN OF result_param, 
             purchasedocument TYPE purchdocde, 
             reduced_price    TYPE p LENGTH 15 DECIMALS 2, 
 
           END OF result_param. 
 
    TYPES result_table_type_2 TYPE TABLE OF result_param. 
    DATA function_input_param TYPE result_table_type_2. 
 
    LOOP AT param_result ASSIGNING FIELD-SYMBOL(<result_param>). 
      APPEND VALUE #( purchasedocument = <result_param>-purchasedocument 
                     reduced_price =  <result_param>-%param-price 
                    ) TO function_input_param. 
    ENDLOOP. 
 
    out->next_section( 
     'Function with input parameter that calculates a discount' 
     )->write( function_input_param ). 
  ENDMETHOD. 
  METHOD fill_table. 
    DELETE FROM demo_purch_doc. 
    INSERT demo_purch_doc FROM TABLE @(  VALUE #( 
    ( purchasedocument = '1' price = 500 status = 'O' ) 
    ( purchasedocument = '2' price = 77 status = 'O' ) 
    ( purchasedocument = '3' price = 12 status = 'O' ) 
    ( purchasedocument = '4' price = 999 status = 'O' ) 
    ( purchasedocument = '5' price = 234 status = 'O' ) 
    ( purchasedocument = '6' price = 665 status = 'O' ) 
    ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class and executes all three functions:

- First, the persistent database table `demo_purch_doc` is filled with values in the method `fill_table` using ABAP SQL. This way, BO instances already exist and do not have to be created using EML.

- The function `getDetails` is executed for two entity instances. These entity instances are determined via the values of their key fields. The function reads the values of the fields `PurchaseDocument`, `Price`, and `Status` for the specified entity instances and returns them in its result structure. The values from the result structure are appended to the internal structure `instance_function` and a screen output is generated.

- The function `calculateTotal` is a static function and thus applies to the complete BO, not to any specific entity instance. The function first filters all entity instances that have the status 'O' (in this example, all entity instances have the status 'O). Then, it sums up the values of the field `Price` of all entity instances with status 'O'. The values from the result structure are appended to the internal structure `static_function` and a screen output is generated.

- The function `calculateDiscount` is an instance function with an input parameter. To execute the function, it is required to specify an entity instance and also a value for the input parameter. In this example, the input parameter represents a discount percentage and the function subtracts the discount from the value of the field `Price` of an entity instance. It returns the reduced price in its result structure. The values from the result structure are appended to the internal structure `function_input_param` and a screen output is generated.

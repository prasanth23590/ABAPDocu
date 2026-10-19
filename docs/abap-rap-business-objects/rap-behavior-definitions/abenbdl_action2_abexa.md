---
title: "RAP - Action with Input Parameter"
source_file: abenbdl_action2_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action > RAP - Examples of Actions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Action with Input Parameter

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a [RAP action](../../abap-glossary/abenrap_action_glosry.md) with input parameter is defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of only one root entity `DEMO_CDS_ACTION_INPUT_PARAM`. The root entity represents a purchase order item.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, managed, action'
define root view entity DEMO_CDS_ACTION_INPUT_PARAM
as select from DEMO_CDS_PURCH_DOC_I
{
  key PurchaseDocumentItem,
  key PurchaseDocument,
  Description,
  Vendor,
  VendorType,
  Price,
  Currency,
  Quantity,
  QuantityUnit,
  OverallItemPrice,
  /* Associations */
  _PurchaseDocument
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CDS_ACTION_INPUT_PARAM` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_cds_action_input_param unique;
strict(2);

define behavior for DEMO_CDS_ACTION_INPUT_PARAM alias PurchaseItem
persistent table demo_purch_doc_i
lock master
authorization master (none)
{
  create;
  update;
  delete;

  action deductDiscount parameter DEMO_CDS_ABSTRACT_DISCOUNT result [1] $self;

  field(readonly:update) PurchaseDocument, PurchaseDocumentItem;

  mapping for DEMO_PURCH_DOC_I corresponding;
}
```

**Action definition**

The behavior definition defines one action: `deductDiscount`. The action has one input parameter that is typed with the CDS abstract entity `DEMO_CDS_ABSTRACT_DISCOUNT` and it defines the output parameter as the same type as the entity for which the action is executed. The purpose is to reduce the purchase order item price by the discount specified via the input parameter.

``` abap
action deductDiscount 
       parameter DEMO_CDS_ABSTRACT_DISCOUNT 
       result [1] $self;
```

The following [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) is used for typing the input parameter:

``` abap
@EndUserText.label: 'CDS abstract entity, discount'
define abstract entity DEMO_CDS_ABSTRACT_DISCOUNT
{
  discount_percent : abap.int1;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_CDS_ACTION_INPUT_PARAM`. This global class implements the local handler class `LHC_DEMO_CDS_ACTION_INPUT_PARA`, which contains the method `deductDiscount` to implement the action. This method is a `FOR MODIFY` method and it is typed based on the `PurchaseItem` entity. Its signature includes the result parameter. The actual implementation takes place in the `BP_DEMO_CDS_ACTION_INPUT_PARAMCCIMP`.

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
CLASS cl_demo_cds_action_reduce DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_action_reduce IMPLEMENTATION. 
  METHOD main. 
 
    DATA(percentage) = 10. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = percentage 
      )->request( ). 
    IF percentage > 100 
    OR percentage < 0. 
      out->write( 'Enter a valid percentage between 0 and 100' ). 
    ENDIF. 
 
    DELETE FROM demo_purch_doc_i. 
    TYPES: BEGIN OF structure, 
             PurchaseDocumentItem TYPE c LENGTH 10, 
             PurchaseDocument     TYPE c LENGTH 10, 
             Price                TYPE i, 
           END OF structure. 
 
    MODIFY ENTITIES OF demo_cds_action_input_param 
    ENTITY PurchaseItem 
    CREATE FIELDS ( PurchaseDocumentItem PurchaseDocument 
       Price ) WITH VALUE #( 
    ( %cid = 'cid1' 
      PurchaseDocumentItem = 'a' 
      PurchaseDocument = '1' 
      Price  = 200 ) 
    ( %cid = 'cid2' 
      PurchaseDocumentItem = 'b' 
      PurchaseDocument = '2' 
      Price  = 999 ) ) 
    FAILED DATA(failed) 
    REPORTED DATA(reported). 
 
    DATA no_discount TYPE SORTED TABLE OF structure 
      WITH UNIQUE KEY PurchaseDocumentItem PurchaseDocument. 
    READ ENTITY  demo_cds_action_input_param 
    ALL FIELDS WITH VALUE #( 
    ( PurchaseDocumentItem = 'a' PurchaseDocument = '1' ) 
    ( PurchaseDocumentItem = 'b' PurchaseDocument = '2' ) ) 
    RESULT FINAL(no_discount1). 
    MOVE-CORRESPONDING no_discount1 TO no_discount. 
    out->next_section(  'full price' 
    )->write( no_discount ). 
 
    TRY. 
        MODIFY ENTITIES OF demo_cds_action_input_param 
    ENTITY PurchaseItem 
    EXECUTE deductDiscount 
    FROM VALUE #( ( PurchaseDocumentItem = 'a' PurchaseDocument = '1' 
                   %param-discount_percent = percentage ) 
                   ( PurchaseDocumentItem = 'b' PurchaseDocument = '2' 
                   %param-discount_percent = percentage ) ) 
    RESULT FINAL(result) 
    FAILED failed 
    REPORTED reported. 
      CATCH cx_sy_conversion_overflow INTO FINAL(exc). 
        out->write( 'percentage not accepted' ). 
    ENDTRY. 
 
    COMMIT ENTITIES RESPONSE OF demo_cds_action_input_param 
    FAILED FINAL(commit_failed) 
    REPORTED FINAL(commit_reported). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT purchasedocumentitem, purchasedocument, Price 
      FROM demo_purch_doc_i 
      INTO TABLE @FINAL(demo_discount). 
 
    out->next_section( 'price with discount' 
      )->write( percentage 
      )->next_section( 'amount with discount' 
      )->write( demo_discount ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- The user is requested to enter the discount percentage.

- Two BO instances are created with the statement `MODIFY ENTITY`.

- The action `deductDiscount` is executed on one of the two instances with the statement `EXECUTE`.

- The `result`, `failed`, and `reported` parameters are returned.

- The changes that were performed by the action in the transactional buffer are committed to the database using the statement `COMMIT ENTITIES RESPONSE OF`.

- A `SELECT` statement is used to read the changed data from the persistent table `DEMO_PURCH_DOC_I`. As a result of the action, the price of a purchase order item is reduced by the percentage specified via the input parameter.

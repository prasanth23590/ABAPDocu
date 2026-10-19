---
title: "RAP - Action"
source_file: abenbdl_action1_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action > RAP - Examples of Actions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Action

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a [RAP action](../../abap-glossary/abenrap_action_glosry.md) is defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_CDS_PURCH_DOC_M` and its child entity `DEMO_CDS_PURCH_DOC_I_M`. The root entity represents a purchase order and the child entity represents a purchase order item.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, purcdoc, RAP managed'

define root view entity DEMO_CDS_PURCH_DOC_M
  as select from DEMO_CDS_OVERALL_PRICE
  composition of exact one to many DEMO_CDS_PURCH_DOC_I_M 
    as _PurchaseDocumentItem
{
  key PurchaseDocument,
      Description,
      Status,
      Priority,
      Currency,
      PurchasingOrganization,
      crea_date_time,
      crea_uname,

      /* Associations */
      _PurchaseDocumentItem
}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, purchdocitem, RAP_m'

define view entity DEMO_CDS_PURCH_DOC_I_M
  as select from DEMO_CDS_PURCH_DOC_I
  association to parent DEMO_CDS_PURCH_DOC_M as _PurchaseDocument 
    on $projection.PurchaseDocument = _PurchaseDocument.PurchaseDocument

{
  key PurchaseDocumentItem,
  key PurchaseDocument,
      Description,
      Vendor,
      VendorType,
      @Semantics.amount.currencyCode: 'Currency'
      Price,
      Currency,
      @Semantics.quantity.unitOfMeasure: 'QuantityUnit'
      Quantity,
      QuantityUnit,

      // Admin Data
      crea_date_time,
      crea_uname,

      /* Associations */
      _PurchaseDocument
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CDS_PURCH_DOC_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_cds_purch_doc_m unique;
strict(2);

define behavior for DEMO_CDS_PURCH_DOC_M alias PurchaseDocument
persistent table demo_purch_doc
lock master
etag master crea_date_time
authorization master (none)
{
  create;
  update;
  delete;
  association _PurchaseDocumentItem { create; }

  action Approve_Order result [1] $self;
  action Reject_Order  result [1] $self;

  field(readonly:update) PurchaseDocument;

  field ( readonly )  crea_uname , crea_date_time;

  mapping for demo_purch_doc corresponding;
}

define behavior for DEMO_CDS_PURCH_DOC_I_M alias PurchaseDocumentItem
persistent table DEMO_PURCH_DOC_I
lock dependent by _PurchaseDocument
authorization dependent by _PurchaseDocument
{
  update;
  delete;
  field ( readonly )  PurchaseDocumentItem , PurchaseDocument;
  field ( mandatory ) Price , Quantity , QuantityUnit;

  association _PurchaseDocument;

  mapping for DEMO_PURCH_DOC_I corresponding;
}
```

**Action definition**

Two actions are defined: `Approve_Order` and `Reject_Order`. If an employee wants to order equipment, the employee creates a purchase order and the manager can approve or reject this purchase order. Both actions have the output parameter `$self` with cardinality 1, so the parameter `result` has the same type as the entity for which the action is executed.

`action Approve_Order result [1] $self;`

`action Reject_Order result [1] $self;`

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_CDS_PURCH_DOC_M`. This global class implements the local handler class `LHC_PURCHASEDOCUMENT`, which contains two methods, `Approve_Order` and `Reject_Order`, to implement the actions. The actual implementation takes place in the `BP_DEMO_CDS_PURCH_DOC_M=======CCIMP` and it works as follows:

- For the passed entity instance, column *Status* is updated with *A* for *Approved* or *R* for *Rejected*, using the `MODIFY ENTITIES` statement.

- A local structure `lt_purchase` is created and filled with the entity instance using the statement `READ ENTITIES`.

- The output parameter `result` is filled. If an output parameter is defined, then it must always be filled.

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
CLASS cl_demo_cds_purchase DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_purchase IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_purch_doc_i. 
    DELETE FROM demo_purch_doc. 
    MODIFY ENTITY demo_cds_purch_doc_m 
          CREATE FIELDS ( PurchaseDocument Description ) 
          WITH VALUE #( 
           ( %cid = 'cid1' 
             PurchaseDocument = 'a' 
             Description = `aaa` ) 
           ( %cid = 'cid2' 
             PurchaseDocument = 'b' 
             Description = `bbb` ) ) 
          FAILED DATA(failed) 
          REPORTED DATA(reported). 
 
    MODIFY ENTITIES OF demo_cds_purch_doc_m 
    ENTITY PurchaseDocument 
    EXECUTE approve_order 
    FROM VALUE #( ( PurchaseDocument = 'a' ) ) 
 
    RESULT FINAL(result) 
    FAILED failed 
    REPORTED reported. 
 
    COMMIT ENTITIES RESPONSE OF demo_cds_purch_doc_m 
    FAILED FINAL(commit_failed) 
    REPORTED FINAL(commit_reported). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT PurchaseDocument, Description, Status 
    FROM demo_purch_doc 
    INTO TABLE @FINAL(demo_purch_doc_approved). 
 
    out->next_section( 'approve order' 
        )->write( demo_purch_doc_approved ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Two BO instances are created with the statement `MODIFY ENTITY`.

- The action `Approve_Order` is executed on one of the two instances with the statement `EXECUTE`.

- The `result`, `failed`, and `reported` parameters are returned.

- The changes that were performed by the action in the transactional buffer are committed to the database with the statement `COMMIT ENTITIES`.

- A `SELECT` statement is used to read the changed data from the persistent table `DEMO_PURCH_DOC`. As a result of the action, the column *Status* of the respective instance is filled with *A* for *Accepted*.

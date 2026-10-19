---
title: "RAP - Validation"
source_file: abenbdl_validation_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - validation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Validation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a validation is defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root view entity `DEMO_SALES_CDS_SO_1`, which represents a sales order.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, so, RAP managed'

define root view entity DEMO_SALES_CDS_SO_1 
as select from demo_sales_order
{
  key so_key as SoKey,
  id as Id,
  lifecycle_status as LifecycleStatus,
  created_by as CreatedBy,
  created_on as CreatedOn,
  created_at as CreatedAt,
  last_changed_by as LastChangedBy,
  last_changed_on as LastChangedOn,
  last_changed_at as LastChangedAt,
  buyer_id as BuyerId,
  ship_to_id as ShipToId,
  quantity_sum as QuantitySum,
  uom_sum as UomSum,
  amount_sum as AmountSum,
  currency_sum as CurrencySum,
  company_code as CompanyCode  
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_SALES_CDS_SO_1` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_sales_cds_so_1 unique;
strict ( 2 );

define behavior for DEMO_SALES_CDS_SO_1 alias SalesOrder
persistent table demo_sales_order
lock master
authorization master ( none )
{
  create;
  update;

  field ( readonly, numbering : managed ) SoKey;

  validation ValidateBuyerId on save { field BuyerId; }

  mapping for demo_sales_order corresponding
    {
      SoKey           = so_key;
      BuyerId         = buyer_id;
      ShipToId        = ship_to_id;
      QuantitySum     = quantity_sum;
      UomSum          = uom_sum;
      AmountSum       = amount_sum;
      CurrencySum     = currency_sum;
      CompanyCode     = company_code;
      CreatedBy       = created_by;
      CreatedAt       = created_at;
      CreatedOn       = created_on;
      LifecycleStatus = lifecycle_status;
      LastChangedBy   = last_changed_by;
      LastChangedOn   = last_changed_on;
      LastChangedAt   = last_changed_at;
    }
}
```

**Definition of validation**

The validation `ValidateBuyerId` checks if the value entered in field `BuyerId` is valid by checking whether this buyer ID exists in the database table `DEMO_SALES_BUPA`, which lists all business partners. It is triggered as soon as the field `BuyerId` is changed. If the buyer ID is not valid, the data changes are rejected and an error message is returned.

`validation ValidateBuyerId on save { field BuyerId; }`

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_SALES_CDS_SO_1`. The actual implementation takes place in the `BP_DEMO_SALES_CDS_SO_1========CCIMP`.

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
CLASS cl_demo_cds_validation DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_validation IMPLEMENTATION. 
  METHOD main. 
 
    fill_table( ). 
    DELETE FROM demo_sales_order. 
    MODIFY ENTITIES OF demo_sales_cds_so_1 
          ENTITY SalesOrder 
            CREATE 
              FIELDS ( BuyerId ) WITH VALUE #( 
               ( %cid = '1' BuyerId = `a` ) ) 
               MAPPED FINAL(mapped) 
               FAILED FINAL(failed) 
               REPORTED FINAL(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    MODIFY ENTITIES OF demo_sales_cds_so_1 
         ENTITY SalesOrder 
           CREATE 
             FIELDS ( BuyerId ) WITH VALUE #( 
              ( %cid = '2' BuyerId = `CCC` ) 
              ( %cid = '3' BuyerId = 'DDD' ) ) 
               MAPPED FINAL(mapped1) 
               FAILED FINAL(failed1) 
               REPORTED FINAL(reported1). 
 
    COMMIT ENTITIES RESPONSE OF demo_sales_cds_so_1 
    FAILED FINAL(failed_commit) 
    REPORTED FINAL(reported_commit). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    READ ENTITY demo_sales_cds_so_1 
    ALL FIELDS WITH CORRESPONDING #( mapped1-salesorder ) 
    RESULT FINAL(result) 
    FAILED FINAL(failed2) 
    REPORTED FINAL(reported2). 
 
    TYPES: BEGIN OF reported_structure, 
             key_field TYPE i, 
             message   TYPE if_abap_behv_message=>t_severity, 
             msgv1     TYPE symsgv, 
             msgv1_2   TYPE c LENGTH 50, 
           END OF reported_structure. 
 
    TYPES reported_table_type TYPE TABLE OF reported_structure. 
    DATA failed_entities TYPE reported_table_type. 
 
    LOOP AT reported2-salesorder ASSIGNING FIELD-SYMBOL(<rep>). 
      APPEND VALUE #(  key_field = <rep>-%key-SoKey 
      message = <rep>-%msg->m_severity 
      msgv1 = <rep>-%msg->if_t100_dyn_msg~msgv1 
       msgv1_2 = <rep>-%msg->if_message~get_text(  ) 
       ) TO failed_entities. 
    ENDLOOP. 
 
    SELECT so_key, buyer_id 
    FROM demo_sales_order 
    INTO TABLE @FINAL(valid_entities). 
 
    out->next_section( 'Valid entities' 
     )->write( valid_entities 
     )->next_section( 'Invalid entities' 
     )->write( failed_entities ). 
 
  ENDMETHOD. 
  METHOD fill_table. 
    DELETE FROM demo_sales_bupa. 
    INSERT demo_sales_bupa FROM TABLE @(  VALUE #( 
    ( id = 'a' gender = 'f'  family_name = 'Doe' ) 
    ( id = 'b' gender = 'm'  family_name = 'Smith' ) 
    ( id = 'c' gender = 'd'  family_name = 'Walker' ) 
    ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- A BO entity instance with the buyer ID `a` is created. This is a valid buyer ID, so the instance is committed to the database.

- Two further BO entity instances are created with invalid buyer IDs. These entity instances are rejected by the validation and they are inserted into an error table instead.

- The valid and the invalid entity instances are created in separate [RAP transactions](../../abap-glossary/abenrap_luw_glosry.md). If all three entity instances were created in one RAP transaction, all three of them would be rejected. All data changes in one RAP transaction must be consistent, otherwise, the complete content of the transactional buffer is rejected.

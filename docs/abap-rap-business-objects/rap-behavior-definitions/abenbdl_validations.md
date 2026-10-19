---
title: "RAP - validation"
source_file: abenbdl_validations.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - validation

## Syntax

``` abap
validation ValName on save { CUD1 | {field Field1}; 
                           [ CUD2;  ...; ]  [field Field2; ...] }  
```

## Description

A [RAP validation](../../abap-glossary/abenrap_validation_glosry.md) checks the consistency of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) based on trigger conditions. A validation is automatically invoked by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) if the trigger condition of the validation is fulfilled. Trigger conditions can be [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) ([create, update, delete](abenbdl_standard_operations.md)) `CUD1; CUD2; ...`, or modified fields `Field1; Field2; ...`. Validations are invoked during the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) at the end of a transaction and this is indicated by the mandatory addition `on save`. An invoked validation can reject inconsistent instance data from being saved and return [messages](../../abap-glossary/abenrap_message_glosry.md) to the consumer. Validations must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR VALIDATE`](../abap-for-rap-business-objects/abaphandler_meth_validate.md) in the local [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md).

The name `ValName` must comply with the general naming rules for RAP behavior definitions described in the topic [RAP BDL - General Syntax Rules](abenbdl_general_syntax_rules.md). In particular, is can have a maximum of 30 characters.

**Trigger Conditions**

There can be one or more trigger conditions. The trigger conditions can be changes of field values or the execution of one of the [standard operations](abenbdl_standard_operations.md) create, update, or delete. When one of these operations is executed for a [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md) or for an [active instance](../../abap-glossary/abenrap_active_instance_glosry.md), validations with the respective trigger operations are triggered. The validation is triggered if at least one trigger condition is fulfilled.

- `create`: The validation is executed when an instance is created.

- `update`: The validation is executed when an instance is updated.

  **Note:** Update works only in combination with the trigger operation `create`.

- `delete`: The validation is executed when an instance is deleted.

- `field`: The validation is executed when the value of the specified field(s) `Field1, Field2, ...` are changed by a create or update operation. The fields that are used for the trigger conditions must belong to the same RAP BO entity the validation is assigned to.

  **Note:** If a field is tagged with the [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md) [`notrigger[:warn]`](abenbdl_field_char.md), it must not be used in a trigger condition.

If a validation fails for a certain entity instance, the following effect takes place:

- The operation fails and the complete content of the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) of the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) is rejected. A commit to the database happens only if all data changes are consistent. One inconsistency leads to a rejection of all the content in the transactional buffer.

- No further data changes are possible as long as the invalid instances aren't corrected. An invalid entity instance must either be corrected using an [update operation](abenbdl_standard_operations.md), or the transactional buffer must be cleared using the EML statement [`ROLLBACK ENTITIES`](../abap-for-rap-business-objects/abaprollback_entities.md). The reason for this is that the [`COMMIT ENTITIES`](../abap-for-rap-business-objects/abapcommit_entities.md) statement aborts the save sequence in case of invalid instances and the transactional buffer is not emptied.

- An error message can be written to the [`reported`](../abap-for-rap-business-objects/abapeml_response.md) structure of the [`MODIFY ENTITIES`](../abap-for-rap-business-objects/abapmodify_entity_entities.md) statement.

- The keys of the failed instances can be written to the [`failed`](../abap-for-rap-business-objects/abapeml_response.md) structure.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP BOs.

  Not available for unmanaged, non-draft RAP BOs.

## Hints

- The execution order of validations is not fixed. If there is more than one validation triggered by the same condition, the execution order is not predictable.

- It is not allowed to use EML [`MODIFY`](../abap-for-rap-business-objects/abapmodify_entity_entities.md) statements in the implementation of validations.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Validations](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/171e26c36cca42699976887b4c8a83bf?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines the validation `ValidateBuyerId`.

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

The validation is implemented in the ABAP behavior pool. It checks if the buyer ID specified in a sales order is valid by checking whether this buyer ID exists in the database table that lists all business partners. It is triggered as soon as the field `BuyerId` is changed. If the buyer ID is not valid, the data changes are rejected and An error message is returned.

``` abap
METHOD ValidateBuyerId. 
  " Read relevant sales order data 
  READ ENTITIES OF demo_sales_cds_so_1 IN LOCAL MODE 
  ENTITY SalesOrder 
  FIELDS (  BuyerId ) WITH CORRESPONDING #(  keys ) 
  RESULT DATA(lt_salesorder) 
FAILED DATA(lt_failed). 
 
  failed =  CORRESPONDING #( DEEP lt_failed  ). 
  DATA lt_buyer TYPE SORTED TABLE OF demo_sales_bupa 
    WITH UNIQUE KEY id. 
 
  lt_buyer = CORRESPONDING #( lt_salesorder 
               MAPPING id = BuyerID EXCEPT * ). 
  DELETE lt_buyer WHERE id IS INITIAL. 
 
  IF  lt_buyer IS NOT INITIAL. 
    " Check if customer ID exists 
    SELECT FROM demo_sales_bupa FIELDS id 
                            FOR ALL ENTRIES IN @lt_buyer 
                            WHERE id = @lt_buyer-id 
    INTO TABLE @DATA(lt_buyer_db). 
  ENDIF. 
 
  " Raise message for non existing customer id 
  LOOP AT lt_salesorder INTO DATA(ls_so). 
    APPEND VALUE #( %tky        = ls_so-%tky 
                    %state_area = 'VALIDATE_BUYER' ) 
                     TO reported-salesorder. 
 
    IF ls_so-BuyerId IS NOT INITIAL 
      AND NOT line_exists( lt_buyer_db[ id = ls_so-BuyerId ] ). 
      APPEND VALUE #( %tky = ls_so-%tky ) TO failed-salesorder. 
      APPEND VALUE #( %tky             = ls_so-%tky 
                      %state_area      = 'VALIDATE_BUYER' 
                      %msg             = new_message_with_text( 
                      severity = if_abap_behv_message=>severity-error 
                      text     = 'validation failed' ) 
                      %element-BuyerID = if_abap_behv=>mk-on ) 
                      TO reported-salesorder. 
    ENDIF. 
  ENDLOOP. 
ENDMETHOD.
```

**EML access 1: Valid instances are committed to the database, for invalid instances, an error message is returned.**

The class `CL_DEMO_CDS_VALIDATION` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md). It creates three BO instances - one of them is valid, two are invalid. The valid entity instance is committed to the database, while for the invalid instances, error messages are returned. The valid entity instance is created in a different RAP transaction than the invalid ones. If all three entity instances were created in one RAP transaction - in this case, with the same `COMMIT ENTITIES` statement - all three of them would be rejected.

Result: Valid instances are committed to the database, for invalid instances, an error message is returned. ![figure](images_abdoc_validation.png)

**EML access 2: If a RAP transaction contains only one inconsistent instance, the complete content of the transactional buffer is rejected.**

The class `CL_DEMO_CDS_VALIDATION_1` demonstrates that validations accept or reject data changes per RAP transaction. It creates the same three BO instances as the report `DEMO_CDS_VALIDATION`, one of them valid, the other two invalid.

Code snippet:

``` abap
DELETE FROM demo_sales_order. 
    MODIFY ENTITIES OF demo_sales_cds_so_1 
          ENTITY SalesOrder 
            CREATE FIELDS ( BuyerId ) WITH VALUE #( 
               ( %cid = '1' BuyerId = `a` ) 
               ( %cid = '2' BuyerId = `CCC` ) 
               ( %cid = '3' BuyerId = 'DDD' ) ) 
               MAPPED FINAL(mapped) 
               FAILED FINAL(failed) 
               REPORTED FINAL(reported). 
    COMMIT ENTITIES.
```

Since this RAP transaction contains two inconsistent instances, all data changes are rejected, even the valid instance.

Result: The valid instance is not committed to the database. ![figure](images_abdoc_validation_failed.png)

**EML access 3: If an invalid instance is not corrected or deleted proactively, no further data changes are possible.**

The class `CL_DEMO_CDS_VALIDATION_2` demonstrates how an invalid instance blocks further changes:

- It creates one valid instance and commits it to the database.

- It tries to create an invalid instance. This is rejected by the validation.

- It tries to create another valid instance. This is rejected. It is required to first correct or delete the invalid instance.

Code snippet:

``` abap
" valid instance: commit works. 
MODIFY ENTITIES OF demo_sales_cds_so_1 
          ENTITY SalesOrder 
          CREATE FIELDS ( BuyerId ) WITH VALUE #( 
               ( %cid = '1' BuyerId = `a` ) ) 
               MAPPED DATA(mapped) 
               FAILED DATA(failed) 
               REPORTED DATA(reported). 
    COMMIT ENTITIES. 
 
" invalid instances: commit fails. 
    MODIFY ENTITIES OF demo_sales_cds_so_1 
         ENTITY SalesOrder 
         CREATE FIELDS ( BuyerId ) WITH VALUE #( 
              ( %cid = '2' BuyerId = `CCC` ) 
              ( %cid = '3' BuyerId = 'DDD' ) ) 
               MAPPED FINAL(mapped1) 
               FAILED FINAL(failed1) 
               REPORTED FINAL(reported1). 
    COMMIT ENTITIES RESPONSE OF demo_sales_cds_so_1 
    FAILED FINAL(failed_commit) 
    REPORTED FINAL(reported_commit). 
 
" valid instance: commit fails. Invalid instances must be 
" corrected or deleted first. 
    MODIFY ENTITIES OF demo_sales_cds_so_1 
         ENTITY SalesOrder 
         CREATE FIELDS ( BuyerId ) WITH VALUE #( 
              ( %cid = '1' BuyerId = `b` ) ) 
              MAPPED mapped 
              FAILED failed 
              REPORTED reported. 
    COMMIT ENTITIES.
```

Result: Only the first valid instance is committed to the database. The second valid instance is blocked. ![figure](images_abdoc_validation_failed_1.png)

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - validation](abenbdl_validation_abexa.md).

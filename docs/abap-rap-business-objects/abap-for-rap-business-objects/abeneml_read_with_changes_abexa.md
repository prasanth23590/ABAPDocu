---
title: "ABAP EML - Read Operations Using WITH CHANGES"
source_file: abeneml_read_with_changes_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES > Examples for ABAP EML READ"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - Read Operations Using WITH CHANGES

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the `WITH CHANGES` addition to both short and long form of the ABAP EML `READ` statement. It also shows a dynamic ABAP EML `READ` statement that includes the `WITH CHANGES` functionality.

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_ENTITY_M`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_RAP_ENTITY_M
  as select from demo_tab_root_5
{
  key key_field,
      field1,
      field2,
      field3,
      field4
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_ENTITY_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_rap_entity_m unique;
strict ( 2 );

define behavior for DEMO_RAP_ENTITY_M
persistent table demo_tab_root_5
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;

  action with_changes;
  action with_changes_dynamic;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_ENTITY_M`. The actual implementation takes place in the `BP_DEMO_RAP_ENTITY_M==========CCIMP`.

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
CLASS cl_demo_rap_eml_read_w_changes DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs, 
      select_from_db_and_display 
        IMPORTING out TYPE REF TO if_demo_output, 
      get_control_flags IMPORTING out  TYPE REF TO if_demo_output 
                                  text TYPE string OPTIONAL. 
    DATA: root_tab        TYPE TABLE OF demo_tab_root_5 WITH EMPTY KEY, 
          failed_response TYPE RESPONSE FOR FAILED demo_rap_entity_m. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_read_w_changes IMPLEMENTATION. 
  METHOD main. 
 
    out->write( |Demonstrating READ ... WITH CHANGES ... and | && 
                |dynamic ABAP EML READ statements\n| ). 
 
    out->write( |Unchanged instances \n| ). 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes 
     FROM VALUE #( ( key_field = 1 ) 
                   ( key_field = 2 ) ) 
     FAILED failed_response. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db_and_display( out ). 
    get_control_flags( out ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( |Updated instance \n| ). 
 
    MODIFY ENTITY demo_rap_entity_m 
     UPDATE FIELDS ( field4 ) 
     WITH VALUE #( ( key_field = 3 field4 = 123 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes 
     FROM VALUE #( ( key_field = 3 ) 
                   ( key_field = 4 ) ) 
     FAILED failed_response. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db_and_display( out ). 
    get_control_flags( out ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( |Created instance \n| ). 
 
    MODIFY ENTITY demo_rap_entity_m 
     CREATE FIELDS ( key_field field4 ) AUTO FILL CID 
     WITH VALUE #( ( key_field = 5 field4 = 456 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes 
     FROM VALUE #( ( key_field = 5 ) ) 
     FAILED failed_response. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db_and_display( out ). 
    get_control_flags( out ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( |Deleted instance \n| ). 
 
    MODIFY ENTITY demo_rap_entity_m 
     DELETE FROM VALUE #( ( key_field = 6 ) 
                          ( key_field = 7 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes 
     FROM VALUE #( ( key_field = 6 ) 
                   ( key_field = 7 ) 
                   ( key_field = 8 ) ) 
     FAILED failed_response. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write( `Instances whose %chg value is ` && 
                `if_abap_behv=>cop-delete in the handler method ` && 
                `implementation:` ). 
    out->write( bp_demo_rap_entity_m=>deleted_keys ). 
    CLEAR bp_demo_rap_entity_m=>deleted_keys. 
 
    select_from_db_and_display( out ). 
    get_control_flags( out ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( |Recreated instance \n| ). 
 
    MODIFY ENTITY demo_rap_entity_m 
     DELETE FROM VALUE #( ( key_field = 9 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     CREATE FIELDS ( key_field field4 ) AUTO FILL CID 
     WITH VALUE #( ( key_field = 9 field4 = 789 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes 
     FROM VALUE #( ( key_field = 9 ) ) 
     FAILED failed_response. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db_and_display( out ). 
    get_control_flags( out ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( |Dynamic ABAP EML READ statement \n| ). 
 
    "Unchanged instance 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes_dynamic 
     FROM VALUE #( ( key_field = 10 ) ( key_field = 11 ) ) 
     FAILED failed_response. 
 
    get_control_flags( out = out 
      text = `Dynamic EML READ (unchanged instances)` ). 
 
    "Created instance 
    MODIFY ENTITY demo_rap_entity_m 
     CREATE FIELDS ( key_field field4 ) AUTO FILL CID 
     WITH VALUE #( ( key_field = 12 field4 = 1234 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes_dynamic 
     FROM VALUE #( ( key_field = 12 ) ) 
     FAILED failed_response. 
 
    get_control_flags( out = out 
                       text = `Dynamic EML READ (created instance)` ). 
 
    "Uupdated instance 
    MODIFY ENTITY demo_rap_entity_m 
     UPDATE FIELDS ( field4 ) 
     WITH VALUE #( ( key_field = 13 field4 = 5678 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes_dynamic 
     FROM VALUE #( ( key_field = 13 ) ) 
     FAILED failed_response. 
 
    get_control_flags( out = out 
                       text = `Dynamic EML READ (updated instance)` ). 
 
    "Deleted instance 
    MODIFY ENTITY demo_rap_entity_m 
      DELETE FROM VALUE #( ( key_field = 14 ) ) 
      FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes_dynamic 
     FROM VALUE #( ( key_field = 14 ) ) 
     FAILED failed_response. 
 
    get_control_flags( out = out 
                       text = `Dynamic EML READ (deleted instance)` ). 
 
    "Recreated instance 
    MODIFY ENTITY demo_rap_entity_m 
     DELETE FROM VALUE #( ( key_field = 15 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     CREATE FIELDS ( key_field field4 ) AUTO FILL CID 
     WITH VALUE #( ( key_field = 15 field4 = 1515 ) ) 
     FAILED failed_response. 
 
    MODIFY ENTITY demo_rap_entity_m 
     EXECUTE with_changes_dynamic 
     FROM VALUE #( ( key_field = 15 ) ) 
     FAILED failed_response. 
 
    get_control_flags( out = out 
                       text = `Dynamic EML READ (recreated instance)` ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db_and_display( out ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
  METHOD get_control_flags. 
    IF text IS SUPPLIED. 
      out->write( text ). 
    ENDIF. 
 
    IF bp_demo_rap_entity_m=>control_flags IS INITIAL. 
      out->write( `Only initial %control component values ` && 
                  `in the read result's type.` ). 
    ELSE. 
      out->write( `Changed %control component values ` && 
                  `in the read result's type:` ). 
      out->write( bp_demo_rap_entity_m=>control_flags ). 
    ENDIF. 
    CLEAR bp_demo_rap_entity_m=>control_flags. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
    INSERT demo_tab_root_5 FROM TABLE @( VALUE #( 
      ( key_field = 1 ) 
      ( key_field = 2 ) 
      ( key_field = 3 ) 
      ( key_field = 4 ) 
      ( key_field = 6 ) 
      ( key_field = 7 ) 
      ( key_field = 8 ) 
      ( key_field = 9 ) 
      ( key_field = 10 ) 
      ( key_field = 11 ) 
      ( key_field = 13 ) 
      ( key_field = 14 ) 
      ( key_field = 15 ) ) ). 
  ENDMETHOD. 
  METHOD select_from_db_and_display. 
    SELECT * 
   FROM demo_tab_root_5 
   ORDER BY key_field 
   INTO TABLE @root_tab. 
 
    IF root_tab IS NOT INITIAL. 
      out->write( root_tab ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class. The example demonstrates the `WITH CHANGES` addition as follows:

- The BDEF specifies two actions: `with_changes` and `with_changes_dynamic`.

- The `with_changes` action implements both the short and long forms of ABAP EML `READ` statements using the `WITH CHANGES` addition. Based on the key values passed to the action, either the short or long form is executed to demonstrate both options.

- The `with_changes_dynamic` action implements a dynamic ABAP EML `READ` statement, showcasing the `WITH CHANGES` functionality by assigning the value `if_abap_behv=>typekind-result_chg` to the `full` component.

- The consumer class executes the actions to illustrate the effects of various ABAP EML `READ` statements following specific operations in a RAP transaction:

  - Unchanged instances

  - Created instances

  - Updated instances

  - Deleted instances

  - Recreated instances

- The `WITH CHANGES` functionality is demonstrated by assigning the `%chg` value of the read result to RAP BO instances in an ABAP EML `MODIFY` statement within the action implementation. Additionally, the `%control` component values of the read result are added to an internal table in the global class of the implementation class. The `%chg` value is assigned to the `field2` field, while `field1` receives a string indicating which ABAP EML `READ` form is used. The non-initial value of the `field4` field indicates the creation, update, or recreation of RAP BO instances in the RAP transaction, while an initial value indicates an unchanged RAP BO instance. To visualize the `%chg` value in the case of deletion, an internal table in the global class of the implementation class is populated.

---
title: "RAP - Factory Action"
source_file: abenbdl_action3_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action > RAP - Examples of Actions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Factory Action

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how factory actions are defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of a single root entity `DEMO_RAP_FACTORY_ACTION`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'test'
define root view entity demo_rap_factory_action
  as select from demo_dbtab_root
{
  key key_field,
      data_field,
      char_field,
      char_field_2,
      dec_field
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_FACTORY_ACTION` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_rap_factory_action unique;
strict(2);

define behavior for demo_rap_factory_action
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;

  // copy instance, assign new unique key value
  factory action copy_instance [1];

  // create new instance with default values
  static factory action new_instance [1];
}
```

**Action definition**

Two factory actions are defined:

- The instance factory action `copy_instance` copies all values of the requested entity instance and assigns a new key value.

- The static factory action `new_instance` creates new entity instances with default values.

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_FACTORY_ACTION`. This global class implements the local handler class `LHC_DEMO_RAP_FACTORY_ACTION`, which contains two methods, `copy_instance` and `new_instance`, to implement the factory actions. The actual implementation takes place in the `BP_DEMO_RAP_FACTORY_ACTION====CCIMP`:

`copy_instance`:

``` abap
METHOD copy_instance. 
  READ ENTITIES OF demo_rap_factory_action IN LOCAL MODE 
      ENTITY demo_rap_factory_action 
      ALL FIELDS WITH CORRESPONDING #( keys ) 
      RESULT DATA(result) 
      FAILED failed. 
 
  SELECT 
  FROM demo_dbtab_root 
  FIELDS MAX( key_field ) 
  INTO @DATA(lv_max_key_field). 
 
  DATA: ls_create TYPE STRUCTURE FOR  CREATE demo_rap_factory_action. 
  DATA: lt_create TYPE TABLE FOR CREATE demo_rap_factory_action. 
 
  LOOP AT keys INTO DATA(key). 
 
    lv_max_key_field = lv_max_key_field + 1. 
    IF line_exists( result[ 
                        KEY entity  key_field = key-key_field ] ). 
      ls_create-%data = CORRESPONDING #( result[ 
                          KEY entity  key_field = key-key_field ]  ). 
      ls_create-key_field = lv_max_key_field. 
    ENDIF. 
    APPEND ls_create TO lt_create. 
  ENDLOOP. 
 
  MODIFY ENTITIES OF demo_rap_factory_action IN LOCAL MODE 
    ENTITY demo_rap_factory_action 
    CREATE 
    AUTO FILL CID 
    FIELDS ( key_field char_field char_field_2 data_field dec_field ) 
    WITH lt_create 
    MAPPED   mapped 
    REPORTED reported 
    FAILED   failed. 
ENDMETHOD.
```

`new_instance`:

``` abap
METHOD new_instance. 
  MODIFY ENTITIES OF demo_rap_factory_action IN LOCAL MODE 
      ENTITY demo_rap_factory_action 
        CREATE FROM VALUE #( FOR <instance> IN keys 
                               ( %cid      = <instance>-%cid 
                                 key_field = '4' 
                                 char_field    = 'C' 
                                 %control  = 
                                 VALUE #( 
                                   key_field = if_abap_behv=>mk-on 
                                   char_field = if_abap_behv=>mk-on ) 
                                   ) ) 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
ENDMETHOD.
```

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
CLASS cl_demo_rap_factory_action DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_factory_action IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_dbtab_root. 
 
    MODIFY ENTITIES OF demo_rap_factory_action 
      ENTITY demo_rap_factory_action 
        CREATE FIELDS ( key_field char_field ) WITH VALUE #( 
        ( %cid = 'cid1' key_field = 1 char_field = 'A' ) 
         ( %cid = 'cid2' key_field = 2 char_field = 'B' ) 
        ) 
        MAPPED FINAL(create_mapped) 
        FAILED FINAL(create_failed) 
        REPORTED FINAL(create_reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(result). 
 
    MODIFY ENTITIES OF demo_rap_factory_action 
          ENTITY demo_rap_factory_action 
    EXECUTE copy_instance 
    AUTO FILL CID WITH VALUE #( ( key_field = 1 ) ) 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
 
    SELECT key_field, char_field 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(result1). 
 
    MODIFY ENTITIES OF demo_rap_factory_action 
      ENTITY demo_rap_factory_action 
    EXECUTE new_instance 
    AUTO FILL CID WITH VALUE #( ( %cid = 'My%CID' ) ) 
    FAILED FINAL(failed1) 
    REPORTED FINAL(reported1). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(result2). 
 
    out->next_section( 'result create' 
        )->write( result 
        )->next_section( 'result instance factory action' 
        )->write( result1 
        )->next_section( 'result static factory action' 
        )->write( result2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Two BO entity instances are created with the statement `MODIFY ENTITY`.

- The action `copy_instance` is executed on one of the two instances with the statement `EXECUTE` and the changes that were performed by the action in the transactional buffer are committed to the database with the statement `COMMIT ENTITIES`.

- The action `new_instance` is executed with the statement `EXECUTE` and the changes that were performed by the action in the transactional buffer are committed to the database with the statement `COMMIT ENTITIES`.

- A `SELECT` statement is used to read the changed data from the persistent table `DEMO_DBTAB_ROOT`. As a result, two new entity instances are created: one is a duplicate of the entity instance with key value '1', but is has a new key value. One is created with default values.

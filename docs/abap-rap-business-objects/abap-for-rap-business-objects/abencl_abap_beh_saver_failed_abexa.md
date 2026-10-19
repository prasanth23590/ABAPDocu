---
title: "Example for CL_ABAP_BEHAVIOR_SAVER_FAILED"
source_file: abencl_abap_beh_saver_failed_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > CL_ABAP_BEHAVIOR_SAVER_FAILED, RAP Saver Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for CL_ABAP_BEHAVIOR_SAVER_FAILED

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the RAP saver class `CL_ABAP_BEHAVIOR_SAVER_FAILED` using a simple managed RAP BO [with unmanaged save](../rap-behavior-definitions/abenbdl_saving.md).

**Data model**

The CDS data model consists of the root entity `DEMO_SAVE_F_UNM_S_M`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_SAVE_F_UNM_S_M as select from demo_tab_root_7
{
  key key_field,
  char1,
  char2,
  num1,
  num2
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_SAVE_F_UNM_S_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed with unmanaged save
implementation in class bp_demo_save_f_unm_s_m unique;
strict ( 2 );

define behavior for DEMO_SAVE_F_UNM_S_M alias root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;
  validation validate on save { create; update; delete; }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_SAVE_F_UNM_S_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_SAVE_F_UNM_S_M========CCIMP` of the behavior pool. The ABP includes the implementation of a validation. In this simple example, the validation fails if particular fields have particular values.

The class `LSC_DEMO_SAVE_F_UNM_S_M` is the RAP saver class that inherits from `CL_ABAP_BEHAVIOR_SAVER_FAILED`. The `SAVE_MODIFIED` saver method is implemented in a way that a save is denied for a RAP BO instance if particular fields have particular values in a RAP create operation.

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
CLASS cl_demo_rap_saver_failed DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      f_early   TYPE RESPONSE FOR FAILED EARLY demo_save_f_unm_s_m, 
      rep_early TYPE RESPONSE FOR REPORTED EARLY demo_save_f_unm_s_m, 
      f_late    TYPE RESPONSE FOR FAILED LATE demo_save_f_unm_s_m, 
      rep_late  TYPE RESPONSE FOR REPORTED LATE demo_save_f_unm_s_m. 
    METHODS: 
      select_from_dbtab, 
      display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_saver_failed IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demonstrating cl_abap_behavior_saver_failed` 
    )->line( 
    )->write( `----- Successful saving ` && 
    `(sy-subcr = 0 after committing) -----` ). 
 
    MODIFY ENTITY demo_save_f_unm_s_m 
      CREATE FIELDS ( key_field char1 char2 num1 num2 ) 
      WITH VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          char1 = 'aaa' 
          char2 = 'bbb' 
          num1 = 11 
          num2 = 111 ) ) 
      REPORTED rep_early 
      FAILED f_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_save_f_unm_s_m 
      FAILED f_late 
      REPORTED rep_late. 
 
    IF sy-subrc <> 0. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
      out->write(  `Issue in the save sequence.`  ). 
    ELSE. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
    ENDIF. 
 
    "If there are entries, displaying early and late 
    "FAILED and REPORTED responses 
    display_responses( ). 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Failure in RAP interaction phase ` && 
    `-----` ). 
 
    MODIFY ENTITY demo_save_f_unm_s_m 
      CREATE FIELDS ( key_field char1 char2 num1 num2 ) 
      WITH VALUE #( 
        ( %cid = 'cid2'  "instance to fail 
          key_field = 1 
          char1 = 'yyy' 
          char2 = 'zzz' 
          num1 = 12 
          num2 = 345 ) 
        ( %cid = 'cid3' 
          key_field = 10 
          char1 = 'ccc' 
          char2 = 'ddd' 
          num1 = 100 
          num2 = 1000 ) ) 
      REPORTED rep_early 
      FAILED f_early. 
 
    "Demonstrating that the failed instance is not available 
    "in the transactional buffer. The read instance is from 
    "the database. 
    DATA(key) = 1. 
 
    READ ENTITY demo_save_f_unm_s_m 
      ALL FIELDS  WITH VALUE #( 
        ( key_field = key ) ) 
      RESULT DATA(res1). 
 
    IF res1 IS INITIAL. 
      out->write(  `Read result is empty for key field with value ` 
                 && key && `.`  ). 
    ELSE. 
      out->write(  res1  ). 
    ENDIF. 
 
    COMMIT ENTITIES RESPONSE OF demo_save_f_unm_s_m 
      FAILED f_late 
      REPORTED rep_late. 
 
    IF sy-subrc <> 0. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
      out->write(  `Issue in the save sequence.`  ). 
    ELSE. 
      out->write( |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
    ENDIF. 
 
    "If there are entries, displaying early and late 
    "FAILED and REPORTED responses 
    display_responses( ). 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Failure in early save phase ` && 
    `(sy-subcr = 4 after committing) -----` ). 
 
    MODIFY ENTITY demo_save_f_unm_s_m 
      CREATE FIELDS ( key_field char1 char2 num1 num2 ) 
      WITH VALUE #( 
        ( %cid = 'cid4' 
          key_field = 2 
          char1 = 'eee' 
          char2 = 'fff' 
          num1 = 22 
          num2 = 222 ) ) 
      REPORTED rep_early 
      FAILED f_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_save_f_unm_s_m 
      FAILED f_late 
      REPORTED rep_late. 
 
    IF sy-subrc <> 0. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
      out->write(  `Issue in the save sequence.`  ). 
 
      "Demonstrating that the RAP BO instance with the key 
      "is still available in the transactional buffer. 
      key = 2. 
 
      READ ENTITY demo_save_f_unm_s_m 
        ALL FIELDS  WITH VALUE #( 
          ( key_field = key ) ) 
        RESULT DATA(res2). 
 
      IF res2 IS INITIAL. 
        out->write(  `Read result is empty for key field with value ` 
                   && key && `.`  ). 
      ELSE. 
        out->write(  res2  ). 
 
        "Correcting failed entry 
        MODIFY ENTITY demo_save_f_unm_s_m 
          UPDATE FIELDS ( num2 ) WITH VALUE #( 
            ( key_field = 2 
              num2 = 2222 ) ). 
 
        COMMIT ENTITIES. 
 
      ENDIF. 
 
    ELSE. 
      out->write( |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
    ENDIF. 
 
    "If there are entries, displaying early and late 
    "FAILED and REPORTED responses 
    display_responses( ). 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Failure in late save phase ` && 
    `(sy-subcr = 8 after committing) -----` ). 
 
    MODIFY ENTITY demo_save_f_unm_s_m 
      CREATE FIELDS ( key_field char1 char2 num1 num2 ) WITH VALUE #( 
        ( %cid = 'cid5' 
          key_field = 3 
          char1 = 'ggg' 
          char2 = 'hhh' 
          num1 = 33 
          num2 = 333 ) ) 
      REPORTED rep_early 
      FAILED f_early. 
 
    "Note: The example is implemented in a way that a RAP BO 
    "cannot be saved if particular values are present in 
    "particular fields. 
    COMMIT ENTITIES RESPONSE OF demo_save_f_unm_s_m 
      FAILED f_late 
      REPORTED rep_late. 
 
    IF sy-subrc <> 0. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
      out->write(  `Issue in the save sequence.`  ). 
 
      key = 3. 
 
      "Demonstrating that there is no RAP BO instance in the 
      "transactional buffer with the key used for the create 
      "operation above. 
      READ ENTITY demo_save_f_unm_s_m 
        ALL FIELDS  WITH VALUE #( 
          ( key_field = key ) ) 
        RESULT DATA(res3). 
 
      IF res3 IS INITIAL. 
        out->write(  `Read result is empty for key field with value ` 
        && key && `.` ). 
      ELSE. 
        out->write(  res3  ). 
      ENDIF. 
 
    ELSE. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }|  ). 
    ENDIF. 
 
    "If there are entries, displaying early and late 
    "FAILED and REPORTED responses 
    display_responses( ). 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
********************************************************************** 
 
    out->write( `----- RAP BO consumer to proceed after an issue in` && 
    ` the late save phase and setting sy-subcr to 8 -----` ). 
 
    "Without a rollback, the exception CX_SADL_DUMP_APPL_MODEL_ERROR 
    "is raised. 
    ROLLBACK ENTITIES. 
 
    MODIFY ENTITY demo_save_f_unm_s_m 
      CREATE FIELDS ( key_field char1 char2 num1 num2 ) WITH VALUE #( 
        ( %cid = 'cid6' 
          key_field = 4 
          char1 = 'iii' 
          char2 = 'jjj' 
          num1 = 44 
          num2 = 444 ) ) 
      REPORTED rep_early 
      FAILED f_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_save_f_unm_s_m 
      FAILED f_late 
      REPORTED rep_late. 
 
    IF sy-subrc <> 0. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }| ). 
      out->write(  `Issue in the save sequence.`  ). 
    ELSE. 
      out->write(  |sy-subrc after COMMIT ENTITIES: { sy-subrc }|  ). 
    ENDIF. 
 
    "If there are entries, displaying early and late 
    "FAILED and REPORTED responses 
    display_responses( ). 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
  ENDMETHOD. 
  METHOD display_responses. 
 
    IF f_early IS NOT INITIAL. 
      out->write( `Failed early: Key: ` && 
                f_early-root[ 1 ]-%key-key_field && 
                `, Fail cause: ` && 
                f_early-root[ 1 ]-%fail-cause ). 
    ENDIF. 
 
    IF rep_early IS NOT INITIAL. 
      out->write( `Reported early: ` && 
                rep_early-root[ 1 ]-%msg->m_severity && 
                `, Key: ` && 
                rep_early-root[ 1 ]-%key-key_field && 
                `, Message: ` && 
                rep_early-root[ 1 ]-%msg->if_message~get_text( ) ). 
    ENDIF. 
 
    IF f_late IS NOT INITIAL. 
      out->write( `Failed late: Key: ` && 
            f_late-root[ 1 ]-%key-key_field && 
            `, Fail cause: ` && 
            f_late-root[ 1 ]-%fail-cause ). 
    ENDIF. 
 
    IF rep_late IS NOT INITIAL. 
      out->write( `Reported late: ` && 
                rep_late-root[ 1 ]-%msg->m_severity && 
                `, Key: ` && 
                rep_late-root[ 1 ]-%key-key_field && 
                `, Message: ` && 
                rep_late-root[ 1 ]-%msg->if_message~get_text( ) ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD select_from_dbtab. 
    SELECT * FROM demo_tab_root_7 
      ORDER BY key_field 
      INTO TABLE @FINAL(db_entries). 
    out->write( db_entries ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_tab_root_7. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The example demonstrates different ABAP EML requests. Among them, there are modify requests including a create operation to create one instance in most cases. `COMMIT ENTITIES` statements trigger the save sequence. These statements include the retrieval of the [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) `failed` and `reported`. After most modify requests, the responses - if there are any - are displayed. A `SELECT` statement retrieves the entries on the database table to show the effect of the RAP operations.

The following is covered:

1.  Successful saving of a RAP BO instance

    Demonstrates a successful RAP create operation. The validation and the saving is carried out successfully. The value of `sy-subrc` is 0 after the `COMMIT ENTITIES` statement. There are no early and late responses.

2.  Failure in the RAP interaction phase

    Demonstrates a failure in the RAP interaction phase. The RAP create operation includes two RAP BO instances. One of these includes a key value that is already available in the database table. Hence, the creation of this instance fails. The early failed response includes an entry. A subsequent read operation shows that the erroneous instance is not present in the transactional buffer. The other instance is then saved to the database.

3.  Failure in the early save phase

    Demonstrates a failure in the early phase of the RAP save sequence (the validation fails). The value of `sy-subrc` is 4 after the `COMMIT ENTITIES` statement. A read operation demonstrates that the RAP BO instance that has failed is still available in the [RAP transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md). A RAP update operation is carried out on the failed instance to correct the issue.

4.  Failure in the late save phase

    Demonstrates a failure in the late phase of the RAP save sequence (in the `SAVE_MODIFIED` method). Due to the implementation mentioned above, the saving of the RAP BO instance is denied. The response parameters are filled in the `SAVE_MODIFIED` method. The value of `sy-subrc` is 8 after the `COMMIT ENTITIES` statement. A read operation demonstrates that the RAP BO instance that has failed is not available in the transactional buffer.

5.  RAP BO consumer proceeds after a failure in the late save phase

    After an issue occurred earlier in the late save phase, `sy-subrc` was set to 8. The RAP BO consumer cannot continue unless there is an explicit rollback. Therefore, the example includes a `ROLLBACK ENTITIES` statement that precedes another RAP create operation. If the statement is not specified, the runtime error `CX_SADL_DUMP_APPL_MODEL_ERROR` will be raised.

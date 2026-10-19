---
title: "RAP Messages: Transition and State Messages"
source_file: abenrap_messages_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP Messages: Transition and State Messages

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [RAP transition](../../abap-glossary/abenrap_trans_mes_glosry.md) and [state messages](../../abap-glossary/abenrap_state_mes_glosry.md) using a [managed](../rap-behavior-definitions/abenbdl_impl_type.md), [draft-enabled RAP business object](../../abap-glossary/abendraft_rap_bo_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_DRAFT_M`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Root entity: draft-enabled, managed BO'
define root view entity demo_draft_m
  as select from demo_tab_root_4

{
  key key_field,
      field1,
      field2,
      field3,
      field4,
      @Semantics.systemDateTime.lastChangedAt: true
      crea_date_time,
      @Semantics.systemDateTime.localInstanceLastChangedAt: true
      lchg_date_time
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_DRAFT_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_draft_m unique;
strict ( 2 );
with draft;

define behavior for demo_draft_m
persistent table demo_tab_root_4
draft table demo_tab_draft
lock master
total etag crea_date_time
etag master lchg_date_time
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
  field ( readonly ) crea_date_time, lchg_date_time;
  validation val on save { field field2; }
  draft action Resume;
  draft action Edit;
  draft action Activate optimized;
  draft action Discard;
  draft determine action Prepare
  {
    validation val;
  }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_DRAFT_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_DRAFT_M===============CCIMP` of the behavior pool. A validation implementation is included. For more information, see the comments in the code.

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
CLASS cl_demo_rap_messages_draft_m DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF responses_struc, 
             key        TYPE demo_draft_m-key_field, 
             early      TYPE abap_boolean, 
             late       TYPE abap_boolean, 
             failed     TYPE abap_boolean, 
             fail_cause TYPE string, 
             reported   TYPE abap_boolean, 
             msg        TYPE string, 
             state_area TYPE string, 
           END OF  responses_struc. 
    DATA: 
      f_early         TYPE RESPONSE FOR FAILED EARLY demo_draft_m, 
      r_early         TYPE RESPONSE FOR REPORTED EARLY demo_draft_m, 
      m_early         TYPE RESPONSE FOR MAPPED EARLY demo_draft_m, 
      f_late          TYPE RESPONSE FOR FAILED LATE demo_draft_m, 
      r_late          TYPE RESPONSE FOR REPORTED LATE demo_draft_m, 
      create_tab      TYPE TABLE FOR CREATE demo_draft_m, 
      update_tab      TYPE TABLE FOR UPDATE demo_draft_m, 
      activate_tab    TYPE TABLE FOR 
                        ACTION IMPORT demo_draft_m~activate, 
      read_tab        TYPE TABLE FOR READ IMPORT demo_draft_m, 
      read_result_tab TYPE TABLE FOR READ RESULT demo_draft_m, 
      responses_table TYPE TABLE OF responses_struc WITH EMPTY KEY. 
    METHODS: 
      select_db, 
      select_draft_db, 
      retrieve_early_responses, 
      retrieve_late_responses, 
      state_area_read_local_mode. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_messages_draft_m IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: RAP state and transition messages` 
    "The example demonstrates RAP state and transition messages. For 
    "this purpose, the validation implementation in the behavior pool 
    "includes the checking of the value of a specific field. A state 
    "message is returned if the validations fails. A transition message 
    "is returned if the validation is successful. Note that, typically, 
    "a validation rather returns a state message than a transition 
    "message. In this example, the inclusion of both types is 
    "intentional to demonstrate the differences between the two message 
    "types. 
    "The validation is assigned to a draft determine action prepare, 
    "i.e. draft data is validated before the transition to active data. 
 
    )->next_section( `1) Successful RAP create operation` 
    )->write( `1a) EML MODIFY CREATE to create instances stored in ` && 
    `the draft table` ). 
 
    "Notes on the code/output: 
    "- A RAP create operation is carried out. One instance is created. 
    "  For the instance, the draft indicator is flagged. 
    "- With the COMMIT ENTITIES statement, the instance is persisted 
    "  to the draft table. 
    "- Various method calls are triggered to retrieve early and late 
    "  responses. The entries of both draft and database table are 
    "  retrieved and displayed. 
    "- At this stage, the entries are available in the draft table 
    "  only. No instances have been persisted to the database table 
    "  yet. Since no errors have occurred, the FAILED and REPORTED 
    "  responses are do not include any entries. 
    "- Note: In this example, the FAILED and REPORTED entries are 
    "  filtered and stored in a separate internal table for display 
    "  purposes. 
    "- Note: In the entire example, the late responses are of no 
    "  relevance. There are never entries available. They are 
    "  just included for the sake of completeness. 
 
    create_tab = VALUE #( ( %is_draft = if_abap_behv=>mk-on 
                            %cid      = `cid` 
                            key_field = 1 
                            field1    = `aaa` 
                            field2    = 'bbb' 
                            field3    = 2 
                            field4    = '3.0' ) ). 
 
    MODIFY ENTITY demo_draft_m 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH create_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
 
    out->write( `1b) activate draft action to persist instances ` && 
    `to the database` ). 
 
    "Notes on the code/output: 
    "- An EML MODIFY request triggers the activate draft action that 
    "  copies the content of the draft database table to the persistent 
    "  database table. 
    "- When executing the activate action, the validation method is 
    "  called. Since the validation is successful and it is implemented 
    "  this way, a transition message is returned for the instance 
    "  informing that the instance is valid. 
    "- The draft table is empty, i.e. the draft instance has been 
    "  activated and thus persisted to the database table, which 
    "  shows the instance. 
 
    activate_tab = CORRESPONDING #( create_tab EXCEPT %cid ). 
 
    "Note: The validation is called when executing the activate action. 
    MODIFY ENTITY demo_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->next_section( `2) Unsuccessful RAP create operation` 
    )->write( `2a) EML MODIFY CREATE to create instances stored in ` && 
    `the draft table` ). 
 
    "Notes on the code/output: 
    "- A RAP create operation is carried out. One instance is to be 
    "  created. In this case, the very same instance is used as above. 
    "  Consequently, the request fails since an instance with the key 
    "  already exists on the  database. 
    "- A standard transition message is returned in REPORTED. An entry 
    "  exists for FAILED. 
    "- There are no entries in the draft table at this stage. The 
    "  database table still only contains the successfully created 
    "  instance from above. 
    "- Consequently, the activate action has no effect since the 
    "  instance does not exist in the draft table. 
 
    MODIFY ENTITY demo_draft_m 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH create_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
 
    out->write( `2b) activate draft action to persist instances ` && 
    `to the database` ). 
 
    activate_tab = CORRESPONDING #( create_tab EXCEPT %cid ). 
 
    "Note: The validation is called when executing the activate action. 
    MODIFY ENTITY demo_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->next_section( `3) RAP create operation with a valid and ` && 
    `invalid instance` 
    )->write( `3a) EML MODIFY CREATE to create instances stored ` && 
    `in the draft table` ). 
 
    "Notes on the code/output: 
    "- A RAP create operation is carried out. Two instances are to be 
    "  created. 
    "  In this case, an instance is included for which the validation 
    "  is successful. 
    "  The validation fails for the other instance. 
    "- The draft table entries shows both instances. The output of the 
    "  database table retrieval shows the persisted entry from the 
    "  operation above. 
    "- The EML MODIFY CREATE request does not return any messages. The 
    "  validation is not triggered at this stage. 
    "- Executing the activate action triggers the calling of the 
    "  validation. For the valid instance, the information transition 
    "  message is returned. FAILED and REPORTED contain entries. The 
    "  error transition message is a standard message coming from the 
    "  framework. 
    "- The entry in FAILED with fail cause UNSPECIFIC comes from the 
    "  implementation in the validation. Note that the state message 
    "  that is added to REPORTED in the validation implementation is 
    "  not available here for the RAP BO consumer. See the next step 
    "  with the EML READ request. 
    "- Note: The validation implementation includes the retrieval of 
    "  REPORTED responses 
    "  after the EML read request. This way, state messages, i.e. the 
    "  original values of %state_area, that are available for specified 
    "  keys can be retrieved. It is implemented in the behavior pool in 
    "  a way that these REPORTED responses are stored in an internal 
    "  which is output here to demonstrate the %state_area value. At 
    "  this stage, there are no state messages in REPORTED. 
 
    DATA(key1) = 2. 
    DATA(key2) = 3. 
 
    create_tab = VALUE #( "valid instance 
                          ( %is_draft = if_abap_behv=>mk-on 
                            %cid = `cid1` 
                            key_field = key1 
                            field1    = `ccc` 
                            field2    = 'ddd' 
                            field3    = 3 
                            field4    = '4.0' ) 
 
                           "invalid instance 
                           ( %is_draft = if_abap_behv=>mk-on 
                            %cid = `cid2` 
                            key_field = key2 
                            field1    = `eee` 
                            field2    = 'X' 
                            field3    = 4 
                            field4    = '5.0' ) ). 
 
    MODIFY ENTITY demo_draft_m 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH create_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
 
    out->write( `3b) activate draft action to persist ` && 
    `instances to the database` ). 
 
    activate_tab = CORRESPONDING #( create_tab EXCEPT %cid ). 
 
    "Note: The validation is called when executing the activate action. 
    MODIFY ENTITY demo_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_early_responses( ). 
    state_area_read_local_mode( ). 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->next_section( `4) RAP read operation` ). 
 
    "Notes on the code/output: 
    "- At this stage, the valid instance from above has been persisted 
    "  to the database. The invalid instance is still available in the 
    "  draft table. It has not yet been persisted. 
    "- A RAP read operation is carried out. The derived type 
    "  on whose basis the read request is made contains multiple 
    "  entries. Two entries for the valid instance and 
    "  two for the invalid instance from above. For both instances, 
    "  an entry exists where the draft indicator is switched on and 
    "  off. 
    "  They are intentionally included for demonstration purposes: 
    "  - Valid instance: 
    "    - draft indicator switched off: Instance is found; has been 
    "      persisted 
    "      to the database 
    "    - draft indicator switched on: Instance is not found; already 
    "      persisted 
    "      and, therefore, not available in the draft table any more 
    "  - Invalid instance: 
    "    - draft indicator switched off: Instance is not found; not yet 
    "      persisted 
    "    - draft indicator switched on: Instance is found; still 
    "      available in the draft table 
    "- The EML READ request is specified to return the REPORTED 
    "  responses. State messages can be retrieved using such an EML 
    "  READ request. Therefore, the state message is contained in 
    "  REPORTED. Note that the %state_area value is not relevant for 
    "  the RAP BO consumer. Therefore, the predefined value %state is 
    "  contained. 
    "- Furthermore, it is also demonstrated that transition messages 
    "  are not available any more. Unlike transition messages, state 
    "  messages are persisted and still available. 
 
    read_tab = VALUE #( "draft indicator switched off 
      ( key_field = key1 %is_draft = if_abap_behv=>mk-off ) "found 
      ( key_field = key2 %is_draft = if_abap_behv=>mk-off  ) "not found 
      "draft indicator switched on 
      ( key_field = key1 %is_draft = if_abap_behv=>mk-on ) "not found 
      ( key_field = key2 %is_draft = if_abap_behv=>mk-on  ) ). "found 
 
    READ ENTITY demo_draft_m 
      ALL FIELDS WITH read_tab 
      RESULT read_result_tab 
      FAILED f_early 
      REPORTED r_early. 
 
    retrieve_early_responses( ). 
    out->write( `Result of read operation` ). 
    out->write( read_result_tab ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `5) RAP update operation` ). 
 
    "Notes on the code/output: 
    "- At this stage, the invalid instance is still available in the 
    "  draft table. 
    "- The RAP update operation corrects the issue that lets the 
    "  validation failed. 
    "- The execution of the activate action triggers the validation. 
    "  This time, the validation is successful. The transition message 
    "  informing that the instance is ok is returned. The REPORTED 
    "  response in the read request in the validation implementation 
    "  includes the state message as well as the original value of 
    "  %state_area. This is demonstrated by displaying the internal 
    "  table in which the value was stored. 
    "- The corrected instance has been successfully persisted to the 
    "  database. The entry is not available in the draft table any 
    "  more. 
 
    "Correcting and updating the invalid instance 
    update_tab = VALUE #( ( %is_draft = if_abap_behv=>mk-on 
                            key_field = key2 
                            field1    = `eee` 
                            field2    = 'fff' 
                            field3    = 4 
                            field4    = '5.0' ) ). 
 
    MODIFY ENTITY demo_draft_m 
      UPDATE FIELDS ( field1 field2 field3 field4 ) 
      WITH update_tab 
      FAILED f_early 
      REPORTED r_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_early_responses( ). 
    state_area_read_local_mode( ). 
    retrieve_late_responses( ). 
 
    activate_tab = CORRESPONDING #( update_tab EXCEPT %cid ). 
 
    MODIFY ENTITY demo_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED m_early 
      FAILED f_early 
      REPORTED r_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_draft_m 
      FAILED f_late 
      REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred.` ). 
    ENDIF. 
 
    retrieve_early_responses( ). 
    state_area_read_local_mode( ). 
    retrieve_late_responses( ). 
    select_draft_db( ). 
    select_db( ). 
 
  ENDMETHOD. 
  METHOD retrieve_early_responses. 
 
    IF f_early IS NOT INITIAL. 
      LOOP AT f_early-demo_draft_m ASSIGNING FIELD-SYMBOL(<a>). 
 
        APPEND VALUE #( key        = <a>-key_field early = abap_true 
                        failed     = abap_true 
                        fail_cause = <a>-%fail-cause ) 
         TO responses_table. 
      ENDLOOP. 
    ENDIF. 
 
    IF r_early IS NOT INITIAL. 
      LOOP AT r_early-demo_draft_m ASSIGNING FIELD-SYMBOL(<b>). 
        APPEND VALUE #( key        = <b>-key_field 
                        early      = abap_true 
                        reported   = abap_true 
                        msg        = |{ <b>-%msg->m_severity }: | && 
                         |{ <b>-%msg->if_message~get_text( ) }| 
                        state_area = <b>-%state_area ) 
                      TO responses_table. 
      ENDLOOP. 
    ENDIF. 
 
    IF f_early IS INITIAL AND r_early IS INITIAL. 
      out->write( `No early responses` ). 
    ELSE. 
      out->write( responses_table ). 
    ENDIF. 
 
    CLEAR responses_table. 
  ENDMETHOD. 
  METHOD retrieve_late_responses. 
    IF f_late IS NOT INITIAL. 
      LOOP AT f_late-demo_draft_m ASSIGNING FIELD-SYMBOL(<a>). 
        APPEND VALUE #( key        = <a>-key_field 
                        late       = abap_true 
                        failed     = abap_true 
                        fail_cause = <a>-%fail-cause ) 
                      TO responses_table. 
      ENDLOOP. 
    ENDIF. 
 
    IF r_late IS NOT INITIAL. 
      LOOP AT r_late-demo_draft_m ASSIGNING FIELD-SYMBOL(<b>). 
        APPEND VALUE #( key        = <b>-key_field 
                        late       = abap_true 
                        reported   = abap_true 
                        msg        = |{ <b>-%msg->m_severity }: | && 
                          |{ <b>-%msg->if_message~get_text( ) }| 
                        state_area = <b>-%state_area ) 
                      TO responses_table. 
      ENDLOOP. 
    ENDIF. 
 
    IF f_late IS INITIAL AND r_late IS INITIAL. 
      out->write( `No late responses` ). 
    ELSE. 
      out->write( responses_table ). 
    ENDIF. 
 
    CLEAR responses_table. 
  ENDMETHOD. 
  METHOD select_db. 
    SELECT * 
      FROM demo_tab_root_4 
      INTO TABLE @DATA(db_entries). 
 
    out->write( db_entries ). 
  ENDMETHOD. 
  METHOD select_draft_db. 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
    FROM demo_tab_draft INTO TABLE @DATA(draft_entries). 
 
    out->write( draft_entries ). 
  ENDMETHOD. 
  METHOD state_area_read_local_mode. 
    IF bp_demo_draft_m=>state_area_table IS INITIAL. 
      out->write( `No entries in internal table for checking ` && 
      `the state area values after EML read in local mode.` ). 
    ELSE. 
      out->write( `Entries in internal table for checking the ` && 
      `state area values after EML read in local mode:` ). 
      out->write( bp_demo_draft_m=>state_area_table ). 
    ENDIF. 
    CLEAR bp_demo_draft_m=>state_area_table. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_tab_root_4.                        "#EC CI_NOWHERE 
    DELETE FROM demo_tab_draft.                         "#EC CI_NOWHERE 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The example demonstrates RAP state and transition messages. For this purpose, the validation implementation in the behavior pool includes the checking of the value of a specific field. A state message is returned if the validations fails. A transition message is returned if the validation is successful. Note that, typically, a validation rather returns a state message than a transition message. In this example, the inclusion of both types is intentional to demonstrate the differences between the two message types. The validation is assigned to the `draft determine action prepare`, i.e. draft data is validated before the transition to active data.

For more information, see the comments in the code.

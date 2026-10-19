---
title: "ABAP EML in Use: Managed RAP BO with External Numbering"
source_file: abensheet_rap_ext_num_m_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML in Use: Managed RAP BO with External Numbering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various [RAP BO standard operations](../../abap-glossary/abenrap_standard_operation_glosry.md) and [non-standard operations](../../abap-glossary/abenrap_nstandard_operation_glosry.md) using ABAP EML in the context of a [managed RAP business object](../../abap-glossary/abenmanaged_rap_bo_glosry.md) with [RAP external numbering](../../abap-glossary/abenrap_ext_numbering_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_CS_RAP_RO_M` and its child entity `DEMO_CS_RAP_CH_M`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_cs_rap_ro_m 
as select from demo_cs_rap_tab1 
composition [0..*] of demo_cs_rap_ch_m as _child
{
  key key_field,
  field1,
  field2,
  field3,
  field4,
  _child
}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_cs_rap_ch_m 
as select from demo_cs_rap_tab2 
association to parent demo_cs_rap_ro_m 
  as _parent on $projection.key_field = _parent.key_field
{
  _parent,
  key key_field,
  key key_ch,
  field_ch1,
  field_ch2
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CS_RAP_RO_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_cs_rap_ro_m unique;
strict ( 2 );

define behavior for demo_cs_rap_ro_m alias root
persistent table DEMO_CS_RAP_TAB1
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  association _child { create; }
  action multiply_by_2;
  validation val on save { field field3; }
  determination det_add_text on save { create; }
  field(readonly:update) key_field;
}

define behavior for demo_cs_rap_ch_m alias child
persistent table DEMO_CS_RAP_TAB2
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  field(readonly:update) key_ch;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_CS_RAP_RO_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_CS_RAP_RO_M===========CCIMP` of the behavior pool. See comments in the code for more information on the implementation.

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
CLASS cl_demo_cs_rap_ext_num_m DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED   demo_cs_rap_ro_m, 
      reported TYPE RESPONSE FOR REPORTED demo_cs_rap_ro_m, 
      mapped   TYPE RESPONSE FOR MAPPED demo_cs_rap_ro_m. 
    METHODS: 
      initialize_dbtabs, 
      "If there are entries in the response parameters following EML 
      "requests, they should be processed for displaying purposes. 
      extract_from_reported RETURNING VALUE(messages) TYPE string_table, 
      extract_from_failed RETURNING VALUE(errors) TYPE string_table, 
      fill_db_tab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cs_rap_ext_num_m IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `RAP Demo: RAP BO Operations Using a ` && 
                      `Managed RAP BO` ). 
 
********************************************************************** 
* 
* Create operation 
* 
********************************************************************** 
 
    out->line( 
    )->next_section( `Create operation` ). 
 
    "Adding an entry to the database table to provoke an error for the 
    "EML create request. 
    fill_db_tab( ). 
 
********************************************************************** 
* Notes: 
* - field4 is purposely not included in the FIELDS list 
* - Effect: 
*   - %control value for field4 is set to if_abap_behv=>mk-off 
*   - Although the derived type (created inline here) includes a 
*     value assignment for field4 in an instance, the field value is 
*     not saved. The initial value is used. 
* - The instance with key_field = 4 will not be saved since an entry 
*   already exists in the database table with the same key. 
* - Response parameters are specified to receive information. 
* - A COMMIT ENTITIES statement triggers the saving of the instances. 
* - The example BDEF includes the definition of a determination on 
*   save for create operations. In this case, the determination 
*   adds some text to the value in field2. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
      ENTITY root 
      CREATE FIELDS ( key_field field1 field2 field3 ) 
        WITH VALUE #( ( %cid = 'cid1' 
                        key_field = 1 
                        field1    = 'aaa' 
                        field2    = 'bbb' 
                        field3    = 10 
                        field4    = 11 ) "Value not considered 
                      ( %cid      = 'cid2' 
                        key_field = 2 
                        field1    = 'ccc' 
                        field2    = 'ddd' 
                        field3    = 20 ) 
                      ( %cid      = 'cid3' 
                        key_field = 3 
                        field1    = 'eee' 
                        field2    = 'fff' 
                        field3    = 30 ) 
                      ( %cid      = 'cid4' "Instance to fail 
                        key_field = 4 
                        field1    = 'error' 
                        field2    = 'error' 
                        field3    = 99 ) ) 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @DATA(tab_root). 
 
    out->write( tab_root ). 
 
    "Displaying response information 
    IF mapped IS NOT INITIAL. 
      out->write( mapped-root ). 
    ENDIF. 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Update operations 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Update operation` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create and an update request. The 
*   create request is included to have a %cid to refer to for demo 
*   purposes. This instance has not yet been persisted. 
* - The EML statement for the create operation includes the ABAP 
*   FROM ... (instead of FIELDS ( ... ) WITH ...) for demo purposes. 
*   Here, the %control values must be set explicitly. 
* - The update request purposely excludes field2 so as not to update 
*   the value of this particular field. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        CREATE FROM VALUE #( 
            %control-key_field = if_abap_behv=>mk-on 
            %control-field1 = if_abap_behv=>mk-on 
            %control-field2 = if_abap_behv=>mk-on 
            %control-field3 = if_abap_behv=>mk-on 
            %control-field4 = if_abap_behv=>mk-on 
          ( %cid = 'cid5' 
            key_field = 5 
            field1    = 'iii' 
            field2    = 'jjj' 
            field3    = 50 
            field4    = 51 ) ) 
        UPDATE FIELDS ( field1 field3 field4 ) 
          WITH VALUE #( 
          "Update via cid_ref 
          ( %cid_ref = 'cid5' 
            field1   = 'up_kkk' 
            field2   = 'up_lll' "Value not considered 
            field3   = 500 
            field4   = 501 ) 
          "Updates via key 
          ( key_field = 1 
            field1    = 'up_mmm' 
            field3    = 100 
            field4    = 101 ) 
          ( key_field = 2 
            field1    = 'up_ooo' 
            field3    = 200 
            field4    = 201 ) 
          ( key_field = 99   "Instance to fail 
            field1    = 'error' 
            field3    = 99 
            field4    = 99 ) ) 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @tab_root. 
 
    out->write( tab_root ). 
 
    "Displaying response information 
    IF mapped IS NOT INITIAL. 
      out->write( mapped-root ). 
    ENDIF. 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Delete operation 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Delete operation` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create and an delete request. The 
*   create request is included to have a %cid to refer to for demo 
*   purposes. This instance has not yet been persisted. 
* - EML statements for delete operations can only be used with the 
*   ABAP word FROM .... 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid      = 'cid_del' 
            key_field = 6 
            field1    = 'mmm' 
            field2    = 'nnn' 
            field3    = 60 
            field4    = 61 ) ) 
        DELETE FROM VALUE #( 
          "Deletion via %cid_ref 
          ( %cid_ref = 'cid_del' ) 
          "Deletions via key 
          ( key_field = 4 ) 
          ( key_field = 5 ) 
          "Instance to fail 
          ( key_field = 100 ) )  "Key not available 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @tab_root. 
 
    out->write( tab_root ). 
 
    "Displaying response information 
    out->write( mapped ). 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Action multiply_by_2 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Action execution: mutliply_by_2` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create request and a request to execute 
*   an action. The create request is included to have a %cid to refer 
*   to for demo purposes. This instance has not yet been persisted. 
* - EML statements for executing actions can only be used with the 
*   ABAP word FROM .... 
* - As the name implies, the action multiplies field 
*   values (field3 and field4) by 2 for requested instances. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid = 'cid_x2' 
            key_field = 7 
            field1    = 'ooo' 
            field2    = 'ppp' 
            field3    = 70 
            field4    = 71 ) ) 
        EXECUTE multiply_by_2 FROM VALUE #( 
          "Executing action via %cid_ref 
          ( %cid_ref = 'cid_x2' ) 
          "Executing action via key 
          ( key_field  =  1  ) 
          ( key_field  =  2  ) 
          ( key_field  =  1234 ) ) "Instance to fail 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @tab_root. 
 
    out->write( tab_root ). 
 
    "Displaying response information 
    out->write( mapped ). 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Create-by-association operation (from root to child entitiy) 
* 
********************************************************************** 
    out->line( ). 
    out->next_section( `Create-by-association operation ` && 
                  `(from parent to child)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create and create-by-association 
*   request, i. e. a "deep create". An instance is created for the 
*   parent entity and, in the same request and based on this 
*   instance, instances are created for the child entity, too. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
              WITH VALUE #( 
              ( %cid      = 'cid_cba' 
                key_field = 9 
                field1    = 'qqq' 
                field2    = 'rrr' 
                field3    = 90 
                field4    = 91 ) ) 
        CREATE BY \_child 
        FIELDS ( key_ch field_ch1 field_ch2 ) WITH VALUE #( 
          "CBA operation via %cid_ref 
          ( %cid_ref = 'cid_cba' 
            %target = VALUE #( ( %cid      = 'cid_ch1' 
                                 key_ch    = 9 
                                 field_ch1 = 'aaa_ch' 
                                 field_ch2 = 99 ) 
                               ( %cid      = 'cid_ch2' 
                                 key_ch    = 10 
                                 field_ch1 = 'bbb_ch' 
                                 field_ch2 =  100 ) ) ) 
          "CBA operation via root key 
          ( key_field = 1 
            %target = VALUE #( ( %cid      = 'cid_ch3' 
                                 key_ch    = 1 
                                 field_ch1 = 'ccc_ch' 
                                 field_ch2 = 11 ) 
                               ( %cid      = 'cid_ch4' 
                                 key_ch    = 2 
                                 field_ch1 = 'ddd_ch' 
                                 field_ch2 = 22 ) ) ) 
          ( key_field = 2 
            %target = VALUE #( ( %cid      = 'cid_ch5' 
                                 key_ch    = 3 
                                 field_ch1 = 'ccc_ch' 
                                 field_ch2 = 33 ) 
                               ( %cid      = 'cid_ch6' 
                                 key_ch    = 4 
                                 field_ch1 = 'ddd_ch' 
                                 field_ch2 = 44 ) ) ) 
          "Instance to fail 
          ( key_field = 123 
            %target = VALUE #( ( %cid      = 'cid_ch7' 
                                 key_ch    = 1 
                                 field_ch1 = 'error' 
                                 field_ch2 = 2 ) 
                               ( %cid      = 'cid_ch8' 
                                 key_ch    = 2 
                                 field_ch1 = 'error' 
                                 field_ch2 = 3 ) ) ) 
                                 ) 
          MAPPED mapped 
          FAILED failed 
          REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @tab_root. 
 
    SELECT FROM demo_cs_rap_tab2 
      FIELDS key_field, key_ch, field_ch1, field_ch2 
      ORDER BY key_field, key_ch 
      INTO TABLE @FINAL(tab_child). 
 
    out->write( tab_root ). 
    out->write( tab_child ). 
 
    "Displaying response information 
    out->write( mapped ). 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Validation val 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Validation val` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create request. The validation's 
*   handler method is implementation in a way that the saving of 
*   instances is disabled if a field value is not allowed. In this 
*   example, the value of the integer in field3 shall not exceed 1000. 
*   Here, the third instance will fail for the validation. 
*   Consequently, all instances of this request are not saved to the 
*   database. Either all is ok and will be saved or nothing. 
* - Note that the response information for the validation is only 
*   available in the response parameters of the COMMIT ENTITIES 
*   statement. Here, the BDEF derived type is 
*   ... TYPE RESPONSE FOR ... LATE .... 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid = 'cid_val1' 
            key_field = 123 
            field1    = 'sss' 
            field2    = 'ttt' 
            field3    = 1 
            field4    = 2 ) 
          ( %cid = 'cid_val2' 
            key_field = 456 
            field1    = 'uuu' 
            field2    = 'vvv' 
            field3    = 3 
            field4    = 4 ) 
          ( %cid = 'cid_val3' 
            key_field = 789 
            field1    = 'www' 
            field2    = 'xxx' 
            field3    = 1001 
            field4    = 5 ) ) 
        MAPPED mapped 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES RESPONSES FAILED FINAL(failed_late) 
      REPORTED FINAL(reported_late). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving and displaying database content 
    SELECT FROM demo_cs_rap_tab1 
      FIELDS key_field, field1, field2, field3, field4 
      ORDER BY key_field 
      INTO TABLE @tab_root. 
 
    out->write( tab_root ). 
 
    "Displaying response information 
    out->write( mapped ). 
    IF failed_late IS NOT INITIAL. 
      out->write( data = failed_late 
                name = `Entries in FAILED LATE response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = reported_late 
                name = `Entries in REPORTED LATEresponse parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Read operation (root entity) 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Read operation (root entity)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read request. The EML statement uses 
*   the ABAP words ALL FIELDS WITH. In this case, as the name implies, 
*   all field values are retrieved. The %control values for all fields 
*   are set to if_abap_behv=>mk-on. 
* - When using the ABAP words FIELDS ( ... ) WITH and specifying the 
*   concrete fields to be read, only for those fields %control is 
*   set accordingly. 
* - Filling the parameter for RESULT is mandatory. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_m 
        ENTITY root 
        ALL FIELDS WITH VALUE #( 
          ( key_field = 1 ) 
          ( key_field = 2 ) 
          ( key_field = 7 ) 
          ( key_field = 5 ) ) "Instance to fail 
        RESULT FINAL(result) 
        FAILED failed 
        REPORTED reported. 
 
    "Displaying the read result 
    out->write( result ). 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************* 
* 
* Read operation (child entity) 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Read operation (child entity)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read request. The read operation is 
*   executed on the child entity directly by specifying the alias, as 
*   it is defined in the BDEF, following the ABAP word ENTITY. 
* - All field values are read using the addition ALL FIELDS WITH. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_m 
          ENTITY child 
          ALL FIELDS WITH VALUE #( 
            ( key_field = 1 key_ch = 1 ) 
            ( key_field = 2 key_ch = 4 ) 
            "Instances to fail 
            ( key_field = 9 ) 
            ( key_field = 9 key_ch = 11 ) ) 
          RESULT FINAL(read_ch) 
          FAILED failed 
          REPORTED reported. 
 
    "Displaying read result 
    out->write( read_ch ). 
 
    "Displaying response information 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Read-by-association operation (from parent to child) 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Read-by-association operation ` && 
                     `(from parent to child)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read-by-association request from the 
*   parent to the child. 
* - All field values are read using the addition ALL FIELDS WITH. 
* - Specifying the parameter for RESULT is mandatory. 
* - Additionally, the optional association links are retrieved. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_m 
          ENTITY root 
          BY \_child 
          ALL FIELDS WITH VALUE #( 
            ( key_field = 2 ) 
            ( key_field = 9 ) 
            ( key_field = 999 ) ) "Instance to fail 
          RESULT FINAL(rba_result) 
          LINK FINAL(association_links) 
          FAILED failed 
          REPORTED reported. 
 
    "Displaying read result and association links 
    out->write( rba_result ). 
    out->write( association_links ). 
 
    "Displaying response information 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Read-by-association operation (from child to parent) 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Read-by-association operation ` && 
                     `(from child to parent)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read-by-association request from the 
*   child to the parent. 
* - All field values are read using the addition ALL FIELDS WITH. 
* - Specifying the parameter for RESULT is mandatory. 
* - Additionally, the optional association links are retrieved. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_m 
      ENTITY child 
      BY \_parent ALL FIELDS WITH VALUE #( 
         ( key_field = 1 key_ch = 1 ) 
         ( key_field = 2 key_ch = 4 ) 
         "Instances to fail 
         ( key_field = 1 key_ch = 3 ) 
         ( key_field = 543 key_ch = 1 ) ) 
       RESULT FINAL(rba_parent) 
       LINK FINAL(association_links_parent) 
       FAILED failed 
       REPORTED reported. 
 
    "Displaying read result and association links 
    out->write( rba_parent ). 
    out->write( association_links_parent ). 
 
    "Displaying response information 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
 
********************************************************************** 
* 
* Excursion: Read and read-by-association operation using dynamic 
* EML statements 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Excursion: Read and read-by-association ` && 
                     `operations using dynamic EML` ). 
 
    DATA: 
      op_tab          TYPE abp_behv_retrievals_tab, 
      read_dyn        TYPE TABLE FOR READ IMPORT demo_cs_rap_ro_m, 
      read_dyn_result TYPE TABLE FOR READ RESULT demo_cs_rap_ro_m, 
      rba_dyn         TYPE TABLE FOR READ IMPORT 
                        demo_cs_rap_ro_m\_child, 
      rba_dyn_result  TYPE TABLE FOR READ RESULT 
                        demo_cs_rap_ro_m\_child, 
      rba_dyn_link    TYPE TABLE FOR READ LINK demo_cs_rap_ro_m\_child. 
 
    read_dyn = VALUE #( 
      ( %key-key_field = 1 
        %control = VALUE #( 
          field1 = if_abap_behv=>mk-on 
          field2 = if_abap_behv=>mk-on 
          field3 = if_abap_behv=>mk-on 
          field4 = if_abap_behv=>mk-on ) ) 
      ( %key-key_field = 2 
        %control = VALUE #( 
          field1 = if_abap_behv=>mk-on 
          field2 = if_abap_behv=>mk-on 
          field3 = if_abap_behv=>mk-on 
          field4 = if_abap_behv=>mk-on ) ) ). 
 
    rba_dyn = VALUE #( 
     ( %key-key_field = 1 
       %control = VALUE #( 
          key_field = if_abap_behv=>mk-on 
          key_ch    = if_abap_behv=>mk-on 
          field_ch1 = if_abap_behv=>mk-on 
          field_ch2 = if_abap_behv=>mk-on ) ) 
      ( %key-key_field = 2 
        %control = VALUE #( 
          key_field = if_abap_behv=>mk-on 
          key_ch    = if_abap_behv=>mk-on 
          field_ch1 = if_abap_behv=>mk-on 
          field_ch2 = if_abap_behv=>mk-on ) ) ). 
 
    op_tab = VALUE #( 
       ( op = if_abap_behv=>op-r-read 
         entity_name = 'DEMO_CS_RAP_RO_M' 
         instances   = REF #( read_dyn ) 
         results     = REF #( read_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read_ba 
         entity_name = 'DEMO_CS_RAP_RO_M' 
         sub_name    = '_CHILD' 
         full        = abap_true 
         instances   = REF #( rba_dyn ) 
         results     = REF #( rba_dyn_result ) 
         links       = REF #( rba_dyn_link ) ) ). 
 
    READ ENTITIES OPERATIONS op_tab. 
 
    out->write_doc( `Read result (root)` ). 
    out->write( read_dyn_result ). 
    out->write_doc( `Read result (read-by-association)` ). 
    out->write( rba_dyn_result ). 
    out->write_doc( `Links` ). 
    out->write( rba_dyn_link ). 
  ENDMETHOD. 
  METHOD extract_from_failed. 
    CLEAR errors. 
 
    LOOP AT failed-root ASSIGNING FIELD-SYMBOL(<err>). 
 
      DATA op TYPE string. 
 
      CASE if_abap_behv=>mk-on. 
        WHEN <err>-%op-%create. 
          op = `create operation`. 
        WHEN <err>-%op-%update. 
          op = `update operation`. 
        WHEN <err>-%op-%delete. 
          op = `delete operation`. 
        WHEN <err>-%op-%assoc-_child. 
          op = `operation involving the child entity`. 
        WHEN <err>-%op-%action-multiply_by_2. 
          op = `executing action multiply_by_2`. 
        WHEN OTHERS. op = `operation`. 
      ENDCASE. 
 
      APPEND `Error for instance with ` && 
           COND #( WHEN <err>-%cid IS NOT INITIAL THEN `%cid = ` 
                   && <err>-%cid 
                   ELSE `key = ` && <err>-key_field ) && 
           `: Fail cause ` &&  <err>-%fail-cause && ` for ` &&  op 
            && `.` TO errors. 
 
    ENDLOOP. 
 
    IF failed-child IS NOT INITIAL. 
      LOOP AT failed-child ASSIGNING FIELD-SYMBOL(<err_ch>). 
        APPEND `Error for child instance with key_field = ` && 
        <err_ch>-key_field && ` and key_ch = ` && 
        <err_ch>-key_ch && `: Fail cause ` 
        && <err_ch>-%fail-cause && `.` TO errors. 
      ENDLOOP. 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD extract_from_reported. 
    CLEAR messages. 
 
    LOOP AT reported-root ASSIGNING FIELD-SYMBOL(<rep>). 
      IF <rep>-%global = if_abap_behv=>mk-on. 
        APPEND <rep>-%msg->m_severity && 
                <rep>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
      ELSE. 
        APPEND `Message for instance with ` && 
               COND #( WHEN <rep>-%cid IS NOT INITIAL 
                       THEN `%cid = ` && <rep>-%cid 
                       ELSE `key = ` && <rep>-key_field ) && 
               `: ` &&  <rep>-%msg->m_severity && ` ` && 
               <rep>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
 
      ENDIF. 
    ENDLOOP. 
 
    IF reported-child IS NOT INITIAL. 
      LOOP AT reported-child ASSIGNING FIELD-SYMBOL(<rep_ch>). 
        APPEND `Message for child instance with key_field = ` && 
        <rep_ch>-key_field && ` and key_ch = ` 
        && <rep_ch>-key_ch && `: ` && <rep_ch>-%msg->m_severity && 
        ` ` && <rep_ch>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
      ENDLOOP. 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD fill_db_tab. 
 
    MODIFY demo_cs_rap_tab1 FROM TABLE @( VALUE #( 
          ( key_field = 4 
             field1   = 'ggg' 
             field2   = 'hhh' 
             field3   = 40 
             field4   = 41 ) ) ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_cs_rap_tab1.                       "#EC CI_NOWHERE 
    DELETE FROM demo_cs_rap_tab2.                       "#EC CI_NOWHERE 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The class demonstrates various RAP BO operations and aspects:

- Create (including a determination on save)

- Update

- Delete

- Executing an action

- Validation

- Create-by-association (parent to child)

- Read

- Read-by-association (parent to child)

- Read (child entity)

- Read-by-association (child to parent)

- Excursion: Dynamic EML statement

See comments in the code for more information.

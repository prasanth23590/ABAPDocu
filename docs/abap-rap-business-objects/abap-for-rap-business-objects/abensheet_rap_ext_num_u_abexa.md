---
title: "ABAP EML in Use: Unmanaged RAP BO with External Numbering"
source_file: abensheet_rap_ext_num_u_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML in Use: Unmanaged RAP BO with External Numbering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various [RAP BO standard operations](../../abap-glossary/abenrap_standard_operation_glosry.md) and [non-standard operations](../../abap-glossary/abenrap_nstandard_operation_glosry.md) using ABAP EML in the context of an [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) with [RAP external numbering](../../abap-glossary/abenrap_ext_numbering_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_CS_RAP_RO_U` and its child entity `DEMO_CS_RAP_CH_U`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_CS_RAP_RO_U 
as select from demo_cs_rap_tab1 
composition [0..*] of DEMO_CS_RAP_CH_U as _child
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
define view entity DEMO_CS_RAP_CH_U 
as select from demo_cs_rap_tab2 
association to parent DEMO_CS_RAP_RO_U 
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CS_RAP_RO_U` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class bp_demo_cs_rap_ro_u unique;
strict ( 2 );

define behavior for DEMO_CS_RAP_RO_U alias root
lock master
authorization master ( instance )

{
  create ( authorization : none );
  update;
  delete;
  association _child { create; }
  action multiply_by_2;
  action ( features : instance ) multiply_by_3;
  action ( features : global ) set_z;
  field ( readonly : update ) key_field;
}

define behavior for DEMO_CS_RAP_CH_U alias child
lock dependent by _parent
authorization dependent by _parent
{
  field ( readonly ) key_field;
  field ( readonly : update ) key_ch;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_CS_RAP_RO_U`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_CS_RAP_RO_U===========CCIMP` of the behavior pool. See comments in the code for more information on the implementation.

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
CLASS cl_demo_cs_rap_ext_num_u DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED demo_cs_rap_ro_u, 
      reported TYPE RESPONSE FOR REPORTED demo_cs_rap_ro_u, 
      mapped   TYPE RESPONSE FOR MAPPED demo_cs_rap_ro_u. 
    METHODS: 
      initialize_dbtabs, 
      "If there are entries in the response parameters following EML 
      "requests, they should be processed for displaying purposes. 
      extract_from_reported RETURNING VALUE(messages) TYPE string_table, 
      extract_from_failed RETURNING VALUE(errors) TYPE string_table, 
      fill_db_tab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cs_rap_ext_num_u IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `RAP Demo: RAP BO Operations Using an ` && 
                      `Unmanaged RAP BO (External Numbering)` ). 
 
********************************************************************** 
* 
* Create operation 
* 
********************************************************************** 
 
    out->line( 
    )->next_section( `Create Operation` ). 
 
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
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
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
                        field1    = 'X' 
                        field2    = 'eee' 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
    out->next_section( `Update Operation` ). 
 
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
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FROM VALUE #( 
            %control-key_field = if_abap_behv=>mk-on 
            %control-field1 = if_abap_behv=>mk-on 
            %control-field2 = if_abap_behv=>mk-on 
            %control-field3 = if_abap_behv=>mk-on 
            %control-field4 = if_abap_behv=>mk-on 
          ( %cid = 'cid5' 
            key_field = 5 
            field1    = 'hhh' 
            field2    = 'iii' 
            field3    = 50 
            field4    = 51 ) ) 
        UPDATE FIELDS ( field1 field3 field4 ) 
          WITH VALUE #( 
          "Update via cid_ref 
          ( %cid_ref = 'cid5' 
            field1   = 'up_jjj' 
            field2   = 'up_kkk' "Value not considered 
            field3   = 500 
            field4   = 501 ) 
          "Updates via key 
          ( key_field = 1 
            field1    = 'up_lll' 
            field3    = 100 
            field4    = 101 ) 
          ( key_field = 2 
            field1    = 'up_mmm' 
            field3    = 200 
            field4    = 201 ) 
          ( key_field = 99       "Instance to fail 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
    out->next_section( `Delete Operation` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create and an delete request. The 
*   create request is included to have a %cid to refer to for demo 
*   purposes. This instance has not yet been persisted. 
* - EML statements for delete operations can only be used with the 
*   addition FROM .... 
* - Note: Instance authorization is defined in the BDEF. In this 
*   example, the corresponding handler method is implemented in a way 
*   that disables the deletion of instances if a field has a certain 
*   value. If field1 has the value 'X', a deletion is disabled. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid      = 'cid_del' 
            key_field = 6 
            field1    = 'a' 
            field2    = 'b' 
            field3    = 60 
            field4    = 61 ) ) 
        DELETE FROM VALUE #( 
          "Deletion via %cid_ref 
          ( %cid_ref = 'cid_del' ) 
          "Deletions via key 
          ( key_field = 4 ) 
          ( key_field = 5 ) 
          "Instances to fail 
          ( key_field = 3 )      "Deletion disabled 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
* Action multiply_by_2 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Executing Action mutliply_by_2` ). 
 
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
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid = 'cid_x2' 
            key_field = 7 
            field1    = 'nnn' 
            field2    = 'ooo' 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
* Action multiply_by_3 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Executing Action mutliply_by_3` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create request and a request to execute 
*   an action. The create request is included to have a %cid to refer 
*   to for demo purposes. This instance has not yet been persisted. 
* - As the name implies, the action multiplies field 
*   values (field3 and field4) by 3 for requested instances. 
* - Note: In the BDEF of this example, this action is defined with 
*   instance feature control. Here, the action execution is disabled 
*   if both integer values are 0. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid = 'cid_x3' 
            key_field = 8 
            field1    = 'ppp' 
            field2    = 'qqq' 
            field3    = 80 
            field4    = 81 ) ) 
        EXECUTE multiply_by_3 FROM VALUE #( 
          "Executing action via %cid_ref 
          ( %cid_ref = 'cid_x3' ) 
          "Executing action via key 
          ( key_field =  1  ) 
          ( key_field =  2  ) 
          "Instances to fail 
          ( key_field =  3 )      "Action execution disabled 
          ( key_field =  1234 ) ) "Key not available 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
* Action set_z 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Executing ACTION set_z` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create request and a request to execute 
*   an action. The create request is included to have a %cid to refer 
*   to for demo purposes. This instance has not yet been persisted. 
* - As the name implies, the action sets the value 'Z' for a 
*   particular field (field2) for requested instances. 
* - Note: In the BDEF of this example, this action is defined with 
*   global feature control. Here, the action execution is disabled 
*   based on a certain time frame in which you run this example. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
          ( %cid      = 'cid_setz' 
            key_field = 9 
            field1    = 'rrr' 
            field2    = 'sss' 
            field3    = 90 
            field4    = 91 ) ) 
        EXECUTE set_z FROM VALUE #( 
          "Executing action via %cid_ref 
          ( %cid_ref = 'cid_setz' ) 
          "Executing action via key 
          ( key_field =  2 ) ) 
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
    IF mapped-root IS NOT INITIAL. 
      out->write( data = mapped-root 
                name = `Entries in MAPPED response parameter ` && 
                       `(root entity)` ). 
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
* Create-by-Association Operation (from Root to Child Entity) 
* 
********************************************************************** 
    out->line( ). 
    out->next_section( `Create-by-Association Operation ` && 
                  `(from Root to Child Entity)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a create and create-by-association 
*   request, i. e. a "deep create". An instance is created for the 
*   root entity and, in the same request and based on this root 
*   instance, instances are created for the child entity, too. 
********************************************************************** 
 
    MODIFY ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
              WITH VALUE #( 
              ( %cid      = 'cid_cba' 
                key_field = 10 
                field1    = 'ttt' 
                field2    = 'uuu' 
                field3    = 100 
                field4    = 101 ) ) 
        CREATE BY \_child 
        FIELDS ( key_ch field_ch1 field_ch2 ) WITH VALUE #( 
          "CBA operation via %cid_ref 
          ( %cid_ref = 'cid_cba' 
            %target = VALUE #( ( %cid      = 'cid_ch1' 
                                 key_ch    = 11 
                                 field_ch1 = 'aaa_ch' 
                                 field_ch2 = 110 ) 
                               ( %cid      = 'cid_ch2' 
                                 key_ch    = 12 
                                 field_ch1 = 'bbb_ch' 
                                 field_ch2 =  120 ) ) ) 
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
                                 field_ch2 = 3 ) ) ) ) 
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
    IF mapped IS NOT INITIAL. 
      out->write( data = mapped 
                name = `Entries in MAPPED response parameter ` && 
                       `(root & child entity)` ). 
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
* Read operation 
* 
********************************************************************** 
 
    out->line( ). 
    out->next_section( `Read Operation (Root Entity)` ). 
 
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
 
    READ ENTITIES OF demo_cs_rap_ro_u 
        ENTITY root 
        ALL FIELDS WITH VALUE #( 
          ( key_field = 1 ) 
          ( key_field = 2 ) 
          ( key_field = 5 ) ) "Instance to fail 
        RESULT FINAL(result) 
        FAILED failed 
        REPORTED reported. 
 
    "Displaying the read result and response information 
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
    out->next_section( `Read Operation (Child Entity)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read request. The read operation is 
*   executed on the child entity directly by specifying the alias, as 
*   it is defined in the BDEF, following the ABAP word ENTITY. 
* - All field values are read using the addition ALL FIELDS WITH. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_u 
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
    out->next_section( `Read-by-Association Operation ` && 
                  `(from Parent to Child)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read-by-association request from the 
*   parent to the child entity. 
* - All field values are read using the addition ALL FIELDS WITH. 
* - Specifying the parameter for RESULT is mandatory. 
* - Additionally, the optional association links are retrieved. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_u 
          ENTITY root 
          BY \_child 
          ALL FIELDS WITH VALUE #( 
            ( key_field = 2 ) 
            ( key_field = 10 ) 
            ( key_field = 111 ) ) "Instance to fail 
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
    out->next_section( `Read-by-Association Operation ` && 
                  `(from Child to Parent)` ). 
 
********************************************************************** 
* Notes: 
* - The EML request includes a read-by-association request from the 
*   child to the parent. 
* - All field values are read using the addition ALL FIELDS WITH. 
* - Specifying the parameter for RESULT is mandatory. 
* - Additionally, the optional association links are retrieved. 
********************************************************************** 
 
    READ ENTITIES OF demo_cs_rap_ro_u 
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
    out->next_section( `Read and Read-by-Association Operations ` && 
                     `Using Dynamic Variants of EML Statements` ). 
 
********************************************************************** 
* Notes: 
* - If the parameter for FULL is not flagged, only the association 
*   links are returned. The parameter for RESULT will be empty. 
********************************************************************** 
 
    DATA: 
      op_tab          TYPE abp_behv_retrievals_tab, 
      read_dyn        TYPE TABLE FOR READ IMPORT demo_cs_rap_ro_u, 
      read_dyn_result TYPE TABLE FOR READ RESULT demo_cs_rap_ro_u, 
      rba_dyn         TYPE TABLE FOR READ IMPORT 
                        demo_cs_rap_ro_u\_child, 
      rba_dyn_result  TYPE TABLE FOR READ RESULT 
                        demo_cs_rap_ro_u\_child, 
      rba_dyn_link    TYPE TABLE FOR READ LINK demo_cs_rap_ro_u\_child. 
 
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
 
    out->write_doc( `<b>Result if FULL parameter is ` && 
                  `not flagged for RBA</b>` ). 
 
    op_tab = VALUE #( 
       ( op = if_abap_behv=>op-r-read 
         entity_name = 'DEMO_CS_RAP_RO_U' 
         instances   = REF #( read_dyn ) 
         results     = REF #( read_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read_ba 
         entity_name = 'DEMO_CS_RAP_RO_U' 
         sub_name    = '_CHILD' 
         full        = '' 
         instances   = REF #( rba_dyn ) 
         results     = REF #( rba_dyn_result ) 
         links       = REF #( rba_dyn_link ) ) ). 
 
    READ ENTITIES OPERATIONS op_tab. 
 
    out->write( read_dyn_result ). 
    out->write( rba_dyn_result ). 
    out->write( rba_dyn_link ). 
 
    out->write_doc( `<b>Result if FULL parameter is ` && 
                  `flagged for RBA</b>` ). 
 
    op_tab = VALUE #( 
           ( op = if_abap_behv=>op-r-read 
             entity_name = 'DEMO_CS_RAP_RO_U' 
             instances   = REF #( read_dyn ) 
             results     = REF #( read_dyn_result ) ) 
           ( op = if_abap_behv=>op-r-read_ba 
             entity_name = 'DEMO_CS_RAP_RO_U' 
             sub_name    = '_CHILD' 
             full        = 'X' 
             instances   = REF #( rba_dyn ) 
             results     = REF #( rba_dyn_result ) 
             links       = REF #( rba_dyn_link ) ) ). 
 
    READ ENTITIES OPERATIONS op_tab. 
 
    out->write( read_dyn_result ). 
    out->write( rba_dyn_result ). 
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
        WHEN <err>-%op-%action-multiply_by_3. 
          op = `executing action multiply_by_3`. 
        WHEN <err>-%op-%action-set_z. 
          op = `executing action set_z`. 
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
 
        APPEND `Error for child instance with ` && 
             COND #( WHEN <err_ch>-%cid IS NOT INITIAL THEN `%cid = ` 
                     && <err_ch>-%cid 
                     ELSE `key_field = ` && <err_ch>-key_field && 
                      ` and key_ch = ` && <err_ch>-key_ch ) && 
             `: Fail cause ` &&  <err_ch>-%fail-cause && 
             ` for operation.` 
             TO errors. 
 
      ENDLOOP. 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD extract_from_reported. 
    CLEAR messages. 
 
    LOOP AT reported-root ASSIGNING FIELD-SYMBOL(<rep>). 
      IF <rep>-%global = if_abap_behv=>mk-on. 
        APPEND <rep>-%msg->m_severity && ` ` && 
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
            field1    = 'fff' 
            field2    = 'ggg' 
            field3    = 40 
            field4    = 41 ) ) ). 
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

- Create

- Update

- Delete

- Executing actions

- Instance and global feature control

- Instance authorization

- Create-by-association (parent to child)

- Read

- Read-by-association (parent to child)

- Read (child entity)

- Read-by-association (child to parent)

- Excursion: Dynamic EML statement

See comments in the code for more information.

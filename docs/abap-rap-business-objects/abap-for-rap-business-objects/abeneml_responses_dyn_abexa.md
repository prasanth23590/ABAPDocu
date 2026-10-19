---
title: "ABAP EML - Responses (Dynamic Forms of ABAP EML Statements)"
source_file: abeneml_responses_dyn_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - response_param > Examples for Responses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - Responses (Dynamic Forms of ABAP EML Statements)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates responses retrieved using the dynamic form of the ABAP EML `MODIFY` and `READ` statements with a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT` and its child entity `DEMO_MANAGED_CHILD`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT
  as select from demo_tab_root
  composition [1..1] of DEMO_MANAGED_CHILD as _child
  {     
    key demo_tab_root.key_field,
        demo_tab_root.data_field1_root,
        demo_tab_root.data_field2_root,
        _child
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_MANAGED_CHILD
  as select from demo_tab_child
  association to parent DEMO_MANAGED_ROOT as _parent 
    on $projection.key_field = _parent.key_field
  {
        _parent,
    key demo_tab_child.key_field,
        demo_tab_child.data_field1_child,
        demo_tab_child.data_field2_child
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root unique;
strict ( 2 );

define behavior for DEMO_MANAGED_ROOT
persistent table demo_tab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }

  field ( readonly : update ) key_field;
}

define behavior for DEMO_MANAGED_CHILD alias child
persistent table demo_tab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly : update ) key_field;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, there is no [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) created.

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
CLASS cl_demo_rap_eml_responses_dyn DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed_dyn   TYPE abp_behv_response_tab, 
      reported_dyn TYPE abp_behv_response_tab, 
      mapped_dyn   TYPE abp_behv_response_tab, 
      failed_tab   TYPE TABLE FOR FAILED demo_managed_root, 
      reported_tab TYPE TABLE FOR REPORTED demo_managed_root, 
      mapped_tab   TYPE TABLE FOR MAPPED demo_managed_root. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_responses_dyn IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
               `Responses for dynamic forms of ABAP EML Statements` 
                   ). 
 
********************************************************************** 
 
    out->begin_section( 
      `Responses for the dynamic form MODIFY ENTITIES OPERATIONS` 
                ). 
 
    DATA: op_tab           TYPE abp_behv_changes_tab, 
          create_root_tab  TYPE TABLE FOR CREATE demo_managed_root, 
          update_root_tab  TYPE TABLE FOR UPDATE demo_managed_root, 
          delete_root_tab  TYPE TABLE FOR DELETE demo_managed_root, 
          cba_tab          TYPE TABLE FOR CREATE 
                              demo_managed_root\_child, 
          update_child_tab TYPE TABLE FOR UPDATE demo_managed_child, 
          delete_child_tab TYPE TABLE FOR DELETE demo_managed_child. 
 
    create_root_tab = VALUE #( 
                ( %cid = 'cid1' 
                  key_field = 1 
                  %control-key_field = if_abap_behv=>mk-on 
                  data_field1_root = 'aaa' 
                  %control-data_field1_root = if_abap_behv=>mk-on 
                  data_field2_root = 'bbb' 
                  %control-data_field2_root = if_abap_behv=>mk-on ) 
                ( %cid = 'cid2' 
                  key_field = 2 
                  %control-key_field = if_abap_behv=>mk-on 
                  data_field1_root = 'ccc' 
                  %control-data_field1_root = if_abap_behv=>mk-on 
                  data_field2_root = 'ddd' 
                  %control-data_field2_root = if_abap_behv=>mk-on ) 
                ( %cid = 'cid3' 
                  key_field = 3 
                  %control-key_field = if_abap_behv=>mk-on 
                  data_field1_root = 'eee' 
                  %control-data_field1_root = if_abap_behv=>mk-on 
                  data_field2_root = 'fff' 
                  %control-data_field2_root = if_abap_behv=>mk-on ) ). 
 
    update_root_tab = VALUE #( 
              ( %cid_ref = 'cid2' 
                data_field1_root = 'GGG' 
                %control-data_field1_root = if_abap_behv=>mk-on 
                data_field2_root = 'HHH' 
                %control-data_field2_root = if_abap_behv=>mk-on ) ). 
 
    cba_tab = VALUE #( 
                ( %cid_ref = 'cid1' 
                  %target = VALUE #( ( 
                    %cid = 'child_cid1' 
                    data_field1_child = 'iii' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'jjj' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) 
                ( %cid_ref = 'cid2' 
                  %target = VALUE #( ( 
                    %cid = 'child_cid2' 
                    data_field1_child = 'kkk' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'lll' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) 
                ( %cid_ref = 'cid3' 
                  %target = VALUE #( ( 
                    %cid = 'child_cid3' 
                    data_field1_child = 'mmm' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'nnn' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) ). 
 
    update_child_tab = VALUE #( 
               ( key_field = 2 
                 data_field1_child = 'OOO' 
                 %control-data_field1_child = if_abap_behv=>mk-on 
                 data_field2_child = 'PPP' 
                 %control-data_field2_child = if_abap_behv=>mk-on ) 
               ( key_field = 5 
                 data_field1_child = 'QQQ' 
                 %control-data_field1_child = if_abap_behv=>mk-on 
                 data_field2_child = 'RRR' 
                 %control-data_field2_child = if_abap_behv=>mk-on ) ). 
 
    delete_root_tab = VALUE #( ( key_field = 3 ) 
                               ( key_field = 4 ) ). 
 
    delete_child_tab = VALUE #( ( key_field = 3 ) 
                                ( key_field = 6 ) ). 
 
    op_tab = VALUE #( 
           ( op = if_abap_behv=>op-m-create 
             entity_name = 'DEMO_MANAGED_ROOT' 
             instances   = REF #( create_root_tab ) ) 
           ( op = if_abap_behv=>op-m-update 
             entity_name = 'DEMO_MANAGED_ROOT' 
             instances   = REF #( update_root_tab ) ) 
           ( op = if_abap_behv=>op-m-delete 
             entity_name = 'DEMO_MANAGED_ROOT' 
             instances   = REF #( delete_root_tab ) ) 
           ( op = if_abap_behv=>op-m-create_ba 
             entity_name = 'DEMO_MANAGED_ROOT' 
             sub_name = '_CHILD' 
             instances   = REF #( cba_tab ) ) 
           ( op = if_abap_behv=>op-m-update 
             entity_name = 'DEMO_MANAGED_CHILD' 
             instances   = REF #( update_child_tab ) ) 
           ( op = if_abap_behv=>op-m-delete 
             entity_name = 'DEMO_MANAGED_CHILD' 
             instances   = REF #( delete_child_tab ) ) 
           ). 
 
    MODIFY ENTITIES OPERATIONS op_tab 
      FAILED   FINAL(failed1) 
      REPORTED FINAL(reported1) 
      MAPPED   FINAL(mapped1). 
 
    out->write_text( `Responses for EML MODIFY operation:` 
      )->write( failed1 
      )->write( reported1 
      )->write( mapped1 ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(root_tab). 
    SELECT * FROM demo_tab_child INTO TABLE @FINAL(child_tab). 
 
    out->write_text( `Database entries of root and child entity` && 
                     `after EML MODIFY operations:` 
               )->write( root_tab 
               )->write( child_tab ). 
 
********************************************************************** 
 
    out->line( 
      )->begin_section( 
            `Responses for the dynamic form READ ENTITIES OPERATIONS` 
                ). 
 
    DATA: 
      op_tab_read      TYPE abp_behv_retrievals_tab, 
      read_dyn         TYPE TABLE FOR READ IMPORT demo_managed_root, 
      read_dyn_result  TYPE TABLE FOR READ RESULT demo_managed_root, 
      rba_dyn          TYPE TABLE FOR READ IMPORT 
                          demo_managed_root\_child, 
      rba_dyn_result   TYPE TABLE FOR 
                         READ RESULT demo_managed_root\_child, 
      read2_dyn        TYPE TABLE FOR READ IMPORT demo_managed_child, 
      read2_dyn_result TYPE TABLE FOR READ RESULT demo_managed_child. 
 
    read_dyn = VALUE #( 
      ( key_field = 1 
        %control = VALUE #( 
           key_field  = if_abap_behv=>mk-on 
           data_field1_root    = if_abap_behv=>mk-on 
           data_field2_root   = if_abap_behv=>mk-on ) ) 
      ( key_field = 2 
        %control = VALUE #( 
           key_field  = if_abap_behv=>mk-on 
           data_field1_root    = if_abap_behv=>mk-on 
           data_field2_root   = if_abap_behv=>mk-on ) ) 
      ( key_field = 3 
        %control = VALUE #( 
           key_field  = if_abap_behv=>mk-on 
           data_field1_root    = if_abap_behv=>mk-on 
           data_field2_root   = if_abap_behv=>mk-on ) ) 
       ). 
 
    rba_dyn = VALUE #( 
     ( key_field = 1 
       %control = VALUE #( 
           key_field          = if_abap_behv=>mk-on 
           data_field1_child  = if_abap_behv=>mk-on 
           data_field2_child  = if_abap_behv=>mk-on ) ) 
     ( key_field = 2 
       %control = VALUE #( 
           key_field          = if_abap_behv=>mk-on 
           data_field1_child  = if_abap_behv=>mk-on 
           data_field2_child  = if_abap_behv=>mk-on ) ) 
         ). 
 
    read2_dyn = VALUE #( 
     ( key_field = 1 
       %control = VALUE #( 
           key_field          = if_abap_behv=>mk-on 
           data_field1_child  = if_abap_behv=>mk-on 
           data_field2_child  = if_abap_behv=>mk-on ) ) 
     ( key_field = 4 
       %control = VALUE #( 
           key_field          = if_abap_behv=>mk-on 
           data_field1_child  = if_abap_behv=>mk-on 
           data_field2_child  = if_abap_behv=>mk-on ) ) 
         ). 
 
 
    op_tab_read = VALUE #( 
       ( op = if_abap_behv=>op-r-read 
         entity_name = 'DEMO_MANAGED_ROOT' 
         instances   = REF #( read_dyn ) 
         results     = REF #( read_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read_ba 
         entity_name = 'DEMO_MANAGED_ROOT' 
         sub_name    = '_CHILD' 
         instances   = REF #( rba_dyn ) 
         results     = REF #( rba_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read 
         entity_name = 'DEMO_MANAGED_CHILD' 
         instances   = REF #( read2_dyn ) 
         results     = REF #( read2_dyn_result ) ) 
                          ). 
 
    READ ENTITIES OPERATIONS op_tab_read 
      FAILED   FINAL(failed2) 
      REPORTED FINAL(reported2). 
 
    out->write_text( `Responses for EML READ operation:` 
      )->write( failed2 
      )->write( reported2 ). 
 
    out->write_text( `Database entries of root and child entity ` && 
                     `according to EML READ operations:` 
               )->write( read_dyn_result 
               )->write( rba_dyn_result 
               )->write( read2_dyn_result ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root. 
    DELETE FROM demo_tab_child. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Dynamic ABAP EML modify operations using `MODIFY ENTITIES OPERATIONS`

  Various operations on data sets of the root and child entity are executed. For that purpose, an internal table with type `ABP_BEHV_CHANGES_TAB` must be defined. This table includes parameters (in this case, among others, other tables holding demo data and being typed with the required BDEF derived type) to carry out the modifications. Errors are intentionally caused for the modify operations so that the response parameters for `FAILED` and `REPORTED` are filled with entries. Furthermore, the `MAPPED` response is included. All three response parameters are of type `ABP_BEHV_RESPONSE_TAB`. The class provides methods to display selected parts of those responses that are put into internal tables that are displayed in the output screen as well as the database table entries after the modifications. The saving of the modification is triggered by a `COMMIT ENTITIES` statement.

- Dynamic ABAP EML read operations using `READ ENTITIES OPERATIONS`

  Various read operations on data sets of the root and child entity are executed. For that purpose, an internal table with type `ABP_BEHV_RETRIEVALS_TAB` must be defined. This table includes parameters (in this case, among others, other tables holding demo data and being typed with the required BDEF derived type) to carry out the reading. Errors are intentionally caused for the read operations so that the parameter for `FAILED` is filled with entries (the `REPORTED` parameter does not get filled by the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) in this example). Also here, the response parameter is of type `ABP_BEHV_RESPONSE_TAB`. Same as above, the responses are put into an internal table that are displayed in the output screen (note that this internal table is shared for the output of failures for the modify and read operations in this example, i. e. the columns for create, delete and update are not relevant for read operations and must be ignored) as well as the database table entries after the read operation.

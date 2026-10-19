---
title: "ABAP EML - MODIFY, Variants"
source_file: abeneml_modify_alternatives_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY, Variants

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the variants of the ABAP EML `MODIFY` statement to manipulate a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md):

- `MODIFY ENTITY bdef`

- `MODIFY ENTITIES OF bdef`

- `MODIFY ENTITIES OPERATIONS op_tab`

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

For the above RAP behavior definition, there is no [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) created and needed since only standard [CRUD](../../abap-glossary/abencrud_glosry.md) operations are used in the example.

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
CLASS cl_demo_rap_eml_modify DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_modify IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
               `MODIFY Statements Alternatives` 
                   ). 
 
    out->begin_section( 
                 `MODIFY ENTITY bdef` 
                ). 
 
    "MODIFY ENTITY 
    MODIFY ENTITY demo_managed_root 
      CREATE FIELDS ( key_field data_field1_root 
          data_field2_root ) WITH VALUE #( 
        ( %cid = 'cid1' key_field = 1 
                        data_field1_root = 'aaa' 
                        data_field2_root = 'bbb' ) 
        ( %cid = 'cid2' key_field = 2 
                        data_field1_root = 'ccc' 
                        data_field2_root = 'ddd' ) ) 
      CREATE BY \_child FIELDS ( data_field1_child 
          data_field2_child ) WITH VALUE #( 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( ( %cid = 'cid3' 
                               data_field1_child = 'eee' 
                               data_field2_child = 'fff' ) 
                           ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( ( %cid = 'cid4' 
                               data_field1_child = 'ggg' 
                               data_field2_child = 'hhh' ) 
                           ) ) 
        ) 
        FAILED   FINAL(fail_mod) 
        REPORTED FINAL(rep_mod) 
        MAPPED   FINAL(map_mod). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(create_tab). 
    SELECT * FROM demo_tab_child INTO TABLE @FINAL(cba_tab). 
 
    out->write_text( 
       `Database table entries after operations using MODIFY ENTITY:` 
               )->write( create_tab 
               )->write( cba_tab ). 
 
    out->begin_section( 
                 `MODIFY ENTITIES OF bdef` 
                ). 
 
    initialize_dbtabs( ). 
 
********************************************************************** 
 
    "MODIFY ENTITIES OF bdef 
    MODIFY ENTITIES OF demo_managed_root 
    ENTITY demo_managed_root 
        CREATE FIELDS ( key_field data_field1_root 
          data_field2_root ) WITH VALUE #( 
          ( %cid = 'cid5' 
            key_field = 3 
            data_field1_root = 'iii' 
            data_field2_root = 'jjj' ) 
          ( %cid = 'cid6' 
            key_field = 4 
            data_field1_root = 'kkk' 
            data_field2_root = 'lll' ) ) 
    ENTITY demo_managed_root 
        UPDATE FIELDS ( data_field1_root 
          data_field2_root ) WITH VALUE #( 
          ( %cid_ref = 'cid6' 
            data_field1_root = 'mmm' 
            data_field2_root = 'nnn' ) ) 
    ENTITY demo_managed_root 
        CREATE BY \_child FIELDS ( data_field1_child 
          data_field2_child ) WITH VALUE #( 
          ( %cid_ref = 'cid5' 
            %target = VALUE #( ( %cid = 'cid7' 
                                 data_field1_child = 'eee' 
                                 data_field2_child = 'fff' ) 
                             ) ) 
          ( %cid_ref = 'cid6' 
            %target = VALUE #( ( %cid = 'cid8' 
                                 data_field1_child = 'ggg' 
                                 data_field2_child = 'hhh' ) 
                             ) ) ) 
    ENTITY child 
        UPDATE FIELDS ( data_field1_child 
            data_field2_child ) WITH VALUE #( 
          ( %cid_ref = 'cid8' 
            data_field1_child = 'ooo' 
            data_field2_child = 'ppp' ) ) 
        FAILED   FINAL(fail_mod2) 
        REPORTED FINAL(rep_mod2) 
        MAPPED   FINAL(map_mod2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(create_tab2). 
    SELECT * FROM demo_tab_child INTO TABLE @FINAL(cba_tab2). 
 
    out->write_text( 
   `Database table entries after operations using MODIFY ENTITIES:` 
               )->write( create_tab2 
               )->write( cba_tab2 ). 
 
    initialize_dbtabs( ). 
 
********************************************************************** 
 
    out->begin_section( 
                 `MODIFY ENTITIES OPERATIONS op_tab` 
                ). 
 
    "MODIFY ENTITIES OPERATIONS op_tab 
    DATA: op_tab           TYPE abp_behv_changes_tab, 
          create_root_tab  TYPE TABLE FOR CREATE demo_managed_root, 
          update_root_tab  TYPE TABLE FOR UPDATE demo_managed_root, 
          delete_root_tab  TYPE TABLE FOR DELETE demo_managed_root, 
          cba              TYPE TABLE FOR 
            CREATE demo_managed_root\_child, 
          update_child_tab TYPE TABLE FOR UPDATE demo_managed_child, 
          delete_child_tab TYPE TABLE FOR DELETE demo_managed_child. 
 
    create_root_tab = VALUE #( 
                ( %cid = 'cid1' 
                  key_field = 5 
                  %control-key_field = if_abap_behv=>mk-on 
                  data_field1_root = 'aaa' 
                  %control-data_field1_root = if_abap_behv=>mk-on 
                  data_field2_root = 'bbb' 
                  %control-data_field2_root = if_abap_behv=>mk-on ) 
                ( %cid = 'cid2' 
                  key_field = 6 
                  %control-key_field = if_abap_behv=>mk-on 
                  data_field1_root = 'ccc' 
                  %control-data_field1_root = if_abap_behv=>mk-on 
                  data_field2_root = 'ddd' 
                  %control-data_field2_root = if_abap_behv=>mk-on ) 
                ( %cid = 'cid3' 
                  key_field = 7 
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
 
    cba = VALUE #( 
                ( %cid_ref = 'cid1' 
                  %target = VALUE #( ( 
                    %cid = 'cid_cba1' 
                    data_field1_child = 'iii' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'jjj' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) 
                ( %cid_ref = 'cid2' 
                  %target = VALUE #( ( 
                    %cid = 'cid_cba2' 
                    data_field1_child = 'kkk' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'lll' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) 
                ( %cid_ref = 'cid3' 
                  %target = VALUE #( ( 
                    %cid = 'cid_cba3' 
                    data_field1_child = 'mmm' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'nnn' 
                    %control-data_field2_child = if_abap_behv=>mk-on 
                ) ) ) ). 
 
    update_child_tab = VALUE #( 
               ( key_field = 6 
                 data_field1_child = 'OOO' 
                 %control-data_field1_child = if_abap_behv=>mk-on 
                 data_field2_child = 'PPP' 
                 %control-data_field2_child = if_abap_behv=>mk-on ) ). 
 
    delete_root_tab = VALUE #( ( key_field = 7 ) ). 
 
    delete_child_tab = VALUE #( ( key_field = 7 ) ). 
 
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
             sub_name    = '_CHILD' 
             instances   = REF #( cba ) ) 
           ( op = if_abap_behv=>op-m-update 
             entity_name = 'DEMO_MANAGED_CHILD' 
             instances   = REF #( update_child_tab ) ) 
           ( op = if_abap_behv=>op-m-delete 
             entity_name = 'DEMO_MANAGED_CHILD' 
             instances   = REF #( delete_child_tab ) ) 
           ). 
 
    MODIFY ENTITIES OPERATIONS op_tab 
      FAILED   FINAL(fail_mod3) 
      REPORTED FINAL(rep_mod3) 
      MAPPED   FINAL(map_mod3). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(create_tab3). 
    SELECT * FROM demo_tab_child INTO TABLE @FINAL(cba_tab3). 
 
    out->write_text( 
      `Database table entries after operations ` && 
      `using MODIFY ENTITIES OPERATIONS:` 
               )->write( create_tab3 
               )->write( cba_tab3 ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root. 
    DELETE FROM demo_tab_child. 
    DELETE FROM demo_tab_assoc. 
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

- `MODIFY ENTITY bdef`

  Two create operations are executed with the statement `MODIFY ENTITY` for single entities. The one for the root entity, the other for the child entity. For that purpose, two internal tables with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) are created. They include demo values to be shown in the output. The RAP query engine reads the data from the respective database tables into a managed [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) in which the create operations take place using the `SET FIELDS` additions. The changes are saved with the statement [`COMMIT ENTITIES`](abapcommit_entities.md), and, thus, the changed data are persisted to the database tables.

- `MODIFY ENTITIES OF bdef`

  Multiple operations are executed on multiple RAP BO entities. In this case, the following is demonstrated: an update and create operation on data sets of the root entity, a create by association operation and an update operation on the child entity directly. The addition `SET FIELDS` is used while the internal tables are created inline holding demo data.

- `MODIFY ENTITIES OPERATIONS op_tab`

  The example demonstrates a dynamic modify operation. There are various operations on data sets of the root and child entity. For that purpose, an internal table with type `ABP_BEHV_CHANGES_TAB` must be defined. This table includes parameters (in this case, among others, other tables holding demo data and being typed with the required BDEF derived type) to carry out the modifications.

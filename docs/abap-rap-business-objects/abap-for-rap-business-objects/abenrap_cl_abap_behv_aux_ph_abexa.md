---
title: "Checking RAP Transactional Phases"
source_file: abenrap_cl_abap_behv_aux_ph_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP-Related System Classes and Functionality > CL_ABAP_BEHV_AUX"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Checking RAP Transactional Phases

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the methods `GET_CURRENT_PHASE` and `GET_CURRENT_HANDLER_KIND` of the class `CL_ABAP_BEHV_AUX`.

**Data model**

The CDS data model consists of the root entity `DEMO_UMANAGED_ROOT_LATE_NUM2`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_umanaged_root_late_num2
  as select from demo_tab_root_3
  composition [1..*] of demo_umanaged_child_late_num2 as _child
  {
    key key_field,
        field1,
        field2,
        field3,
        field4,
        _child
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UMANAGED_ROOT_LATE_NUM2` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class
 bp_demo_umanaged_root_late_nu2 unique;
strict(2);

define behavior for demo_umanaged_root_late_num2
lock master
authorization master ( global )
late numbering
{
  create;
  update;
  delete;
  field ( readonly ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UMANAGED_ROOT_LATE_NU2`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UMANAGED_ROOT_LATE_NU2CCIMP` of the behavior pool.

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
CLASS cl_demo_rap_transaction_phases DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed_early TYPE RESPONSE FOR 
        FAILED EARLY demo_umanaged_root_late_num2, 
      failed_late  TYPE RESPONSE FOR 
        FAILED LATE demo_umanaged_root_late_num2. 
    METHODS: 
      initialize_dbtabs, 
      display_dbtab_entries, 
      display_phases. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_transaction_phases IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: RAP Transactional Phases` ). 
 
    APPEND VALUE #( phase    = cl_abap_behv_aux=>get_current_phase( ) 
                    meth_log = `No handler/saver method. Outside of` && 
                    ` RAP transactional phases.` ) 
      TO bp_demo_umanaged_root_late_nu2=>phases. 
 
    display_phases( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->begin_section( `RAP create operation including a RAP BO ` && 
    `instance that fails in the finalize method` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
        ( %cid = 'cid1' 
          field1 = 'create_1' 
          field2 = 'create_2' 
          field3 = 55 
          field4 = 55 ) ) 
     FAILED failed_early. 
 
    COMMIT ENTITIES 
      RESPONSE OF demo_umanaged_root_late_num2 FAILED failed_late. 
 
    IF sy-subrc <> 0. 
      out->write( 
        `ERROR: An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_phases( ). 
 
    display_dbtab_entries( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->begin_section( `Successful RAP create operation` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
        ( %cid = 'cid2' 
          field1 = 'create_3' 
          field2 = 'create_4' 
          field3 = 50 
          field4 = 55 ) ) 
     FAILED failed_early. 
 
    COMMIT ENTITIES 
      RESPONSE OF demo_umanaged_root_late_num2 FAILED failed_late. 
 
    IF sy-subrc <> 0. 
      out->write( 
        `ERROR: An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_phases( ). 
 
    display_dbtab_entries( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->begin_section( `RAP create operation including a RAP BO ` && 
    `instance that fails in the check_before_save method` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
        ( %cid = 'cid3' 
          field1 = 'create_5' 
          field2 = 'create_6' 
          field3 = 100 
          field4 = 200 ) ) 
      FAILED failed_early. 
 
    COMMIT ENTITIES 
      RESPONSE OF demo_umanaged_root_late_num2 FAILED failed_late. 
 
    IF sy-subrc <> 0. 
      out->write( 
        `ERROR: An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_phases( ). 
 
    display_dbtab_entries( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->begin_section( `Successful RAP create operation` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
        ( %cid = 'cid4' 
          field1 = 'create_7' 
          field2 = 'create_8' 
          field3 = 100 
          field4 = 20 ) ) 
      FAILED failed_early. 
 
    COMMIT ENTITIES 
      RESPONSE OF demo_umanaged_root_late_num2 FAILED failed_late. 
 
    IF sy-subrc <> 0. 
      out->write( 
        `ERROR: An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_phases( ). 
 
    display_dbtab_entries( ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
  ENDMETHOD. 
  METHOD display_dbtab_entries. 
    SELECT key_field, field1, field2, field3, field4 
       FROM demo_tab_root_3 ORDER BY key_field 
       INTO TABLE @DATA(db_tab). 
 
    out->write( `Database table entries after RAP operation:` 
    )->write( db_tab ). 
  ENDMETHOD. 
  METHOD display_phases. 
    out->write( `Transactional phases log table:` 
    )->write( bp_demo_umanaged_root_late_nu2=>phases ). 
 
    CLEAR bp_demo_umanaged_root_late_nu2=>phases. 
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

The example contains four RAP create operations using an ABAP EML `MODIFY` statement:

- Two RAP create operations fail. One operation intentionally fails in the [`finalize`](abensaver_finalize.md) [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md). Another operations fails in the [`check_before_save`](abensaver_check_before_save.md) method.

- Two RAP create operations are successful.

- The example is implemented in a way that in the RAP handler and saver methods a log table is filled. The log table includes, among other things, information about the current RAP transactional phase (retrieved using `CL_ABAP_BEHV_AUX=>GET_CURRENT_PHASE`) and the current handler kind (retrieved using `CL_ABAP_BEHV_AUX=>GET_CURRENT_HANDLER_KIND`).

- The log table and the database table entries as result of the RAP create operations are displayed.

- The log table for the failed instances shows that the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md) is not reached, only the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md). The RAP transaction is concluded with the [RAP cleanup phase](../../abap-glossary/abenrap_cleanup_phase_glosry.md) demonstrated by the successful RAP create operations.

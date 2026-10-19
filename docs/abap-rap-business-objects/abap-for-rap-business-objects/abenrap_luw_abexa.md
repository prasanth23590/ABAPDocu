---
title: "Transactional Phases in a RAP Transaction"
source_file: abenrap_luw_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Transactional Phases in a RAP Transaction

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the transactional phases of a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) using an [unmanaged](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) with [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_LUW_LN_U`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_RAP_LUW_LN_U
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_LUW_LN_U` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class bp_demo_rap_luw_ln_u unique;
strict ( 2 );

define behavior for DEMO_RAP_LUW_LN_U  alias root
late numbering
lock master
authorization master ( global )

{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_LUW_LN_U`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_RAP_LUW_LN_U==========CCIMP` of the behavior pool.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demonstrating the Phases of the RAP LUW</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_luw_ln_u DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      select_from_dbtab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_luw_ln_u IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demonstrating the Phases of the RAP LUW` 
    )->line( 
    )->write( `---------- Successful save  ----------` ). 
 
    MODIFY ENTITY demo_rap_luw_ln_u 
        CREATE FIELDS ( field1 field2 field3 field4 ) 
        WITH VALUE #( 
          ( %cid = 'cid1' field1 = 'aaa' 
            field2 = 'bbb' field3 = 1 field4 = 2  ) 
          ( %cid = 'cid2' field1 = 'ccc' 
            field2 = 'ddd' field3 = 3 field4 = 4  ) ) 
         FAILED DATA(f_mod) 
         REPORTED DATA(r_mod). 
 
    COMMIT ENTITIES RESPONSE OF demo_rap_luw_ln_u FAILED DATA(f). 
 
    IF sy-subrc <> 0. 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
      out->write( f ). 
 
    ELSE. 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
    ENDIF. 
 
    out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
    CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Failure in FINALIZE method -----` ). 
 
    MODIFY ENTITY demo_rap_luw_ln_u 
       CREATE FIELDS ( field1 field2 field3 field4 ) 
       WITH VALUE #( 
         ( %cid = 'cid3' field1 = 'eee123' 
           field2 = 'fff' field3 = 5 field4 = 6 ) ) 
       FAILED f_mod 
       REPORTED r_mod. 
 
    COMMIT ENTITIES RESPONSE OF demo_rap_luw_ln_u FAILED f. 
 
    IF sy-subrc <> 0. 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
      out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
      CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
      out->write( f ). 
 
 
      MODIFY ENTITY demo_rap_luw_ln_u 
           CREATE FIELDS ( field1 field2 field3 field4 ) 
           WITH VALUE #( 
             ( %cid = 'cid4' field1 = 'eee' 
               field2 = 'fff' field3 = 7 field4 = 8 ) ) 
           FAILED f_mod 
           REPORTED r_mod. 
 
      COMMIT ENTITIES RESPONSE OF demo_rap_luw_ln_u FAILED f. 
 
      IF sy-subrc = 0. 
        out->write( `sy-subrc was set to ` && sy-subrc && 
        ` after COMMIT ENTITIES statement.` ). 
 
        out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
        CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
      ENDIF. 
    ELSE. 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
    ENDIF. 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Failure in CHECK_BEFORE_SAVE method -----` ). 
 
    MODIFY ENTITY demo_rap_luw_ln_u 
       CREATE FIELDS ( field1 field2 field3 field4 ) 
       WITH VALUE #( 
         ( %cid = 'cid1' field1 = 'ggg' 
           field2 = 'XXX' field3 = 9 field4 = 9 ) ) 
       FAILED f_mod 
       REPORTED r_mod. 
 
    COMMIT ENTITIES RESPONSE OF demo_rap_luw_ln_u FAILED f. 
 
    IF sy-subrc <> 0. 
 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
      out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
      CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
      out->write( f ). 
 
      MODIFY ENTITY demo_rap_luw_ln_u 
         CREATE FIELDS ( field1 field2 field3 field4 ) 
         WITH VALUE #( 
           ( %cid = 'cid1' field1 = 'ggg' 
             field2 = 'hhh' field3 = 10 field4 = 11 ) ) 
         FAILED f_mod 
         REPORTED r_mod. 
 
      COMMIT ENTITIES. 
      IF sy-subrc = 0. 
 
        out->write( `sy-subrc was set to ` && sy-subrc && 
        ` after COMMIT ENTITIES statement.` ). 
 
        out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
        CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
      ENDIF. 
    ELSE. 
      out->write( `sy-subrc was set to ` && sy-subrc && 
      ` after COMMIT ENTITIES statement.` ). 
 
    ENDIF. 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `----- Rollback -----` ). 
 
    MODIFY ENTITY demo_rap_luw_ln_u 
       CREATE FIELDS ( field1 field2 field3 field4 ) 
       WITH VALUE #( 
         ( %cid = 'cid1' field1 = 'eee' 
           field2 = 'fff' field3 = 10 field4 = 12 ) 
         ( %cid = 'cid2' field1 = 'ggg123' 
           field2 = 'hhh' field3 = 14 field4 = 16 ) ) 
       FAILED f_mod 
       REPORTED r_mod. 
 
    ROLLBACK ENTITIES. 
 
    out->write( bp_demo_rap_luw_ln_u=>meth_called ). 
    CLEAR bp_demo_rap_luw_ln_u=>meth_called. 
 
    "Displaying database table entries after modify request 
    select_from_dbtab( ). 
 
    out->line( ). 
  ENDMETHOD. 
  METHOD select_from_dbtab. 
    SELECT * FROM demo_tab_root_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(db_entries). 
    out->write( db_entries ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_tab_root_5. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The class demonstrates the following:

- A successful save, i.e. the interaction phase and the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) have been processed successfully. Two [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) are created. A `COMMIT ENTITIES` statement triggers the save sequence. The value of `sy-subrc` is displayed after the commit. During the execution of the method implementation code in the ABP, an internal table is populated that stores the following information: position of the method call sequence, name of the method, if there is an error, a flag for the interaction, early, or late save phase. This table is displayed as well as the entries of the database table as a result of the RAP create operation.

- Failure in the `finalize` method: An instance is created. The same steps are taken as described above. In this case, the failure in the `finalize` method triggers the call of the `cleanup_finalize` method. `sy-subrc` is set to 4 after the commit. There is then another RAP create operation on the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md). This time, the RAP transaction is completed with a successful save.

- Failure in the `check_before_save` method: The steps are the same as described above. A failure also triggers the `cleanup_finalize` method. In all other examples, this method is not called. It is only called if an error occurs in the `finalize` or `check_before_save` method.

- Rollback. This example has no `COMMIT ENTITIES` statement. The purpose is to demonstrate that the `ROLLBACK ENTITIES` statement only triggers the call of the `cleanup` method in the [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md).

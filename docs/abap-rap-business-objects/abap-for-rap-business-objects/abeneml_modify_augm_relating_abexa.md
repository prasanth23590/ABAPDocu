---
title: "ABAP EML - MODIFY AUGMENTING, RELATING TO"
source_file: abeneml_modify_augm_relating_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP EML - Providing RAP BOs > ABAP EML - MODIFY AUGMENTING ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY AUGMENTING, RELATING TO

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the ABAP EML `MODIFY` statement with the additions `AUGMENTING` and `RELATING TO` with a RAP projection business object.

**Base BDEF**

The base BDEF is the managed RAP behavior definition `DEMO_MANAGED_ROOT_RELATING`.

``` abap
managed implementation in class bp_demo_managed_root_relating unique;
strict ( 2 );

define behavior for demo_managed_root_relating alias _Root
persistent table demo_tab_root_5
lock master
authorization master ( none )

{
  create;
  update ( precheck );
  delete;
  field ( readonly : update ) key_field;
}
```

**Projection BDEF**

The projection BDEF reuses the standard operations from the base BDEF and augments `update` operations.

``` abap
projection implementation in class bp_demo_managed_proj_relating unique;
strict ( 2 );

define behavior for DEMO_MANAGED_PROJ_RELATING
{
  use create;
  use update ( augment );
  use delete;
  field ( readonly ) field2;
}
```

**Behavior implementation**

For the above projection BDEF, one [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_PROJ_RELATING`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_PROJ_RELATING=CCIMP` of the behavior pool. In the behavior pool, operation augmentation is implemented in the following method:

- `augment_update`

  It does not augment an original base instance for the operation `update`. Instead, the example augmentation updates a field value of another instance. For demonstration purposes, instances are referred to using a different key value. In this case, the key value of the other instance is determined just by using the next higher integer value of the key field. A specific field is updated that will - based on specific values - intentionally fail in the precheck for the update operation in the ABAP behavior pool `BP_DEMO_MANAGED_PROJ_RELATING`. The update is rejected if the field `field2` has the value `up2` and `up3`. Failed and reported messages are then added. To relate the augment instances to original instances, variable of type `ABP_BEHV_RELATING_TAB` is filled.

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
CLASS cl_demo_rap_eml_augm_relating DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs, 
      select_from_db_and_display, 
      display_early_responses IMPORTING out TYPE REF TO if_demo_output, 
      display_late_responses IMPORTING out TYPE REF TO if_demo_output. 
    DATA root_tab TYPE TABLE OF demo_tab_root_5 WITH EMPTY KEY. 
    DATA m TYPE RESPONSE FOR MAPPED EARLY demo_managed_proj_relating. 
    DATA f TYPE RESPONSE FOR FAILED EARLY demo_managed_proj_relating. 
    DATA r TYPE RESPONSE FOR REPORTED EARLY demo_managed_proj_relating. 
    DATA f_late TYPE abp_behv_response_tab. 
    DATA r_late TYPE abp_behv_response_tab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_augm_relating IMPLEMENTATION. 
  METHOD main. 
 
    "Creating RAP BO instances for update operations 
    MODIFY ENTITY demo_managed_proj_relating 
       CREATE FIELDS ( key_field field1 field3 field4 ) 
       WITH VALUE #( ( %cid = 'cid1' 
                       key_field = 1 
                       field1 = 'abc' 
                       field3 = 10 
                       field4 = 100 ) 
                     ( %cid = 'cid2' 
                       key_field = 2 
                       field1 = 'def' 
                       field3 = 20 
                       field4 = 200 ) 
                     ( %cid = 'cid3' 
                       key_field = 3 
                       field1 = 'ghi' 
                       field3 = 30 
                       field4 = 300 ) 
                     ( %cid = 'cid4' 
                       key_field = 4 
                       field1 = 'jkl' 
                       field3 = 40 
                       field4 = 400 ) 
                     ( %cid = 'cid5' 
                       key_field = 5 
                       field1 = 'mno' 
                       field3 = 50 
                       field4 = 500 ) 
                     ( %cid = 'cid6' 
                       key_field = 6 
                       field1 = 'pqr' 
                       field3 = 60 
                       field4 = 600 ) ) 
       MAPPED m 
       FAILED f 
       REPORTED r. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write( 
    `Database table entries of ROOT after the create operation:` ). 
 
    select_from_db_and_display( ). 
 
    out->line( ). 
 
********************************************************************** 
 
    out->write( `Demonstrating a working augmentation` ). 
 
    MODIFY ENTITY demo_managed_proj_relating 
           UPDATE FIELDS ( field1 ) WITH VALUE #( ( key_field = 1 
                                                    field1 = 'X' ) ) 
           FAILED f 
           REPORTED r. 
 
    display_early_responses( out ). 
 
    COMMIT ENTITIES RESPONSES FAILED f_late REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_late_responses( out ). 
 
    out->write( 
    `Database table entries of ROOT after the augmentation:` ). 
 
    select_from_db_and_display( ). 
 
    out->write( `RELATING table` 
    )->write( bp_demo_managed_proj_relating=>relates_mapping_tab ). 
 
    out->line( ). 
    ROLLBACK ENTITIES. 
 
********************************************************************** 
 
    out->write( `Demonstrating a failing augmentation (1)` ). 
 
    MODIFY ENTITY demo_managed_proj_relating 
           UPDATE FIELDS ( field1 ) WITH VALUE #( ( key_field = 2 
                                                    field1 = 'Y' ) ) 
           FAILED f 
           REPORTED r. 
 
    display_early_responses( out ). 
 
    COMMIT ENTITIES RESPONSES FAILED f_late REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_late_responses( out ). 
 
    out->write( 
    `Database table entries of ROOT after the augmentation:` ). 
 
    select_from_db_and_display( ). 
 
    out->write( `RELATING table` 
    )->write( bp_demo_managed_proj_relating=>relates_mapping_tab ). 
 
    out->line( ). 
    ROLLBACK ENTITIES. 
 
********************************************************************** 
 
    out->write( `Demonstrating a failing augmentation (2)` ). 
 
    MODIFY ENTITY demo_managed_proj_relating 
           UPDATE FIELDS ( field1 ) WITH VALUE #( ( key_field = 3 
                                                    field1 = 'Z' ) ) 
           FAILED f 
           REPORTED r. 
 
    display_early_responses( out ). 
 
    COMMIT ENTITIES RESPONSES FAILED f_late REPORTED r_late. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_late_responses( out ). 
 
    out->write( 
    `Database table entries of ROOT after the augmentation:` ). 
 
    select_from_db_and_display( ). 
 
    out->write( `RELATING table` 
    )->write( bp_demo_managed_proj_relating=>relates_mapping_tab ). 
 
    ROLLBACK ENTITIES. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
  ENDMETHOD. 
  METHOD display_early_responses. 
    IF f IS NOT INITIAL. 
      out->write( f ). 
    ENDIF. 
    IF r IS NOT INITIAL. 
      out->write( r ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD display_late_responses. 
    IF f_late IS NOT INITIAL. 
      out->write( f_late ). 
    ENDIF. 
    IF r_late IS NOT INITIAL. 
      out->write( r_late ). 
    ENDIF. 
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

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Using an ABAP EML `MODIFY` statement, multiple instances are created via the projection BO for demonstration data. Three `MODIFY` statements follow for update operations.

- First update operation:

  - An ABAP EML modify request for one instance updates one field via the projection BO. This modify request is successful, and an additional instance is updated via the augment request. The effect of the statements is demonstrated by displaying the retrieved data from the underlying database table. In case of failures, early and late failed and reported responses are displayed. The content of the table used for the `RELATING` addition is also displayed for demonstration.

- Second and third update operation:

  - These operations are similar to the first but the augment requests deliberately fail, as the prechecks are not successful. The implementation uses `MODIFY AUGMENTING` with the `RELATING TO` addition, ensuring that the augment instance relates to the original instance.

  - The relation of the augment instance to the original instance is illustrated by the example in the early failed response. The original instance with `key_field = 2` is augmented. In the augment request the instance with `key_field = 3` is updated, but the update fails due to the precheck, resulting in early failed and reported messages. The early failed response shows the relation: An issue for instance with `key_field = 2` is added, not for the instance with `key_field = 3`. The latter appears in the reported response.

  - The same applies to the third update operation. If the `MODIFY AUGMENTING` statement was used without the `RELATING TO` addition, as is hinted in the implementation with the commented out code section, relating the augment instance to the original instance would not be possible and would violate the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md).

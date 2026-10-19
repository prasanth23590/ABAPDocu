---
title: "Using %pre / %tmp / %pky"
source_file: abenderived_types_pre_tmp_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %pre / %tmp / %pky

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%pre`, `%tmp` and `%pky` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenario.

Note that this example does not cover a production business scenario for late numbering. Instead it is intended to give an idea about the use of the BDEF derived type components.

**Data model**

The CDS data model consists of the root entity `DEMO_UMANAGED_ROOT_LATE_NUM3`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_UMANAGED_ROOT_LATE_NUM3
  as select from demo_tab_root_3
  {
    key key_field,
        field1,
        field2,
        field3,
        field4
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UMANAGED_ROOT_LATE_NUM3` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class
  bp_demo_umanaged_root_late_nu3 unique;
strict(2);

define behavior for DEMO_UMANAGED_ROOT_LATE_NUM3
late numbering
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UMANAGED_ROOT_LATE_NU3`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UMANAGED_ROOT_LATE_NU3CCIMP` of the behavior pool.

The following class is relevant for the example:

- `lcl_buffer`: Constitutes the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) which is an internal table in this example. It contains all fields of the database table and further fields that are used in the example, for example, the internal table also contains the components [`%pid`](abapderived_types_pid.md) and [`%cid`](abapderived_types_cid.md). Furthermore, there are components representing flags like `changed` and `final_key_assigned`. The first one is used to flag whether an instance has been created or changed and thus should be saved. The second specifies whether final keys have been assigned to the instance.

The following methods are relevant for the example:

- `create`: Creates the instances and writes them to the transactional buffer. In this case, a `%pid` as well as a preliminary value for [`%key`](abapderived_types_key.md) is created for the instances.

- `update`: Updates instances. Here, the use cases are covered when instances are updated that already have the final keys assigned and have not.

- `prep_root_buffer`: Prepares the transactional buffer. In case of an update request on persisted instances, these instances are read from the database table into the transactional buffer.

- [`adjust_numbers`](abensaver_adjust_numbers.md): Assigns the final keys. In this simple example, the final keys are assigned integers. Furthermore, the [`MAPPED LATE`](abaptype_response_for.md), which shows `%pre` and `%tmp`, and [`REPORTED LATE`](abaptype_response_for.md) response structures are filled. For demonstration purposes, the entries for both structures are stored in two internal tables that are displayed in the output.

- The [`save`](abensaver_method_save.md), [`cleanup`](abensaver_method_cleanup.md) and [`cleanup_finalize`](abapsaver_class_cleanup_finalize.md) methods save the entries in the transactional buffer to the database table or clearing the entries respectively.

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
CLASS cl_demo_rap_drvd_types_latenu2 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: ls_mapped TYPE STRUCTURE FOR MAPPED 
                      demo_umanaged_root_late_num3, 
           BEGIN OF ls_keys, 
             pid       TYPE abp_behv_pid, 
             tmp_key   TYPE i, 
             key_field TYPE i, 
           END OF ls_keys. 
    DATA: 
      mapped_early           TYPE RESPONSE FOR MAPPED EARLY 
                               demo_umanaged_root_late_num3, 
      failed_early           TYPE RESPONSE FOR FAILED EARLY 
                               demo_umanaged_root_late_num3, 
      reported_early         TYPE RESPONSE FOR REPORTED EARLY 
                               demo_umanaged_root_late_num3, 
      lt_mapped_late_content TYPE TABLE FOR MAPPED LATE 
                               demo_umanaged_root_late_num3, 
      lt_keys                TYPE TABLE OF ls_keys. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_latenu2 IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type components: ` && 
                        `%pre / %tmp / %pky` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num3 
       CREATE FIELDS ( field1 field2 field3 field4  ) 
          WITH VALUE #( 
            ( %cid = 'cid1' field1 = 'aaa' field2 = 'bbb' 
              field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' field1 = 'bbb' field2 = 'ccc' 
              field3 = 12 field4 = 13 ) 
            ( %cid = 'cid3' field1 = 'ddd' field2 = 'eee' 
              field3 = 14 field4 = 15 ) 
            ( %cid = 'cid4' field1 = 'fff' field2 = 'ggg' 
              field3 = 16 field4 = 17 ) 
            ( %cid = 'cid5' field1 = 'hhh' field2 = 'iii' 
              field3 = 18 field4 = 19 ) 
            ( %cid = 'cid6' field1 = 'jjj' field2 = 'kkk' 
              field3 = 20 field4 = 21 ) 
 
              ) 
           MAPPED mapped_early 
           FAILED failed_early 
           REPORTED reported_early. 
 
    "Note: This is a non-draft scenario, hence, %pky can be used to 
    "refer to the preliminary keys and %pid (%pky contains %pid and 
    "%key). %tky could be used as well. It is even recommended that 
    "you use it since you are prepared for a potential switch to a 
    "draft scenario (here, %tky contains the same components as 
    "%pky, but if need be, also %is_draft). 
 
    MODIFY ENTITY demo_umanaged_root_late_num3 
     UPDATE FIELDS ( field1 field3 ) WITH VALUE #( 
          ( %pky = mapped_early-demo_umanaged_root_late_num3[ 1 ]-%pky 
            field1 = 'up1' field3 = 100 ) 
          ( %pky = mapped_early-demo_umanaged_root_late_num3[ 2 ]-%pky 
            field1 = 'up2' field3 = 200 ) 
          ( %pky = mapped_early-demo_umanaged_root_late_num3[ 3 ]-%pky 
            field1 = 'up3' field3 = 300 ) ) 
         FAILED failed_early 
         REPORTED reported_early. 
 
    COMMIT ENTITIES BEGIN RESPONSES FAILED FINAL(failed_late) 
     REPORTED FINAL(reported_late). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    LOOP AT mapped_early-demo_umanaged_root_late_num3 
      ASSIGNING FIELD-SYMBOL(<mapped_early>). 
 
      CONVERT KEY OF demo_umanaged_root_late_num3 
        FROM TEMPORARY VALUE #( %pid = <mapped_early>-%pid 
                                %tmp = <mapped_early>-%key ) 
        TO FINAL(lv_final_key). 
 
      APPEND VALUE #( %pid = <mapped_early>-%pid 
                      %tmp = <mapped_early>-%key 
                      %key = lv_final_key ) 
                      TO lt_mapped_late_content. 
    ENDLOOP. 
 
    COMMIT ENTITIES END. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(itab). 
 
    out->write( 
        `Database table entries after the operations:` 
       )->write( itab 
        ). 
 
    IF reported_late IS NOT INITIAL. 
      out->write_doc( `MAPPED LATE response:` 
        )->write( lt_mapped_late_content ). 
    ENDIF. 
 
    IF failed_late IS NOT INITIAL. 
      out->write_doc( `FAILED LATE response:` 
        )->write( failed_late ). 
    ENDIF. 
 
    IF reported_late IS NOT INITIAL. 
      out->write_doc( `REPORTED LATE response:` 
        )->write( reported_late ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

There are two ABAP EML modify requests. The first creates multiple [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) and the second updates the new instances.

In the create request, `%key` is not specified. The `create` method creates `%pid` and `%key` for the instances.

The update request includes the modification of the previously created instances that have not yet been persisted to the database. The reference to the instances is made by using `%pky`. `%pky` contains `%pid` and the preliminary keys in `%key`. Note that this is a non-draft scenario, hence, `%pky` can be used. `%tky` could be used as well. It is even recommended that you use it since you are prepared for a potential switch to a draft scenario (here, `%tky` contains the same components as `%pky` but, if need be, it also includes `%is_draft`).

The save sequence is triggered using a [`COMMIT ENTITIES`](abapcommit_entities.md) statement. In this case, the `COMMIT ENTITIES` variant is used with a `CONVERT KEY OF` statement to retrieve the preliminary keys of the instances for demonstration purposes.

The [`adjust_numbers`](abensaver_adjust_numbers.md) method assigns the final keys to the instances. In this example, the method simply adds an integer to the key. Furthermore, the internal tables in the global class mentioned above are filled demonstrating how `%pre` and `%tmp` might be addressed. Finally, the `save` method saves the instances to the database table.

The output shows three tables:

1.  A table that displays the outcome of the RAP operations, i. e. the successfully saved entries in the database table.

2.  A table showing the [`MAPPED LATE`](abaptype_response_for.md) information.

3.  A table showing the [`REPORTED LATE`](abaptype_response_for.md) information. Both mapped and reported information were filled in the course of the `adjust_numbers` method.

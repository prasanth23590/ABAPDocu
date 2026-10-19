---
title: "ABAP EML - COMMIT ENTITIES BEGIN, END with CONVERT KEY OF"
source_file: abencommit_entities_beginend_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES > Examples for ABAP EML COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - COMMIT ENTITIES BEGIN, END with CONVERT KEY OF

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the `COMMIT ENTITIES` variant `COMMIT ENTITIES ... END` including `CONVERT KEY OF` with a simple [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_UMANAGED_ROOT_LATE_NUM`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_UMANAGED_ROOT_LATE_NUM
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UMANAGED_ROOT_LATE_NUM` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class bp_demo_umanaged_root_late_num unique;
strict(2);

define behavior for DEMO_UMANAGED_ROOT_LATE_NUM
lock master
authorization master ( none )
late numbering

{
  create;
  update;
  field ( readonly ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UMANAGED_ROOT_LATE_NUM`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UMANAGED_ROOT_LATE_NUMCCIMP` of the behavior pool:

- `lcl_buffer` constitutes the transactional buffer. It includes an internal table to handle the data.

- `lhc_demo_unmanaged_root_late_nu` is the handler class of the behavior pool. The only relevant methods in this example are `create` and `update`.

- `lsc_demo_unmanaged_root_late_nu` is the saver class of the behavior pool. The methods of this class implement the actual modification of the persistent data.

**Details of the ABP**

- `lcl_buffer`

  In this local class, an internal table is constructed that serves as transactional buffer. `root_late_num_buffer` is the transactional buffer for the root entity. The underlying structured data type is built in a way that simplifies the handling of the buffer. `gty_late_num_buffer`, as the structured data type for `root_buffer`, contains all the key and data fields of the root entity's underlying CDS view with the same type. Plus, the structure includes the components `cid` and `pid` to hold the content and preliminary ID. The preliminary ID is necessary for late numbering. Plus, for a more comfortable processing of saving and deleting instances, it includes two fields (`changed` and `deleted`) acting as flags (while deleting is not relevant in this example). These flags are set in the course of modify operations, i. e. if an instance is created or changed, the `changed` field is given an `X`.

- Method `create`

  Note that the method implementation is intentionally kept simple. For example, a filling of the `REPORTED` parameter or checking if an instance already exists are not included so as not to overload the code. The method only covers the creation of `%pid` and the filling of the transactional buffer as well as the `MAPPED` response parameter. A `LOOP` statement is responsible for processing the transactional buffer with the individual instances that come in as input parameters (`entities`). In this case, the following steps are implemented: At first, a preliminary ID (`%pid`) is created for the instance that is processed. Here, it is a UUID. The transactional buffer is then filled with all the provided input including `%cid`, the new `%pid`, the data fields and a flag in the `changed` field so that the instance can be created. The keys do actually not play a role here since the final keys are not drawn until the save phase. Finally, the `MAPPED` response structure is filled with `%cid` and the new `%pid`. At this stage, the `MAPPED` response structure is of type `MAPPED EARLY`.

- Method `update`

  Note that the method implementation is intentionally kept simple. For example, a filling of the `FAILED` and `REPORTED` parameters or checking whether an instance exists are not included so as not to overload the code. The method only covers the update of fields if they are provided. This is done within a `LOOP` statement that processes the transactional buffer with the individual instances that come in as input parameters (`entities`). The implementation is done in a way that the instances to be updated are identified by the preliminary ID `%pid`. Only data fields, not the keys, are relevant. A flag is set for the `changed` field so that the instance can be updated.

- Class `lsc_demo_unmanaged_root`

  The `finalize` method deletes all the content IDs from the transactional buffer since they must not be used during the save phase. The `adjust_numbers` method assigns the real and final key value to the instance. The lines of the transactional buffer table are processed using a `LOOP` statement. In this oversimplified example, the key field is given a (dummy) value and the `MAPPED` response structure is filled. Here, the structure is typed with `MAPPED LATE`. The `save` method includes statements that are responsible for saving the instances from the transactional buffer, i. e. from the internal table `root_late_num_buffer`, to the database table (`demo_tab_root_3`). Here, an internal helper table is created to store those instances that have a flag for the `changed` field. This helper table is then used for an ABAP SQL `MODIFY` statement that finally changes the database tables with only those instances a change is intended for. The `cleanup` method clears the buffer table.

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
CLASS cl_demo_rap_eml_commit_3 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: ls_mapped TYPE STRUCTURE FOR MAPPED 
                      demo_umanaged_root_late_num, 
           BEGIN OF ls_keys, 
             pid       TYPE abp_behv_pid, 
             key_field TYPE i, 
           END OF ls_keys. 
    DATA: 
      mapped_early TYPE RESPONSE FOR MAPPED EARLY 
                    demo_umanaged_root_late_num, 
      lt_root_key  TYPE TABLE OF ls_mapped, 
      lt_keys      TYPE TABLE OF ls_keys. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_commit_3 IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY ENTITY demo_umanaged_root_late_num 
       CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
              ( %cid = 'cid1' field1 = 'A' field2 = 'B' 
                              field3 = 1 field4 = 2  ) 
              ( %cid = 'cid2' field1 = 'C' field2 = 'D' 
                              field3 = 3 field4 = 4  ) 
              ( %cid = 'cid3' field1 = 'E' field2 = 'F' 
                              field3 = 5 field4 = 6  ) 
              ) 
        MAPPED mapped_early. 
 
    MODIFY ENTITY demo_umanaged_root_late_num 
        UPDATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
( %pid = mapped_early-demo_umanaged_root_late_num[ 
  KEY cid %cid = 'cid1' ]-%pid 
  field1 = 'G' field2 = 'H' field3 = 7  field4 = 8  ) 
( %pid = mapped_early-demo_umanaged_root_late_num[ 
  KEY cid %cid = 'cid2' ]-%pid 
  field1 = 'I' field2 = 'J' field3 = 9 field4 = 10  ) 
( %pid = mapped_early-demo_umanaged_root_late_num[ 
  KEY cid %cid = 'cid3' ]-%pid field1 = 'K' field2 = 'L' 
  field3 = 11 field4 = 12  ) ). 
 
    COMMIT ENTITIES BEGIN. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    LOOP AT mapped_early-demo_umanaged_root_late_num 
      ASSIGNING FIELD-SYMBOL(<mapped_early>). 
 
      CONVERT KEY OF demo_umanaged_root_late_num 
        FROM <mapped_early>-%pid 
        TO FINAL(lv_root_key). 
      APPEND VALUE #( %pid = <mapped_early>-%pid 
                      %key = lv_root_key ) 
                      TO lt_root_key. 
 
    ENDLOOP. 
 
    COMMIT ENTITIES END. 
 
    out->begin_section( `COMMIT ENTITIES Variant: ` && 
         `COMMIT ENTITIES BEGIN ... END including CONVERT KEY OF` 
      )->write_text( `Result of CONVERT KEY OF statement:` ). 
 
    lt_keys = CORRESPONDING #( lt_root_key MAPPING pid = %pid ). 
 
    out->write( lt_keys ). 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 
    INTO TABLE @FINAL(lt_result). 
 
    out->write_text( `Database table entries after EML MODIFY ` && 
    `operations:` 
      )->write( lt_result ). 
 
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

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) from an ABAP class.

An ABAP EML `MODIFY` statement that includes a `CREATE` operation for creating new [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) is followed by an `UPDATE` operation updating these new created instances. The `MODIFY` statement with `CREATE` also includes the filling of the `MAPPED` response parameter (`mapped_early`). When the `create` method is called, this parameter is given the provided `%cid` and also `%pid`, which is created by the method. This information is used to identify the instances for the `UPDATE` operation.

The save sequence is initiated by `COMMIT ENTITIES BEGIN` and ends with `COMMIT ENTITIES END`. A `CONVERT KEY OF` statement is available, which is not necessary in this non-business related example. Yet, for showcasing purposes, the assumption is that getting the keys is indeed of interest here. Hence, the final keys that are drawn in the `adjust_numbers` method are retrieved. Since the preliminary IDs (`%pid`) are available until the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) is terminated, the conversion of the keys can be done on those `%pid` components. In the example, a `LOOP` statement processes the lines of the `MAPPED` table for the RAP BO entity. The `CONVERT KEY` statement is given the final keys of the individual instances based on the preliminary ID identifying these instances. The individual key is written to a local variable. For demonstration purposes, `%pid` and the key values are then stored in an internal table.

The output window shows the result of the `CONVERT KEY OF` statement, i. e. a table that includes `%pid` and the corresponding key values, and the instances, that are successfully saved to the database, as a result of the ABAP EML `MODIFY` operations.

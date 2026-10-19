---
title: "Using %pid"
source_file: abenderived_types_pid_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %pid

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%pid` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenario.

**Data model**

The CDS data model consists of the root entity ` DEMO_UMANAGED_ROOT_LATE_NUM`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP unmanaged, draft'
define root view entity DEMO_UNMANAGED_ROOT_DRAFT
  as select from demo_tab_root_4
  composition [1..*] of DEMO_UNMANAGED_CHILD_DRAFT as _child
  {
    key key_field,
        field1,
        field2,
        field3,
        field4,
        @Semantics.systemDateTime.lastChangedAt: true
        crea_date_time,
        @Semantics.systemDateTime.localInstanceLastChangedAt: true
        lchg_date_time,
        _child
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

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UMANAGED_ROOT_LATE_NUM`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UMANAGED_ROOT_LATE_NUMCCIMP` of the behavior pool. See more details on the implementation in the example [`COMMIT ENTITIES BEGIN, END` with `CONVERT KEY OF`](abencommit_entities_beginend_abexa.md).

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
CLASS cl_demo_rap_drvd_types_pid DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      mapped_early   TYPE RESPONSE FOR MAPPED EARLY 
                      demo_umanaged_root_late_num, 
      lt_mapped_late TYPE TABLE FOR MAPPED LATE 
                       demo_umanaged_root_late_num. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_pid IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type component: ` && 
                        `%pid` ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num 
       CREATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
              ( %cid = 'cid1' field1 = 'aaa' field2 = 'bbb' 
                              field3 = 10 field4 = 11  ) 
              ( %cid = 'cid2' field1 = 'ccc' field2 = 'ddd' 
                              field3 = 20 field4 = 21  ) 
              ( %cid = 'cid3' field1 = 'eee' field2 = 'fff' 
                              field3 = 30 field4 = 31 ) 
              ) 
        MAPPED mapped_early. 
 
    IF mapped_early IS NOT INITIAL. 
      out->write_doc( `MAPPED EARLY response:` 
        )->write( mapped_early ). 
    ENDIF. 
 
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
                      %key = lv_root_key 
                      ) 
                      TO lt_mapped_late. 
 
    ENDLOOP. 
 
    COMMIT ENTITIES END. 
 
    IF lt_mapped_late IS NOT INITIAL. 
      out->write_doc( `MAPPED LATE response:` 
        )->write( lt_mapped_late ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM demo_tab_root_3 
      INTO TABLE @FINAL(db_tab_entries). 
 
    out->write_html( 
  `<b>Database table entries after RAP operations with final keys:</b>` 
      )->write( db_tab_entries ). 
 
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

There is one ABAP EML modify request that creates several [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). Here, the keys are left empty because a preliminary ID `%pid` is assigned in the course of the `create` method in the behavior pool.

With a [`COMMIT ENTITIES BEGIN ... END`](abapemlcommit_entities_late.md) statement, which includes a [`CONVERT KEY OF`](abapconvert_key.md) statement, the instances are saved to the database table. The [`adjust_numbers`](abensaver_adjust_numbers.md) method assigns the final keys to the instances. Using the `CONVERT KEY OF` statement, the key information for the instances is retrieved.

The output shows two tables for the mapping information. The first one includes the [`MAPPED EARLY`](abaptype_response_for.md) mapping information that shows initial values for the key. The second one shows the [`MAPPED LATE`](abaptype_response_for.md) mapping information including the final keys. Note that `%tmp` is not used and relevant in this scenario, hence, `%tmp` shows initial values. Another table shows the database table entries after the create operation.

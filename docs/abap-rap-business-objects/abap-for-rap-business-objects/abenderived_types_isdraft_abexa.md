---
title: "Using %is_draft"
source_file: abenderived_types_isdraft_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %is_draft

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the draft indicator `%is_draft` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenario.

**Data model**

The CDS data model consists of the root entity ` DEMO_UNMANAGED_ROOT_DRAFT` and its child entity `DEMO_UNMANAGED_CHILD_DRAFT`. The child entity is not used in the example.

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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UNMANAGED_ROOT_DRAFT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class
  bp_demo_unmanaged_root_draft unique;
strict(2);
with draft;

define behavior for DEMO_UNMANAGED_ROOT_DRAFT
draft table demo_tab_dr_ro
lock master
total etag crea_date_time
etag master lchg_date_time
authorization master ( global, instance )
early numbering
{
  create;
  update( features : global );
  delete( features : global );
  association _child { create; with draft; }
  field ( features : instance ) field3;
  action action1;
  action action2 result [1] $self;
  action action3 parameter DEMO_CDS_ABSTRACT_DISCOUNT
      result selective [1] $self;
  factory action( precheck ) action4 [1];
  static function (authorization:none) function1
    result [1] DEMO_CDS_ABSTRACT_SUM;
  function (authorization:none) function2
    parameter DEMO_CDS_DEDUCT_DISCOUNT
    result [1] $self;
  function (authorization:none) function3
    result selective [1] $self;
  validation validation on save { field field3; }
  determination det_on_save on save { create; }
  determination det_on_modify on modify { create; }
  draft action Resume with additional implementation;
  draft action Edit with additional implementation;
  draft action Activate optimized with additional implementation;
  draft action Discard with additional implementation;
  draft determine action Prepare { determination det_on_save;
                                   validation validation; }
  field ( readonly:update ) key_field;
  field ( readonly ) crea_date_time, lchg_date_time;
}

define behavior for DEMO_UNMANAGED_CHILD_DRAFT
draft table demo_tab_dr_ch
lock dependent by _parent
etag dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly:update ) key_field, key_field_child;
  association _parent { with draft; }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UNMANAGED_ROOT_DRAFT`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UNMANAGED_ROOT_DRAFT==CCIMP` of the behavior pool. See a detailed description of the [RAP handler methods](abapmethods_for_rap_behv.md) in this topic: [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md).

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
CLASS cl_demo_rap_drvd_types_isdraft DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      mapped       TYPE RESPONSE FOR MAPPED demo_unmanaged_root_draft, 
      activate_tab TYPE TABLE FOR ACTION IMPORT 
                   demo_unmanaged_root_draft~activate. 
    METHODS: 
      initialize_dbtabs, 
      display_mapped. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_isdraft IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type component: ` && 
                        `%is_draft` ). 
 
    out->line( 
     )->next_section( `1) Creating and updating active instances` ). 
 
    "Draft indicator %is_draft is disabled. 
    MODIFY ENTITY demo_unmanaged_root_draft 
       CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' %is_draft = if_abap_behv=>mk-off 
              key_field = 1 
              field1 = 'aaa' field2 = 'bbb' 
              field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' %is_draft = if_abap_behv=>mk-off 
              key_field = 2 
              field1 = 'ccc' field2 = 'ddd' 
              field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' %is_draft = if_abap_behv=>mk-off 
              key_field = 3 
              field1 = 'eee' field2 = 'fff' 
              field3 = 30 field4 = 31 ) ) 
        "Note: For demo purposes, the key is referred to in 
        "diverse ways. All options have the same effect. 
        UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              %key-key_field = 1 ) 
              field2 = 'zzz' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              key_field = 2 ) 
              field2 = 'yyy' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              %pky-%key-key_field = 3 ) 
              field2 = 'xxx' ) 
             ) 
          FAILED   FINAL(failed) 
          REPORTED FINAL(reported) 
          MAPPED mapped. 
 
    display_mapped(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
       FROM demo_tab_root_4 
       ORDER BY key_field 
       INTO TABLE @FINAL(db_entries). 
 
    out->write_html( 
      '<b>Database table entries after RAP operations</b>' 
            )->write( data = db_entries  ). 
 
********************************************************************** 
 
    out->line( 
      )->next_section( `2) Creating draft instances` ). 
 
    "Draft indicator %is_draft is enabled. 
    MODIFY ENTITY demo_unmanaged_root_draft 
     CREATE FIELDS ( field1 field2 field3 field4 ) 
     WITH VALUE #( 
        ( %cid = 'cid4' %is_draft = if_abap_behv=>mk-on 
          key_field = 4 field1 = 'ggg' field2 = 'hhh' 
          field3 = 40 field4 = 41 ) 
        ( %cid = 'cid5' %is_draft = if_abap_behv=>mk-on 
          key_field = 5 field1 = 'iii' field2 = 'jjj' 
          field3 = 50 field4 = 51 ) 
        ( %cid = 'cid6' %is_draft = if_abap_behv=>mk-on 
          key_field = 6 field1 = 'kkk' field2 = 'lll' 
          field3 = 60 field4 = 61 ) ) 
        FAILED FINAL(failed2) 
        REPORTED FINAL(reported2) 
        MAPPED mapped. 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
    `The MAPPED responses before and after committing the` && 
    ` draft instances demonstrate the change of the ` && 
    `draft indicator flag from enabled to disabled.` ) 
       )->write_doc( `<b>a) Responses before committing the ` && 
                       `created draft instances</b>` ). 
 
    display_mapped(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_tab_dr_ro 
     ORDER BY key_field 
     INTO TABLE @FINAL(draft_parent_before_act). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_tab_root_before_act). 
 
    "Get keys for activate action. 
    LOOP AT mapped-demo_unmanaged_root_draft 
      ASSIGNING FIELD-SYMBOL(<key>). 
      APPEND VALUE #( key_field = <key>-%key-key_field ) 
                             TO activate_tab. 
    ENDLOOP. 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED mapped 
      FAILED FINAL(failed3) 
      REPORTED FINAL(reported4). 
 
    CLEAR activate_tab. 
 
    out->write_html( `<b>b) Responses of the ACTIVATE action ` && 
                     `before committing</b>` ). 
 
    display_mapped(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
      FROM demo_tab_dr_ro 
      ORDER BY key_field 
      INTO TABLE @FINAL(draft_parent_afer_act). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
      FROM demo_tab_root_4 
      ORDER BY key_field 
      INTO TABLE @FINAL(db_tab_root_after_act). 
 
    out->write_html( `<b>c) Draft and database tables</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
    `The following tables demonstrate the effect on the draft and ` && 
    `database tables. ` && 
    `The first two tables show the state ` && 
    `of the draft and database table before the activation, i. e. ` && 
    `new draft instances are created and, thus, available in the ` && 
    `draft table. The data fields are changed due to the ` && 
    `implementation in the ABAP behavior pool.` && 
    ` There have not been any changes to the database table.` && 
    ` The next two tables show the state of the draft and database` && 
    ` tables after the activation.` && 
    ` The database table now includes the former draft instances` && 
    ` that have been persisted to the database while the ` && 
    `draft table is empty.` ) 
      )->write( data = draft_parent_before_act exclude = `client` 
                name = 'Draft table before activation' 
      )->write( data = db_tab_root_before_act exclude = `client` 
                name = 'Database table before activation' 
      )->write( data = draft_parent_afer_act exclude = `client` 
                name = 'Draft table after activation' 
      )->write( data = db_tab_root_after_act exclude = `client` 
                name = 'Database table after activation' 
      ). 
  ENDMETHOD. 
  METHOD display_mapped. 
    IF mapped IS NOT INITIAL. 
      out->write_doc( `MAPPED response:` 
        )->write( mapped ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_4. 
    DELETE FROM demo_tab_child_4. 
    DELETE FROM demo_tab_dr_ro.                         "#EC CI_NOWHERE 
    DELETE FROM demo_tab_dr_ch.                         "#EC CI_NOWHERE 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

There are two ABAP EML modify requests that cover RAP modify operations:

1.  The first ABAP EML modify request covers a create operation to create new [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) and an update operation on those newly created instances. In this case, the RAP operations are executed on active instances since the draft indicator `%is_draft` is disabled for all instances. For demonstration purposes, the instances in the update operation are referred to using [`%tky`](abapderived_types_tky.md). Within `%tky`, the key is referred in different ways just to visualize the [component groups](../../abap-glossary/abencomponent_group_glosry.md). All options have the same effect and refer to the same. With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the instances are saved to the database. The output shows the database table entries as well as the mapped responses for the root entity to visualize the mapping of `%cid` and the keys, including the draft indicator.

2.  The second ABAP EML modify request covers the creation of draft instances. In this case, the draft indicator `%is_draft` is enabled for all instances. With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the draft instances are saved to the draft table. The [draft action](../rap-behavior-definitions/abenbdl_draft_action.md) `activate` which is followed by a `COMMIT ENTITIES` statement that finally saves the instances to the database table. The output shows the following:

    - Mapped responses after the RAP create operation and after the execution of the `activate` action, but before committing. It shows the change of the draft indicator, i. e. it is changed from disabled to enabled.

    - Tables are displayed that demonstrate the effect on the draft and database tables. The first two tables show the state of the draft and database table before the activation, i. e. new draft instances are created and, thus, available in the draft table. The data fields are changed due to the implementations in the ABAP behavior pool. At this stage, there have not been any changes to the database table. The next two tables show the state of the draft and database tables after the activation. The database table now includes the former draft instances that have been persisted to the database. The draft table is empty.

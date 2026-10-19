---
title: "Using %tky"
source_file: abenderived_types_tky_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %tky

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%tky` in two scenarios:

1.  a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) in a non-draft scenario

2.  a managed RAP BO in a [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenario

**Data models**

**Non-draft scenario**: The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_4` and its child entity `DEMO_MANAGED_CHILD_4`. The child entity is not used in the example.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_managed_root_4
  as select from demo_tab_root_3
  composition [1..*] of demo_managed_child_4 as _child
  {
    key key_field,
        field1,
        field2,
        field3,
        field4,
        _child
  }
```

**Draft scenario**: The CDS data model consists of the root entity `DEMO_MANAGED_DRAFT_ROOT` and its child entity `DEMO_MANAGED_DRAFT_CHILD`. The child entity is not used in the example.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP unmanaged, draft'
define root view entity DEMO_MANAGED_DRAFT_ROOT
  as select from demo_tab_root_4
  composition [1..*] of DEMO_MANAGED_DRAFT_CHILD as _child
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

**Non-draft scenario**: The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_4` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_4 unique;
strict(2);

define behavior for demo_managed_root_4
persistent table DEMO_TAB_ROOT_3
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  association _child { create; }
  field(readonly:update) key_field;
}

define behavior for demo_managed_child_4 alias _child
persistent table DEMO_TAB_CHILD_3
lock dependent by _parent
authorization dependent by _parent

{
  update;
  delete;
  field ( readonly ) key_field;
  association _parent;
  field(readonly:update) key_field_child;
}
```

**Draft scenario**: The BDEF is `DEMO_MANAGED_DRAFT_ROOT`. It is defined as follows:

``` abap
managed implementation in class bp_demo_managed_draft_root unique;
strict(2);
with draft;

define behavior for DEMO_MANAGED_DRAFT_ROOT
persistent table demo_tab_root_4
draft table demo_tab_dr_ro
lock master
total etag crea_date_time
etag master lchg_date_time
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; with draft; }
  draft action Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare;
  field ( readonly : update ) key_field;
  field ( readonly ) crea_date_time, lchg_date_time;
}

define behavior for DEMO_MANAGED_DRAFT_CHILD
persistent table demo_tab_child_4
draft table demo_tab_dr_ch
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  field ( readonly : update ) key_field_child;
  association _parent { with draft; }
}
```

**Behavior implementation**

- **Non-draft scenario**: For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_4`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_4========CCIMP` of the behavior pool. In this case, the behavior pool does not include any implementations that are relevant for the example.

- **Draft scenario**: The global class of the behavior pool is `BP_DEMO_MANAGED_DRAFT_ROOT`. The actual implementation is here: `BP_DEMO_MANAGED_DRAFT_ROOT====CCIMP`. In this case, the behavior pool does not include any implementations that are relevant for the example.

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
CLASS cl_demo_rap_drvd_types_tky DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed_info TYPE RESPONSE FOR FAILED demo_managed_root_4. 
    METHODS: 
      initialize_dbtabs, 
      display_failed. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_tky IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type component: ` && 
                        `%tky` ). 
 
    out->line( 
     )->next_section( `1) Non-draft scenario` ). 
 
    MODIFY ENTITY demo_managed_root_4 
       CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' %key-key_field = 1 
              field1 = 'aaa' field2 = 'bbb' field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' %key = VALUE #( key_field = 2 ) 
              field1 = 'ccc' field2 = 'ddd' field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' key_field = 3 
              field1 = 'eee' field2 = 'fff' field3 = 30 field4 = 31 ) 
            ( %cid = 'cid4' %data-%key-key_field = 4 
              field1 = 'ggg' field2 = 'hhh' field3 = 40 field4 = 41 ) 
            ( %cid = 'cid5' %data-key_field = 5 
              field1 = 'iii' field2 = 'jjj' field3 = 50 field4 = 51 ) ) 
          UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %tky-%key-key_field = 1 field2 = 'up1' ) 
            ( %tky-key_field = 2 field2 = 'up2' ) 
            ( %tky-%pky-%key-key_field = 3 field2 = 'up3' ) 
            ( %tky-%pky-key_field = 4 field2 = 'up4' ) 
            ( %key-key_field = 5 field2 = 'up5' ) 
            ( key_field = 6 field2 = 'up6' ) 
            ( %pky-key_field = 7 field2 = 'up7' ) 
            ( %pky-%key-key_field = 8 field2 = 'up8' ) 
            ( %data-%key-key_field = 9 field2 = 'up9' ) 
            ( %data-key_field = 10 field2 = 'up10' ) ) 
           MAPPED FINAL(mapped) 
           FAILED failed_info 
           REPORTED FINAL(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab). 
 
    display_failed(  ). 
 
    out->write_html( 
        `<b>Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab ). 
 
    out->line( 
      )->next_section( `2) Draft scenario` 
      )->write_html( 
       `<b>a) RAP operations on active RAP BO` && 
       ` instances with a draft BO (%is_draft is disabled)</b>` ). 
 
    "Draft indicator %is_draft is disabled. 
    MODIFY ENTITY demo_managed_draft_root 
       CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' %is_draft = if_abap_behv=>mk-off 
              key_field = 4 
              field1 = 'aaa' field2 = 'bbb' 
              field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' %is_draft = if_abap_behv=>mk-off 
              key_field = 5 
              field1 = 'ccc' field2 = 'ddd' 
              field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' %is_draft = if_abap_behv=>mk-off 
              key_field = 6 
              field1 = 'eee' field2 = 'fff' 
              field3 = 30 field4 = 31 ) ) 
        "Note: For demo purposes, the key is referred to in 
        "diverse ways. All options have the same effect. 
        UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              %key-key_field = 4 ) 
              field2 = 'up1' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              key_field = 5 ) 
              field2 = 'up2' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-off 
                              %pky-%key-key_field = 6 ) 
              field2 = 'up3' ) 
             ) 
          FAILED   FINAL(failed_nodraft) 
          REPORTED FINAL(reported_nodraft) 
          MAPPED FINAL(mapped_nodraft). 
 
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
 
    out->write_html( `<b>Database table entries after` && 
    ` RAP operations</b>` 
      )->write( data = db_entries ). 
 
    "Get active instances in draft table. 
    MODIFY ENTITY demo_managed_draft_root 
     EXECUTE Edit AUTO FILL CID WITH 
     VALUE #( ( %key-key_field = 4 
                %param-preserve_changes = abap_false ) 
              ( %key-key_field = 5 
                %param-preserve_changes = abap_false ) 
              ( %key-key_field = 6 
                %param-preserve_changes = abap_false ) ) 
     REPORTED FINAL(reported_edit) 
     FAILED FINAL(failed_edit) 
     MAPPED FINAL(mapped_edit). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Update draft instances. Draft indicator %is_draft is enabled. 
    MODIFY ENTITY demo_managed_draft_root 
    UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                              %key-key_field = 4 ) 
              field2 = 'up_draft1' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                              key_field = 5 ) 
              field2 = 'up_draft2' ) 
            ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                              %pky-%key-key_field = 6 ) 
              field2 = 'up_draft3' ) ) 
        FAILED FINAL(failed_draft_up) 
        REPORTED FINAL(reported_draft_up) 
        MAPPED FINAL(mapped_draft_up). 
 
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
 
 
    MODIFY ENTITY demo_managed_draft_root 
      EXECUTE Activate AUTO FILL CID WITH 
       VALUE #( ( %key-key_field = 4 ) 
                ( %key-key_field = 5 ) 
                ( %key-key_field = 6 ) ) 
      MAPPED FINAL(mapped_act) 
      FAILED FINAL(failed_act) 
      REPORTED FINAL(reported_act). 
 
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
 
    out->write_html( `<b>b) RAP operations on draft instances` && 
                     ` (%is_draft is enabled)</b>` 
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
  ` that have been persisted to the database while the draft table ` && 
  `is empty.` ) 
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
  METHOD display_failed. 
    IF failed_info IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed_info ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_child_3. 
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

There are two scenarios covered to demonstrate the use of `%tky`:

1.  **Non-draft scenario**

    - An ABAP EML modify request covers a create operation to create new [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) and an update operation on those newly created instances. In the RAP create operation, the key is specified with different options. The update operation on the newly created instances updates a specific field. The instances are referred to using `%tky` and others to demonstrate that `%tky` can also be used to refer to the keys in non-draft scenarios. See the topic [Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md) for more information. With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the instances are saved to the database. The output shows the database table entries as well as the failed messages that are returned for those instances for which an update operation cannot be executed.

2.  **Draft scenario**

    ABAP EML modify requests are covered to execute RAP operations on active and draft instances

    - **RAP operations on active instances**: An ABAP EML modify request covers a create operation to create new, active [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) and an update operation on those newly created instances. The update operation on the newly created instances update a specific field. The instances are referred to using `%tky` to demonstrate that `%tky` can also be used to refer to the keys in draft scenarios while disabling the included `%is_draft` component to execute RAP operations on active instances. A `COMMIT ENTITIES` statement saves the instances to the database. The output shows those entries.

    - **RAP operations on draft instances**: The previously created active instances are put to the draft table using the [draft action](../rap-behavior-definitions/abenbdl_draft_action.md) `edit` and the `COMMIT ENTITIES` statement that follows. Then, an update operation on those draft instances is carried out by referring to the keys with `%tky`. The draft indicator is enabled. The following `COMMIT ENTITIES` statement save the updated values in the draft table. With the draft action `activate` and a `COMMIT ENTITIES` statement, the updates done on the draft table get saved to the database. The output shows different tables to demonstrate the effect on the draft and database tables. The first two tables show the state of the draft and database table before the activation, i. e. the update on the draft instances is shown. At this stage, there have not been any changes to the database table. The next two tables show the state of the draft and database tables after the activation. The database table now includes the former draft instances that have been persisted to the database. The draft table is empty.

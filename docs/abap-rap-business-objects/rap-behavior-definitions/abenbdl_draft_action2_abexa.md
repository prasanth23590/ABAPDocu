---
title: "RAP - Draft Actions Edit, Discard, Prepare"
source_file: abenbdl_draft_action2_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - draft action > RAP - Examples of Draft Actions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Draft Actions Edit, Discard, Prepare

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the draft actions `Edit`, `Discard`, and `Prepare` are defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_MANAGED_DRAFT_ACTIONS`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP managed, draft'
define root view entity DEMO_RAP_MANAGED_DRAFT_ACTIONS
  as select from demo_dbtab_root
{
  key key_field      as KeyFieldRoot,
      data_field     as DataFieldRoot,
      char_field     as CharFieldRoot,
      @Semantics.systemDateTime.lastChangedAt: true
      crea_date_time as Timestamp,
      @Semantics.systemDateTime.localInstanceLastChangedAt: true
      lchg_date_time as LastChangedAt
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_MANAGED_DRAFT_ACTIONS` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below.

The determination `setCharField` is defined. It is executed on save whenever the field `Timestamp` is modified. It is implemented in the ABAP behavior pool and it sets the value of the field `CharFieldRoot` of the respective entity instance to 'A'.

``` abap
managed implementation in class bp_demo_rap_managed_draft_acti unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_MANAGED_DRAFT_ACTIONS alias ParentEntity
persistent table demo_dbtab_root
draft table demo_dbtab_draft
lock master
total etag Timestamp
authorization master ( none )
{
  create;
  update;
  delete;

  determination setCharField on save { field Timestamp; }

  draft action ( authorization : none ) Edit;
  draft action Activate optimized with additional implementation;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare
  { determination ( always ) setCharField; }
  field ( readonly : update ) KeyFieldRoot;
  field ( readonly ) Timestamp;
  internal draft action AdditionalSave;

  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      Timestamp     = crea_date_time;
      LastChangedAt = lchg_date_time;
    }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_MANAGED_DRAFT_ACTI`. This global class implements the local handler class `LHC_PARENTENTITY`, which contains the method `setCharField` to implement the determination. The actual implementation takes place in the `BP_DEMO_RAP_MANAGED_DRAFT_ACTICCIMP`. It sets the value of the field `CharFieldRoot` of the respective entity instance to 'A'.

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
CLASS cl_demo_rap_mngd_draft_actns DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_mngd_draft_actns IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_draft. 
    MODIFY ENTITIES OF demo_rap_managed_draft_actions 
          ENTITY parententity 
            CREATE AUTO FILL CID WITH 
            VALUE #( (  %is_draft          = if_abap_behv=>mk-off 
                   %control-keyfieldroot = if_abap_behv=>mk-on 
                   %data-keyfieldroot    = 11 ) 
                     ( %is_draft          = if_abap_behv=>mk-off 
                   %control-keyfieldroot = if_abap_behv=>mk-on 
                   %data-keyfieldroot    = 22 ) ) 
      REPORTED DATA(create_reported) 
      FAILED DATA(create_failed) 
      MAPPED DATA(create_mapped). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    DELETE FROM demo_dbtab_draft. 
    MODIFY ENTITIES OF demo_rap_managed_draft_actions 
      ENTITY parententity 
        EXECUTE edit AUTO FILL CID WITH 
        VALUE #( ( %key-keyfieldroot           = 11 
                   %param-preserve_changes = 'X' ) 
                   ( %key-keyfieldroot           = 22 
                   %param-preserve_changes = 'X' ) ) 
      REPORTED FINAL(edit_reported) 
      FAILED FINAL(edit_failed) 
      MAPPED FINAL(edit_mapped). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
         FROM demo_dbtab_draft 
         INTO TABLE @FINAL(draft_table). 
 
    SELECT * 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(root_table). 
 
    out->next_section( 'active table' 
    )->write( root_table 
     )->next_section( 'draft table after Edit' 
     )->write( draft_table ). 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_actions 
      ENTITY parententity 
        EXECUTE prepare FROM 
        VALUE #( ( %key-keyfieldroot = 11 ) 
                 ( %key-keyfieldroot = 22 ) ) 
      REPORTED FINAL(resume_reported) 
      FAILED FINAL(resume_failed) 
      MAPPED FINAL(resume_mapped). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
         FROM demo_dbtab_draft 
         INTO TABLE @FINAL(draft_table_1). 
 
    out->next_section( 'draft table after Prepare' 
    )->write( draft_table_1 ). 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_actions 
         ENTITY parententity 
        EXECUTE discard FROM 
       VALUE #( ( %key-keyfieldroot = 11 ) 
       ( %key-keyfieldroot = 22 ) ) 
     REPORTED create_reported 
     FAILED create_failed 
     MAPPED create_mapped. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
       FROM demo_dbtab_draft 
       INTO TABLE @FINAL(draft_table_2). 
 
    out->next_section( 'draft table after Discard' 
     )->write( draft_table_2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Two active BO instances are created with the statement `MODIFY ENTITIES...CREATE`.

- The draft action `Edit` is executed on both instances using `MODIFY ENTITIES...EXECUTE`. The effect is that the active instances are copied to the draft database table.

- The draft action `Prepare` is executed for the two draft instances that were copied from the persistent table to the draft table during the `Edit`. The assigned determination `setCharField` is executed and it inserts a value into field `CharFieldRoot`.

- The draft action `Discard` is executed. It deletes both instances from the draft database table.

- Using the ABAP SQL `SELECT` statement, the content of the draft and persistent tables are displayed. It can be seen that the draft action `Edit` copies the active BO instances to the draft database table. The action `Prepare` fills the field `CharFieldRoot` of the draft database table. The draft action `Discard` deletes the instances from the draft database table.

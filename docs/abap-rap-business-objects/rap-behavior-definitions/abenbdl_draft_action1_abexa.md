---
title: "RAP - Draft Action Activate"
source_file: abenbdl_draft_action1_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - draft action > RAP - Examples of Draft Actions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Draft Action Activate

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the draft action `Activate` is defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_MANAGED_DRAFT_1`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #CHECK
@EndUserText.label: 'CDS view entity, RAP managed, draft'
define root view entity DEMO_RAP_MANAGED_DRAFT_1
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_MANAGED_DRAFT_1` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It has all mandatory syntax elements required for a draft scenario:

- `with draft;` is defined in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md).

- The [draft table](../../abap-glossary/abendraft_table_glosry.md) `DEMO_DBTAB_DRAFT` is defined.

- The [total ETag](abenbdl_etag.md) field `Time stamp` is defined in the correct position, namely directly after the `lock master`

- The draft actions are defined explicitly

The draft is completely handled by the RAP framework; no implementation in the ABAP behavior pool is required.

``` abap
managed
implementation in class bp_demo_rap_managed_draft_1 unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_MANAGED_DRAFT_1 alias ParentEntity
persistent table demo_dbtab_root
draft table demo_dbtab_draft
lock master
total etag Timestamp
etag master LastChangedAt
authorization master ( none )

{
  create;
  update;
  delete;
  field ( readonly : update ) KeyFieldRoot;
  field ( readonly ) Timestamp, LastChangedAt;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;

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
CLASS cl_demo_rap_managed_activate DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_managed_activate IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_draft. 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_1 
      ENTITY parententity 
        CREATE FROM 
        VALUE #( ( %cid = 'cid1' 
                   %is_draft = if_abap_behv=>mk-on 
                   %control-keyfieldroot = if_abap_behv=>mk-on 
                   %data-keyfieldroot = 81000 
                   %control-charfieldroot = if_abap_behv=>mk-on 
                   charfieldroot = 'AAA' 
                   %control-datafieldroot = if_abap_behv=>mk-on 
                   datafieldroot = 'AAA' ) 
                 ( %cid = 'cid2' 
                   %is_draft = if_abap_behv=>mk-on 
                   %control-keyfieldroot = if_abap_behv=>mk-on 
                   %data-keyfieldroot = 81001 
                   %control-charfieldroot = if_abap_behv=>mk-on 
                   charfieldroot = 'BBB' 
                   %control-datafieldroot = if_abap_behv=>mk-on 
                   datafieldroot = 'BBB' ) ) 
        MAPPED FINAL(create_mapped) 
        FAILED FINAL(create_failed) 
        REPORTED FINAL(create_reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
      FROM demo_dbtab_draft 
      INTO TABLE @FINAL(draft_parent). 
 
    SELECT * 
      FROM demo_dbtab_root 
      INTO TABLE @FINAL(active_parent). 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_1 
    ENTITY parententity 
      EXECUTE activate AUTO FILL CID WITH 
      VALUE #( ( %key-keyfieldroot = 81000 ) 
               ( %key-keyfieldroot = 81001 ) ) 
      REPORTED FINAL(activate_reported) 
      FAILED FINAL(activate_failed) 
      MAPPED FINAL(activate_mapped). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
     FROM demo_dbtab_draft 
     INTO TABLE @FINAL(draft_parent_1). 
 
    SELECT * 
      FROM demo_dbtab_root 
      INTO TABLE @FINAL(active_parent_1). 
 
    out->next_section( 'new draft table' 
        )->write( draft_parent 
        )->next_section( 'active table' 
        )->write( active_parent 
        )->next_section( 'draft table after activation' 
        )->write( draft_parent_1 
        )->next_section( 'active table after activation' 
        )->write( active_parent_1 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Two draft instances are created with the statement `MODIFY ENTITIES...CREATE`.

- The draft action `Activate` is executed on both instances using `MODIFY ENTITIES...EXECUTE`.

- Using the ABAP SQL `SELECT` statement, the content of the draft and persistent table before and after activation is displayed. Before the activation, the draft table contains the two new draft instances. After the activation, the instances are copied to the persistent table and the content from the draft table is cleared.

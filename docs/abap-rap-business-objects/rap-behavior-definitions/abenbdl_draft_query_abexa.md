---
title: "RAP - RAP BO with DCL Access Control"
source_file: abenbdl_draft_query_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics > RAP - draft table > RAP - query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - RAP BO with DCL Access Control

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how read access control is implemented and evaluated for a RAP BO for active data and for draft data using the CDS data control language [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md).

**Data model**

The CDS data model consists of the root view entity `DEMO_RAP_MANAGED_DRAFT_QUERY`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP managed, draft'
define root view entity DEMO_RAP_MANAGED_DRAFT_QUERY
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

This CDS root view entity has the CDS DCL access condition `DEMO_RAP_DRAFT_QUERY` attached to it, which restricts read access to the active data.

CDS or DDIC source code was not found

**Draft Query View**

The following CDS view entity `DEMO_RAP_DRAFT_QUERY_VIEW` defines a draft query view. It selects all fields from a RAP draft table. It has a CDS DCL source attached to it, which defines read access restrictions for the draft data.

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity used as draft query view'
@Metadata.ignorePropagatedAnnotations: true

define view entity DEMO_RAP_DRAFT_QUERY_VIEW
  as select from demo_dbtab_draft
{
  key keyfieldroot                  as Keyfieldroot,
      datafieldroot                 as Datafieldroot,
      charfieldroot                 as Charfieldroot,
      timestamp                     as Timestamp,
      lastchangedat                 as Lastchangedat,
      draftentitycreationdatetime   as Draftentitycreationdatetime,
      draftentitylastchangedatetime as Draftentitylastchangedatetime,
      draftadministrativedatauuid   as Draftadministrativedatauuid,
      draftentityoperationcode      as Draftentityoperationcode,
      hasactiveentity               as Hasactiveentity,
      draftfieldchanges             as Draftfieldchanges
}
```

This CDS view entity has the CDS DCL access condition `DEMO_RAP_DCL_DRAFT` attached to it, which restricts read access to the draft data.

CDS or DDIC source code was not found

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_MANAGED_DRAFT_QUERY` is managed and draft-enabled. It specifies the CDS view entity `DEMO_RAP_DRAFT_QUERY_VIEW` as draft query view.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) are not implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) here.

``` abap
managed implementation in class bp_demo_rap_managed_draft_quer unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_MANAGED_DRAFT_QUERY alias RootEntity
persistent table demo_dbtab_root
draft table demo_dbtab_draft query DEMO_RAP_DRAFT_QUERY_VIEW
lock master
total etag Timestamp
authorization master ( none )

{
  create;
  update;
  delete;

  field ( readonly : update ) KeyFieldRoot;
  field ( readonly ) Timestamp;

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
CLASS cl_demo_rap_draft_query_view DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_draft_query_view IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_draft. 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_query 
           ENTITY rootentity 
           CREATE 
             FIELDS ( keyfieldroot charfieldroot ) 
              AUTO FILL CID WITH VALUE #( 
            ( %cid = 'cid1'  keyfieldroot = 1 charfieldroot = 'AAA' ) 
            ( %cid = 'cid2'  keyfieldroot = 2 charfieldroot = 'AAA' ) 
            ( %cid = 'cid3'  keyfieldroot = 3 charfieldroot = 'BBB' ) 
            ( %cid = 'cid4'  keyfieldroot = 4 charfieldroot = 'CCC' ) ) 
      REPORTED DATA(create_reported1) 
      FAILED DATA(create_failed2) 
      MAPPED DATA(create_mapped2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    READ ENTITIES OF demo_rap_managed_draft_query 
         ENTITY rootentity 
         ALL FIELDS WITH VALUE #( 
         ( %key-keyfieldroot = 1 ) 
         ( %key-keyfieldroot = 2 ) 
         ( %key-keyfieldroot = 3 ) 
         ( %key-keyfieldroot = 4 ) ) 
         RESULT FINAL(read_result) 
         FAILED FINAL(failed_result). 
 
    SELECT * 
         FROM demo_dbtab_root 
         INTO TABLE @DATA(active_table). 
 
    MODIFY ENTITIES OF demo_rap_managed_draft_query 
         ENTITY rootentity 
         CREATE AUTO FILL CID WITH 
         VALUE #( 
         ( %cid = 'cid5' 
         %is_draft = if_abap_behv=>mk-on 
         %control-keyfieldroot = if_abap_behv=>mk-on 
         %data-keyfieldroot = 11111 
         %control-charfieldroot = if_abap_behv=>mk-on 
         charfieldroot = 'AAA' ) 
 
         ( %cid = 'cid6' 
         %is_draft = if_abap_behv=>mk-on 
         %control-keyfieldroot = if_abap_behv=>mk-on 
         %data-keyfieldroot = 22222 
         %control-charfieldroot = if_abap_behv=>mk-on 
         charfieldroot = 'AAA' ) 
 
         ( %cid = 'cid7' 
         %is_draft = if_abap_behv=>mk-on 
         %control-keyfieldroot = if_abap_behv=>mk-on 
         %data-keyfieldroot = 33333 
         %control-charfieldroot = if_abap_behv=>mk-on 
         charfieldroot = 'BBB' ) 
 
         ( %cid = 'cid8' 
         %is_draft = if_abap_behv=>mk-on 
         %control-keyfieldroot = if_abap_behv=>mk-on 
         %data-keyfieldroot = 44444 
         %control-charfieldroot = if_abap_behv=>mk-on 
         charfieldroot = 'CCC' ) ) 
 
      REPORTED DATA(create_reported) 
      FAILED DATA(create_failed) 
      MAPPED DATA(create_mapped). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    READ ENTITIES OF demo_rap_managed_draft_query 
        ENTITY rootentity 
        ALL FIELDS WITH VALUE #( 
        ( %key-keyfieldroot = 11111 %is_draft = if_abap_behv=>mk-on ) 
        ( %key-keyfieldroot = 22222 %is_draft = if_abap_behv=>mk-on ) 
        ( %key-keyfieldroot = 33333 %is_draft = if_abap_behv=>mk-on ) 
        ( %key-keyfieldroot = 44444 %is_draft = if_abap_behv=>mk-on ) ) 
        RESULT FINAL(read_result_draft) 
        FAILED FINAL(failed_result_draft). 
 
    SELECT * 
    FROM demo_dbtab_draft 
    INTO TABLE @DATA(draft_table). 
 
    out->next_section( 'Active data, SQL read: full data' 
    )->write( active_table 
    )->next_section( 'Active data, EML read: DCL access control applied' 
    )->write( read_result 
    )->next_section( 'Draft table, SQL read: full data' 
    )->write( draft_table 
    )->next_section( 'draft table, EML read: DCL access control applied' 
    )->write( read_result_draft ). 
 
    "Discard draft data 
    MODIFY ENTITIES OF demo_rap_managed_draft_query 
           ENTITY rootentity 
           EXECUTE discard FROM 
           VALUE #( ( %key-keyfieldroot = 11111 ) 
           ( %key-keyfieldroot = 22222 ) 
           ( %key-keyfieldroot = 33333 ) 
           ( %key-keyfieldroot = 44444 ) ) 
 
         REPORTED create_reported 
         FAILED create_failed 
         MAPPED create_mapped. 
 
    COMMIT ENTITIES. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML and ABAP SQL**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) to access the RAP business object from an ABAP class:

- It creates four active entity instances using the EML statement [`MODIFY ENTITIES CREATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md).

- It reads these active instances, first with the EML statement [`READ ENTITIES`](../abap-for-rap-business-objects/abapread_entity_entities.md), and afterwards with ABAP SQL [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md). In the EML read, the DCL access condition is applied and the result set is filtered according to the access condition. Some data sets are filtered out. By contrast, the ABAP SQL `SELECT` displays all instances that were saved on the database.

- It creates four draft instances using the EML statement `MODIFY ENTITIES CREATE`.

- It reads these draft instances, first with the EML statement `READ ENTITIES`, and afterwards with ABAP SQL `SELECT`. In the EML read, the DCL access condition attached to the draft query view is applied and the result set is filtered according to the access condition. Some data sets are filtered out. By contrast, the ABAP SQL `SELECT` displays all instances that were saved in the RAP draft table.

- Finally, the RAP draft table is cleared using the draft action [`Discard`](abenbdl_draft_action.md).

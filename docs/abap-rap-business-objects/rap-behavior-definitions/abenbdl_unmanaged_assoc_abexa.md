---
title: "RAP - Unmanaged Association Implementation"
source_file: abenbdl_unmanaged_assoc_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations > RAP - AssocImplType"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Unmanaged Association Implementation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the unmanaged [read-by-association operation](../../abap-glossary/abenrap_rba_operation_glosry.md) and [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md) for an [intra-BO composition](../../abap-glossary/abencds_intra_bo_assoc_glosry.md) relationship.

The [CDS data model](../../abap-glossary/abencds_data_definition_glosry.md) defines an [association](../../abap-glossary/abencds_association_glosry.md) with a filter in the ON condition. Since this filter condition is not considered by the managed [RAP read-by-association operation](../../abap-glossary/abenrap_rba_operation_glosry.md) and [RAP create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md) provider, an unmanaged [association](../../abap-glossary/abencds_association_glosry.md) with a custom implementation is created.

**Data model**

The [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the BO consists of a [parent](../../abap-glossary/abenparent_entity_glosry.md) (`DEMO_RAP_UNMANAGED_ASSOC_SRC`, referred to as "source") and a [child entity](../../abap-glossary/abenchild_entity_glosry.md) (`DEMO_RAP_UNMANAGED_ASSOC_TGT`, referred to as "target").

The source entity defines two associations:

- The to-child association to the target entity.

- The same relationship from the parent to the child entity is added a second time as a regular association. This is needed as a basis for the unmanaged association in the behavior definition. The association has an on condition that filters instances where the "Filter" field value is 'A'.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Source Entity for Unmanaged Association'
@Metadata.ignorePropagatedAnnotations: true
define root view entity DEMO_RAP_UNMANAGED_ASSOC_SRC
  as select from demo_tab_ua_src as SourceEntity
  composition of exact one to many DEMO_RAP_UNMANAGED_ASSOC_TGT 
  as _ToChild
  association of exact one to many DEMO_RAP_UNMANAGED_ASSOC_TGT 
  as _ToTargetWithFilter 
  on  $projection.SourceId       = _ToTargetWithFilter.SourceId
  and _ToTargetWithFilter.Filter = 'A'
{

  key source_id             as SourceId,
      local_last_changed_at as LocalLastChangedAt,
      last_changed_at       as LastChangedAt,

      _ToChild,
      _ToTargetWithFilter
}
```

**Behavior Definition**

The association `_ToTargetWithFilter` is declared as unmanaged in the [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_UNMANAGED_ASSOC_SRC`. It is enabled for [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) and for [draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md).

...

`unmanaged association _ToTargetWithFilter { create; with draft; }`

...

**Behavior Pool**

The behavior pool `BP_DEMO_RAP_UNMANAGED_ASSOC_SR` includes the implementation of the create-by-association (cba) and read-by-association (rba) methods. Both method implementations consider the filter condition from the CDS data model.

``` abap
METHOD cba_ToTargetWithFilter. 
" Prepare an internal table for managed similar association keys, 
" convert input CBA entities into CBA-compatible structure 
  DATA keys_cbc TYPE TABLE FOR CREATE 
  demo_rap_unmanaged_assoc_src\_ToChild. 
 
  keys_cbc = CORRESPONDING #( DEEP entities_cba ). 
 
  DATA failed_targets LIKE failed-targetentity. 
  LOOP AT keys_cbc ASSIGNING FIELD-SYMBOL(<key_cbc>). 
 
    CLEAR <key_cbc>-%cid_ref. 
 
    LOOP AT <key_cbc>-%target ASSIGNING FIELD-SYMBOL(<target>). 
 
      IF <target>-%control-Filter = if_abap_behv=>mk-on. 
      " Remove all targets with Filter value different than 'A' 
        IF <target>-Filter <> 'A'. 
 
        " Record the failure for this target entity creation 
          APPEND INITIAL LINE TO failed_targets 
          ASSIGNING FIELD-SYMBOL(<failed_target>). 
          <failed_target> = VALUE #( %cid      = <target>-%cid 
          %is_draft = <target>-%is_draft 
          %fail     = VALUE 
          #( cause = if_abap_behv=>cause-unspecific ) ). 
 
        " Remove invalid target from creation list 
          DELETE <key_cbc>-%target. 
        ENDIF. 
      ELSE. 
 
      " If 'Filter' control flag is off, 
      " switch it on and set Filter='A' 
        <target>-%control-Filter = if_abap_behv=>mk-on. 
        <target>-Filter = 'A'. 
      ENDIF. 
 
    ENDLOOP. 
  ENDLOOP. 
 
" Delegates actual persistent creation of child entities 
" to managed association handler 
  MODIFY ENTITY IN LOCAL MODE demo_rap_unmanaged_assoc_src 
         CREATE BY \_ToChild 
         FROM keys_cbc 
         MAPPED mapped 
         FAILED failed 
         REPORTED reported. 
 
" Append any failed targets detected earlier 
  APPEND LINES OF failed_targets TO failed-targetentity. 
ENDMETHOD.
```abap
METHOD rba_ToTargetWithFilter. 
  DATA keys_rbc TYPE TABLE FOR READ IMPORT 
  demo_rap_unmanaged_assoc_src\_ToChild. 
  keys_rbc = CORRESPONDING #( keys_rba ). 
 
  LOOP AT keys_rbc ASSIGNING FIELD-SYMBOL(<key_rbc>). 
  " Set control flag to switch on filtering on child entities 
    <key_rbc>-%control-Filter = if_abap_behv=>mk-on. 
  ENDLOOP. 
 
" Read child entities of SourceEntity via managed association _ToChild 
  READ ENTITY IN LOCAL MODE demo_rap_unmanaged_assoc_src 
       BY \_ToChild 
       FROM keys_rbc 
       RESULT result 
       LINK DATA(link_tab) 
       FAILED failed. 
 
  LOOP AT result ASSIGNING FIELD-SYMBOL(<result_row>). 
  " Remove any child rows that do NOT have Filter='A' 
    IF <result_row>-Filter = 'A'. 
      CONTINUE. 
    ENDIF. 
  " Remove links and result rows for filtered-out entities 
    DELETE link_tab WHERE target-%tky = <result_row>-%tky. 
    DELETE result. 
  ENDLOOP. 
 
" Return filtered association links 
  association_links = CORRESPONDING #( link_tab ). 
ENDMETHOD.
```

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for Unmanaged Association CBA</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_unm_cba DEFINITION 
INHERITING FROM cl_demo_classrun 
PUBLIC 
  FINAL 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION. 
 
  PRIVATE 
SECTION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_unm_cba IMPLEMENTATION. 
  METHOD main. 
    " Clean up the DB tables before demo to start with empty tables 
    DELETE FROM demo_tab_ua_src. 
    DELETE FROM demo_tab_ua_tgt. 
 
    " Prepare a source entity instance with SourceId=1 and insert in DB 
    DATA source TYPE demo_tab_ua_src. 
    source = VALUE #( source_id = 1 ). 
    INSERT demo_tab_ua_src FROM @source. 
    COMMIT ENTITIES. 
 
    " Create target entities using unmanaged create-by-association 
    MODIFY ENTITY demo_rap_unmanaged_assoc_src 
           CREATE BY \_ToTargetWithFilter 
           FROM VALUE #( ( SourceId = source-source_id 
 
     %target  = VALUE #( ( %cid            = 'cid1' 
                           Filter          = 'A' 
                           %control-Filter = if_abap_behv=>mk-on ) 
                         ( %cid            = 'cid2' 
                           Filter          = 'B' 
                           %control-Filter = if_abap_behv=>mk-on ) 
                                    ( %cid = 'cid3' 
                                    Filter = 'A' ) ) ) ). 
 
 
    " Create target entities using managed create-by-association 
    MODIFY ENTITY demo_rap_unmanaged_assoc_src 
           CREATE BY \_ToChild 
           FROM VALUE #( ( 
            SourceId = source-source_id 
            %target  = VALUE #( ( 
            %cid     = 'cid1' 
            Filter   = 'C' 
     %control-Filter = if_abap_behv=>mk-on ) ) ) ). 
 
    " Check for errors in RAP save sequence 
    COMMIT ENTITIES. 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    " Read back target entities using read-by-association 
    READ ENTITY demo_rap_unmanaged_assoc_src 
         BY \_ToTargetWithFilter 
         ALL FIELDS WITH VALUE #( ( SourceId = source-source_id  ) ) 
         RESULT FINAL(result_rba). 
 
    out->write( result_rba ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The intention of the code example is to demonstrate the implementation of the unmanaged association operations. In the first part, three instances are to be created on the target entity via EML. The implemented create-by-association method ensures that only the instances with matching filter conditions are actually created. In the second part, the implemented read-by-association method ensures that only those instances are read that match the filter conditions.

The code example includes the following steps:

- The database tables are cleared.

- On the source table, an instance with the `source_id = 1` is created.

- With the [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md), three instances are to be created on the target entity:

  - Instance 1: `cid1, filter = 'A', %control-Filter = *on*`

  - Instance 2: ` cid2, Filter = 'B', %control-Filter = *on*`

  - Instance 3: `cid3, Filter = 'A'`

- The intention of the code example is to ensure, that instance 1 is created, since the filter condition is fulfilled. The second instance must be rejected, since the filter condition is not fulfilled. The third instance should be created with `Filter = 'A'`, as the unset `%control` causes that the value for that field is set internally by the CBA handler.

- The executable example includes another cba using the composition `_ToChild` only. The *Filter* field is filled with the value *C*. The instance is written to the database table, since the filter criterium is not applied here. The purpose of this step is also to demonstrate the RBA in the next section.

- The rba is performed through the association `_ToTargetWithFilter`. Since the association is declared unmanaged in the BDEF, the method `rba_Totargetwithstatus` in the behavior pool `BP_DEMO_RAP_UNMANAGED_ASSOC_SR` is called. Only those instances are read, where the *Filter* value is *A*.

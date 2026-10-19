---
title: "RAP - SyntaxShortForm"
source_file: abenbdl_short_syntax.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - SyntaxShortForm

## Syntax

``` abap
 ([lock][, authorization][, etag] [, changedocuments]) dependent by _Assoc  
```

## Description

The following statements can be combined:

- `lock dependent by _Assoc`

- `authorization dependent by _Assoc`

- `etag dependent by _Assoc`

- `changedocuments dependent by _Assoc`

This syntax short form can be used if the [RAP authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md), [RAP lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md), [RAP ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md), and [RAP change documents master entity](../../abap-glossary/abenrap_change_doc_master_glosry.md) are defined in the same entity which is reached via the association `_Assoc`.

Each of the components `lock`, `authorization`, `etag`, and `changedocuments` is optional but at least one of them must be specified within the parentheses.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following RAP behavior definition of type `managed` consists of four nodes. The root node is declared as lock master, authorization master, and ETag master entity. The three child nodes use the syntax short form to refer to the root entity for authorization control, locking, and optimistic concurrency control.

``` abap
managed implementation in class bp_demo_rap_extensible_root unique;
strict(2);
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

with draft;
define behavior for DEMO_RAP_EXTENSIBLE_ROOT alias Root
persistent table demo_dbtab_root
draft table demo_dbtab_exdrf
lock master
total etag Timestamp
authorization master ( instance, global )
extensible

etag master LastChangedAt
{
  create;
  update;
  delete;
  association _child { create; with draft; }

  draft action ( authorization : none ) Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare extensible;

  field(readonly:update) KeyField;
  field(readonly) Timestamp;

  mapping for demo_dbtab_root corresponding extensible
  {
    KeyField = key_field;
    DataField = data_field;
    CharField = char_field;
    CharField2 = char_field_2;
    DecField = dec_field;
    Timestamp = crea_date_time;
    LastChangedAt = lchg_date_time;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_CHILD alias Child
persistent table demo_dbtab_child
draft table demo_dbtab_exchl
(lock, etag, authorization) dependent by _parent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField;
  association _parent { with draft; }
  association _grchld { create; with draft; }

  field(readonly:update) KeyFieldChild;

  mapping for demo_dbtab_child corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    DataField = data_field;
    CharField = char_field;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_GRCHLD alias GrandChild
persistent table demo_dbtab_grchl
draft table demo_dbtab_grch
(lock,authorization,etag) dependent by _GrandParent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField, KeyFieldChild;
  association _GrandParent { with draft; }
  association _parent { with draft; }
  association _child { create; with draft; }

  field(readonly:update) KeyFieldGrchld;

  mapping for demo_dbtab_grchl corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    KeyFieldGrchld = key_field_grchld;
    DataField = data_field;
    CharField = char_field;
  }
}

define behavior for DEMO_RAP_EXTENSIBLE_GGCHLD alias GreatGrandChild
persistent table demo_dbtab_ggchl
draft table demo_dbtab_ggrch
(lock, authorization, etag) dependent by _GreatGrandParent
extensible
{
  update;
  delete;
  field ( readonly ) KeyField, KeyFieldChild, KeyFieldGrChld;
  association _GrandParent { with draft; }
  association _parent { with draft; }
  association _GreatGrandParent { with draft; }

  field(readonly:update) KeyFieldGgchld;

  mapping for demo_dbtab_ggchl corresponding extensible
  {
    KeyField = key_field;
    KeyFieldChild = key_field_child;
    KeyFieldGrchld = key_field_grchld;
    KeyFieldGgchld = key_field_ggchld;
    DataField = data_field;
    CharField = char_field;
  }
}
```

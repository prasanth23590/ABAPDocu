---
title: "RAP - RAP BO Extension Using Interface"
source_file: abenbdl_using_interface_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - using interface, Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - RAP BO Extension Using Interface

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a RAP BO extension via a RAP BO interface.

## Base RAP BO

**Data model**

The CDS data model consists of four nodes which form a hierarchical CDS composition tree. They are connected via CDS compositions.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS root view entity, extensibility demo'
define root view entity DEMO_RAP_EXTENSIBLE_ROOT
  as select from demo_dbtab_root
  composition of exact one to many DEMO_RAP_EXTENSIBLE_CHILD as _child
{
  key demo_dbtab_root.key_field      as KeyField,
      demo_dbtab_root.data_field     as DataField,
      @Consumption.hidden
      demo_dbtab_root.char_field     as CharField,
      demo_dbtab_root.char_field_2   as CharField2,
      demo_dbtab_root.dec_field      as DecField,
      demo_dbtab_root.crea_date_time as Timestamp,
      demo_dbtab_root.lchg_date_time as LastChangedAt,
      _child
}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, child'
define view entity DEMO_RAP_EXTENSIBLE_CHILD
  as select from demo_dbtab_child
  association to parent DEMO_RAP_EXTENSIBLE_ROOT   as _parent 
    on $projection.KeyField = _parent.KeyField
  composition of exact one to many DEMO_RAP_EXTENSIBLE_GRCHLD as _grchld
{
  key demo_dbtab_child.key_field       as KeyField,
  key demo_dbtab_child.key_field_child as KeyFieldChild,
      demo_dbtab_child.data_field      as DataField,
      demo_dbtab_child.char_field      as CharField,
      _parent,
      _grchld
}
```

Grandchild entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, grandchild'
@AbapCatalog.extensibility.allowNewCompositions
define view entity DEMO_RAP_EXTENSIBLE_GRCHLD
  as select from demo_dbtab_grchl
  composition of exact one to many DEMO_RAP_EXTENSIBLE_GGCHLD as _child
  association        to parent DEMO_RAP_EXTENSIBLE_CHILD  as _parent
    on  $projection.KeyField      = _parent.KeyField
    and $projection.KeyFieldChild = _parent.KeyFieldChild
  association to exact one DEMO_RAP_EXTENSIBLE_ROOT   as _GrandParent
    on  $projection.KeyField = _GrandParent.KeyField
{
  key demo_dbtab_grchl.key_field        as KeyField,
  key demo_dbtab_grchl.key_field_child  as KeyFieldChild,
  key demo_dbtab_grchl.key_field_grchld as KeyFieldGrchld,
      demo_dbtab_grchl.data_field       as DataField,
      demo_dbtab_grchl.char_field       as CharField,
      _parent,
      _GrandParent,
      _child
}
```

Great-grandchild entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Great-grandchild'
define view entity DEMO_RAP_EXTENSIBLE_GGCHLD
  as select from demo_dbtab_ggchl
  association     to parent DEMO_RAP_EXTENSIBLE_GRCHLD 
                                                  as _parent           
    on  $projection.KeyField       = _parent.KeyField
    and $projection.KeyFieldChild  = _parent.KeyFieldChild
    and $projection.KeyFieldGrchld = _parent.KeyFieldGrchld
  association     to DEMO_RAP_EXTENSIBLE_CHILD    as _GrandParent      
    on  $projection.KeyField      = _GrandParent.KeyField
    and $projection.KeyFieldChild = _GrandParent.KeyFieldChild
  association [1..1] to DEMO_RAP_EXTENSIBLE_ROOT  as _GreatGrandParent
    on  $projection.KeyField = _GreatGrandParent.KeyField
{
  key key_field        as KeyField,
  key key_field_child  as KeyFieldChild,
  key key_field_grchld as KeyFieldGrchld,
  key key_field_ggchld as KeyFieldGgchld,
      data_field       as DataField,
      char_field       as CharField,
      _parent,
      _GrandParent,
      _GreatGrandParent
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_EXTENSIBLE_ROOT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It defines a managed, draft-enabled RAP BO with multiple extension points.

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

**Behavior implementation**

For the RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_EXTENSIBLE_ROOT`, see `BP_DEMO_RAP_EXTENSIBLE_ROOT===CCIMP`. It implements the method `get_instance_authorizations` for instance authorization control. It returns information on whether update and delete operations are allowed on instances. In this example, these operations are not allowed if `CharField` has a particular value.

**Note:** This is a simple example that serves demonstration purposes.

## RAP BO Interface

**CDS data model projection**

Root node projection:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_RAP_EXT_USING_INTERFACE
  provider contract transactional_interface
  as projection on DEMO_RAP_EXTENSIBLE_ROOT
{
  key KeyField as KeyInt,
      DataField as DataInt,
      CharField as CharInt,
      DecField as DecInt,
      _child: 
        redirected to composition child DEMO_RAP_EXT_USING_INT_CHILD
}
```

Child node projection:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_EXT_USING_INT_CHILD 
as projection on DEMO_RAP_EXTENSIBLE_CHILD {
  key KeyField,
  key KeyFieldChild,
  DataField,
  CharField,
  /* Associations */
  _grchld: 
    redirected to composition child DEMO_RAP_EXT_USING_INT_GRCHLD,
  _parent: redirected to parent DEMO_RAP_EXT_USING_INTERFACE
}
```

Projection of grandchild node:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_EXT_USING_INT_GRCHLD 
as projection on DEMO_RAP_EXTENSIBLE_GRCHLD {
  key KeyField,
  key KeyFieldChild,
  key KeyFieldGrchld,
  DataField,
  CharField,
  /* Associations */
  _child: 
    redirected to composition child DEMO_RAP_EXT_USING_INT_GGCHLD,
//  _Children4Ext,
  _GrandParent: redirected to DEMO_RAP_EXT_USING_INTERFACE,
  _parent: redirected to parent DEMO_RAP_EXT_USING_INT_CHILD

}
```

Projection of great-grandchild node:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_EXT_USING_INT_GGCHLD 
as projection on DEMO_RAP_EXTENSIBLE_GGCHLD {
  key KeyField,
  key KeyFieldChild,
  key KeyFieldGrchld,
  key KeyFieldGgchld,
  DataField,
  CharField,
  /* Associations */
  _GrandParent: redirected to DEMO_RAP_EXT_USING_INT_CHILD,
  _GreatGrandParent: redirected to DEMO_RAP_EXT_USING_INTERFACE,
  _parent: redirected to parent DEMO_RAP_EXT_USING_INT_GRCHLD
}
```

**RAP interface behavior definition**

The following interface BDEF projects the base RAP BO.

``` abap
interface;
use draft;
extensible;
use side effects;

define behavior for DEMO_RAP_EXT_USING_INTERFACE alias RootInterface
{
  use create;
  use update;
  use delete;

  use action Edit;
  use action Activate;
  use action Discard;
  use action Resume;
  use action Prepare;

  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_CHILD alias ChildInterface
{
  use update;
  use delete;

  use association _parent { with draft; }
  use association _grchld { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_GRCHLD alias GrandChildInterface
{
  use update;
  use delete;

  use association _GrandParent { with draft; }
  use association _parent { with draft; }
  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_USING_INT_GGCHLD alias GreatGrandChildInterface
{
  use update;
  use delete;

  use association _GrandParent { with draft; }
  use association _parent { with draft; }
  use association _GreatGrandParent { with draft; }
}
```

## BDEF Extension

The BDEF extension `DEMO_RAP_EXT_USING_INTERF` extends the RAP BO via its interface. It addresses the root node by its interface name, `RootInterface`. It adds one extension action to the RAP BO.

``` abap
extension using interface DEMO_RAP_EXT_USING_INTERFACE
 implementation in class bp_demo_rap_ext_using_interf unique;

extend behavior for RootInterface {

action (authorization : instance) SetValue_ext;

}

extend behavior for ChildInterface {
}

extend behavior for GrandChildInterface {
}

extend behavior for GreatGrandChildInterface {
}
```

**Extension ABP**

The extension action `setValue_ext` is implemented in the extension ABP, see `BP_DEMO_RAP_EXT_USING_INTERF==CCIMP`. When executed, it changes the value of field `CharInt`.

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
CLASS cl_demo_rap_ext_via_interface DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_ext_via_interface IMPLEMENTATION. 
  METHOD main. 
 
    "Empty tables 
    DELETE FROM demo_dbtab_root. 
 
    MODIFY ENTITIES OF demo_rap_ext_using_interface 
    ENTITY rootinterface 
    CREATE FIELDS ( keyint dataint charint ) 
    WITH VALUE #( ( %cid = 'cid1' 
                    keyint = 1 
                    dataint = `aaa` 
                    charint = 'AAA' ) 
                    ( %cid = 'cid2' 
                    keyint = 2 
                    dataint = `bbb` 
                    charint = 'BBB' )  ) 
     MAPPED FINAL(mapped) 
     FAILED DATA(failed) 
     REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field, char_field 
    FROM  demo_dbtab_root 
    INTO TABLE @FINAL(create_root). 
 
    MODIFY ENTITIES OF demo_rap_ext_using_interface 
      ENTITY rootinterface 
      EXECUTE setvalue_ext 
      FROM VALUE #( ( keyint = 1 ) ) 
      FAILED failed 
      REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field, char_field 
      FROM  demo_dbtab_root 
      INTO TABLE @FINAL(action_setvalue_ext). 
 
    "Display 
    out->next_section( 'CREATE (root entity)' 
            )->write( create_root 
            )->next_section( 'Execute action' 
            )->write( action_setvalue_ext ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses ABAP SQL and [ABAP EML](../../abap-glossary/abeneml_glosry.md) to access the RAP BO interface from an ABAP class and performs the following steps:

- It creates two instances of the root entity.

- It executes the action `setValue_ext` for one of the instances.

- The content of the database table after the create operation and after the action is displayed.

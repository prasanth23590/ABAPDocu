---
title: "RAP - Node Extension"
source_file: abenbdl_assoc_ext_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - Extension Entity Behavior Definition > RAP - ancestor association"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Node Extension

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to add an extension node with behavior to a RAP BO.

## Original RAP BO

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

## Extension RAP BO

**CDS data model extension**

One extension node is added to the RAP BO on the hierarchy level of the great-grandchild: `DEMO_RAP_EXTENSIBLE_EXT`. It defines associations to all four original nodes.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, extension node'
define view entity DEMO_RAP_EXTENSIBLE_EXT
  as select from demo_ggchl_ex_ba
  association        to parent DEMO_RAP_EXTENSIBLE_GRCHLD 
                                                  as _parent            
    on  $projection.Keyfield       = _parent.KeyField
    and $projection.Keyfieldchild  = _parent.KeyFieldChild
    and $projection.Keyfieldgrchld = _parent.KeyFieldGrchld
  association        to DEMO_RAP_EXTENSIBLE_GGCHLD
                                                  as _Sibling4          
    on  $projection.Keyfield       = _Sibling4.KeyField
    and $projection.Keyfieldchild  = _Sibling4.KeyFieldChild
    and $projection.Keyfieldgrchld = _Sibling4.KeyFieldGrchld
    and $projection.Keyfieldggchld = _Sibling4.KeyFieldGgchld
  association [1..1] to DEMO_RAP_EXTENSIBLE_ROOT  as _GreatGrandParent1
    on  $projection.Keyfield = _GreatGrandParent1.KeyField
  association        to DEMO_RAP_EXTENSIBLE_CHILD as _GrandParent2      
    on  $projection.Keyfield      = _GrandParent2.KeyField
    and $projection.Keyfieldchild = _GrandParent2.KeyFieldChild
{
  key key_field                      as Keyfield,
  key key_field_child                 as Keyfieldchild,
  key key_field_grchld                as Keyfieldgrchld,
  key key_field_ggchld                as Keyfieldggchld,
      data_field                     as Datafield,
      char_field                     as Charfield,
      _GreatGrandParent1.Timestamp   as Timestamp,

      _parent,
      _Sibling4,
      _GreatGrandParent1,
      _GrandParent2
}
```

The direct parent entity of the extension node `DEMO_RAP_EXTENSIBLE_GRCHLD` is extended. The extension defines and exposes a to-child association to the extension node.

``` abap
extend view entity DEMO_RAP_EXTENSIBLE_GRCHLD with
composition of exact one to many DEMO_RAP_EXTENSIBLE_EXT as _Children4Ext 
 {
  _Children4Ext
}
```

**BDEF extension**

The BDEF extension `DEMO_RAP_EXTENSION_1` adds the extension node to the RAP BO. It adds behavior to the extension node with the `define behavior for` syntax. It uses the syntax `ancestor association` for all associations except the one that leads to the direct parent node.

``` abap
extension using interface demo_rap_ext_using_interface;
foreign entity demo_rap_factory_ACTION;
extend behavior for GrandChildInterface
{
  association _Children4Ext { create; with draft; }
}

define behavior for DEMO_RAP_EXTENSIBLE_EXT alias ExtNode
  using DEMO_RAP_EXT_USING_INT_EXT
persistent table demo_ggchl_ex_ba
draft table demo_ggrch_ext
etag master Timestamp
( lock, authorization ) dependent

{
  update;
  delete;
  field ( readonly )
  KeyField, KeyFieldchild, Keyfieldgrchld;

  field ( readonly : update ) Keyfieldggchld;
  field ( readonly ) Timestamp;

  association _parent { with draft; }
  association _Sibling4 { with draft; }
  ancestor association _GrandParent2 { with draft; }
  ancestor association _GreatGrandParent1 { with draft; }

  mapping for demo_ggchl_ex_ba
  {
    Keyfield = key_field;
    Keyfieldchild = key_field_child;
    Keyfieldgrchld = key_field_grchld;
    Keyfieldggchld = key_field_ggchld;
    Datafield = data_field;
    Charfield = char_field;
    Timestamp = timestamp;
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
CLASS cl_demo_rap_node_extension DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_node_extension IMPLEMENTATION. 
  METHOD main. 
 
    "Empty tables 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_exdrf. 
    DELETE FROM demo_dbtab_child. 
    DELETE FROM demo_dbtab_exchl. 
    DELETE FROM demo_dbtab_grchl. 
    DELETE FROM demo_dbtab_grch. 
    DELETE FROM demo_dbtab_ggchl. 
    DELETE FROM demo_dbtab_ggrch. 
    DELETE FROM demo_ggchl_ex_ba. 
    DELETE FROM demo_ggrch_ext. 
 
    "Deep Create 
    MODIFY ENTITIES OF demo_rap_ext_using_interface 
    ENTITY RootInterface 
    CREATE FIELDS ( KeyInt DataInt CharInt DecInt ) 
    WITH VALUE #( ( %cid = 'cid1' 
                    KeyInt = 1 
                    DataInt = 'aaa' 
                    CharInt = 'AAA' 
                    DecInt = 500 ) ) 
 
     CREATE BY \_child FIELDS ( KeyFieldChild DataField CharField ) 
     WITH VALUE #( ( %cid_ref = 'cid1' 
                     %target = VALUE #( ( %cid = 'cid2' 
                                          KeyFieldChild = 11 
                                          DataField = 'child' 
                                          CharField = 'BBB' ) ) ) ) 
 
     ENTITY ChildInterface 
     CREATE BY \_grchld FIELDS ( KeyFieldGrchld DataField CharField ) 
     WITH VALUE #( ( %cid_ref = 'cid2' 
                     %target = VALUE #( ( %cid = 'cid3' 
                                          KeyFieldGrchld = 111 
                                          DataField = 'grandchild' 
                                          CharField = 'CCC'  ) ) ) ) 
 
     ENTITY GrandChildInterface 
     CREATE BY \_child FIELDS ( KeyFieldGgchld DataField CharField ) 
     WITH VALUE #( ( %cid_ref = 'cid3' 
                     %target = VALUE #( ( %cid = 'cid4' 
                                          KeyFieldGgchld = 1111 
                                          DataField = 'greatgrandchild' 
                                          CharField = 'eee'  ) ) ) ) 
 
     ENTITY GrandChildInterface 
     CREATE BY \_Children4Ext 
     FIELDS ( Keyfieldggchld DataField CharField ) 
     WITH VALUE #( ( %cid_ref = 'cid3' 
                     %target = 
                     VALUE #( ( %cid = 'cid5' 
                                Keyfieldggchld = 1111 
                                DataField = 'extension' 
                                CharField = 'extension'  ) ) ) ) 
     MAPPED DATA(mapped) 
     FAILED DATA(failed) 
     REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    MODIFY ENTITIES OF demo_rap_ext_using_interface 
    ENTITY ExtNode 
    UPDATE 
    FIELDS ( Datafield ) WITH VALUE #( ( KeyField = 1 
                               Keyfieldchild = 11 
                               Keyfieldgrchld = 111 
                               Keyfieldggchld = 1111 
                               DataField = 'update' ) ) 
                    MAPPED mapped 
                    FAILED failed 
                    REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(root_tab). 
    SELECT * 
    FROM demo_dbtab_child 
    INTO TABLE @FINAL(child_tab). 
    SELECT * 
    FROM demo_dbtab_grchl 
    INTO TABLE @FINAL(grandchild_tab). 
    SELECT * 
    FROM demo_dbtab_ggchl 
    INTO TABLE @FINAL(greatgrandchild_tab). 
    SELECT * 
    FROM demo_ggchl_ex_ba 
    INTO TABLE @FINAL(extension_node). 
 
    "Display 
    out->next_section( 'CREATE (root entity)' 
            )->write( root_tab 
            )->next_section( 'CREATE BY assoc (child entity)' 
            )->write( child_tab 
            )->next_section( 'CREATE BY assoc (grandchild)' 
            )->write( grandchild_tab 
            )->next_section( 'CREATE BY assoc (great-grandchild)' 
            )->write( greatgrandchild_tab 
            )->next_section( 'CREATE BY assoc (extension node)' 
            )->write( extension_node ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses ABAP SQL and [ABAP EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) from an ABAP class and performs the following steps:

- It performs a deep create, that means, it creates an instance of each entity of the composition tree, including the extension node.

- It performs an update operation on the extension node. The instance authorization control for update operations, which is implemented in the ABP of the extended RAP BO, is checked and the update operation succeeds.

- All five database tables used to store the entity data are displayed.

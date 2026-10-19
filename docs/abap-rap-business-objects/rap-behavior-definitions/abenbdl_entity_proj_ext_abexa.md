---
title: "RAP - BDEF Projection Extension, Node Extension"
source_file: abenbdl_entity_proj_ext_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Projection Extension > RAP - extension for projection"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BDEF Projection Extension, Node Extension

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the behavior of a projection BDEF is extended by means of a projection BDEF extension.

## Original Base RAP BO

**Data model**

The CDS data model consists of one root node without child entities:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, beh ext'
@AbapCatalog.extensibility.allowNewCompositions: true
define root view entity DEMO_RAP_BEH_EXT
  as select from demo_dbtab_field

{
  key key_field,
      char_field1,
      int_field1,
      int_field2
}
```

**CDS transactional interface**

The following [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is created for the root node to fulfill the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md) requirements for [RAP extensibility](../../abap-glossary/abenrap_extensibility_glosry.md).

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.extensibility.allowNewCompositions: true
define root view entity DEMO_RAP_BEH_EXT_INT 
provider contract transactional_interface
as projection on DEMO_RAP_BEH_EXT as RootInterface
{
  key key_field,
  char_field1,
  int_field1,
  int_field2
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_BEH_EXT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It defines implementation-relevant components and extension points.

``` abap
managed implementation in class bp_demo_rap_beh_ext unique;
strict(2);
extensible { with determinations on modify; }
with privileged mode disabling ac_base;
define behavior for DEMO_RAP_BEH_EXT
persistent table DEMO_DBTAB_FIELD
lock master
authorization master ( global )
extensible
{
  create;
  update (features:instance);
  delete;

  validation Limit on save { create; }
  field(readonly:update) key_field;
}
define authorization context ac_base
{ 'AUTHOBJ1'; }

define own authorization context by privileged mode;
```

**Behavior implementation**

For the RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_BEH_EXT`, see `BP_DEMO_RAP_BEH_EXT===========CCIMP`. This global class implements the following methods:

- `get_instance_features`: Instance feature control for the standard operation `update`. If the value of field `int_field1` is more than 50, updates are not allowed. If the value is equal to or smaller than 50, updates are allowed.

- `get_global_authorizations`: Global authorization control defines that create, update, and delete are always allowed.

- `Limit`: Validation that checks the value of field `int_field2`. If the value is greater than 500, the validation fails and the entity instance is not saved.

**Interface BDEF**

The following [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md) `DEMO_RAP_BEH_EXT_INT` is required as stable interface for extensions.

``` abap
interface;
extensible;

define behavior for DEMO_RAP_BEH_EXT_INT alias RootInterface
{
  use create;
  use update;
  use delete;
}
```

## Extension RAP BO

**Data model extension**

A child node is added to the RAP BO:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, beh ext'
define view entity DEMO_RAP_BEH_EXT_CHILD
  as select from demo_dbtab_fi_ch
  association to parent DEMO_RAP_BEH_EXT as _parent 
    on $projection.key_field = _parent.key_field
{
  key key_field,
  key key_field_child,
      char_field1,
      int_field1,
      int_field3,
      _parent
}
```

A CDS transactional interface is created for the child node to fulfill the RAP BO contract requirements for RAP extensibility.

``` abap
@EndUserText.label: 'CDS interface child'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_BEH_EXT_INT_CH 
as projection on DEMO_RAP_BEH_EXT_CHILD
{
  key key_field,
  key key_field_child,
  char_field1,
  int_field1,
  int_field3,
  /* Associations */
  _parent: redirected to parent DEMO_RAP_BEH_EXT_INT
}
```

A [to-child association](../../abap-glossary/abento_parent_association_glosry.md) is added to the root node via a CDS view entity extension on the base layer:

``` abap
extend view entity DEMO_RAP_BEH_EXT with 
composition of exact one to many DEMO_RAP_BEH_EXT_CHILD as _child
{
  _child
}
```

The same to-child association is also added on the interface layer:

``` abap
extend view entity DEMO_RAP_BEH_EXT_INT with 
{
RootInterface._child:
  redirected to composition child DEMO_RAP_BEH_EXT_INT_CH
}
```

**Behavior extension**

The BDEF extension `DEMO_RAP_BEH_EXT_CH` extends the root node and defines behavior for the extension child node via the BDEF interface layer.

``` abap
extension using interface DEMO_RAP_BEH_EXT_INT
implementation in class bp_demo_rap_beh_ext_ch unique;

extend behavior for RootInterface
{

  association _child { create; }

  action ( features : global, authorization : global ) setValue
    result [1] $self;
}

define behavior for DEMO_RAP_BEH_EXT_CHILD alias ChildInterface
using DEMO_RAP_BEH_EXT_INT_CH
persistent table demo_dbtab_fi_ch
( lock, authorization ) dependent
{
  update;
  delete;
  field ( readonly ) key_field;
  field ( readonly ) key_field_child;
  association _parent;
  determination myDet on modify { field int_field3; }
  action ( authorization : global ) ActionExt;
}
```

**ABP extension**

The ABP extension is implemented in the global class `BP_DEMO_RAP_BEH_EXT_CH`, see `BP_DEMO_RAP_BEH_EXT_CH========CCIMP`. This global class implements the following methods:

- **Extension of the parent entity**

  - `get_global_features`: Global feature control for the action `setValue`. This action can only be executed in the time period between 6 am and 10 pm (day shift).

  - `get_global_authorizations`: The original RAP BO defines global authorization control. RAP BO operations added via an extension require their own implementation of the global authorization control. This method generally allows execution of the method `setValue`. There are no access restrictions.

  - `setValue`: Action that sets field `int_field2` to value *888*.

- **Extension entity behavior definition for the child entity**

  - `get_global_authorizations`: The original RAP BO defines global authorization control. For the action `ActionExt`, defined in the child node, a separate implementation of the authorization control method is required. The implementation generally allows execution of the method `ActionExt`. There are no access restrictions.

  - `myDet`: Determination on modify. Sets the value of field `int_field1` to *777*.

  - `ActionExt`: Action that updates field `char_field1` for all requested entity instances.

## Projection Layer

**Data model projection**

Projection of the root node:

``` abap
@EndUserText.label: 'CDS root pv, RAP extensibility'
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.extensibility.allowNewCompositions: true
define root view entity demo_rap_proj_ext_beh 
provider contract transactional_query
as projection on DEMO_RAP_BEH_EXT {
  key key_field,
  char_field1,
  int_field1,
  int_field2

}
```

Projection of the child node:

``` abap
@EndUserText.label: 'CDS pv child,RAP projection extension'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_PROJ_EXT_BEH_CH
  as projection on DEMO_RAP_BEH_EXT_CHILD
{
  key key_field,
  key key_field_child,
      char_field1,
      int_field1,
      int_field3,
        _parent: redirected to parent demo_rap_proj_ext_beh 
}
```

View entity extension `DEMO_RAP_VE_EXTENSION` that establishes a to-child association between original root node and extended child node:

``` abap
extend view entity demo_rap_proj_ext_beh with {
  /* Associations */
  _child : redirected to composition child DEMO_RAP_PROJ_EXT_BEH_CH
}
```

**Behavior Projection**

The projection BDEF defines behavior for the root node. It declares the root node as extensible and exposes the RAP BO standard operations.

``` abap
projection;
strict(2);
extensible;

define behavior for demo_rap_proj_ext_beh alias Root
extensible
{
  use create;
  use update;
  use delete;
}
```

**BDEF projection extension**

The BDEF projection extension `DEMO_RAP_PROJ_EXT_BEH_1` extends the root node and defines behavior for the extension child node.

``` abap
extension for projection;

extend behavior for Root
//authorization (global)
{
  use association _child {create;}
  use action setValue;

//  mapping for demo_rap_struc corresponding;
}

define behavior for DEMO_RAP_PROJ_EXT_BEH_CH alias Child
{
  use association _parent;
  use action ActionExt;
  field ( readonly ) int_field3;
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
CLASS cl_demo_rap_proj_ext DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_proj_ext IMPLEMENTATION. 
  METHOD main. 
    "Empty tables 
    DELETE FROM demo_dbtab_field. 
    DELETE FROM demo_dbtab_fi_ch. 
    CLEAR bp_demo_unmanaged_root_draft=>handlers_called. 
 
    "Deep Create 
    MODIFY ENTITIES OF demo_rap_proj_ext_beh 
    ENTITY root 
    CREATE FIELDS ( key_field char_field1 int_field1 int_field2 ) 
    WITH VALUE #( ( %cid = 'cid1' 
                    key_field = '12AB111AABBCC334' 
                    char_field1 = 'A' 
                    int_field1 = 51 
                    int_field2 = 11 ) 
                    ( %cid = 'cid2' 
                    key_field = '1111111122222222' 
                    char_field1 = 'B' 
                    int_field1 = 10 
                    int_field2 = 500 )  ) 
 
     CREATE BY \_child FIELDS ( char_field1 int_field1 ) 
     WITH VALUE #( ( %cid_ref = 'cid1' 
                     %target = VALUE #( ( 
                       %cid = 'cid3' 
                       key_field_child = 11 
                       char_field1 = 'AA' 
                       int_field1 = 10 
                       int_field3 = 100 ) ) ) 
                 ( %cid_ref = 'cid2' %target = VALUE #( ( %cid = 'cid4' 
                   key_field_child = 22 
                   char_field1 = 'BB' 
                   int_field1 = 11 
                   int_field3 = 200 ) ) ) ) 
     MAPPED DATA(mapped) 
     FAILED DATA(failed) 
     REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field1, int_field1, int_field2 
    FROM  demo_dbtab_field 
    INTO TABLE @FINAL(create_parent). 
    SELECT key_field, char_field1, int_field1 
    FROM  demo_dbtab_fi_ch 
    INTO TABLE @FINAL(create_child). 
 
 
******* UPDATE: only allowed if int_field1 <= 50. feature control****** 
    MODIFY ENTITIES OF demo_rap_proj_ext_beh 
        ENTITY root 
        UPDATE 
        FIELDS ( char_field1  ) 
        WITH VALUE #( ( key_field = '12AB111AABBCC334' 
                                   char_field1 = 'update' 
                                    ) 
                                    ( key_field = '1111111122222222' 
                                   char_field1 = 'update' 
                                    ) 
                                     ) 
                        MAPPED mapped 
                        FAILED failed 
                        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field1, int_field1, int_field2 
    FROM  demo_dbtab_field 
    INTO TABLE @FINAL(update_parent). 
 
    MODIFY ENTITIES OF demo_rap_proj_ext_beh 
      ENTITY root 
      EXECUTE setvalue 
      FROM VALUE #( ( key_field = '1111111122222222' ) ) 
 
      RESULT FINAL(result) 
      FAILED failed 
      REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field1, int_field1, int_field2 
    FROM  demo_dbtab_field 
    INTO TABLE @FINAL(action_setvalue). 
 
    MODIFY ENTITIES OF demo_rap_proj_ext_beh 
        ENTITY child 
        EXECUTE actionext 
        FROM VALUE #( ( key_field = '12AB111AABBCC334' 
                        key_field_child = 11 ) ) 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, char_field1, int_field1 
    FROM  demo_dbtab_fi_ch 
    INTO TABLE @FINAL(action_actionext). 
 
    "Display 
    out->next_section( 'CREATE (root entity)' 
            )->write( create_parent 
            )->next_section( 'CREATE BY assoc (child entity)' 
            )->write( create_child 
            )->next_section( 'UPDATE (root entity)' 
            )->write( update_parent 
            )->next_section( 'EXECUTE action SetValue' 
            )->write( action_setvalue 
            )->next_section( 'EXECUTE action ActionExt' 
            )->write( action_actionext 
            )->write_html( '<b>Handler methods called</b>' 
            )->write( data = bp_demo_rap_beh_ext=>handlers_called 
               name = 'Handler methods log table' ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [ABAP EML](../../abap-glossary/abeneml_glosry.md) to access the projection BO from an ABAP class:

- It inserts two parent entity instances and two child entity instances.

- It updates the two parent entity instances

- It executes the action `setValue` from the projection extension.

- It executes the action `ActionExt` from the extension to the original base RAP BO.

The screen output includes a table that lists the execution order of handler methods of the ABAP behavior pool. This shows which methods in which order are executed when accessing the RAP BO.

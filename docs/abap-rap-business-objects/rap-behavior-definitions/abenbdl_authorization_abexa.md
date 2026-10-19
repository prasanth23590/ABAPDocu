---
title: "RAP - Global Authorization"
source_file: abenbdl_authorization_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics > RAP - Authorization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Global Authorization

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a global authorization check is defined, implemented, and consumed in an unmanaged RAP BO.

**Note:** This example is meant for documentation purposes only. It is not intended for direct use in a production system. It can use demo artifacts that are not [released as APIs](../../abap-glossary/abenreleased_api_glosry.md) for use in [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_UNMANAGED_AUTH` and its child entity `DEMO_RAP_UNMANAGED_AUTH_CHILD`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP unmanaged, auth'
define root view entity DEMO_RAP_UNMANAGED_AUTH
  as select from demo_dbtab_root
  composition [1..*] of DEMO_RAP_UNMANAGED_AUTH_CHILD as _child
  association [1..1] to DEMO_RAP_MANAGED_ASSOC_EXT   as _ext
    on $projection.KeyFieldRoot = _ext.KeyFieldExt
{
  key key_field      as KeyFieldRoot,
      data_field     as DataFieldRoot,
      char_field     as CharFieldRoot,
      dec_field      as DecFieldRoot,
      @Semantics.systemDateTime.lastChangedAt: true
      crea_date_time as Timestamp,
      @Semantics.systemDateTime.localInstanceLastChangedAt: true
      lchg_date_time as LastChangedAt,
      _child,
      _ext
}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED            
@EndUserText.label: 'CDS view entity, RAP unmanaged, auth'
define view entity DEMO_RAP_UNMANAGED_AUTH_CHILD
  as select from demo_dbtab_child
  association to parent DEMO_RAP_UNMANAGED_AUTH as _parent 
  on $projection.KeyField = _parent.KeyFieldRoot
{
  key key_field       as KeyField,
  key key_field_child as KeyFieldChild,
      data_field      as DataFieldChild,
      _parent
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_UNMANAGED_AUTH` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It defines the root view entity as [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and the child entity as authorization dependent entity.

``` abap
unmanaged implementation in class bp_demo_rap_unmanaged_auth unique;
strict(2);

define behavior for DEMO_RAP_UNMANAGED_AUTH
lock master
authorization master (global)
{
  create;
  update;
  delete;
  field ( readonly:update ) KeyFieldRoot;
  association _child {create;}
}

define behavior for DEMO_RAP_UNMANAGED_AUTH_CHILD
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;

  field ( readonly:update ) KeyField, KeyFieldChild;

  association _parent { }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_UNMANAGED_AUTH`. This global class implements the method `get_global_auth` for global authorization control (see `BP_DEMO_RAP_UNMANAGED_AUTH====CCIMP`). It works as follows:

- For incoming update requests, authorization is always granted.

- For incoming delete requests, authorization is always rejected and an error message is written into the [`REPORTED`](../abap-for-rap-business-objects/abapeml_response.md) structure.

  **Note:** This example is intentionally kept short and simple and serves demonstration purposes only. A realistic implementation requires an instance-independent authorization check, for example, based on authorization objects.

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
CLASS cl_demo_rap_unmanaged_auth DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_unmanaged_auth IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_child. 
 
    MODIFY ENTITIES OF demo_rap_unmanaged_auth 
         ENTITY demo_rap_unmanaged_auth 
           CREATE AUTO FILL CID 
             FIELDS ( keyfieldroot charfieldroot ) WITH VALUE #( 
              ( %cid = '1' keyfieldroot = 1 charfieldroot = 'A' ) 
              ( %cid = '2' keyfieldroot = 2 charfieldroot = 'B' ) 
              ( %cid = '3' keyfieldroot = 3 charfieldroot = 'C' ) ) 
 
     ENTITY demo_rap_unmanaged_auth 
        CREATE BY \_child AUTO FILL CID 
          FIELDS ( keyfieldchild datafieldchild ) WITH VALUE #( 
          ( 
          %cid_ref  = '1' 
            %target   = VALUE #( 
            ( keyfieldchild = 111 datafieldchild = 'AAA' ) 
            ( keyfieldchild = 222 datafieldchild = 'BBB' ) ) ) ) 
               MAPPED DATA(mapped) 
               FAILED DATA(failed) 
               REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field, char_field 
    FROM demo_dbtab_root 
    ORDER BY key_field ASCENDING 
    INTO TABLE @FINAL(result). 
 
    SELECT key_field, key_field_child, data_field 
    FROM demo_dbtab_child 
    INTO TABLE @FINAL(result_child). 
 
    MODIFY ENTITIES OF demo_rap_unmanaged_auth 
       ENTITY demo_rap_unmanaged_auth 
       UPDATE FIELDS ( datafieldroot ) WITH VALUE #( 
       ( keyfieldroot = 1 datafieldroot = 'aa' ) 
       ( keyfieldroot = 2 datafieldroot = 'bb' ) ) 
          MAPPED mapped 
          FAILED  failed 
          REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field, char_field 
    FROM demo_dbtab_root 
    ORDER BY key_field ASCENDING 
    INTO TABLE @FINAL(result1). 
 
    MODIFY ENTITIES OF demo_rap_unmanaged_auth 
       ENTITY demo_rap_unmanaged_auth 
   DELETE  FROM VALUE #( ( keyfieldroot = 3  ) ) 
   ENTITY demo_rap_unmanaged_auth_child 
   DELETE FROM VALUE #( (  keyfield = 1 keyfieldchild = 111 ) ) 
   FAILED failed 
   REPORTED reported. 
 
    TYPES: BEGIN OF reported_structure, 
             message TYPE if_abap_behv_message=>t_severity, 
             msgv1   TYPE symsgv, 
           END OF reported_structure. 
 
    TYPES reported_table_type TYPE TABLE OF reported_structure. 
    DATA failed_entities TYPE reported_table_type. 
 
    LOOP AT reported-demo_rap_unmanaged_auth 
      ASSIGNING FIELD-SYMBOL(<rep>). 
      APPEND VALUE #( 
      message = <rep>-%msg->m_severity 
      msgv1 = <rep>-%msg->if_t100_dyn_msg~msgv1 
       ) TO failed_entities. 
    ENDLOOP. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, key_field_child, data_field 
    FROM demo_dbtab_child 
    INTO TABLE @FINAL(result_child1). 
 
    out->next_section( 'Parent table after create' 
    )->write( result 
    )->next_section( 'Child table after create' 
    )->write( result_child 
    )->next_section( 'Parent table after update' 
    )->write( result1 
    )->next_section( 'Delete: authorization failed' 
    )->write( failed_entities 
    )->next_section( 'Child table after delete' 
    )->write( result_child1 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) from an ABAP class:

- Three instances of the parent entity and two instances of the child entity are created with the statement `MODIFY ENTITY`.

- Two instances of the parent entity are updated. This update is authorized.

- The EML consumer tries to delete an instance of the parent entity and an instance of the child entity. The delete operation on the parent entity is not authorized and the operation fails. The delete operation on the child entity is directed to the authorization master entity (in this example the same as the parent entity). It is interpreted as update request of the authorization master entity. Update operations are authorized, so the delete operation of the child entity instance is successful.

- Using the ABAP SQL `SELECT` statement, the content of the parent and child tables after the create, update, and delete operations are displayed. For the failed delete operation of the parent entity, an error message is returned.

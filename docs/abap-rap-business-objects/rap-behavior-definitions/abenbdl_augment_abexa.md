---
title: "RAP - Operation Augmentation"
source_file: abenbdl_augment_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF > RAP - augment"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Operation Augmentation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to define and implement the operation augmentation in a RAP projection business object.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

**Base BDEF**

The base BDEF is the managed RAP behavior definition `DEMO_RAP_MANAGED_ASSOC_ROOT`. It defines the behavior for two entities which are connected via a [CDS composition](../../abap-glossary/abencds_composition_glosry.md) relation.

``` abap
managed
implementation in class BP_DEMO_RAP_MANAGED_ASSOC_ROOT unique;
strict ( 2 );
with cross associations;

define behavior for DEMO_RAP_MANAGED_ASSOC_ROOT alias _Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  association _ext { create; }
  field ( readonly : update ) KeyFieldRoot;

  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      CharFieldRoot2 = char_field_2;
      DecFieldRoot  = dec_field;
      constant 'Demo' = char_field_3;
    }
}

define behavior for DEMO_RAP_MANAGED_ASSOC_CHILD alias _Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;

  association _parent { }

  field ( readonly : update ) KeyField, KeyFieldChild;
  mapping for demo_dbtab_child
    {
      KeyField      = key_field;
      KeyFieldChild = key_field_child;
      DataField     = data_field;
      CharField     = char_field;
    }
}
```

**Projection BDEF**

The projection behavior definition is defined as shown below. It reuses the standard operations from the base BDEF and augments the `create`, `update`, and `create-by-association` operations.

``` abap
projection
implementation in class bp_demo_rap_proj_augment unique;
strict ( 2 );

define behavior for DEMO_RAP_PROJ_AUGMENT alias _Parent
{
  use create ( augment );
  use update ( augment );
  use delete;

  use association _child { create ( augment ); }

  field ( modify ) VirtualElement;
  field ( readonly ) DecFieldRoot;
}

define behavior for DEMO_RAP_PROJ_AUGMENT_CHILD alias _Child
{
  use update;
  use delete;

  use association _parent;
}
```

**Behavior implementation**

In the ABAP behavior pool, the operation augmentation is implemented in three methods: `augment_create`, `augment_update`, and `augment_cba_child`.

`augment_create` implements the following:

- It augments an original base instance for the operation `create`. Whenever new instances are created, the value of field `CharFieldRoot` is set to *A*.

- It augments the operation create by adding new instances. Whenever a create operation is performed, the augmentation adds an additional entity instance. The key value for this new entity instance is a random integer.

``` abap
METHOD augment_create. 
  "when new instance is created, set CharFieldRoot to value augment 
  DATA: variable_create 
         TYPE TABLE FOR CREATE demo_rap_managed_assoc_root, 
        rel_tab         TYPE abp_behv_relating_tab. 
 
  LOOP AT entities_create ASSIGNING FIELD-SYMBOL(<fs1>). 
    APPEND sy-tabix TO rel_tab. 
 
    APPEND VALUE #( %cid                   = <fs1>-%cid 
                    %key                   = CORRESPONDING #( <fs1>-%key ) 
                    CharFieldRoot          = 'augment' 
                    %control-CharFieldRoot = if_abap_behv=>mk-on 
                  ) TO variable_create. 
 
  ENDLOOP. 
 
  MODIFY AUGMENTING ENTITIES OF demo_rap_managed_assoc_root 
  ENTITY _Root 
  CREATE FROM variable_create RELATING TO entities_create BY rel_tab. 
 
*    "whenever a new instance is created, 
*    "add an additional entity instance 
*    DATA: variable_create_new 
*         TYPE TABLE FOR CREATE demo_rap_managed_assoc_root. 
* 
*    "Determine max integer of key field 
*    SORT variable_create BY keyfieldroot DESCENDING. 
*    IF variable_create IS NOT INITIAL. 
*      DATA(max_nom) = variable_create[ 1 ]-KeyFieldRoot. 
*    ENDIF. 
* 
*    LOOP AT variable_create ASSIGNING FIELD-SYMBOL(<fs2>). 
* 
*      APPEND VALUE #( KeyFieldRoot = 
*        cl_abap_random_int=>create( 
*          seed = cl_abap_random=>seed( 
*             ) min = max_nom + 1 max = 100 )->get_next( ) 
*                      DataFieldRoot = 'augment' 
*                      CharFieldRoot = <fs2>-CharFieldRoot 
*                      %control         = VALUE #( 
*                        KeyFieldRoot = if_abap_behv=>mk-on 
*                        DataFieldRoot = if_abap_behv=>mk-on 
*                        CharFieldRoot = if_abap_behv=>mk-on ) 
*                    ) TO variable_create_new. 
* 
*    ENDLOOP. 
* 
*    MODIFY AUGMENTING ENTITIES OF demo_rap_managed_assoc_root 
*      ENTITY _Root 
*      CREATE AUTO FILL CID WITH variable_create_new 
*      RELATING TO entities_create BY rel_tab. 
 
ENDMETHOD.
```

`augment_update` augments an original base instance for the operation `update`. Whenever an existing entity instance is updated, the value of field `DecFieldRoot` is set to *100.2*.

``` abap
METHOD augment_update. 
  "when an instance is updated, set DecFieldRoot to value 100.2 
  DATA: variable_update 
          TYPE TABLE FOR UPDATE demo_rap_managed_assoc_root, 
        relates_update  TYPE abp_behv_relating_tab. 
 
  LOOP AT entities_update INTO DATA(perform_update). 
    APPEND sy-tabix TO relates_update. 
 
    APPEND VALUE #( %key             = CORRESPONDING #( perform_update-%key ) 
                    %cid_ref         = perform_update-%cid_ref 
                    DecFieldRoot      = '100.2' 
                    %control-DecFieldRoot = if_abap_behv=>mk-on 
                  ) TO variable_update. 
 
  ENDLOOP. 
 
  MODIFY AUGMENTING ENTITIES OF demo_rap_managed_assoc_root 
    ENTITY _Root 
    UPDATE FROM variable_update 
    RELATING TO entities_update BY relates_update. 
 
ENDMETHOD.
```

`augment_cba_child` implements the following:

- It augments an original base instance for the operation `create by association`. Whenever new child instances are created via the parent entity, the value of field `DataField` is set to *AAA*.

- It augments the operation create by association by adding new child instances. For each parent instance, an additional child instance with the key value *26* is added.

``` abap
METHOD augment_cba_Child. 
  "whenever a new child instance is created, set DataField to value augment 
  DATA: variable_cba 
         TYPE TABLE FOR CREATE demo_rap_managed_assoc_root\_child. 
 
  LOOP AT entities_cba ASSIGNING FIELD-SYMBOL(<variable_cba>). 
    LOOP AT <variable_cba>-%target ASSIGNING FIELD-SYMBOL(<fs2>). 
 
      APPEND VALUE #( 
      %cid_ref = <variable_cba>-%cid_ref 
     KeyFieldRoot = <variable_cba>-KeyFieldRoot 
                           %target            = VALUE #( ( 
                           %cid            = <fs2>-%cid 
                           KeyFieldChild = <fs2>-KeyFieldChild 
                           DataField = 'augment' 
                           %control-DataField = if_abap_behv=>mk-on 
                          ) ) ) TO variable_cba. 
    ENDLOOP. 
  ENDLOOP. 
 
  MODIFY AUGMENTING ENTITY demo_rap_managed_assoc_root 
      CREATE BY \_Child AUTO FILL CID WITH variable_cba. 
 
  "whenever a new child instance is created, 
  "add an additional child instance 
  "with key value 26. 
  DATA: variable_cba_new 
   TYPE TABLE FOR CREATE demo_rap_managed_assoc_root\_child. 
 
  LOOP AT entities_cba INTO DATA(hallo_cba). 
    APPEND VALUE #( %cid_ref = hallo_cba-%cid_ref 
                    KeyFieldRoot = hallo_cba-KeyFieldRoot 
                    %target            = VALUE #( ( 
                    KeyField = hallo_cba-KeyFieldRoot 
                    KeyFieldChild = 26 
 
                    %control         = VALUE #( 
                      KeyField = if_abap_behv=>mk-on 
                      KeyFieldChild = if_abap_behv=>mk-on 
 
                       ) ) ) 
                 )  TO variable_cba_new. 
  ENDLOOP. 
 
  MODIFY AUGMENTING ENTITY demo_rap_managed_assoc_root 
          CREATE BY \_Child AUTO FILL CID WITH variable_cba_new. 
ENDMETHOD.
```

For the full implementation, see `BP_DEMO_RAP_PROJ_AUGMENT======CCIMP`.

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
CLASS cl_demo_rap_proj_augment DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_proj_augment IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_dbtab_root. 
    DELETE FROM demo_dbtab_child. 
 
    MODIFY ENTITIES OF demo_rap_proj_augment 
    ENTITY _Parent 
          CREATE FIELDS ( KeyFieldRoot  ) 
          WITH VALUE #( 
           ( %cid = 'cid1' KeyFieldRoot = 1  ) 
           ( %cid = 'cid2' KeyFieldRoot = 2 ) ) 
 
           UPDATE FIELDS ( DataFieldRoot ) WITH VALUE #( 
           ( %cid_ref = 'cid1' 
             DataFieldRoot = 'bbb' ) ) 
 
          FAILED DATA(failed) 
          REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field, char_field, dec_field 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(result). 
 
    MODIFY ENTITIES OF demo_rap_proj_augment 
       ENTITY _Parent 
       CREATE BY \_Child 
       FIELDS ( KeyFieldChild CharField  ) 
       WITH VALUE #( 
       ( KeyFieldRoot = 1 
         %target = VALUE #( ( %cid = 'cid3' 
                              KeyFieldChild = 1 
                              CharField = 'XXX' ) ) ) 
       ( KeyFieldRoot = 2 
         %target = VALUE #( ( %cid = 'cid4' 
                              KeyFieldChild = 2 
                              CharField = 'YYY' ) ) ) ) 
        FAILED failed 
        REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * 
    FROM demo_dbtab_child 
    INTO TABLE @FINAL(result_child). 
 
    out->next_section( 'root' 
        )->write( result 
        )->next_section( 'child' 
        )->write( result_child ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- It creates two parent entity instances. The operation augmentation automatically adds the value *A* for field `CharFieldRoot` for each entity instance. Moreover, for each created entity instance, another entity instance is added by the operation augment with a random integer as key value.

- It updates one of the entity instances. The operation augmentation automatically adds the value *100.2* for field `DecFieldRoot` for all updated entity instances.

- It creates a child entity instance for each parent entity instance via a create-by-association operation. The operation augmentation automatically adds the value *AAA* for field `DataFieldRoot` for each newly created child entity instance. Moreover, it adds an additional child entity instance for each parent entity instance with the child entity key *26*.

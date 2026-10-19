---
title: "ABAP EML - MODIFY, Standard Operations (Managed)"
source_file: abeneml_modify_op_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY, Standard Operations (Managed)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various standard operations to manipulate a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). It also includes the use of `READ` statements.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT` and its child entity `DEMO_MANAGED_CHILD`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT
  as select from demo_tab_root
  composition [1..1] of DEMO_MANAGED_CHILD as _child
  {     
    key demo_tab_root.key_field,
        demo_tab_root.data_field1_root,
        demo_tab_root.data_field2_root,
        _child
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_MANAGED_CHILD
  as select from demo_tab_child
  association to parent DEMO_MANAGED_ROOT as _parent 
    on $projection.key_field = _parent.key_field
  {
        _parent,
    key demo_tab_child.key_field,
        demo_tab_child.data_field1_child,
        demo_tab_child.data_field2_child
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root unique;
strict ( 2 );

define behavior for DEMO_MANAGED_ROOT
persistent table demo_tab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }

  field ( readonly : update ) key_field;
}

define behavior for DEMO_MANAGED_CHILD alias child
persistent table demo_tab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly : update ) key_field;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, there is no [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) created and needed since only standard [CRUD](../../abap-glossary/abencrud_glosry.md) operations are used in the example.

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
CLASS cl_demo_rap_eml_modify_op_2 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_modify_op_2 IMPLEMENTATION. 
  METHOD main. 
 
    "Empty tables 
    DELETE FROM demo_tab_root. 
    DELETE FROM demo_tab_child. 
 
    "CREATE Operations 
    MODIFY ENTITY demo_managed_root 
    CREATE FIELDS ( key_field data_field1_root data_field2_root ) 
    WITH VALUE #( 
        ( %cid = 'cid1' key_field = 1 
          data_field1_root = 'aaa' data_field2_root = 'bbb' ) 
        ( %cid = 'cid2' key_field = 2 
          data_field1_root = 'ccc' data_field2_root = 'ddd' ) 
        ( %cid = 'cid3' key_field = 3 
          data_field1_root = 'eee' data_field2_root = 'fff' ) 
        ( %cid = 'cid4' key_field = 4 
          data_field1_root = 'ggg' data_field2_root = 'hhh' ) 
              ). 
 
    "CREATE BY assoc (child entity) 
    MODIFY ENTITY demo_managed_root 
    CREATE BY \_child 
    FIELDS ( data_field1_child data_field2_child ) WITH VALUE #( 
        ( key_field = 1 
          %target = VALUE #( ( %cid = 'cid3' 
                               data_field1_child = 'iii' 
                               data_field2_child = 'jjj' ) 
                                         ) ) 
        ( key_field = 2 
          %target = VALUE #( ( %cid = 'cid4' 
                               data_field1_child = 'kkk' 
                               data_field2_child = 'lll' ) 
                           ) ) 
              ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root 
      INTO TABLE @FINAL(create_root_tab).     "#EC CI_ALL_FIELDS_NEEDED 
    SELECT * FROM demo_tab_child 
      INTO TABLE @FINAL(create_child_tab).    "#EC CI_ALL_FIELDS_NEEDED 
    SELECT * FROM demo_tab_assoc 
      INTO TABLE @FINAL(create_assoc_tab).    "#EC CI_ALL_FIELDS_NEEDED 
 
    "UPDATE Operation 
    MODIFY ENTITY demo_managed_root 
    UPDATE FIELDS ( data_field1_root data_field2_root ) WITH VALUE #( 
       ( key_field = 3 
         data_field1_root = 'qqq' 
         data_field2_root = 'rrr' ) 
       ( key_field = 4 
         data_field1_root = 'sss' 
         data_field2_root = 'ttt' ) 
      ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(update_tab). 
 
    "DELETE Operation 
    MODIFY ENTITY demo_managed_root 
    DELETE  FROM VALUE #( 
      ( key_field = 4  ) 
             ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root INTO TABLE @FINAL(delete_tab). 
 
    "READ Operations 
    "READ bdef (root entity) 
    READ ENTITY demo_managed_root 
    ALL FIELDS WITH VALUE #( 
          ( key_field = 1  ) 
          ( key_field = 2  ) 
          ( key_field = 3  ) 
          ) 
    RESULT FINAL(read_result). 
 
    "READ BY assoc (child) 
    READ ENTITY demo_managed_root 
    BY \_child 
    ALL FIELDS WITH VALUE #( 
          ( key_field = 1  ) 
          ( key_field = 2  ) 
          ) 
    RESULT FINAL(read_by_child_tab). 
 
    "Display 
    out->next_section( 'CREATE (root entity)' 
            )->write( create_root_tab 
            )->next_section( 'CREATE BY assoc (child entity)' 
            )->write( create_child_tab 
            )->next_section( 'UPDATE' 
            )->write( update_tab 
            )->next_section( 'DELETE' 
            )->write( delete_tab 
            )->next_section( 'READ (root entity)' 
            )->write( read_result 
            )->next_section( 'READ BY assoc (child entity)' 
            )->write( read_by_child_tab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Modify operations with `CREATE` and `CREATE BY`

  Two `MODIFY ENTITY` operations are executed to create data sets for the root entity using the `CREATE` statement as well as data sets for associations defined in the BDEF using `CREATE BY`.

- Modify operation with `UPDATE`

  Data sets of the root entity are updated.

- Modify operation with `DELETE`

  Data sets of the root entity are deleted.

- Read operation with `READ` and `READ BY`

  Data sets are read from the root and child entities.

For demonstration purposes, several internal tables with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) are created to be used with the modify operations. They include demo values to be shown in the output. The [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) reads the data from the respective database tables into a managed [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) in which the operations take place. The changes are saved with the statement [`COMMIT ENTITIES`](abapcommit_entities.md), and, thus, the changed data are persisted to the database tables.

---
title: "ABAP EML - MODIFY AUGMENTING"
source_file: abeneml_modify_augmenting_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP EML - Providing RAP BOs > ABAP EML - MODIFY AUGMENTING ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY AUGMENTING

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the ABAP EML `MODIFY` statement with the addition `AUGMENTING` with a RAP projection business object.

**Base BDEF**

The base BDEF is the managed RAP behavior definition `DEMO_MANAGED_ROOT_WAS`. It defines the behavior for two entities which are connected via a CDS composition relation.

``` abap
managed implementation in class bp_demo_managed_root_was unique;
strict(2);

define behavior for DEMO_MANAGED_ROOT_WAS alias _Root
persistent table demo_tab_root_3
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  field(readonly:update) key_field;
}

define behavior for DEMO_MANAGED_CHILD_WAS alias _Child
persistent table demo_tab_child_3
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  field(readonly:update) key_field_child;
  association _parent;

}
```

**Projection BDEF**

The projection BDEF reuses the standard operations from the base BDEF and augments the `create`, `update`, and `create-by-association` operations.

``` abap
projection implementation in class bp_demo_managed_root_proj unique;
strict ( 2 );

define behavior for DEMO_MANAGED_ROOT_PROJ alias _Parent
{
  use create ( augment );
  use update ( augment );
  use delete;

  use association _child { create ( augment ); }

}

define behavior for DEMO_MANAGED_CHILD_PROJ alias _Child
{
  use update;
  use delete;

  use association _parent;
}
```

**Behavior implementation**

For the above projection BDEF, one [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_PROJ`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_PROJ=====CCIMP` of the behavior pool. In the behavior pool, operation augmentation is implemented in the following methods:

- `augment_create`

  Augments an original base instance for the operation `create`. Whenever new instances are created, the value of field `field1` is set to `create_augment`.

- `augment_update`

  Augments an original base instance for the operation `update`. Whenever an existing entity instance is updated, the value of field `field4` is set to *222*.

- `augment_cba_child`

  Augments an original base instance for the operation `create by association`. Whenever new child instances are created via the parent entity, the value of field `field2` is set to `cba_augment`.

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
CLASS cl_demo_rap_eml_modify_agmntng DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_modify_agmntng IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY ENTITY demo_managed_root_proj 
       CREATE FIELDS ( key_field 
            field2 field3 field4 ) WITH  VALUE #( 
          ( %cid = 'cid1' 
            key_field = 1 
            field2 = 'create_1' 
            field3 = 1 
            field4 = 2 ) 
          ( %cid = 'cid2' 
            key_field = 2 
            field2 = 'create_2' 
            field3 = 3 
            field4 = 4 ) ) 
       MAPPED FINAL(m1) 
       FAILED FINAL(f1) 
       REPORTED FINAL(r1). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    MODIFY ENTITY demo_managed_root_proj 
          UPDATE FIELDS ( field3 ) WITH VALUE #( 
              ( key_field = 1 
                field3 = 111 ) ) 
          FAILED FINAL(f2) 
          REPORTED FINAL(r2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM demo_tab_root_3 
      ORDER BY key_field 
      INTO TABLE @FINAL(root_tab). 
 
    out->begin_section( `Demo for MODIFY AUGMENTING` 
      )->write_doc( 
`Database table entries after the create and update operations:` 
      )->write( root_tab ). 
 
    MODIFY ENTITY demo_managed_root_proj 
       CREATE BY \_Child FIELDS ( key_field_child field1 
            field3 field4 ) WITH VALUE #( 
          ( key_field = 1 
            %target = VALUE #( ( %cid = 'cid3' 
                                 key_field_child = 1 
                                 field1 = 'cba1' 
                                 field3 = 1 
                                 field4 = 2 ) ) ) 
          ( key_field = 2 
            %target = VALUE #( ( %cid = 'cid4' 
                                 key_field_child = 2 
                                 field1 = 'cba2' 
                                 field3 = 3 
                                 field4 = 4 ) ) ) ) 
       MAPPED FINAL(m3) 
       FAILED FINAL(f3) 
       REPORTED FINAL(r4). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, key_field_child, field1, field2, field3, field4 
          FROM demo_tab_child_3 
          ORDER BY key_field 
          INTO TABLE @FINAL(child_tab). 
 
    out->write_doc( 
`Database table entries after the create-by-association operation:` 
      )->write( child_tab ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_child_3. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Using an ABAP EML `MODIFY` statement, two parent entity instances are created. In the same request, one of the created instances gets updated. The operation augmentation automatically adds the value `create_augment` for field `field1` for each entity instance. For the updated entity instance, `field4` is set to *222*.

- With a further ABAP EML `MODIFY` statement, a child entity instance for each parent entity instance is created via a create-by-association operation. The operation augmentation automatically adds the value *cba_augment* for field `field2` for each newly created child entity instance.

- The output window shows the database entries of the root and child entities' tables.

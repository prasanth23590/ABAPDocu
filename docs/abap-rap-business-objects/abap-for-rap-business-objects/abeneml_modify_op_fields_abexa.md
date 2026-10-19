---
title: "ABAP EML - MODIFY, Field Specification Expressions"
source_file: abeneml_modify_op_fields_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY, Field Specification Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various standard operations and variants of field specification expressions to set up internal tables for ABAP EML `MODIFY ENTITY` statements to manipulate a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

The following standard operations and field specification alternatives are covered in the example:

**Operations**

- `CREATE`

- `CREATE BY` association

- `UPDATE`

- `DELETE`

**Field specification alternatives**

- `FROM`

- `FIELDS (...) WITH`

- `SET FIELDS WITH`

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
CLASS cl_demo_rap_eml_modify_oprtns DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED   demo_managed_root, 
      reported TYPE RESPONSE FOR REPORTED demo_managed_root. 
    METHODS: 
      initialize_dbtabs, 
      display_dbtabs 
        IMPORTING title TYPE string, 
      display_errors. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_modify_oprtns IMPLEMENTATION. 
  METHOD main. 
 
    "MODIFY operations with the addition FROM 
    MODIFY ENTITY demo_managed_root 
      CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'aaa' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'bbb' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'ccc' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'ddd' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3' 
          key_field = 3 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'eee' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'fff' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid4' 
          key_field = 4 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'ggg' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'hhh' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
         ) 
      CREATE BY \_child FROM  VALUE #( 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( ( %cid = 'cid5' 
                   data_field1_child = 'zzz' 
                   %control-data_field1_child = if_abap_behv=>mk-on 
                   data_field2_child = 'yyy' 
                   %control-data_field2_child = if_abap_behv=>mk-on ) 
                           ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( ( %cid = 'cid6' 
                    data_field1_child = 'xxx' 
                    %control-data_field1_child = if_abap_behv=>mk-on 
                    data_field2_child = 'www' 
                    %control-data_field2_child = if_abap_behv=>mk-on ) 
                            ) ) 
        ) 
      UPDATE FROM VALUE #( 
        ( %cid_ref = 'cid3' 
          data_field1_root = 'iii' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'jjj' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
         ) 
      DELETE FROM VALUE #( ( %cid_ref = 'cid4' ) ) 
        FAILED   failed 
        REPORTED reported. 
 
    display_errors( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_dbtabs( `Modify Operations with FROM` ). 
 
    "MODIFY operations with the addition FIELDS ( ... ) WITH 
    MODIFY ENTITY demo_managed_root 
      CREATE FIELDS ( key_field data_field1_root 
                      data_field2_root ) 
        WITH VALUE #( 
        ( %cid = 'cid7' 
          key_field = 5 
          data_field1_root = 'kkk' 
          data_field2_root = 'lll'  ) 
        ( %cid = 'cid8' 
          key_field = 6 
          data_field1_root = 'mmm' 
          data_field2_root = 'nnn'  ) 
        ) 
      CREATE BY \_child FIELDS ( data_field1_child 
                                 data_field2_child ) 
        WITH VALUE #( 
        ( %cid_ref = 'cid8' 
          %target = VALUE #( ( %cid = 'cid9' 
                               data_field1_child = 'vvv' 
                               data_field2_child = 'uuu' ) 
                           ) ) 
        ) 
      UPDATE FIELDS ( data_field1_root 
                      data_field2_root ) 
        WITH VALUE #( 
       ( %cid_ref = 'cid7' 
         data_field1_root = 'ooo' 
         data_field2_root = 'ppp' ) 
         ) 
        FAILED   failed 
        REPORTED reported. 
 
    display_errors( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_dbtabs( 
     `Modify Operations with FIELDS ( ... ) WITH` 
     ). 
 
    "MODIFY operations with the addition SET FIELDS WITH 
    MODIFY ENTITY demo_managed_root 
      CREATE SET FIELDS 
      WITH VALUE #( 
        ( %cid = 'cid10' 
          key_field = 7 
          data_field1_root = 'qqq' 
          data_field2_root = 'rrr'  ) 
        ( %cid = 'cid11' 
          key_field = 8 
          data_field1_root = 'sss' 
          data_field2_root = 'ttt'  ) 
        ) 
      CREATE BY \_child SET FIELDS WITH VALUE #( 
        ( %cid_ref = 'cid10' 
          %target = VALUE #( ( %cid = 'cid12' 
                               data_field1_child = 'ttt' 
                               data_field2_child = 'sss' ) 
                           ) ) 
        ( %cid_ref = 'cid11' 
          %target = VALUE #( ( %cid = 'cid13' 
                               data_field1_child = 'rrr' 
                               data_field2_child = 'qqq' ) 
                           ) ) 
        ) 
      UPDATE SET FIELDS WITH VALUE #( 
        ( %cid_ref = 'cid11' 
          data_field1_root = 'uuu' 
          data_field2_root = 'vvv' ) 
         ) 
        FAILED   failed 
        REPORTED reported. 
 
    display_errors( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_dbtabs( 
    `Modify Operations with SET FIELDS WITH` 
    ). 
  ENDMETHOD. 
  METHOD display_dbtabs. 
    SELECT * FROM demo_tab_root 
      INTO TABLE @FINAL(modifiy_parent). 
    SELECT * FROM demo_tab_child 
      INTO TABLE @FINAL(modifiy_child). 
    out->next_section( title 
      )->write( modifiy_parent 
      )->write( modifiy_child ). 
  ENDMETHOD. 
  METHOD display_errors. 
    LOOP AT reported-demo_managed_root 
      ASSIGNING FIELD-SYMBOL(<reported>). 
      out->write( <reported>-%msg->if_message~get_text( ) ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root. 
    DELETE FROM demo_tab_child. 
    DELETE FROM demo_tab_assoc. 
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

- Modify operations with `FROM`

  Two `MODIFY ENTITY` operations are executed with `FROM` for both root and child entity. To cover several operations in one go, four new data sets are created for the root entity of which one is updated and deleted in the same `MODIFY` statement. Furthermore, two data sets are created for the child entity via a create-by-association operation.

- Modify operations with `FIELDS (...) WITH`

  A `CREATE`, `CREATE BY` and `UPDATE` operation is demonstrated within one `MODIFY ENTITY` statement using the addition `FIELDS (...) WITH`.

- Modify operations with `SET FIELDS WITH`

  A `CREATE`, `CREATE BY` and `UPDATE` operation is demonstrated within one `MODIFY ENTITY` statement using the addition `SET FIELDS WITH`.

For demonstration purposes, several internal tables with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) are created to be used with the modify operations. They include demo values to be shown in the output. The [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) reads the data from the respective database tables into a managed [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) in which the operations take place. The changes are saved with the statement [`COMMIT ENTITIES`](abapcommit_entities.md), and, thus, the changed data are persisted to the database tables.

---
title: "Using %cid / %cid_ref"
source_file: abenderived_types_cid_cidref_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %cid / %cid_ref

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%cid` and `%cid_ref` with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). Furthermore, it includes the use of the addition [`AUTO FILL CID`](abapmodify_entity_entities_fields.md) with a RAP create operation.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_4` and its child entity `DEMO_MANAGED_CHILD_4`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_managed_root_4
  as select from demo_tab_root_3
  composition [1..*] of demo_managed_child_4 as _child
  {
    key key_field,
        field1,
        field2,
        field3,
        field4,
        _child
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_managed_child_4
  as select from demo_tab_child_3
  association to parent demo_managed_root_4 
  as _parent on $projection.key_field = _parent.key_field
  {
        _parent,
    key key_field,
    key key_field_child,
        field1,
        field2,
        field3,
        field4
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_4` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_4 unique;
strict(2);

define behavior for demo_managed_root_4
persistent table DEMO_TAB_ROOT_3
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  association _child { create; }
  field(readonly:update) key_field;
}

define behavior for demo_managed_child_4 alias _child
persistent table DEMO_TAB_CHILD_3
lock dependent by _parent
authorization dependent by _parent

{
  update;
  delete;
  field ( readonly ) key_field;
  association _parent;
  field(readonly:update) key_field_child;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_4`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_4========CCIMP` of the behavior pool. In this case, the behavior pool does not include any implementations that are relevant for the example.

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
CLASS cl_demo_rap_drvd_types_cid DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      mapped   TYPE RESPONSE FOR MAPPED   demo_managed_root_4, 
      failed   TYPE RESPONSE FOR FAILED   demo_managed_root_4, 
      reported TYPE RESPONSE FOR REPORTED demo_managed_root_4. 
    METHODS: 
      initialize_dbtabs, 
      display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_cid IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type components: ` && 
                        `%cid and %cid_ref` ). 
 
    MODIFY ENTITY demo_managed_root_4 
          CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' key_field = 1 
              field1 = 'aaa' field2 = 'bbb' 
              field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' key_field = 2 
              field1 = 'ccc' field2 = 'ddd' 
              field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' key_field = 3 
              field1 = 'eee' field2 = 'fff' 
              field3 = 30 field4 = 31 ) 
            ( %cid = 'cid4' key_field = 4 
              field1 = 'to be deleted' field2 = 'to be deleted' 
              field3 = 40 field4 = 41 ) 
                 ) 
          CREATE BY \_child 
          FIELDS ( key_field_child field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid_ref = 'cid1' 
              %target = VALUE #( 
                ( %cid = 'cid_child1' key_field_child = 10 
                  field1 = 'ggg' field2 = 'hhh' 
                  field3 = 100 field4 = 101  ) ) ) 
            ( %cid_ref = 'cid2' 
              %target = VALUE #( 
                ( %cid = 'cid_child2' key_field_child = 20 
                  field1 = 'iii' field2 = 'jjj' 
                  field3 = 200 field4 = 201 ) ) 
                ) ) 
          UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %cid_ref = 'cid3' field2 = 'UPDATED' ) ) 
          DELETE FROM VALUE #( 
            ( %cid_ref = 'cid4' ) ) 
           MAPPED mapped 
           FAILED failed 
           REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab). 
 
    SELECT key_field, key_field_child, field1, field2, field3, field4 
    FROM demo_tab_child_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(child_tab). 
 
    display_responses(  ). 
    out->write_html( 
        `<b>Root entity: Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab 
       )->write_html( 
        `<b>Child entity: Database table entries ` && 
        `after the operations</b>` 
       )->write( child_tab 
       )->line( ). 
 
    out->next_section( 
     `AUTO FILL CID` ). 
 
    MODIFY ENTITY demo_managed_root_4 
          CREATE AUTO FILL CID FIELDS ( key_field field1 field2 
                                        field3 field4 ) 
          WITH VALUE #( 
            ( key_field = 5 
              field1 = 'kkk' field2 = 'lll' 
              field3 = 50 field4 = 51 ) 
            ( key_field = 6 
              field1 = 'mmm' field2 = 'nnn' 
              field3 = 60 field4 = 61 ) ) 
          CREATE BY \_child AUTO FILL CID 
          FIELDS ( key_field_child field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( key_field = 3 
              %target = VALUE #( 
                ( key_field_child = 30 
                  field1 = 'ggg' field2 = 'hhh' 
                  field3 = 300 field4 = 301  ) ) 
                ) ) 
           MAPPED mapped 
           FAILED failed 
           REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab2). 
 
    SELECT key_field, key_field_child, field1, field2, field3, field4 
    FROM demo_tab_child_3 
    ORDER BY key_field 
    INTO TABLE @FINAL(child_tab2). 
 
    display_responses(  ). 
    out->write_html( 
        `<b>Root entity: Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab2 
       )->write_html( 
        `<b>Child entity: Database table entries ` && 
        `after the operations</b>` 
       )->write( child_tab2 ). 
 
  ENDMETHOD. 
  METHOD display_responses. 
    IF mapped IS NOT INITIAL. 
      out->write_doc( `MAPPED response:` 
        )->write( mapped ). 
    ENDIF. 
 
    IF failed IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed ). 
    ENDIF. 
 
    IF reported IS NOT INITIAL. 
      out->write_doc( `REPORTED response:` 
        )->write( reported ). 
    ENDIF. 
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

There are two ABAP EML modify requests that cover multiple RAP modify operations:

1.  With a RAP create operation, multiple [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) are created that include user-defined content IDs `%cid`. In the same ABAP EML request, a create-by-association operation creates RAP BO instances for the child entity while using `%cid_ref` to refer to the instances that have just been created for the root entity. The RAP BO instances for the child also include content IDs `%cid` which are not referred to in the example. This operation is followed by an update and delete operation in the same request. Both operations use `%cid_ref` to refer to the instances that have just been created, too. With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the instances are saved to the database. The output shows the database table entries as well as the mapped responses for root and child entity to visualize the mapping of `%cid` and the keys.

2.  For demonstration purposes, the example also covers the use of `AUTO FILL CID` in a RAP create and create-by-association operation. When specifying the create operation with the addition `AUTO FILL CID`, `%cid` is filled automatically. With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the instances are saved to the database. The output shows the database table entries - including the entries from the first ABAP EML modify request - as well as the mapped responses for root and child entity.

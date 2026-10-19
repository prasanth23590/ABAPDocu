---
title: "Using %fail"
source_file: abenderived_types_fail_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %fail

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%fail` with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

**Data model**

The CDS data model consists of the [root entity](../../abap-glossary/abenroot_entity_glosry.md) `DEMO_MANAGED_ROOT_FAILED` and its [child entity](../../abap-glossary/abenchild_entity_glosry.md) `DEMO_MANAGED_CHILD_FAILED`. The child entity is not used in the example.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT_FAILED
  as select from demo_tab_root_5
  composition [1..*] of DEMO_MANAGED_CHILD_FAILED as _child
  {        
     key key_field,
        field1,
        field2,
        field3,
        field4,
        _child
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_FAILED` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_failed unique;
strict(2);

define behavior for DEMO_MANAGED_ROOT_FAILED
persistent table DEMO_TAB_ROOT_5
lock master
authorization master ( instance, global )

{
  create;
  update( features : instance );
  delete;
  association _child { create; }
  field(readonly:update) key_field;
}

define behavior for DEMO_MANAGED_CHILD_FAILED
persistent table DEMO_TAB_CHILD_5
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

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_FAILED`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_FAILED===CCIMP` of the behavior pool.

The following methods are relevant for the example:

- `get_instance_authorizations`: If an instance has a specific value in a field, the update and delete operations should be denied, i. e. the operations are marked as `unauthorized`. `%fail-cause` is assigned accordingly. `%fail-cause` and the key of the RAP BO instance is stored in the `failed` response structure.

- `get_instance_features`: If an instance has a specific value in a field, update operations should be denied, i. e. the operations are marked as `readonly`. `%fail-cause` is assigned accordingly. `%fail-cause` and the key of the RAP BO instance is stored in the `failed` response structure.

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
CLASS cl_demo_rap_drvd_types_fail DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      mapped   TYPE RESPONSE FOR MAPPED   demo_managed_root_failed, 
      failed   TYPE RESPONSE FOR FAILED   demo_managed_root_failed, 
      reported TYPE RESPONSE FOR REPORTED demo_managed_root_failed. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_fail IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type component %fail` 
    )->line( 
    )->next_section( `RAP modify operation` ). 
 
    MODIFY ENTITY demo_managed_root_failed 
       CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' %key-key_field = 1 
              field1 = 'aaa' field2 = 'bbb' field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' %key-key_field = 2 
              field1 = 'ccc' field2 = 'ZZZ' field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' %key-key_field = 3 
              field1 = 'YYY' field2 = 'ddd' field3 = 30 field4 = 31 ) 
            ( %cid = 'cid4' %key-key_field = 4 
              field1 = 'YYY' field2 = 'eee' field3 = 40 field4 = 41 ) 
              ) 
           MAPPED mapped 
           FAILED failed 
           REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_5 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab). 
 
    IF failed IS INITIAL. 
      out->write( `No FAILED responses.` ). 
    ELSE. 
      out->write( `FAILED responses:` 
        )->write( failed ). 
    ENDIF. 
 
    out->write_html( 
        `<b>Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab 
       )->line( 
       )->next_section( `RAP update and delete operations` ). 
 
    MODIFY ENTITY demo_managed_root_failed 
       UPDATE FIELDS ( field1 field2 field3 field4 ) WITH VALUE #( 
            ( %key-key_field = 1 
              field1 = 'up1' field2 = 'up2' field3 = 99 field4 = 98 ) 
            ( %key-key_field = 2 
              field1 = 'up3' field2 = 'up4' field3 = 97 field4 = 96 ) 
            ( %key-key_field = 3 
              field1 = 'up5' field2 = 'up6' field3 = 95 field4 = 94 ) 
              ) 
       DELETE FROM VALUE #( ( %key-key_field = 4 ) ) 
           MAPPED mapped 
           FAILED failed 
           REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_5 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab2). 
 
    IF failed IS INITIAL. 
      out->write( `No FAILED responses.` ). 
    ELSE. 
      out->write( `FAILED responses:` 
        )->write( failed ). 
    ENDIF. 
 
    out->write_html( 
       `<b>Database table entries ` && 
       `after the operations</b>` 
      )->write( root_tab2 
      )->line( 
      )->next_section( `RAP read operation` ). 
 
    READ ENTITY demo_managed_root_failed 
    ALL FIELDS WITH VALUE #( ( %key-key_field = 1 ) 
                             ( %key-key_field = 2 ) 
                             ( %key-key_field = 3 ) 
                             ( %key-key_field = 4 ) 
                             ( %key-key_field = 5 ) 
                             ( %key-key_field = 6 ) 
                             ( %key-key_field = 7 ) ) 
     RESULT FINAL(read_result) 
     FAILED failed. 
 
    IF failed IS INITIAL. 
      out->write( `No FAILED responses.` ). 
    ELSE. 
      out->write( `FAILED responses:` 
        )->write( failed ). 
    ENDIF. 
 
    out->write_html( 
      `<b>Result of read operation:</b>` 
     )->write( read_result ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The class includes multiple ABAP EML requests:

1.  **ABAP EML modify request**: Multiple RAP BO instances are created. A [`COMMIT ENTITIES`](abapcommit_entities.md) statement triggers the saving of the instances to the database. The output shows for all requests the content of the [`failed`](abaptype_response_for.md) response. In this case, none of the instances show any failures. Furthermore, an internal table is filled with the database table entries. In the output, all newly created RAP BO instances have been saved to the database and are displayed in the internal table.

2.  **ABAP EML update and delete requests**: Specific RAP BO instances are updated and deleted. The outcome of calling the `get_instance_authorizations` and `get_instance_features` is that several instances cannot be updated and deleted because of the conditions implemented in the methods. Since these methods fill the `failed` responses, an internal table that contains the entries of the `failed` response consequently shows the different failure causes for those RAP BO instances that could not be saved to or deleted from the database table. `%fail-cause` is in this case `READONLY` and `UNAUTHORIZED`. As above, a `COMMIT ENTITIES` statement saves those instances that did not show any failures. The outcome of these ABAP EML requests is also shown in an internal table.

3.  **ABAP EML read request**: Multiple RAP BO instances are read from the database table. The read result is stored in an internal table which is displayed in the output. Since not all instances that are requested exist on the database table, an internal table containing the `failed` response consequently shows entries. `%fail-cause` is in this case `NOT_FOUND`.

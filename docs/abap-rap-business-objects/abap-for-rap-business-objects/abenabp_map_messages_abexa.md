---
title: "Example for RAP Saver Method map_messages"
source_file: abenabp_map_messages_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods > Examples for RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for RAP Saver Method map_messages

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the RAP saver method `map_messages` within a RAP saver class using unmanaged RAP BOs.

**Data model**

The CDS data model consists of the root entity ` DEMO_UNMANAGED_MAP_MESSAGES`, which represents the exposed RAP BO, and the [foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) `DEMO_UNMANAGED_FOREIGN_ENTITY`, i. e. the RAP BO that is not exposed.

CDS data model of the exposed BO:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Root entity for unmanaged BO'
define root view entity DEMO_UNMANAGED_MAP_MESSAGES 
as select from demo_tab_root_5 {
  key key_field,
  field1,
  field2,
  field3,
  field4
}
```

CDS data model of foreign entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Root entity for unmanaged BO'
define root view entity DEMO_UNMANAGED_FOREIGN_ENTITY 
as select from demo_tab_root_7 {
  key key_field,
  char1,
  char2,
  num1,
  num2
}
```

**Behavior definition**

The following [RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md), that are defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md), are relevant for the example:

- `DEMO_UNMANAGED_MAP_MESSAGES`

``` abap
unmanaged
implementation in class bp_demo_unmanaged_map_messages unique;
strict ( 2 );
foreign entity DEMO_UNMANAGED_FOREIGN_ENTITY;

define behavior for DEMO_UNMANAGED_MAP_MESSAGES
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
}
```

- `DEMO_UNMANAGED_MAP_MESSAGES`

``` abap
unmanaged
implementation in class bp_demo_unmanaged_foreign_enti unique;
strict(2);

define behavior for DEMO_UNMANAGED_FOREIGN_ENTITY
lock master
authorization master ( global )

{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;

}
```

**Behavior implementation**

For each of the above RAP behavior definitions, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created:

- Global class of the behavior pool: `BP_DEMO_UNMANAGED_MAP_MESSAGES`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UNMANAGED_MAP_MESSAGESCCIMP` of the behavior pool.

- Global class of the behavior pool: `BP_DEMO_UNMANAGED_FOREIGN_ENTI`. The `BP_DEMO_UNMANAGED_FOREIGN_ENTICCIMP` contains the actual behavior implementation.

The ABPs purposely include only a few method implementations to keep the example small. In this case, only the `create` method is implemented on [handler](abenabp_handler_class.md) side. On [saver](abenabp_saver_class.md) side, only the `save` method is implemented. The ABP of the exposed BO also includes the implementation of the `map_messages` method.

In this simple example, the `map_messages` method is implemented as follows: The messages that are available in the [`REPORTED LATE`](abaptype_table_for.md) table of the foreign entity are sequentially processed within a [`LOOP AT`](../../abap-programming-language/abap-processing-internal-data/abaploop_at_itab_variants.md) statement. Here, the message from the foreign entity is first replaced, and then inserted into the `REPORTED LATE` table of the exposed BO. After the loop, the content of the `REPORTED LATE` table of the foreign entity is deleted.

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
CLASS cl_demo_rap_unm_map_messages DEFINITION 
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
CLASS cl_demo_rap_unm_map_messages IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY ENTITY demo_unmanaged_map_messages 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH VALUE #( 
       ( %cid = 'cid_exposed_bo_1' 
         key_field = 1 
         field1 = 'exp_bo_1' 
         field2 = 'exp_bo_2' 
         field3 = 100 
         field4 = 200 ) 
        ( %cid = 'cid_exposed_bo_2' 
         key_field = 2 
         field1 = 'exp_bo_3' 
         field2 = 'exp_bo_4' 
         field3 = 200 
         field4 = 300 ) ). 
 
    MODIFY ENTITY demo_unmanaged_foreign_entity 
      CREATE FIELDS ( key_field num1 num2 char1 char2 ) 
      WITH VALUE #( 
        ( %cid = 'cid_foreign_bo_1' 
          key_field = 11 
          char1 = 'foreign_1' 
          char2 = 'foreign_2' 
          num1 = 1000 
          num2 = 2000 ) 
        ( %cid = 'cid_foreign_bo_2' 
          key_field = 22 
          char1 = 'foreign_3' 
          char2 = 'foreign_4' 
          num1 = 3000 
          num2 = 4000 ) ). 
 
    COMMIT ENTITIES RESPONSES REPORTED FINAL(rep). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(exposed_bo). 
 
    SELECT key_field, char1, char2, num1, num2 
       FROM demo_tab_root_7 
         ORDER BY key_field 
         INTO TABLE @FINAL(foreign_entity). 
 
    out->begin_section( 'Demo: Mapping Messages' 
     )->write_doc( 'Database table entries after the create operations:' 
     )->write( exposed_bo 
     )->write( foreign_entity 
     )->write_doc( 'REPORTED LATE entries:' 
     )->write( rep 
     ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
    DELETE FROM demo_tab_root_7. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The example includes two ABAP EML `MODIFY` requests within one [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). Each of the `MODIFY` requests includes a [create operation](../../abap-glossary/abenrap_create_operation_glosry.md) using [`CREATE`](abapmodify_entity_entities_op.md) statements that create two instances for the exposed BO and the foreign entity. A [`COMMIT ENTITIES`](abapemlcommit_entities_dyn.md) statement triggers the save sequence and terminates the RAP transaction.

The output shows the result of the `MODIFY` requests. The instances that have been saved to the database table are selected from the database table into an internal table. The `COMMIT ENTITIES` statement includes the `REPORTED` response. The content of this response is output, too, demonstrating the effect of the `map_messages` method. The original messages for the instances of the foreign entity are available for the exposed BO. Furthermore, the messages have been changed and the `REPORTED` table of the foreign entity does not show any entries since the content has been deleted.

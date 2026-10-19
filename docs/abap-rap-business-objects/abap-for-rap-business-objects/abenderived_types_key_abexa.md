---
title: "Using %key"
source_file: abenderived_types_key_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using %key

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of `%key` with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) in the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_4` and its child entity `DEMO_MANAGED_CHILD_4`. The child entity is not used in the example.

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
CLASS cl_demo_rap_drvd_types_key DEFINITION 
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
CLASS cl_demo_rap_drvd_types_key IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type component: ` && 
                        `%key` ). 
 
    MODIFY ENTITY demo_managed_root_4 
          CREATE FROM VALUE #( 
             %control = VALUE #( key_field = if_abap_behv=>mk-on 
                                 field1 = if_abap_behv=>mk-on 
                                 field2 = if_abap_behv=>mk-on 
                                 field3 = if_abap_behv=>mk-on 
                                 field4 = if_abap_behv=>mk-on ) 
            ( %cid = 'cid1' %key-key_field = 1 
              field1 = 'aaa' field2 = 'bbb' field3 = 10 field4 = 11 ) 
            ( %cid = 'cid2' %key = VALUE #( key_field = 2 ) 
              field1 = 'ccc' field2 = 'ddd' field3 = 20 field4 = 21 ) 
            ( %cid = 'cid3' key_field = 3 
              field1 = 'eee' field2 = 'fff' field3 = 30 field4 = 31 ) 
            ( %cid = 'cid4' %data-%key-key_field = 4 
              field1 = 'ggg' field2 = 'hhh' field3 = 40 field4 = 41 ) 
            ( %cid = 'cid5' %data-key_field = 5 
              field1 = 'iii' field2 = 'jjj' field3 = 50 field4 = 51 ) ) 
          "Other options for referring to the key besides using %key 
          "are demonstrated. 
          UPDATE FIELDS ( field2 ) WITH VALUE #( 
            ( %key-key_field = 1 field2 = 'up1' ) 
            ( key_field = 2 field2 = 'up2' ) 
            ( %tky-%key-key_field = 3 field2 = 'up3' ) 
            ( %tky-key_field = 4 field2 = 'up4' ) 
            ( %tky-%pky-%key-key_field = 5 field2 = 'up5' ) 
            ( %tky-%pky-key_field = 6 field2 = 'up6' ) 
            ( %pky-key_field = 7 field2 = 'up7' ) 
            ( %pky-%key-key_field = 8 field2 = 'up8' ) 
            ( %data-%key-key_field = 9 field2 = 'up9' ) 
            ( %data-key_field = 10 field2 = 'up10' ) ) 
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
 
    display_responses(  ). 
    out->write_html( 
        `<b>Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab 
        ). 
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

There is one ABAP EML modify request that covers a RAP create and update operation. In both create and update operation, `%key` is specified in different ways just to demonstrate the variety of specification options of this [component group](../../abap-glossary/abencomponent_group_glosry.md). See more information on this in the topic [Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md).

With a [`COMMIT ENTITIES`](abapcommit_entities.md) statement, the instances are saved to the database. The output shows the database table entries as well as the mapped and failed responses for the root entity.

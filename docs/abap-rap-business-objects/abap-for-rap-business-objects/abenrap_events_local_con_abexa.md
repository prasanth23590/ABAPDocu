---
title: "Local Consumption of RAP Business Events (Database Table Modification)"
source_file: abenrap_events_local_con_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for RAP Business Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Local Consumption of RAP Business Events (Database Table Modification)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the local consumption of [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) using a [managed RAP business object](../../abap-glossary/abenmanaged_rap_bo_glosry.md).

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_EVENT_M`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_ALLOWED
define root view entity DEMO_RAP_LOCAL_EVT_M as select from demo_tab_root_5 {
  key key_field,
  field1,
  field2,
  field3,
  field4
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_LOCAL_EVT_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
// Note:
// The RAP event handler class for this example is the class
// cl_demo_rap_local_evt. In the CCIMP include of the class,
// the RAP event handler methods are implemented.

managed with additional save with full data
implementation in class bp_demo_rap_local_evt_m unique;
strict ( 2 );

define behavior for DEMO_RAP_LOCAL_EVT_M
persistent table demo_tab_root_5
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
  event created;
  event updated parameter DEMO_ABSTRACT_ROOT_1;
  event deleted parameter DEMO_ABSTRACT_ROOT_1;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_LOCAL_EVT_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_RAP_LOCAL_EVT_M=======CCIMP` of the behavior pool.

**RAP event handler class**

The global class of the RAP event handler class is `CL_DEMO_RAP_EVENT_HANDLER`. The events are handled in the `CL_DEMO_RAP_LOCAL_EVT=========CCIMP`.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p>The RAP event handler class for this example is the class 
"! {@link cl_demo_rap_local_evt}. In the CCIMP include of the class, 
"! the RAP event handler methods are implemented.</p> 
"! 
"! <p>The RAP business events in this example are raised using 
"! <em>RAISE ENTITY EVENT</em> statements in the 
"! <em>save_modified</em> saver method that is implemented in the 
"! CCIMP include of the ABAP behavior pool 
"! {@link bp_demo_rap_local_evt_m}.</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_local_evt_con DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_local_evt_con IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `RAP Demo: Local Consumption of ` && 
      `RAP Business Events (Database Modifications)` ). 
 
    "RAP create operation 
    MODIFY ENTITY demo_rap_local_evt_m 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH VALUE #( ( %cid      = 'cid1' 
                      key_field = 1 
                      field1    = 'aaa' 
                      field2    = 'bbb' 
                      field3    = 11 
                      field4    = 111 ) 
                    ( %cid      = 'cid2' 
                      key_field = 2 
                      field1    = 'ccc' 
                      field2    = 'ddd' 
                      field3    = 22 
                      field4    = 222 ) 
                    ( %cid      = 'cid3' 
                      key_field = 3 
                      field1    = 'eee' 
                      field2    = 'fff' 
                      field3    = 33 
                      field4    = 333 ) 
                    ( %cid      = 'cid4' 
                      key_field = 4 
                      field1    = 'ggg' 
                      field2    = 'hhh' 
                      field3    = 44 
                      field4    = 444 ) ) 
      FAILED DATA(f1). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
********************************************************************** 
 
    "RAP update operation 
    MODIFY ENTITY demo_rap_local_evt_m 
      UPDATE FIELDS ( field1 field2 field3 field4 ) 
      WITH VALUE #( ( key_field = 2 
                      field1    = 'iii_up' 
                      field2    = 'jjj_up' 
                      field3    = 222 
                      field4    = 22 ) 
                    ( key_field = 3 
                      field1    = 'kkk_up' 
                      field2    = 'lll_up' 
                      field3    = 333 
                      field4    = 33 ) ) 
     FAILED DATA(f2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
********************************************************************** 
 
    "RAP delete operation 
    MODIFY ENTITY demo_rap_local_evt_m 
     DELETE FROM VALUE #( ( key_field = 4 ) ) 
     FAILED DATA(f3). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
********************************************************************** 
 
    "Note: Due to the asynchronous call of the events, a WAIT statement 
    "is included to wait for messages that are raised by events to be 
    "written to a database table so that they can be 
    "displayed here. 
 
    WAIT UP TO 2 SECONDS. 
 
    "Getting and displaying persisted instances 
    SELECT key_field, field1, field2, field3, field4 
     FROM demo_tab_root_5 
     ORDER BY key_field 
     INTO TABLE @DATA(dbtab_entries). 
 
    out->write( `Database table entries after the RAP operations` 
      )->write( dbtab_entries ). 
 
    "Getting and displaying database table entries that were inserted 
    "in the event handler method implementations to demonstrate that 
    "events have been triggered. 
 
    SELECT id, details, created_at 
     FROM demo_tab_evt_log 
     ORDER BY created_at 
     INTO TABLE @DATA(evt_log_entries). 
 
    IF evt_log_entries IS INITIAL. 
      out->write( `There are no entries in the log table.` && 
        ` Try and run the example again.` ). 
    ELSE. 
      out->write( `Log database table entries created by the ` && 
        `raised events` 
        )->write( evt_log_entries ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_tab_root_5. 
    DELETE FROM demo_tab_evt_log. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The example contains three ABAP EML modify requests: a RAP create, update and delete operation. For each of the operations, an event is raised using a [`RAISE ENTITY EVENT`](abapraise_entity_event.md) statement. The events are raised in the [`save_modified`](abaprap_saver_meth_save_modified.md) RAP saver method.

When the events are raised, the [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md), which are implemented in the CCIMP include of the `CL_DEMO_RAP_EVENT_HANDLER` class, are called asynchronously. To demonstrate the effect of the events, a log database table is filled.

In the output of the example, the content of an internal table is displayed that demonstrates the effect of the RAP operations. The internal table is filled by selecting from the database table where the [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) are persisted to. Additionally, the content of an internal table is displayed including the entries that have been inserted into the log database table by the event handler methods.

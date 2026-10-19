---
title: "RAP - RAP Explicit Save Order"
source_file: abenbdl_save_after_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader > RAP - save after"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - RAP Explicit Save Order

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates explicit save order using the two unrelated RAP BOs, `DEMO_RAP_SAVE_AFTER_A` and `DEMO_RAP_SAVE_AFTER_B`. `DEMO_RAP_SAVE_AFTER_A` specifies `save after` and is set to save after `DEMO_RAP_SAVE_AFTER_B`. Both BOs specify `late numbering`.

**Behavior definitions**

`DEMO_RAP_SAVE_AFTER_A`:

``` abap
managed with additional save
implementation in class bp_demo_rap_save_after_a unique;
strict ( 2 );
save after demo_rap_save_after_b;

define behavior for demo_rap_save_after_a
persistent table demo_tab_root_5
lock master
authorization master ( none )
late numbering

{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
}
```

`DEMO_RAP_SAVE_AFTER_B`:

``` abap
managed with additional save
implementation in class bp_demo_rap_save_after_b unique;
strict ( 2 );

define behavior for demo_rap_save_after_b
persistent table demo_tab_root
lock master
authorization master ( none )
late numbering
{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
}
```

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
CLASS cl_demo_rap_save_after DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_save_after IMPLEMENTATION. 
  METHOD main. 
 
    out->write( `Explicit Save Order Demo` ). 
 
    MODIFY ENTITY demo_rap_save_after_a 
        CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
        WITH VALUE #( 
          ( %cid = `cid_a1` 
            field1 = 'aaa' field2 = 'bbb' 
            field3 = 1 field4 = 2 ) 
          ( %cid = `cid_a2` 
            field1 = 'ccc' field2 = 'ddd' 
            field3 = 3 field4 = 4 ) ). 
 
    MODIFY ENTITY demo_rap_save_after_b 
        CREATE FIELDS ( key_field data_field1_root data_field2_root ) 
        WITH VALUE #( 
          ( %cid = `cid_b1` 
            data_field1_root = `eee` data_field2_root = `fff` ) 
          ( %cid = `cid_b2` 
            data_field1_root = `ggg` data_field2_root = `hhh` ) ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_5 
      INTO TABLE @FINAL(db_entries_a). 
    SELECT * FROM demo_tab_root 
      INTO TABLE @FINAL(db_entries_b). 
 
    out->write( db_entries_a ). 
    out->write( db_entries_b ). 
    "Displaying log table 
    out->write( bp_demo_rap_save_after_a=>log_tab ). 
    "Displaying table with preliminary ID and key values of RAP BO 
    "demo_rap_save_after_b converted in the adjust_numbers 
    "implementation of RAP BO demo_rap_save_after_a 
    out->write( bp_demo_rap_save_after_a=>converted_keys ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
    DELETE FROM demo_tab_root. 
 
    INSERT demo_tab_root_5 FROM TABLE @( VALUE #( 
      ( key_field = 1 field1 = '###' field2 = '###' 
        field3 = 0 field4 = 0 ) 
      ( key_field = 2 field1 = '###' field2 = '###' 
        field3 = 0 field4 = 0 ) ) ). 
 
    INSERT demo_tab_root FROM TABLE @( VALUE #( 
      ( key_field = 7 data_field1_root = '###' 
        data_field2_root = '###' ) 
      ( key_field = 8 data_field1_root = '###' 
        data_field2_root = '###' ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML and ABAP SQL**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business objects from an ABAP class:

- Two ABAP EML `MODIFY` statements create two instances for each RAP BO. The `COMMIT ENTITIES` statement triggers the saving of these instances. Then, ABAP SQL `SELECT` statements retrieve the saved instances from the database.

- The database entries and the content of internal tables that act as log tables are displayed. The constructor of the demo class includes deleting and populating the database tables so that the simplified key assignment in the `adjust_numbers` methods does not work with the same key values for both RAP BOs.

- Context of the log tables:

  - Both BDEFs specify `with additional save`. Consequently, the [ABAP behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md), `BP_DEMO_RAP_SAVE_AFTER_A` and `BP_DEMO_RAP_SAVE_AFTER_B`, include the `save_modified` [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md). **Note:** The [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) scenario does not relate to the `save after` specification in the example. It is used only for demonstration, allowing a log table to be populated when calling the `save_modified` methods.

  - Both implementations of `save_modified` iterate through the created instances, adding an entry with a time stamp to the log table for each instance.

  - When the save sequence for both create operations is triggered, the `save_modified` methods are called. However, due to the explicitly set save order, the `save_modified` method of `DEMO_RAP_SAVE_AFTER_B` is executed before `DEMO_RAP_SAVE_AFTER_A`. This order is reflected in the log table entries. If the save sequencing was not explicitly set, the `save_modified` method of `DEMO_RAP_SAVE_AFTER_A` executes before `DEMO_RAP_SAVE_AFTER_B`.

  - The `adjust_numbers` method implementation of RAP BO `DEMO_RAP_SAVE_AFTER_B` adds `%pid` values to an internal table that is declared in the global class of the ABAP behavior pool. The content of this internal table is accessed in the `adjust_numbers` method implementation of RAP BO `DEMO_RAP_SAVE_AFTER_A`. The `%pid` values are used by a `CONVERT KEY` statement, demonstrating that final keys can be accessed this way. The `%pid` and key values are added to an internal table that is output in the example.

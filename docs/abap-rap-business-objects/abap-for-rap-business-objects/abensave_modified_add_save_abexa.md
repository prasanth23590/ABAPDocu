---
title: "Example for save_modified in a Managed RAP BO with Additional Save"
source_file: abensave_modified_add_save_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods > Examples for RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for save_modified in a Managed RAP BO with Additional Save

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the RAP saver method `save_modified` as well as the use of the BDEF-derived types `TYPE REQUEST FOR CHANGE` and `TYPE REQUEST FOR DELETE` in the context of a managed RAP BO whose BDEF is specified with `with additional save`.

In this simplified example, all changes to the root instance of the demo BO are recorded (i. e. they are additionally saved) in the log table `DEMO_TAB_LOG`. This log table contains the following fields:

| **Log table field**  | **Details**                                                                              |
|----------------------|------------------------------------------------------------------------------------------|
| `change_id`          | Identifier for an individual change. In this case, it is a [UUID](../../abap-glossary/abenuuid_glosry.md). |
| `key_field`          | Key field of the [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md).                     |
| `changing_operation` | Standard operation that has been carried out (`CREATE`, `UPDATE` or `DELETE`).           |
| `changed_field_name` | Name of the RAP BO instance's field that has been created or changed.                    |
| `changed_value`      | Value of a created or changed field of the RAP BO instance.                              |
| `created_at`         | Date and time of the instance data creation, update or deletion.                         |

**Data model**

The CDS data model consists of the root entity ` DEMO_MANAGED_ADDITIONAL_SAVE`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ADDITIONAL_SAVE
  as select from demo_tab_root_3
  {
    key key_field,
        field1,
        field2,
        field3,
        field4
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ADDITIONAL_SAVE` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed with additional save with full data
implementation in class bp_demo_managed_additional_sav unique;
strict(2);

define behavior for DEMO_MANAGED_ADDITIONAL_SAVE
persistent table DEMO_TAB_ROOT_3
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ADDITIONAL_SAV`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ADDITIONAL_SAVCCIMP` of the behavior pool.

The following method is relevant in this example:

- `save_modified`

  At first, several type and variable declarations are available just for demonstration purposes. Among them, there are the [BDEF-derived types](../../abap-glossary/abenrap_derived_type_glosry.md) `TYPE REQUEST FOR CHANGE`, `TYPE REQUEST FOR DELETE`, `TYPE TABLE FOR CHANGE` and `TYPE STRUCTURE FOR CHANGE`. These BDEF-derived types are only relevant in the context of a managed RAP BO with additional save and unmanaged save. Basically, the structures `create` and `update` (that are of type `TYPE REQUEST FOR CHANGE`) as well as `delete` (that is of type `TYPE REQUEST FOR DELETE`) - they contain those instances that are to be created, changed or deleted - are available here by default and can be referred to directly instead of extra variable and type declarations as it is the case in this example. The declarations are followed by further declarations of internal tables that are responsible for storing the input for the log table in the database. `IF` statements then check whether instances have been created, updated or deleted by a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) In doing so, the `%control` structure is used to get information on which fields have been set when creating, updating or deleting the instance. The `IF` statement processing those instances that have been created is implemented as follows: The internal table `lt_log` is filled with the instance data created by the `CREATE` operation. A `LOOP` statement processes the individual instances: The `changing_operation` receives the value `CREATE`. The creation time is logged (`created_at` field). Then the instance data is read into an internal table to handle the `%control` information for certain fields. In this case, it is checked if `field1` is marked as enabled. If so, a [UUID](../../abap-glossary/abenuuid_glosry.md) is created and assigned to the `change_id` field. Since `field1` is affected, the field `changed_field_name` gets the value `field1`. The field `changed_value` receives the value that is provided by the RAP BO consumer. Finally, the entries are added to the internal table `lt_log_c`. The same procedure is done for `field2`. At the end of the `IF` statement, all the entries in the internal table are inserted in the log table on the database (`demo_tab_log`). The `IF` statement processing those instances that have been updated are implemented similarly to above (here, `field3` and `field4` of the entity are used). The `IF` statement for the deleted instances does not take the fields `changed_field_name` and `changed_value` into consideration. They are not relevant.

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
CLASS cl_demo_rap_save_mdfd_add_sav DEFINITION 
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
CLASS cl_demo_rap_save_mdfd_add_sav IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY ENTITY demo_managed_additional_save 
     CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 1 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 2 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 3 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 4 
          %control-field4 = if_abap_behv=>mk-on ) 
        ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @FINAL(dbtab_after_create). 
 
    SELECT change_id, key_field, changing_operation, 
           changed_field_name, changed_value, created_at 
    FROM demo_tab_log ORDER BY key_field 
    INTO TABLE @FINAL(log_tab_after_create). 
 
    out->begin_section( `Demo for TYPE REQUEST FOR CHANGE/DELETE` 
      )->next_section( `CREATE operation` 
      )->write_text( 'DB table entries after the CREATE operation' 
      )->write( dbtab_after_create 
      )->write_text( 
      'Entries in the log table after the CREATE operation' 
      )->write( log_tab_after_create ). 
 
********************************************************************* 
 
    MODIFY ENTITY demo_managed_additional_save 
     UPDATE FROM VALUE #( 
        ( key_field = 1 
          field1 = 'update_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 5 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 6 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 2 
          field1 = 'update_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 7 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 8 
          %control-field4 = if_abap_behv=>mk-on ) 
        ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @FINAL(dbtab_after_update). 
 
    SELECT change_id, key_field, changing_operation, 
           changed_field_name, changed_value, created_at 
    FROM demo_tab_log ORDER BY key_field 
    INTO TABLE @FINAL(log_tab_after_update). 
 
    out->line( 
      )->next_section( `UPDATE operation` 
      )->write_text( 'DB table entries after the UPDATE operation' 
      )->write( dbtab_after_update 
      )->write_text( 
      'Entries in the log table after the UPDATE operation' 
      )->write( log_tab_after_update ). 
 
********************************************************************* 
 
    MODIFY ENTITY demo_managed_additional_save 
     DELETE FROM VALUE #( ( key_field = 2 ) ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @FINAL(dbtab_after_delete). 
 
    SELECT change_id, key_field, changing_operation, 
           changed_field_name, changed_value, created_at 
    FROM demo_tab_log ORDER BY key_field 
    INTO TABLE @FINAL(log_tab_after_delete). 
 
    out->line( 
      )->next_section( `DELETE operation` 
      )->write_text( 'DB table entries after the DELETE operation' 
      )->write( dbtab_after_delete 
      )->write_text( 
      'Entries in the log table after the DELETE operation' 
      )->write( log_tab_after_delete ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_log. 
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

- An ABAP EML `CREATE` operation is carried out. Two instances are created. The save sequence is triggered by the `COMMIT ENTITIES` statement. The underlying BDEF includes the syntax `with unmanaged save`. Thus, the ABP method `save_modified` is called in this example that saves certain entries to a log table in the database as described above.

- The `CREATE` operation is followed by an `UPDATE` operation that modifies the two previously created instances. The changes get committed as well.

- Finally, one of the existing instances is deleted via a `DELETE` operation. Another commit deletes the instance.

- The output window shows the result of all three operations. For each operation, an internal table is displayed showing the entries of the database table. Another internal table shows the entries of the log table as a result of the implementations in the `save_modified` method.

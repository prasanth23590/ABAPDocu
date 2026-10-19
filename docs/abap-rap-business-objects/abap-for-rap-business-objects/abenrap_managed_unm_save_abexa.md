---
title: "ABAP EML - TYPE REQUEST FOR in a Managed RAP BO with Unmanaged Save"
source_file: abenrap_managed_unm_save_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > TYPE REQUEST FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - TYPE REQUEST FOR in a Managed RAP BO with Unmanaged Save

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the BDEF-derived types `TYPE REQUEST FOR CHANGE` and `TYPE REQUEST FOR DELETE` in the context of a managed RAP BO whose BDEF is specified with [`with unmanaged save`](../rap-behavior-definitions/abenbdl_saving.md). The saving of created, changed or deleted [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) is user-implemented in the `save_modified` method of the [ABP](../../abap-glossary/abenbehavior_pool_glosry.md).

**Data model**

The CDS data model consists of the root entity ` DEMO_MANAGED_UNMANAGED_SAVE`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_UNMANAGED_SAVE
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_UNMANAGED_SAVE` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed with unmanaged save
implementation in class bp_demo_managed_unmanaged_save unique;
strict ( 2 );

define behavior for DEMO_MANAGED_UNMANAGED_SAVE
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_UNMANAGED_SAVE`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_UNMANAGED_SAVECCIMP` of the behavior pool.

The following method is relevant in this example:

- `save_modified`

  At first, several type and variable declarations are available just for demonstration purposes. Among them, there are the [BDEF-derived types](../../abap-glossary/abenrap_derived_type_glosry.md) `TYPE REQUEST FOR CHANGE`, `TYPE REQUEST FOR DELETE`, `TYPE TABLE FOR CHANGE` and `TYPE STRUCTURE FOR CHANGE`. These BDEF-derived types are only relevant in the contexts of a managed RAP BO [`with additional save`](../rap-behavior-definitions/abenbdl_saving.md) and a managed RAP BO [`with unmanaged save`](../rap-behavior-definitions/abenbdl_saving.md). Basically, the structures `create` and `update` (that are of type `TYPE REQUEST FOR CHANGE`) as well as `delete` (that is of `TYPE REQUEST FOR DELETE`) - they contain those instances that are to be created, changed or deleted - are available here by default and can actually be referred to directly instead of extra variable and type declarations as it is the case in this example. The declarations are followed by a further declaration of an internal table (`lt_tab`) that acts as a helper table to temporarily store the instances that are to be created, changed or deleted. `IF` statements then check whether instances have been created, updated or deleted by a RAP BO consumer. In doing so, the `%control` structure is used to get information on which fields have been set when creating, updating or deleting the instance. The `IF` statement for the created instances is implemented as follows: The internal table `lt_tab` is filled with the instance data created by the `CREATE` operation. A `LOOP` statement processes the individual instances. The data field values only get written to the internal table `lt_tab` if the data fields are not disabled for the operation in the `%control` structure. At the end of the `IF` statement, all the entries in the table `lt_tab` are saved to the database table `demo_tab_root_3` using an ABAP SQL `MODIFY` statement. The `IF` statement processing those instances that have been updated is implemented similarly to above. However, to make sure that the update operation does not write blanks to the internal table `lt_tab`, an ABAP SQL `SELECT` statement gets all existing entries of the database table `demo_tab_root_3` at first. Hence, if a value for a particular data field is not provided or the field is marked as disabled in the `%control` structure, the already existing field value is taken over and not overwritten with an initial value. The `IF` statement for the deleted instances deletes the entries from the database table using an ABAP SQL `DELETE` statement.

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
CLASS cl_demo_rap_managed_unm_save DEFINITION 
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
CLASS cl_demo_rap_managed_unm_save IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY ENTITY demo_managed_unmanaged_save 
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
 
    out->begin_section( 
      `Demo for a managed RAP BO with unmanaged save` 
      )->next_section( `CREATE operation` 
      )->write_text( 'DB table entries after the CREATE operation' 
      )->write( dbtab_after_create 
      ). 
 
********************************************************************** 
 
    MODIFY ENTITY demo_managed_unmanaged_save 
     UPDATE FROM VALUE #( 
        ( key_field = 1 
          field1 = 'update_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_2' 
          %control-field2 = if_abap_behv=>mk-off 
          field3 = 5 
          %control-field3 = if_abap_behv=>mk-off 
          field4 = 6 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 2 
          field1 = 'update_3' 
          %control-field1 = if_abap_behv=>mk-off 
          field2 = 'update_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 7 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 8 
          %control-field4 = if_abap_behv=>mk-off ) 
        ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @FINAL(dbtab_after_update). 
 
    out->line( 
      )->next_section( `UPDATE operation` 
      )->write_text( 'DB table entries after the UPDATE operation' 
      )->write( dbtab_after_update 
      ). 
 
********************************************************************** 
 
    MODIFY ENTITY demo_managed_unmanaged_save 
     DELETE FROM VALUE #( ( key_field = 2 ) ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @FINAL(dbtab_after_delete). 
 
    out->line( 
      )->next_section( `DELETE operation` 
      )->write_text( 'DB table entries after the DELETE operation' 
      )->write( dbtab_after_delete 
      ). 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
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

- An ABAP EML `CREATE` operation is carried out. Two instances are created. The save sequence is triggered by the `COMMIT ENTITIES` statement. The underlying BDEF includes the syntax `with unmanaged save`. Thus, the ABP method `save_modified` is called in this example that saves the instances to the database table `demo_tab_root_3` as described in section **Behavior implementation**.

- The `CREATE` operation is followed by an `UPDATE` operation that modifies the two previously created instances. The changes get committed as well. Some of the fields are disabled in the `%control` structure (using `if_abap_behv=>mk-off`). Hence, the existing field values are not changed.

- Finally, one of the existing instances is deleted via a `DELETE` operation. Another commit triggers the deletion of the instance.

- The output window shows the result of all three operations. For each operation, an internal table is displayed showing the entries of the database table.

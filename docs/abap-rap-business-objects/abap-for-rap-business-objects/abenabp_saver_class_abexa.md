---
title: "Example for RAP Saver Methods"
source_file: abenabp_saver_class_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods > Examples for RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for RAP Saver Methods

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates RAP saver methods within a RAP saver class using a simple unmanaged RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_UNMANAGED_ROOT` and its child entity `DEMO_UNMANAGED_CHILD`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_UNMANAGED_ROOT
  as select from demo_tab_root_3
  composition [1..*] of DEMO_UNMANAGED_CHILD as _child
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
define view entity DEMO_UNMANAGED_CHILD
  as select from demo_tab_child_3
  association to parent DEMO_UNMANAGED_ROOT 
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UNMANAGED_ROOT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class bp_demo_unmanaged_root unique;
strict(2);

define behavior for DEMO_UNMANAGED_ROOT
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  field ( readonly:update ) key_field;
}

define behavior for DEMO_UNMANAGED_CHILD alias child
lock dependent by _parent
authorization dependent by _parent
{
  field ( readonly ) key_field, key_field_child;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UNMANAGED_ROOT`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UNMANAGED_ROOT========CCIMP` of the behavior pool. **Note**: The ABP purposely includes only few handler method implementations since the focus is on the saver methods.

The class `lsc_demo_unmanaged_root` is the RAP saver class that includes the following RAP saver methods:

| **Method**          | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `finalize`          | Triggers any final calculations involving all BOs in the current LUW before the data gets saved to the database. In this example, the method is implemented in a way to do a calculation on a data field. `field3` should be divided by 2. Since the field is of type `i`, a division by 2 with uneven numbers results in an error. In case of an error, the `FAILED` and `reported` parameters get filled. If the division is successful, `field3` receives the result and a success message is included in the `reported` parameter for the particular instance. A log table (`DEMO_TAB_SAVELOG`) is then filled with content of the `failed` (if available) and `reported` structures. The purpose of this log table is to show the returned messages of the `finalize`, `check_before_save` and `save` methods in the output. |
| `check_before_save` | Contains a consistency check. An instance should only get saved if the value of data field `field4` does not exceed *100*. Furthermore, the `failed` and `reported` parameters as well as the log table `DEMO_TAB_SAVELOG` are filled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `save`              | Saves the data from the transactional buffer to the database. The method is only called if the `finalize`, `check_before_save` and `adjust_numbers` methods have been processed successfully. Once the data has been saved, a success message is included in the `reported` parameter and the log table `DEMO_TAB_SAVELOG`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `cleanup`           | Clears the transactional buffer. The method is called if the `save` method has been processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `cleanup_finalize`  | Clears the transactional buffer. The method is called if issues arise in the `finalize` and `check_before_save` methods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

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
CLASS cl_demo_rap_unm_saver_mthds DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED   demo_unmanaged_root, 
      reported TYPE RESPONSE FOR REPORTED demo_unmanaged_root, 
      mapped   TYPE RESPONSE FOR MAPPED demo_unmanaged_root. 
    METHODS: 
      initialize_dbtabs, 
      get_saver_response, 
      get_saver_meth, 
      get_db_entries. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_unm_saver_mthds IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
         `RAP saver methods with an unmanaged RAP BO` 
      )->line( 
      )->next_section( `1st EML MODIFY operation` ). 
 
    MODIFY ENTITY demo_unmanaged_root 
     CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 2 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 4 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 5 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 6 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3' 
          key_field = 3 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_5' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_6' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 7 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 8 
          %control-field4 = if_abap_behv=>mk-on ) 
          ) 
        FAILED   failed 
        REPORTED reported 
        MAPPED mapped. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    get_saver_meth( ). 
    get_saver_response( ). 
    get_db_entries( ). 
 
    out->line( 
       )->next_section( `2nd EML MODIFY operation` ). 
 
    MODIFY ENTITY demo_unmanaged_root 
     CREATE FROM VALUE #( 
        ( %cid = 'cid4' 
          key_field = 4 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_7' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_8' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 10 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 102 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid5' 
          key_field = 5 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_9' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_10' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 12 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 14 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid6' 
          key_field = 6 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_11' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_12' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 16 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 104 
          %control-field4 = if_abap_behv=>mk-on ) 
          ) 
        FAILED   failed 
        REPORTED reported 
        MAPPED mapped. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    get_saver_meth( ). 
    get_saver_response( ). 
    get_db_entries( ). 
 
    out->line( 
      )->next_section( `3rd EML MODIFY operation` ). 
 
    MODIFY ENTITY demo_unmanaged_root 
     CREATE FROM VALUE #( 
        ( %cid = 'cid7' 
          key_field = 7 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_13' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_14' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 18 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 20 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid8' 
          key_field = 8 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_15' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_16' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 22 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 24 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid9' 
          key_field = 9 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_17' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_18' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 26 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 28 
          %control-field4 = if_abap_behv=>mk-on ) ) 
        FAILED   failed 
        REPORTED reported 
        MAPPED mapped. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    get_saver_meth( ). 
    get_saver_response( ). 
    get_db_entries( ). 
 
  ENDMETHOD. 
  METHOD get_db_entries. 
    SELECT * FROM demo_tab_root_3 
    ORDER BY key_field 
    INTO TABLE @DATA(db_tab). 
 
    IF db_tab IS INITIAL. 
      out->write_html( 
      '<b>DB table entries after the operation:</b>' 
    )->write( 'The database table is initial. No entries available.' ). 
 
    ELSE. 
      out->write_html( 
       '<b>c) Database table entries after the operation:</b>' 
        )->write( db_tab ). 
 
    ENDIF. 
    CLEAR db_tab. 
  ENDMETHOD. 
  METHOD get_saver_meth. 
    out->write_html( '<b>a) Saver methods called</b>' 
     )->write( data = bp_demo_unmanaged_root=>saver_meth_called 
               name = `Saver methods` ). 
    CLEAR bp_demo_unmanaged_root=>saver_meth_called. 
  ENDMETHOD. 
  METHOD get_saver_response. 
    out->write_html( 
        '<b>b) Saver methods responses</b>' 
        )->write( bp_demo_unmanaged_root=>saver_log ). 
    CLEAR bp_demo_unmanaged_root=>saver_log. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_child_3. 
    DELETE FROM demo_tab_savelog. 
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

The example demonstrates three different ABAP EML `MODIFY` requests. Each of the `MODIFY` requests includes `CREATE` operations to create three instances. `COMMIT ENTITIES` statements trigger the save sequence.

1.  First `MODIFY` request: The `finalize` method is not processed successfully which prevents the data from being saved.

2.  Second `MODIFY` request: The `finalize` method is processed successfully while the `check_before_save` method is not. The data is not saved.

3.  Third `MODIFY` request: Both `finalize` and `check_before_save` method are processed successfully. As a consequence, the `save` method is called and the data is saved to the database table.

The output shows three sections for each `MODIFY` request:

- A log table including the saver methods that have been called.

- A log table including information that has been returned for `failed` and `reported`.

- A table including the database table entries after the `CREATE` operations. However, the output of the first two `MODIFY` statements does not show the table since the `CREATE` operations cannot be processed successfully on purpose.

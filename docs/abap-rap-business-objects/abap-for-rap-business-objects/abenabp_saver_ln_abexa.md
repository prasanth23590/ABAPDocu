---
title: "Example for RAP Saver Methods (Late Numbering Scenario)"
source_file: abenabp_saver_ln_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods > Examples for RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for RAP Saver Methods (Late Numbering Scenario)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates RAP saver methods within a RAP saver class using a simple unmanaged RAP BO with late numbering to also cover the `adjust_numbers` saver method.

**Data model**

The CDS data model consists of the root entity `DEMO_UMANAGED_ROOT_LATE_NUM2` and its child entity `DEMO_UMANAGED_CHILD_LATE_NUM2`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_umanaged_root_late_num2
  as select from demo_tab_root_3
  composition [1..*] of demo_umanaged_child_late_num2 as _child
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
define view entity demo_umanaged_child_late_num2
  as select from demo_tab_child_3
  association to parent demo_umanaged_root_late_num2 as _parent 
  on $projection.key_field = _parent.key_field
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UMANAGED_ROOT_LATE_NUM2` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class
 bp_demo_umanaged_root_late_nu2 unique;
strict(2);

define behavior for demo_umanaged_root_late_num2
lock master
authorization master ( global )
late numbering
{
  create;
  update;
  delete;
  field ( readonly ) key_field;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_UMANAGED_ROOT_LATE_NU2`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UMANAGED_ROOT_LATE_NU2CCIMP` of the behavior pool. **Note:** The ABP purposely includes only few handler method implementations since the focus is on the saver methods.

The class `lsc_demo_umanaged_root_late_nu` is the RAP saver class that includes the following RAP saver methods:

| **Method**          | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `finalize`          | Triggers any final calculations involving all BOs in the current LUW before the data gets saved to the database. In this example, the method is implemented in a way to do a calculation on a data field. `field3` should be divided by 2. Since the field is of type `i`, a division by 2 with uneven numbers results in an error. In case of an error, the `FAILED` and `reported` parameters get filled. If the division is successful, `field3` receives the result and a success message is included in the `reported` parameter for the particular instance. A log table (`DEMO_TAB_LOG_LN`) is then filled with content of the `failed` (if available) and `reported` structures. The purpose of this log table is to show the returned messages of the `finalize`, `check_before_save` and `save` methods in the output. |
| `check_before_save` | Contains a consistency check. An instance should only get saved if the value of data field `field4` does not exceed *100*. Furthermore, the `failed` and `reported` parameters as well as the log table `DEMO_TAB_LOG_LN` are filled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `adjust_numbers`    | Assigns the final primary keys of the [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). In the given example, a random integer gets assigned. Once the method is called, a point of no return has been reached. The method must ensure that there are no issues with the key assignment. Therefore, a check is implemented to guarantee a random number does not yet exist for instances, neither in the transactional buffer nor in the database table. Furthermore, the `failed` and `reported` parameters as well as the log table `DEMO_TAB_LOG_LN` are filled.                                                                                                                                                                                                                                                           |
| `save`              | Saves the data from the transactional buffer to the database. The method is only called if the `finalize`, `check_before_save` and `adjust_numbers` methods have been processed successfully. Once the data has been saved, a success message is included in the `reported` parameter and the log table `DEMO_TAB_LOG_LN`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `cleanup`           | Clears the transactional buffer. The method is called if the `save` method has been processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `cleanup_finalize`  | Clears the transactional buffer. The method is called if issues arise in the `finalize` and `check_before_save` methods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

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
CLASS cl_demo_rap_unm_saver_mthds_ln DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED demo_umanaged_root_late_num2, 
      reported TYPE RESPONSE FOR REPORTED demo_umanaged_root_late_num2, 
      mapped   TYPE RESPONSE FOR MAPPED demo_umanaged_root_late_num2. 
    METHODS: 
      initialize_dbtabs, 
      get_saver_response, 
      get_saver_meth, 
      get_db_entries. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_unm_saver_mthds_ln IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
    `RAP saver methods with an unmanaged RAP BO (late numbering)` 
      )->line( 
      )->next_section( `1) 1st EML MODIFY request` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
`The first EML MODIFY request includes the creation of several ` && 
`instances. However, the instances are not saved to the ` && 
`database table because the saver method <code>finalize</code> ` && 
`fails for instances. In the given example, the method fails for ` && 
`instances that include uneven numbers in field <code>field3</code>` && 
`. The saver methods that are called for this MODIFY request after ` && 
`triggering the save sequence with <code>COMMIT ENTITIES</code> are` && 
` logged in the first table. The second table is set up to hold ` && 
`entries from the <code>FAILED</code> and <code>REPORTED</code> ` && 
`response structures for the root entity. A third table including ` && 
`saved instances is not displayed since the <code>finalize</code> ` && 
`method fails. The buffer table is cleared when calling the ` && 
`<code>cleanup_finalize</code> method.` ) ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          field1 = 'create_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 2 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 4 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          field1 = 'create_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 5 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 6 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3' 
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
 
********************************************************************** 
 
    out->line( 
       )->next_section( `2) 2nd EML MODIFY request` 
       )->write_doc( cl_demo_output_helper=>get_infobox_html( 
`The second EML MODIFY request includes the creation of several ` && 
`instances, too. However, the instances are not saved to the ` && 
`database table because the saver method ` && 
`<code>check_before_save</code> fails for instances. ` && 
`In the given example, the method fails for ` && 
`instances that include values in field <code>field4</code> that ` && 
`are higher than 100. The saver methods that are called for ` && 
`this MODIFY request after triggering the save sequence with ` && 
`<code>COMMIT ENTITIES</code> are logged in the first table. ` && 
`The second table is set up to hold entries from the ` && 
`<code>FAILED</code> and <code>REPORTED</code> response structures ` && 
`for the root entity. A third table including ` && 
`saved instances is not displayed since the ` && 
`<code>check_before_save</code> method fails for instances. The ` && 
`buffer table is cleared when calling the ` && 
`<code>cleanup_finalize</code> method.` ) ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FROM VALUE #( 
        ( %cid = 'cid4' 
          field1 = 'create_7' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_8' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 10 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 102 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid5' 
          field1 = 'create_9' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_10' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 12 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 14 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid6' 
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
 
********************************************************************** 
 
    out->line( 
      )->next_section( `3) 3rd EML MODIFY request` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
`The third EML MODIFY request includes the creation of several ` && 
`instances, too. All instances are saved to the ` && 
`database table because the saver methods <code>finalize</code> ` && 
`and <code>check_before_save</code> do not return any issues. ` && 
`Since the given example is a late numbering scenario, the ` && 
`<code>adjust_numbers</code> method is called and assigns the key ` && 
`values. Afterwards, the <code>save</code> method takes care of ` && 
`saving all instances to the database table. The saver methods ` && 
` that are called for this MODIFY request after triggering the ` && 
`save sequence with <code>COMMIT ENTITIES</code> are logged ` && 
`in the first table. The second table is set up to hold entries ` && 
`from the <code>FAILED</code> and <code>REPORTED</code> ` && 
`response structures for the root entity. In this case, the ` && 
` 0 values for <code>key_field</code> for <code>finalize</code> ` && 
`and <code>check_before_save</code> as well as the <code>pid</code>` && 
` entry for <code>save</code> can be ignored. ` && 
`The third table includes the instances that are saved to the ` && 
`database table. The buffer table is cleared when calling the ` && 
`<code>cleanup</code> method.` ) ). 
 
    MODIFY ENTITY demo_umanaged_root_late_num2 
     CREATE FROM VALUE #( 
        ( %cid = 'cid7' 
          field1 = 'create_13' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_14' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 18 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 20 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid8' 
          field1 = 'create_15' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_16' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 22 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 24 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid9' 
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
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_3 ORDER BY key_field 
    INTO TABLE @DATA(db_tab). 
 
    IF db_tab IS INITIAL. 
      out->write_html( 
      '<b>c) Database table entries after the operation:</b>' 
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
     )->write( data = bp_demo_umanaged_root_late_nu2=>saver_meth_called 
               name = `Saver methods` ). 
    CLEAR bp_demo_umanaged_root_late_nu2=>saver_meth_called. 
  ENDMETHOD. 
  METHOD get_saver_response. 
 
    out->write_html( 
            '<b>b) Saver log</b>' 
    )->write( bp_demo_umanaged_root_late_nu2=>saver_log_late_num ). 
    CLEAR bp_demo_umanaged_root_late_nu2=>saver_log_late_num. 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_child_3. 
    DELETE FROM demo_tab_log_ln. 
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

1.  First `MODIFY` request: The `finalize` method is not fully processed successfully which prevents the data from being saved.

2.  Second `MODIFY` request: The `finalize` method is processed successfully while the `check_before_save` method is not. The data is not saved.

3.  Third `MODIFY` request: Both `finalize` and `check_before_save` methods are fully processed successfully. As a consequence, the `adjust_numbers` and `save` methods are called and the data is saved to the database table.

The output shows three sections for each `MODIFY` request:

- A log table including the saver methods that have been called.

- A log table including information that has been returned for `FAILED` and `REPORTED`. In all cases, the preliminary ID `%pid` for the instances is included. In case of the final request, the newly assigned keys are included, too.

- A table including the database table entries after the `CREATE` operations. However, the first two `MODIFY` do not show the table since the `CREATE` operations cannot be processed successfully on purpose.

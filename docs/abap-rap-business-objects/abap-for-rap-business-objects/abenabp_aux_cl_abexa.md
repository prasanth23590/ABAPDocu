---
title: "ABP Auxiliary Class"
source_file: abenabp_aux_cl_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > CLASS, FOR BEHAVIOR OF > ABP Auxiliary Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABP Auxiliary Class

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates an ABP auxiliary class.

**Data model**

The CDS data model consists of the root entity `DEMO_AUX_M`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS root view entity'
define root view entity DEMO_AUX_M
  as select from demo_tab_root_8
{
  key key_field,
      field1,
      field2,
      field3,
      field4
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_AUX_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_aux_m unique;
strict ( 2 );
auxiliary class cl_demo_rap_abp_aux_cl;

define behavior for demo_aux_m
persistent table demo_tab_root_8
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
  action div;
  action multiply;
  action powers;
}
```

**Behavior implementation**

For the above BDEF, one [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_AUX_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_AUX_M=================CCIMP` of the behavior pool as well as the auxiliary class `CL_DEMO_RAP_ABP_AUX_CL`.

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
CLASS cl_demo_rap_abp_aux DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS select_from_db. 
    METHODS display_responses. 
    DATA fail TYPE RESPONSE FOR FAILED EARLY demo_aux_m. 
    DATA rep  TYPE RESPONSE FOR REPORTED EARLY demo_aux_m. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_abp_aux IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Demo: ABP Auxiliary Classes` 
      )->write_doc( `<b>Database table entries after ` && 
      `create operation</b>` ). 
 
    MODIFY ENTITY demo_aux_m 
      CREATE FIELDS ( key_field field1 field2 ) 
      WITH VALUE #( "Instances for DIV action 
      ( %cid = 'cid1'  key_field = 1  field1 = 4 field2 = 4 ) 
      ( %cid = 'cid2'  key_field = 2  field1 = 1 field2 = 4 ) 
      ( %cid = 'cid3'  key_field = 3  field1 = 10 field2 = 2 ) 
      ( %cid = 'cid4'  key_field = 4  field1 = 1 field2 = 0 ) 
                    "Instances for POWERS action 
      ( %cid = 'cid5'  key_field = 5  field1 = 2 field2 = 3 ) 
      ( %cid = 'cid6'  key_field = 6  field1 = 4 field2 = 2 ) 
      ( %cid = 'cid7'  key_field = 7  field1 = 5 field2 = 5 ) 
      ( %cid = 'cid8'  key_field = 8  field1 = 1234567 
        field2 = 890123456 ) 
                    "Instances for MULTIPLY action 
      ( %cid = 'cid9'  key_field = 9  field1 = 30 field2 = 3 ) 
      ( %cid = 'cid10' key_field = 10 field1 = 4 field2 = 3 ) 
      ( %cid = 'cid11' key_field = 11 field1 = 12 field2 = 5 ) 
      ( %cid = 'cid12' key_field = 12 field1 = 99999999 
        field2 = 99999999 ) ) 
    MAPPED DATA(mapped) 
    FAILED fail 
    REPORTED rep. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db( ). 
    display_responses( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write_doc( `<b>Database table entries after executing ` && 
    `the DIV action</b>` ). 
 
    MODIFY ENTITY demo_aux_m 
     EXECUTE div 
      FROM VALUE #( ( key_field = 1 ) 
                    ( key_field = 2 ) 
                    ( key_field = 3 ) 
                    ( key_field = 4 ) ) 
     FAILED fail 
     REPORTED rep. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db( ). 
    display_responses( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write_doc( `<b>Database table entries after executing ` && 
    `the POWERS action</b>` ). 
 
 
    MODIFY ENTITY demo_aux_m 
     EXECUTE powers 
      FROM VALUE #( ( key_field = 5 ) 
                    ( key_field = 6 ) 
                    ( key_field = 7 ) 
                    ( key_field = 8 ) ) 
     FAILED fail 
     REPORTED rep. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db( ). 
    display_responses( ). 
    out->line( ). 
 
********************************************************************** 
 
    out->write_doc( `<b>Database table entries after executing ` && 
    `the MULTIPLY action</b>` ). 
 
 
    MODIFY ENTITY demo_aux_m 
     EXECUTE multiply 
      FROM VALUE #( ( key_field = 9 ) 
                    ( key_field = 10 ) 
                    ( key_field = 11 ) 
                    ( key_field = 12 ) ) 
     FAILED fail 
     REPORTED rep. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    select_from_db( ). 
    display_responses( ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_tab_root_8. 
  ENDMETHOD. 
  METHOD select_from_db. 
    SELECT * 
      FROM demo_tab_root_8 
      ORDER BY key_field 
      INTO TABLE @DATA(itab). 
    out->write( itab ). 
  ENDMETHOD. 
  METHOD display_responses. 
    IF fail IS NOT INITIAL. 
      out->write_doc( `FAILED Responses` ). 
      out->write( fail ). 
    ENDIF. 
 
    IF rep IS NOT INITIAL. 
      out->write_doc( `REPORTED Responses` ). 
      out->write( rep ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- First, a RAP create operation is performed. This creates multiple instances.

- Then, an action is performed using some values of the created instances. In this case, the action performs a division of two integer values. The action implementation includes a method call. The method is implemented in an auxiliary class.

  - **Note:** The example here contains an implementation that should be avoided. Completely outsourcing the implementation of methods to an auxiliary class is not recommended. It comes with significant overhead, such as the additional BDEF derived type declarations for method parameters in auxiliary classes. The example is intended only to demonstrate the `IN LOCAL MODE` addition to ABAP EML statements that are possible in auxiliary classes.

- Two more actions are executed. One action performs a multiplication and another one calculates powers. In both cases, the handler method implementation includes method calls that call methods in an auxiliary class. They demonstrate reusable methods in auxiliary classes and that the `IN LOCAL MODE` addition to ABAP EML statements is possible in auxiliary classes.

- `COMMIT ENTITIES` statements follow all operations to persist the created or modified instances to the databases. All data is then retrieved from the database for display. The example output shows the database table entries after the operations, as well as messages available in the `reported` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md).

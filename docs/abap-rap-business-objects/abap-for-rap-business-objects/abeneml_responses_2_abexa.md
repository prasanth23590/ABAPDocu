---
title: "ABAP EML - TYPE RESPONSE FOR"
source_file: abeneml_responses_2_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > TYPE RESPONSE FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - TYPE RESPONSE FOR

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the response parameters `FAILED`, `MAPPED` and `REPORTED` with a simple managed RAP BO. To show content for the responses, errors are intentionally produced in the context of a `MODIFY` statement trying to create new instances.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT` and its child entity `DEMO_MANAGED_CHILD`.

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_custom unique;
strict ( 2 );

define behavior for DEMO_MANAGED_ROOT_CUSTOM
persistent table demo_tab_root_2
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  action calcPercentage
    parameter DEMO_CDS_ABSTRACT_CALCULATE result [1] $self;
  action calculate
    parameter DEMO_CDS_ABSTRACT_CALCULATE result [1] $self;
  field ( readonly : update ) key_field;
  function ( authorization : none ) demo_from_behv_b result [1]
      DEMO_CDS_ABSTRACT_TEXT;
}

define behavior for DEMO_MANAGED_CHILD_CUSTOM
persistent table demo_tab_child_2
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, there is no [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) available.

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
CLASS cl_demo_rap_eml_responses_2 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      mapped   TYPE RESPONSE FOR MAPPED   demo_managed_root, 
      failed   TYPE RESPONSE FOR FAILED   demo_managed_root, 
      reported TYPE RESPONSE FOR REPORTED demo_managed_root. 
    METHODS: 
      initialize_dbtabs, 
      display_dbtabs 
        IMPORTING title TYPE string, 
      display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_responses_2 IMPLEMENTATION. 
  METHOD main. 
 
    MODIFY demo_tab_root FROM TABLE @( VALUE #( 
         ( key_field = 4 
           data_field1_root = 'www' 
           data_field2_root = 'xxx' ) 
         ( 
          key_field = 5 
          data_field1_root = 'yyy' 
          data_field2_root = 'zzz' ) 
         ) ). 
 
    MODIFY ENTITY demo_managed_root 
      CREATE FIELDS ( key_field data_field1_root 
          data_field2_root ) WITH VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          data_field1_root = 'aaa' 
          data_field2_root = 'bbb' ) 
        ( %cid = 'cid2' 
          key_field = 2 
          data_field1_root = 'ccc' 
          data_field2_root = 'ddd' ) 
        ( %cid = 'cid3' 
          key_field = 3 
          data_field1_root = 'eee' 
          data_field2_root = 'fff' ) 
        ( %cid = 'cid4' 
          key_field = 4 
          data_field1_root = 'ggg' 
          data_field2_root = 'hhh' ) 
        ( %cid = 'cid5' 
          key_field = 5 
          data_field1_root = 'iii' 
          data_field2_root = 'jjj' ) 
         ) 
        FAILED   failed 
        MAPPED   mapped 
        REPORTED reported. 
 
    out->begin_section( `Demo for EML Responses` 
     )->write_doc( `Responses for modify operation:` ). 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    display_dbtabs( 
     `Database table entries after modify operation` 
     ). 
 
  ENDMETHOD. 
  METHOD display_dbtabs. 
    SELECT * FROM demo_tab_root 
      ORDER BY key_field ASCENDING 
      INTO TABLE @FINAL(dbtab) . 
    out->next_section( title 
      )->write( dbtab ). 
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
    DELETE FROM demo_tab_root. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

An ABAP EML modify operation is meant to trigger the creation of instances using the keyword `CREATE`. It includes the response structures `ls_fail`, `ls_map` and `ls_report` following the respective keywords `FAILED`, `MAPPED` and `REPORTED` for getting those responses. The structures are declared externally with `TYPE RESPONSE FOR`. The EML modify operation is preceded by an ABAP SQL modify operation that creates some entries in the database table directly. In doing so, the subsequent EML operation runs into errors regarding those entries because the same keys are used. Therefore, the instances with those keys cannot be created and finally not being saved to the database. The saving is triggered by the `COMMIT ENTITIES.` statement.

The instances that cannot be created are reflected in the response structures `ls_fail` and `ls_report`. The mapping information for the successfully created instances is available in `ls_map`. To display all the responses in the output screen, the `display_responses` method comprises the construction and filling of internal tables to hold the returned information for the entity `demo_managed_root`. The information provided in those internal tables is intentionally kept simple and limited. The table for `FAILED` includes the fail cause, content ID and key of the affected instance as well as the affected operation or association (which is indicated by the entry 01). The table for `REPORTED` comprises information about the severity of the incident, content ID and key as well as a message. The table for `MAPPED` includes the content ID and the corresponding key of the instance.

After displaying the responses, the output screen shows an internal table that is filled with the current entries of the database (using a `SELECT` statement in the `display_dbtabs` method). It includes those entries whose creation has successfully been triggered by the EML modify operation as well as those entries having been created by the ABAP SQL statement.

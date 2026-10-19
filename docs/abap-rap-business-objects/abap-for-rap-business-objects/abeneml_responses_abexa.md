---
title: "ABAP EML - Responses"
source_file: abeneml_responses_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - response_param > Examples for Responses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - Responses

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the response parameters that follow the additions `FAILED`, `MAPPED`, and `REPORTED` in a managed RAP BO. The scenario intentionally triggers errors when attempting to modify [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) using the `MODIFY` statement. The output results are displayed for demonstration purposes.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_CUSTOM` and its child entity `DEMO_MANAGED_CHILD_CUSTOM`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT_CUSTOM
  as select from demo_tab_root_2
  composition [1..1] of DEMO_MANAGED_CHILD_CUSTOM 
    as _child
  {
        _child,        
    key demo_tab_root_2.key_field,
        demo_tab_root_2.data_field1_root,
        demo_tab_root_2.data_field2_root,
        demo_tab_root_2.data_field3_root,
        demo_tab_root_2.data_field4_root
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_MANAGED_CHILD_CUSTOM
  as select from demo_tab_child_2
  association to parent DEMO_MANAGED_ROOT_CUSTOM as _parent 
    on $projection.key_field = _parent.key_field
  {
        _parent,
    key demo_tab_child_2.key_field,
        demo_tab_child_2.data_field1_child,
        demo_tab_child_2.data_field2_child,
        demo_tab_child_2.data_field3_child,
        demo_tab_child_2.data_field4_child
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_CUSTOM` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

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

For the above RAP behavior definition, there is an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) available. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_CUSTOM`. This global class implements the local handler class `LHC_DEMO_MANAGED_ROOT_CUSTOM`. The actual implementation takes place in the `BP_DEMO_MANAGED_ROOT_CUSTOM===CCIMP`. The details of the behavior implementation are not relevant for this example since no custom operations are used.

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
CLASS cl_demo_rap_eml_responses DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    CONSTANTS x_true  TYPE abp_behv_flag VALUE '01'. 
    CONSTANTS x_false TYPE abp_behv_flag VALUE '00'. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED   demo_managed_root_custom, 
      mapped   TYPE RESPONSE FOR MAPPED demo_managed_root_custom, 
      reported TYPE RESPONSE FOR REPORTED demo_managed_root_custom. 
    METHODS: 
      initialize_dbtabs, 
      display_dbtabs, 
      display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_responses IMPLEMENTATION. 
  METHOD main. 
 
    "Create data sets for root and child entity 
    MODIFY ENTITY demo_managed_root_custom 
        CREATE FIELDS ( key_field data_field1_root data_field2_root 
          data_field3_root data_field4_root 
        ) WITH VALUE #( 
          (  %cid = 'cid1' 
             key_field = 1 
             data_field1_root = 'aaa' 
             data_field2_root = 'bbb' 
             data_field3_root = 1 
             data_field4_root = 2 ) 
          (  %cid = 'cid2' 
             key_field = 2 
             data_field1_root = 'ccc' 
             data_field2_root = 'ddd' 
             data_field3_root = 3 
             data_field4_root = 4 ) 
                ) 
        CREATE BY \_child FIELDS ( data_field1_child data_field2_child 
          data_field3_child data_field4_child 
        ) WITH VALUE #( 
          ( %cid_ref = 'cid1' 
            %target = VALUE #( ( %cid = 'cid3' 
                                 data_field1_child = 'zzz' 
                                 data_field2_child = 'yyy' 
                                 data_field3_child = 10 
                                 data_field4_child = 20 ) 
                             ) ) 
          ( %cid_ref = 'cid2' 
            %target = VALUE #( ( %cid = 'cid4' 
                                 data_field1_child = 'xxx' 
                                 data_field2_child = 'www' 
                                 data_field3_child = 30 
                                 data_field4_child = 40 ) 
                             ) ) 
                ) 
          FAILED   failed 
          MAPPED mapped 
          REPORTED reported. 
 
    out->begin_section( `1st modification` 
      )->write_html( '<u><b><i>Responses:</i></b></u>' ). 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write_html( 
      '<u><b><i>Result of 1st modification:</i></b></u>' ). 
    display_dbtabs( ). 
 
    "Modify operations on root and child entity 
    MODIFY ENTITIES OF demo_managed_root_custom 
     ENTITY demo_managed_root_custom 
         CREATE FIELDS ( key_field data_field1_root data_field2_root 
         data_field3_root data_field4_root ) WITH VALUE #( 
         (  %cid = 'cid3' 
            key_field = 3 
            data_field1_root = 'eee' 
            data_field2_root = 'fff' 
            data_field3_root = 5 
            data_field4_root = 6 ) 
         (  %cid = 'cid4' 
            key_field = 4 
            data_field1_root = 'ggg' 
            data_field2_root = 'hhh' 
            data_field3_root = 7 
            data_field4_root = 8 ) 
               ) 
     ENTITY demo_managed_root_custom 
         UPDATE FIELDS ( data_field1_root data_field2_root 
         data_field3_root data_field4_root ) WITH VALUE #( 
           ( %cid_ref = 'cid4' 
             data_field1_root = 'iii' 
             data_field2_root = 'jjj' 
             data_field3_root = 9 
             data_field4_root = 10  ) 
           ( key_field = 6 
             data_field1_root = 'kkk' 
             data_field2_root = 'lll' 
             data_field3_root = 11 
             data_field4_root = 12 ) 
               ) 
     ENTITY demo_managed_root_custom 
         DELETE FROM VALUE #( ( %cid_ref = 'cid3'  ) 
                              ( key_field = 7  ) 
                            ) 
     ENTITY demo_managed_root_custom 
        CREATE BY \_child FIELDS ( data_field1_child data_field2_child 
         data_field3_child data_field4_child ) WITH VALUE #( 
          ( %cid_ref = 'cid3' 
            %target = VALUE #( ( %cid = 'cid5' 
                                 data_field1_child = 'vvv' 
                                 data_field2_child = 'uuu' 
                                 data_field3_child = 50 
                                 data_field4_child = 60 ) 
                                  ) ) 
          ( %cid_ref = 'cid4' 
            %target = VALUE #( ( %cid = 'cid6' 
                                 data_field1_child = 'ttt' 
                                 data_field2_child = 'sss' 
                                 data_field3_child = 70 
                                 data_field4_child = 80 ) 
                             ) ) 
               ) 
     ENTITY demo_managed_child_custom 
         UPDATE FIELDS ( 
         data_field1_child data_field2_child 
         data_field3_child data_field4_child ) WITH VALUE #( 
          ( key_field = 2 
            data_field1_child = 'rrr' 
            data_field2_child = 'qqq' 
            data_field3_child = 90 
            data_field4_child = 100 ) 
          ( key_field = 9 
            data_field3_child = 110 
            data_field4_child = 120 ) 
            ) 
         FAILED   failed 
         MAPPED mapped 
         REPORTED reported. 
 
    out->begin_section( `2nd modification` 
      )->write_html( '<u><b><i>Responses:</i></b></u>' ). 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write_html( 
      '<u><b><i>Result of 2nd modification:</i></b></u>' ). 
    display_dbtabs( ). 
 
  ENDMETHOD. 
  METHOD display_dbtabs. 
    SELECT * FROM demo_tab_root_2 
      ORDER BY key_field 
      INTO TABLE @FINAL(modifiy_entity_parent). 
    SELECT * FROM demo_tab_child_2 
      ORDER BY key_field 
      INTO TABLE @FINAL(modifiy_entity_child). 
    out->write( modifiy_entity_parent 
      )->write( modifiy_entity_child ). 
  ENDMETHOD. 
  METHOD display_responses. 
    IF mapped IS NOT INITIAL. 
      out->write_doc( `MAPPED response:` 
        )->write( mapped ). 
    ELSE. 
      out->write_doc( `No MAPPED response.` ). 
    ENDIF. 
 
    IF failed IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed ). 
    ELSE. 
      out->write_doc( `No FAILED response.` ). 
    ENDIF. 
 
    IF reported IS NOT INITIAL. 
      out->write_doc( `REPORTED response:` 
        )->write( reported ). 
    ELSE. 
      out->write_doc( `No REPORTED response.` ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_2. 
    DELETE FROM demo_tab_child_2. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The example covers multiple ABAP EML modify requests. Some of them are successful. For both the root and child entity, there are data sets defined that will cause an error.

As a consequence, apart from the mapping information, the responses for `FAILED` and `REPORTED` that are displayed in the output cover the information of the affected data sets for which errors occurred. Furthermore, tables display the data sets for which the create, update, and delete operations were successful for both the root and child entity.

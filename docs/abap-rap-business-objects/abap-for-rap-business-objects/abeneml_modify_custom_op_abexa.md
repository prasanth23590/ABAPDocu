---
title: "ABAP EML - MODIFY, Nonstandard Operations"
source_file: abeneml_modify_custom_op_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY, Nonstandard Operations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates This example demonstrates how a `MODIFY` statement can be used to access a managed RAP BO and execute an action. The scenario is a simple calculation based on existing values in two columns of a table whose result is inserted in another column.

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

**Action definition**

The action `calculate` triggers a calculation based on the respective math symbol to be inserted by a user. The action has the output parameter `$self` with cardinality 1. In doing so, the parameter `result` returns the same entity instance for which the action is executed.

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_CUSTOM`. This global class implements the local handler class `LHC_DEMO_MANAGED_ROOT_CUSTOM`, which contains the `calculate` method to implement the action. The actual implementation takes place in the `BP_DEMO_MANAGED_ROOT_CUSTOM===CCIMP`:

- The existing values of two columns are read using a `READ` EML statement into the transactional buffer so as to get the numbers for which the calculation is to be carried out.

- Depending on the math symbol provided, the calculation is carried out.

- Using a `MODIFY` EML statement, the fields of a third column are updated with the result of the calculation.

- The output parameter `result` is finally filled so that the calculation result can be displayed in the column.

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
CLASS cl_demo_rap_custom_op_m DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_custom_op_m IMPLEMENTATION. 
  METHOD main. 
 
    DATA(math_symbol) = '+'. 
    cl_demo_input=>new( 
       )->add_field( CHANGING field = math_symbol 
       )->request( ). 
 
    IF math_symbol NE '+' 
      AND math_symbol NE '-' 
      AND math_symbol NE '/' 
      AND math_symbol NE '*'. 
      out->write( 
       'Only the following math symbols are valid: + - * / ' 
       ). 
      RETURN. 
    ENDIF. 
 
    DELETE FROM demo_tab_root_2. 
 
    MODIFY ENTITY demo_managed_root_custom 
    CREATE FIELDS ( key_field data_field3_root ) 
    WITH VALUE #( ( %cid = 'cid1' 
                    key_field = 2 
                    data_field3_root  = 3 ) 
                  ( %cid = 'cid2' 
                    key_field = 6 
                    data_field3_root  = 8 ) 
                ) 
    FAILED DATA(failed) 
    REPORTED DATA(reported). 
 
    TYPES: BEGIN OF structure, 
             key_field        TYPE i, 
             data_field3_root TYPE i, 
             data_field4_root TYPE decfloat16, 
           END OF structure. 
    DATA no_calc TYPE SORTED TABLE OF structure 
      WITH UNIQUE KEY key_field. 
    READ ENTITY  demo_managed_root_custom 
    ALL FIELDS WITH VALUE #( ( key_field = 2 ) ( key_field = 6 ) ) 
    RESULT FINAL(res). 
    MOVE-CORRESPONDING res TO no_calc. 
    out->next_section(  'Values before EXECUTE operation' 
    )->write( no_calc ). 
 
    MODIFY ENTITIES OF demo_managed_root_custom 
    ENTITY demo_managed_root_custom 
      EXECUTE calculate 
      FROM VALUE #( ( key_field = 2 
                      %param-calculation = math_symbol ) 
                    ( key_field = 6 
                      %param-calculation = math_symbol ) ) 
      FAILED failed 
      REPORTED reported. 
 
    COMMIT ENTITIES RESPONSE OF demo_managed_root_custom 
      FAILED FINAL(commit_failed) 
      REPORTED FINAL(commit_reported). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, data_field3_root, data_field4_root 
     FROM demo_tab_root_2 INTO TABLE @FINAL(calc_result). 
 
    out->next_section( 'Values after EXECUTE operation' 
        )->write( calc_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- As initial step in the example, the user is prompted to insert a math symbol on whose basis the calculation is done.

- Using a `MODIFY` statement, demo values (that is, numbers for the calculation) are created. These values are displayed after they were read from the [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) using a `READ` statement.

- The action `calculate` is executed on the instance with the statement `EXECUTE` using the math symbol that has been provided.

- The `result`, `failed`, and `reported` parameters are returned.

- The changes that were performed by the action in the transactional buffer are committed to the database with a `COMMIT ENTITIES` statement.

- A `SELECT` statement is finally used to read the changed data from the persistent table `DEMO_TAB_ROOT_2` to fill the output table. As a result of the action, the third column is filled with the calculation result.

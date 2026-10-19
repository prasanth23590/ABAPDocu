---
title: "RAP - Draft Scope"
source_file: abenbdl_dependent_draft_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Draft Scope

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Using the [dependent draft](../../abap-glossary/abenrap_dependent_draft_bo_glosry.md) functionality in [cross-BO](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenarios, multiple related [business objects](../../abap-glossary/abenbusiness_object_glosry.md) can be edited as a single logical unit of work ([LUW](../../abap-glossary/abenluw_glosry.md)), ensuring consistency across related [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md).

This example demonstrates how to define and implement the dependent draft in a [RAP](../../abap-glossary/abenrap_glosry.md) cross-BO scenario. It consists of two business objects, referred to as BO A and BO B. They are linked with each other through the associations `_to_A` and `_to_B`, as defined in the [data definitions](../../abap-glossary/abencds_data_definition_glosry.md) `DEMO_RAP_R_DEPENDENT_DRAFT_A` and `DEMO_RAP_R_DEPENDENT_DRAFT_B`. BO B holds the keys of BO A in the [field](../../abap-glossary/abenfield_glosry.md) `a_key`.

The dependent draft functionality is implemented in the respective behavior definitions of the [projection layer](../../abap-glossary/abenpresentation_layer_glosry.md) (see below).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [*Draft Scope*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/6a13ef2f6c1499fb90505c1cf3c0be3?version=sap_cross_product_abap).

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

**BO A**

The base BDEF of BO A is the managed RAP behavior definition `DEMO_RAP_R_DEPENDENT_DRAFT_A`.

``` abap
managed implementation in class bp_demo_rap_r_dependent_drafta unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_R_DEPENDENT_DRAFT_A
persistent table demo_dd_a
draft table demo_dd_ad
etag master local_last_changed_at
lock master total etag last_changed_at
authorization master ( none )
{
  field ( readonly, numbering : managed ) a_key;

  create;
  update;
  delete;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;

  association _to_B using DEMO_RAP_R_DEPENDENT_DRAFT_B \_to_A {
    create;
    with draft;
  }
}
```

The projection behavior definition is defined as shown below. It reuses the association `_to_B` from the base BDEF. With the addition `with dependent draft;`, the association gets control over the draft handling of the dependent draft BO.

``` abap
projection;
strict ( 2 );
use draft;

define behavior for DEMO_RAP_C_DEPENDENT_DRAFT_A
use etag
{
  use create;
  use update;
  use delete;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

    use association _to_B {
    create;
    with dependent draft;
  }
}
```

**BO B**

The base BDEF of BO B is the managed RAP behavior definition `DEMO_RAP_R_DEPENDENT_DRAFT_B`. In the header, the statement `with cross associations;` must be added.

``` abap
managed implementation in class bp_demo_rap_r_dependent_draftb unique;
strict ( 2 );
with draft;
with cross associations;

define behavior for DEMO_RAP_R_DEPENDENT_DRAFT_B
persistent table demo_dd_b
draft table demo_dd_bd
etag master local_last_changed_at
lock master total etag last_changed_at
authorization master ( none )

{
  field ( readonly, numbering : managed )
  b_key;
  field ( readonly )
  a_key;


  create;
  update;
  delete;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;

  association _to_A
  {
    create;
    with draft;
    link action linkAction;
    unlink action unlinkAction;
    inverse function inverseFunction;
  }
}
```

The projection behavior definition of BO B is defined as shown below. The statement `use draft as dependent;` defines it as a draft dependent object.

``` abap
projection;
strict ( 2 );
use draft as dependent;

define behavior for DEMO_RAP_C_DEPENDENT_DRAFT_B
{
  //use create;
  use update;
  use delete;

  use association _to_A { with draft; create; }
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
CLASS cl_demo_rap_dependent_draft DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  FINAL 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_dependent_draft IMPLEMENTATION. 
  METHOD main. 
    " Clearing the database tables 
    DELETE FROM demo_dd_a. 
    DELETE FROM demo_dd_b. 
    DELETE FROM demo_dd_ad. 
    DELETE FROM demo_dd_bd. 
 
    " Creating new instance on BO A 
    MODIFY ENTITY demo_rap_c_dependent_draft_a 
           CREATE FIELDS ( char_field ) 
           WITH VALUE #( ( %cid       = 'mycid' 
                           char_field = 'aaa' ) ) 
 
           " Creating related instances on BO B 
           CREATE BY \_to_b 
           FIELDS ( char_field ) 
           WITH VALUE #( 
                         ( %cid_ref   = 'mycid' 
                           %target    = VALUE #( ( %cid = 'mycid2' 
                                             char_field = 'bbb' ) 
                                           ( %cid       = 'mycid3' 
                                             char_field = 'ccc' ) ) ) ) 
 
           FAILED DATA(failed) 
           REPORTED DATA(reported) 
           MAPPED DATA(mapped). 
 
    out->write( mapped ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    " Reading the key of the new instance on BO A 
    TYPES ty_a_key TYPE demo_dd_a-a_key. 
 
    DATA lt_a_key TYPE TABLE OF ty_a_key. 
    DATA ls_a_key TYPE ty_a_key. 
 
    SELECT a_key FROM demo_dd_a ORDER BY PRIMARY KEY 
    INTO TABLE @lt_a_key . 
 
    READ TABLE lt_a_key INTO ls_a_key INDEX 1. 
 
    " Executing edit action on the respective instance on BO A 
    MODIFY ENTITY demo_rap_c_dependent_draft_a 
           EXECUTE edit 
           FROM VALUE #( ( %cid       = 'mycid4' 
                           %key-a_key = ls_a_key ) ) 
           FAILED DATA(failed_edit) 
           REPORTED DATA(reported_edit). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    " Reading the draft table of BO A 
    DATA lt_bo_a_draft_table TYPE TABLE OF demo_dd_ad. 
 
    SELECT * FROM demo_dd_ad 
      INTO TABLE @lt_bo_a_draft_table. 
 
    IF sy-subrc = 0. 
      out->write( lt_bo_a_draft_table ). 
    ELSE. 
      out->write( 'No data found in DEMO_DD_AD.' ). 
    ENDIF. 
 
    " Reading the draft table of BO B 
    DATA lt_bo_b_draft_table TYPE TABLE OF demo_dd_bd. 
 
    SELECT * FROM demo_dd_bd 
      INTO TABLE @lt_bo_b_draft_table. 
 
    IF sy-subrc = 0. 
      out->write( lt_bo_b_draft_table ). 
    ELSE. 
      out->write( 'No data found in DEMO_DD_BD.' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- In the first step, an instance is created on the active table of BO A.

- Using a create-by-association with association `_to_B`, two related instances are created on BO B. These instances are mapped to the instance of BO A through the key field `a_key`, which is stored as foreign key in BO B (see also the console output of the mapped data).

- In the following step, an edit action is executed on the instance on BO A, which sets the existing instance on BO A to draft. The following select statements read the content of the draft tables of both BO A and BO B. The console output shows the content of the draft tables, indicating that the corresponding instances of BO B have also been set to draft with the edit on the instance of BO A.

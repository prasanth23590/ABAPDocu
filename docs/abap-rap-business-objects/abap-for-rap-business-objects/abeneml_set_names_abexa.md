---
title: "ABAP EML - Variants of SET NAMES"
source_file: abeneml_set_names_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP > SET NAMES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - Variants of SET NAMES

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the variants of the `SET NAMES` statement.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_MAP` and its child entity `DEMO_MANAGED_CHILD_MAP`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT_MAP
  as select from demo_tab_root_3
  composition [1..*] of DEMO_MANAGED_CHILD_MAP as _child
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
define view entity DEMO_MANAGED_CHILD_MAP
  as select from demo_tab_child_3
  association to parent DEMO_MANAGED_ROOT_MAP 
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_MAP` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_map unique;
strict(2);

define behavior for DEMO_MANAGED_ROOT_MAP
persistent table demo_tab_root_3
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  association _child { create; }
  field(readonly:update) key_field;

  mapping for demo_struc corresponding
  {
    key_field = b_key_field;
    field1 = b_field1;
    field2 = b_field2;
    field3 = b_field3;
    field4 = b_field4;
  }

  mapping for demo_struc2 control demo_struc2_ctrl corresponding
  {
    key_field = a_key_field control a_ctrl_key_field;
    field1 = a_field1 control a_ctrl_field1;
    field2 = a_field2 control a_ctrl_field2;
    field3 = a_field3 control a_ctrl_field3;
    field4 = a_field4 control a_ctrl_field4;
  }

  mapping for demo_struc3 control demo_struc3_ctrl corresponding
  {
     key_field = z_key_field control z_ctrl_key_field;
     field1 = z_field1 control z_ctrl_field1;
     field2 = z_field2 control z_ctrl_field2;
     field3 = z_field3 control z_ctrl_field3;
     field4 = z_field4 control z_ctrl_field4;
  }
}

define behavior for DEMO_MANAGED_CHILD_MAP alias child
persistent table demo_tab_child_3
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  field(readonly:update) key_field_child;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one ABP (`BP_DEMO_MANAGED_ROOT_MAP`) is created. It is not relevant for the example.

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
CLASS cl_demo_rap_eml_set_names DEFINITION 
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
CLASS cl_demo_rap_eml_set_names IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `SET NAMES Variants` ). 
 
    "Variant: SET NAMES fields FROM FLAGS src. 
    "Example with %control 
    out->write_html( 
       '<b><i>Variant: SET NAMES fields FROM FLAGS src.</i></b>' 
                   ). 
 
    DATA: fields TYPE abp_field_name_tab, 
          src    TYPE STRUCTURE FOR UPDATE demo_managed_root_map. 
 
    src-%control = VALUE #( key_field = if_abap_behv=>mk-on 
                                  field1    = if_abap_behv=>mk-off 
                                  field2    = if_abap_behv=>mk-on 
                                  field3    = if_abap_behv=>mk-on 
                                  field4    = if_abap_behv=>mk-on 
                                ). 
 
    SET NAMES fields FROM FLAGS src. 
 
    "Example with %element 
    DATA: fields2 TYPE abp_field_name_tab, 
          src2    TYPE STRUCTURE FOR REPORTED demo_managed_root_map. 
 
    src2-%element = VALUE #( key_field     = if_abap_behv=>mk-on 
                             field1        = if_abap_behv=>mk-on 
                             field2        = if_abap_behv=>mk-off 
                             field3        = if_abap_behv=>mk-on 
                             field4        = if_abap_behv=>mk-on 
                             %assoc-_child = if_abap_behv=>mk-on 
                           ). 
 
    SET NAMES fields2 FROM FLAGS src2. 
 
    out->write_text( 'Example with %control' 
      )->write( fields 
      )->write_text( 'Example with %element' 
      )->write( fields2 ). 
 
    "Variant: SET NAMES fields FROM FLAGS src MAPPING TYPE p_type. 
    out->write_html( '<b><i>Variant: SET NAMES fields </i></b>' && 
               '<b><i>FROM FLAGS src MAPPING TYPE p_type.</i></b>' 
                   ). 
 
    DATA: fields3 TYPE abp_field_name_tab, 
          src3    TYPE STRUCTURE FOR UPDATE demo_managed_root_map. 
 
    src3-%control = VALUE #( key_field = if_abap_behv=>mk-on 
                             field1    = if_abap_behv=>mk-on 
                             field2    = if_abap_behv=>mk-on 
                             field3    = if_abap_behv=>mk-off 
                             field4    = if_abap_behv=>mk-on 
                           ). 
 
    SET NAMES fields3 FROM FLAGS src3 
      MAPPING TYPE demo_struc. 
 
    out->write( fields3 ). 
 
    "SET NAMES fields FROM FLAGS src MAPPING LIKE var. 
    out->write_html( '<b><i>Variant: SET NAMES fields </i></b>' && 
                     '<b><i>FROM FLAGS src MAPPING LIKE var.</i></b>' 
                   ). 
 
    DATA: fields4 TYPE abp_field_name_tab, 
          src4    TYPE STRUCTURE FOR UPDATE demo_managed_root_map, 
          var     TYPE demo_struc. 
 
    src4-%control = VALUE #( key_field = if_abap_behv=>mk-on 
                             field1    = if_abap_behv=>mk-on 
                             field2    = if_abap_behv=>mk-on 
                             field3    = if_abap_behv=>mk-on 
                             field4    = if_abap_behv=>mk-off 
                           ). 
 
    SET NAMES fields4 FROM FLAGS src4 MAPPING LIKE var. 
 
    out->write( fields4 ). 
 
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

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

For all variants of the `SET NAMES` statement, variables are declared for the field list typed with `ABP_FIELD_NAME_TAB` and for the source that is typed with a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) which includes the `%control` structure. The components of the `%control` structure include a value that is initial and, thus, not contained in the field list.

The field lists for all variants are displayed in an output window. The first variant comprises examples for both `%control` and `%element` for the source.

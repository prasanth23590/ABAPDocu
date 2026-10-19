---
title: "ABAP EML - CORRESPONDING, Type Mapping"
source_file: abeneml_type_mapping_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP > CORRESPONDING, Type Mapping for ABAP EML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - CORRESPONDING, Type Mapping

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates type mapping variants in ABAP EML using the `CORRESPONDING` operator with a simple managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_MAP` and its child entity `DEMO_MANAGED_CHILD_MAP` which is not used in this example.

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

For the above RAP behavior definition, one ABP is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_MAP`. It is not relevant in this example.

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
CLASS cl_demo_rap_eml_type_mapping DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_type_mapping IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      ent_in_tab   TYPE TABLE FOR UPDATE demo_managed_root_map, 
      ent_out_tab  TYPE TABLE FOR READ RESULT demo_managed_root_map, 
      ty1_tab      TYPE STANDARD TABLE OF demo_struc1, 
      ty2_tab      TYPE STANDARD TABLE OF demo_struc2, 
      ty2_ctrl_tab TYPE STANDARD TABLE OF demo_struc2_ctrl, 
      ty3_tab      TYPE STANDARD TABLE OF demo_struc3, 
      ty3_ctrl_tab TYPE STANDARD TABLE OF demo_struc3_ctrl, 
      tmp          TYPE TABLE OF demo_managed_root_map. 
 
    out->begin_section( 
    'Type mapping variants in ABAP EML' & 
    ' using the CORRESPONDING operator' 
                      ). 
 
********************************************************************** 
*MAPPING FROM ENTITY 
********************************************************************** 
 
    CLEAR: ent_in_tab, ty2_tab. 
 
    ent_in_tab = VALUE #( ( key_field = 1 field1 = 'aaa' field2 = 'bbb' 
                            field3 = 1 field4 = 2 ) ). 
 
    out->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ty2_tab` ). 
    ty2_tab = CORRESPONDING #( ent_in_tab MAPPING FROM ENTITY ). 
    out->end_code( `ty2_tab` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
     `<ul><li>The table <code>ent_in_tab</code> shows values of ` && 
     ` the internal table's first line.` && 
     ` It is typed with the input derived type <code>TYPE TABLE FOR` && 
     ` UPDATE</code>.</li><li>The table <code>ty2_tab</code> ` && 
     ` is a non-RAP-native internal table. It shows the result  ` && 
     ` of applying the <code>CORRESPONDING</code> operator with  ` && 
     ` <code>MAPPING FROM ENTITY</code>.</li></ul>` ) 
     )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
     )->write( ty2_tab ). 
 
********************************************************************** 
*MAPPING TO ENTITY 
********************************************************************** 
 
    CLEAR: ent_out_tab, ty3_tab. 
 
    ty3_tab = VALUE #( 
      ( z_key_field = 2 z_field1 = 'ccc' 
        z_field2 = 'ddd' z_field3 = 3 z_field4 = 4 ) ). 
 
    out->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ent_out_tab` ). 
    ent_out_tab = CORRESPONDING #( ty3_tab MAPPING TO ENTITY ). 
    out->end_code( `ent_out_tab` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>ty3_tab</code> ` && 
      ` is a non-RAP-native internal table. It shows values of ` && 
      ` the internal table's first line.` && 
      ` <li>The table <code>ent_out_tab</code> ` && 
      ` is typed with the output derived type <code>TYPE TABLE FOR ` && 
      ` READ RESULT</code> and shows the result  ` && 
      ` of applying the <code>CORRESPONDING</code> operator with  ` && 
      ` <code>MAPPING TO ENTITY</code>.</li></ul>` ) 
      )->write( ty3_tab 
      )->write( data = ent_out_tab[ 1 ]-%data name = 'ent_out_tab' 
      ). 
 
********************************************************************** 
*Syntax for non-BDEF control types 
********************************************************************** 
 
    CLEAR: ty2_tab, ent_in_tab. 
    ent_in_tab = VALUE #( 
        ( key_field = 3 field1 = 'eee' field2 = 'fff' field3 = 5 
          field4 = 6 
          %control = VALUE #( key_field = if_abap_behv=>mk-on 
                              field1    = if_abap_behv=>mk-on 
                              field2    = if_abap_behv=>mk-on 
                              field3    = if_abap_behv=>mk-on 
                              field4    = if_abap_behv=>mk-off ) ) ). 
 
    out->line( 
      )->write_doc( 
      `<b><i>Example: Syntax for control types</i></b>` && 
      `<br/><b>Syntax:</b>` 
      )->begin_code( `ty2_ctrl_tab` ). 
    ty2_tab = CORRESPONDING #( ent_in_tab MAPPING FROM ENTITY ). 
    ty2_ctrl_tab = CORRESPONDING #( ent_in_tab MAPPING FROM ENTITY ). 
    out->end_code( `ty2_ctrl_tab` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<p>Use case: Control information is mapped to a non-BDEF ` && 
      `derived type</p><ul><li>The table <code>ent_in_tab</code> ` && 
      ` is typed with the input derived type <code>TYPE TABLE FOR ` && 
      `UPDATE</code> and shows values of the internal table's first` && 
      ` line.</li><li>The table <code>ent_in_tab_ctrl</code>` && 
      ` shows the %control information of the ` && 
      ` table's first line.</li>` && 
      ` <li><code>ty2_tab</code> is a non-RAP-native` && 
      ` internal table ` && 
      `showing the result of the type mapping after applying the ` && 
      `<code>CORRESPONDING</code> operator with <code>MAPPING FROM` && 
      ` ENTITY</code> taking the control information into` && 
      ` consideration (table <code>ty2_ctrl_tab</code>).</li></ul>` ) 
      )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
      )->write( data = ent_in_tab[ 1 ]-%control name 
           = 'ent_in_tab_ctrl' 
      )->write( ty2_tab 
      )->write( ty2_ctrl_tab ). 
 
*********************************************************************** 
*USING CONTROL 
*********************************************************************** 
 
    CLEAR: ent_in_tab, ty1_tab. 
 
    ent_in_tab = VALUE #( 
      ( key_field = 4 field1 = 'ggg' field2 = 'hhh' 
                       field3 = 7 field4 = 8 
        %control = VALUE #( key_field = if_abap_behv=>mk-on 
                            field1    = if_abap_behv=>mk-off 
                            field2    = if_abap_behv=>mk-on 
                            field3    = if_abap_behv=>mk-on 
                            field4    = if_abap_behv=>mk-on ) ) ). 
 
    out->line( 
    )->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ty1_tab` ). 
    ty1_tab = CORRESPONDING #( ent_in_tab USING CONTROL ). 
    out->end_code( `ty1_tab` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
    `<ul><li>The table <code>ent_in_tab</code> ` && 
    ` is typed with the input derived type <code>TYPE TABLE FOR ` && 
    `UPDATE</code> and shows values of the internal table's first` && 
    ` line.</li><li>The table <code>ent_in_tab_ctrl</code>` && 
    ` shows the %control information of the table's` && 
    ` first line.</li>` && 
    `<li><code>ty1_tab</code> is a non-RAP-native internal table` && 
    ` showing the result of the type mapping after applying the ` && 
    `<code>CORRESPONDING</code> operator with <code>USING CONTROL` && 
    `</code>.</li></ul>` ) 
    )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
    )->write( data = ent_in_tab[ 1 ]-%control name 
          = 'ent_in_tab_ctrl' 
    )->write( ty1_tab ). 
 
*********************************************************************** 
*MAPPING FROM ENTITY USING CONTROL 
*********************************************************************** 
 
    CLEAR: ent_in_tab, ty2_tab. 
 
    ent_in_tab = VALUE #( 
    ( key_field = 5 field1 = 'iii' field2 = 'jjj' 
                    field3 = 9 field4 = 10 
      %control = VALUE #( key_field = if_abap_behv=>mk-on 
                          field1    = if_abap_behv=>mk-on 
                          field2    = if_abap_behv=>mk-off 
                          field3    = if_abap_behv=>mk-on 
                          field4    = if_abap_behv=>mk-on ) ) ). 
 
    out->line( 
    )->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ty2_tab_2` ). 
    ty2_tab = CORRESPONDING #( ent_in_tab MAPPING FROM 
                                          ENTITY USING CONTROL ). 
    out->end_code( `ty2_tab_2` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>ent_in_tab</code> ` && 
      ` is typed with the input derived type <code>TYPE TABLE FOR ` && 
      `UPDATE</code> and shows values of the internal table's first` && 
      ` line.</li><li>The table <code>ent_in_tab_ctrl</code>` && 
      ` shows the %control information of the table's` && 
      ` first line.</li> <code>ty1_tab</code>` && 
      `  is a non-RAP-native internal table showing` && 
      ` the result of the type mapping after applying the ` && 
      `<code>CORRESPONDING</code> operator with <code>MAPPING FROM ` && 
      `ENTITY USING CONTROL</code>.</li></ul>` ) 
      )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
      )->write( data = ent_in_tab[ 1 ]-%control name = 
          'ent_in_tab_ctrl' 
      )->write( ty2_tab ). 
 
*********************************************************************** 
*CHANGING CONTROL 
*********************************************************************** 
 
    CLEAR: ent_in_tab, ty1_tab. 
 
    ty1_tab = VALUE #( 
    "field1 not specified 
    ( key_field = 6  field2 = 'kkk' field3 = 11 field4 = 12 ) ). 
 
    out->line( 
    )->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ent_in_tab_2` ). 
    ent_in_tab = CORRESPONDING #( ty1_tab CHANGING CONTROL ). 
    out->end_code( `ent_in_tab_2` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>ty1_tab</code> ` && 
      `is a non-RAP-native internal table showing values of the` && 
      ` table's first line.</li><li>The table` && 
      ` <code>ent_in_tab</code>` && 
      ` is typed with the input derived type <code>TYPE TABLE FOR ` && 
      `UPDATE</code> and shows values of the internal table's first` && 
      ` line as a result of the type mapping after applying the ` && 
      `<code>CORRESPONDING</code> operator with <code>CHANGING ` && 
      `CONTROL</code></li><li>Likewise, the table` && 
      ` <code>ent_in_tab_ctrl</code> shows the %control information` && 
      ` of the table's first line.</li></ul>` ) 
      )->write( ty1_tab 
      )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
      )->write( data = ent_in_tab[ 1 ]-%control name = 
          'ent_in_tab_ctrl' ). 
 
 
*********************************************************************** 
*CHANGING CONTROL (including a preceding mapping) 
*********************************************************************** 
 
    CLEAR: ent_in_tab, ty2_tab. 
 
    ty2_tab = VALUE #( 
    ( a_key_field = 7 a_field1 = 'lll' a_field3 = 13  a_field4 = 14 ) ). 
 
    out->line( 
    )->write_doc( `<b>Syntax:</b>` 
    )->begin_code( `ent_in_tab_3` ). 
    tmp        = CORRESPONDING #( ty2_tab MAPPING TO ENTITY ). 
    ent_in_tab = CORRESPONDING #( tmp CHANGING CONTROL ). 
    out->end_code( `ent_in_tab_3` ). 
 
    out->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>ty2_tab</code> ` && 
      `is a non-RAP-native internal table showing values ` && 
      ` of the table's first line.` && 
      ` A mapping for the non-BDEF-derived type is done ` && 
      `separately using the helper variable <code>tmp</code>.</li>` && 
      `<li>The table <code>ent_in_tab</code>` && 
      ` is typed with the input derived type <code>TYPE TABLE FOR ` && 
      `UPDATE</code> and shows values of the internal table's first` && 
      ` line as a result of the type mapping after applying the ` && 
      `<code>CORRESPONDING</code> operator with <code>CHANGING ` && 
      `CONTROL</code>.</li><li>Likewise, the table` && 
      ` <code>ent_in_tab_ctrl</code> shows the %control information` && 
      ` of the table's first line.</li></ul>` ) 
       )->write( ty2_tab 
       )->write( data = ent_in_tab[ 1 ]-%data name = 'ent_in_tab' 
       )->write( 
          data = ent_in_tab[ 1 ]-%control name = 'ent_in_tab_ctrl' ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class. The following variants are covered:

- `ntype = CORRESPONDING dtype|#( in_d_type MAPPING FROM ENTITY ).`

  An internal table typed with the input derived type `TYPE TABLE FOR UPDATE` gets filled, i. e. values for data fields are specified for a single line. A non-BDEF-derived type (i. e. a non-RAP-native DDIC type), which has different field names than those of the RAP BO, is given the values using the `CORRESPONDING` operator variant mentioned above. As a prerequisite, a mapping for the non-BDEF-derived type is specified in the BDEF. The output window shows two internal tables with the single line that gets created: one internal table typed with the derived type, the other one with the non-BDEF-derived type.

- `out_d_type = CORRESPONDING dtype|#( ntype MAPPING TO ENTITY ).`

  An internal table typed with a non-BDEF-derived type gets filled, i. e. values for data fields are specified for a single line. The field names differ from those of the RAP BO. An internal table typed with the output derived type `TYPE TABLE FOR READ RESULT` receives the values using the `CORRESPONDING` operator variant mentioned above. As a prerequisite, a mapping for the non-BDEF-derived type is specified in the BDEF. The output window shows two internal tables with the single line that gets created: one internal table typed with the derived type, the other one with the non-BDEF-derived type.

- Excursion: Syntax for non-BDEF control types

  The example uses the variant `MAPPING FROM ENTITY` and includes control information that is available in another non-BDEF-derived type. As a prerequisite, a mapping for the non-BDEF-derived type and the type that holds the control information is specified in the BDEF (`MAPPING ... CONTROL ...`). An internal table typed with the input derived type `TYPE TABLE FOR UPDATE` gets filled, i. e. values for data fields and the `%control` structure are specified. One component of the `%control` structure gets disabled. A non-BDEF-derived type, that has different field names than those of the RAP BO, receives the values using the `CORRESPONDING` operator variant mentioned above. As a second step, the partner control type receives the values from the `%control` structure. The output window shows the one line of the internal table as well as the `%control` structure for the derived type that get created. Likewise, the internal tables for the non-BDEF-derived type and the type control information is displayed demonstrating the effect of applying the `CORRESPONDING` operator variant. The field that is disabled in the `%control` structure is consequently left blank in the table typed with the partner control type.

- `ntype = CORRESPONDING dtype|#( in_d_type USING CONTROL ).`

  An internal table typed with the input derived type `TYPE TABLE FOR UPDATE` gets filled, i. e. values for data fields and the `%control` structure are specified for a single line. One component of the `%control` structure gets disabled. A non-BDEF-derived type, that h same field names as those of the RAP BO, receives the values using the `CORRESPONDING` operator variant mentioned above. Here, the `%control` structure values are taken into consideration. A mapping for the non-BDEF-derived type is not needed in the BDEF in this case. The output window shows the data fields and the `%control` structure values that are specified for the derived type and the effect of applying the `CORRESPONDING` operator variant. The internal table typed with the non-BDEF-derived type receives the values. However, `field1`, which is marked as disabled in the `%control` structure of the derived type, does not contain a value.

- `ntype = CORRESPONDING dtype|#( in_d_type MAPPING FROM ENTITY USING CONTROL ).`

  An internal table typed with the input derived type `TYPE TABLE FOR UPDATE` gets filled, i. e. values for data fields and the `%control` structure are specified for a single line. One component of the `%control` structure gets disabled. A non-BDEF-derived type, that h different field names than those of the RAP BO, receives the values using the `CORRESPONDING` operator variant mentioned above. Here, the `%control` structure values and the mapping are taken into consideration. As a prerequisite, a mapping for the non-BDEF-derived type must be specified in the BDEF in this case. The output window shows the data fields and the `%control` structure values that are specified for the derived type and the effect of applying the `CORRESPONDING` operator variant. The internal table typed with the non-BDEF-derived type receives the values. However, `field2`, which is marked as disabled in the `%control` structure of the derived type, does not contain a value.

- `in_d_type = CORRESPONDING dtype|#( ntype CHANGING CONTROL ).`

  An internal table typed with a non-BDEF-derived type gets filled, i. e. values for data fields are specified for a single line. All data fields are specified except one. An internal table, that is typed with the input derived type `TYPE TABLE FOR UPDATE`, receives the values using the `CORRESPONDING` operator variant mentioned above. Since the non-BDEF-derived type's field names are the those of the RAP BO, a mapping for the non-BDEF-derived type is not need BDEF in this case. The output window shows the values of the data fields of the single line that is created for an internal table typed with a non-BDEF-derived type. The following two tables demonstrate the effect of applying the `CORRESPONDING` operator variant. The internal table typed with derived type receives the values. Due to the fact that a value has not been specified for a field in the non-BDEF-derived type, the `%control` structure of the derived type shows that the particular field is marked as disabled.

- Excursion: Variant with `CHANGING CONTROL` including a preceding mapping

  An internal table typed with a non-BDEF-derived type gets filled, i. e. values for data fields are specified for a single line. All data fields are specified except one. An internal table, that is typed with the input derived type `TYPE TABLE FOR UPDATE`, receives the values using the `CORRESPONDING` operator variant with the addition `USING CONTROl`. The non-BDEF-derived type's field names are different from those of the RAP BO. A mapping for the non-BDEF-derived type is required in the BDEF. The mapping must be done separately in ABAP. In this example, a helper variable typed with the entity type is used for a separate statement with the `CORRESPONDING` operator and the addition `MAPPING TO ENTITY` succeeded by a statement with the addition `CHANGING CONTROL` also using the helper variable. The output shows the values of the data fields of the single line that is created for an internal table typed with a non-BDEF-derived type. The following two tables demonstrate the effect of applying the `CORRESPONDING` operator variant. The internal table typed with derived type receives the values. Due to the fact that a value has not been specified for a field in the non-BDEF-derived type, the `%control` structure of the derived type shows that the particular field is marked as disabled.

---
title: "ABAP SQL Statements with the Addition MAPPING FROM ENTITY"
source_file: abensql_mapping_from_entity_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP > ABAP SQL Statements with MAPPING FROM ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL Statements with the Addition MAPPING FROM ENTITY

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates ABAP SQL statements using the additions `MAPPING FROM ENTITY`. The internal tables and work areas used in the example are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). These types are based on a simple [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

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
CLASS cl_demo_rap_mapping_from_entty DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs, 
      display_dbtab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_mapping_from_entty IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for ABAP SQL addition ` && 
                      `MAPPING FROM ENTITY` 
    )->line( ). 
 
    "INSERT 
    DATA ins_tab TYPE TABLE FOR CREATE demo_managed_root_map. 
    DATA ins_wa TYPE STRUCTURE FOR CREATE demo_managed_root_map. 
    DATA ins_wa2 TYPE STRUCTURE FOR CREATE demo_managed_root_map. 
 
    ins_wa = VALUE #( key_field = 1 
                      field1 = `ins_1` 
                      field2 = `ins_2` 
                      field3 = 100 
                      field4 = 101 ). 
 
    ins_wa2 = VALUE #( key_field = 2 
                       field1 = `ins_3` 
                       field2 = `ins_4` 
                       field3 = 102 
                       field4 = 103 ). 
 
    ins_tab = VALUE #( ( key_field = 3 
                         field1 = `ins_5` 
                         field2 = `ins_6` 
                         field3 = 104 
                         field4 = 105 ) 
                       ( key_field = 4 
                         field1 = `ins_7` 
                         field2 = `ins_8` 
                         field3 = 106 
                         field4 = 107 ) ). 
 
    INSERT demo_tab_root_3 FROM @ins_wa MAPPING FROM ENTITY. 
    INSERT demo_tab_root_3 FROM TABLE @ins_tab MAPPING FROM ENTITY. 
    INSERT INTO demo_tab_root_3 VALUES @ins_wa2 MAPPING FROM ENTITY. 
 
    out->write_doc( `Database table entries after INSERT statements:` ). 
    display_dbtab( ). 
 
    "UPDATE 
    DATA up_tab TYPE TABLE FOR UPDATE demo_managed_root_map. 
    DATA up_wa TYPE STRUCTURE FOR UPDATE demo_managed_root_map. 
 
    up_wa = VALUE #( key_field = 1 
                     field1 = `up_1` 
                     field2 = `up_2` 
                     field3 = 200 
                     field4 = 201 ). 
 
 
    up_tab = VALUE #( ( key_field = 2 
                        field1 = `upd_3` 
                        field2 = `upd_4` 
                        field3 = 202 
                        field4 = 203 ) 
                      ( key_field = 3 
                        field1 = `upd_5` 
                        field2 = `upd_6` 
                        field3 = 204 
                        field4 = 205 ) ). 
 
    UPDATE demo_tab_root_3 FROM @up_wa MAPPING FROM ENTITY. 
    UPDATE demo_tab_root_3 FROM TABLE @up_tab MAPPING FROM ENTITY. 
 
    out->write_doc( `Database table entries after UPDATE statements:` ). 
    display_dbtab( ). 
 
    up_wa = VALUE #( key_field = 1 
                     field1 = `set_7` 
                     field2 = `set_8` 
                     field3 = 206 
                     field4 = 207 
                     %control = VALUE #( 
                                 key_field = if_abap_behv=>mk-on 
                                 field1    = if_abap_behv=>mk-off 
                                 field2    = if_abap_behv=>mk-on 
                                 field3    = if_abap_behv=>mk-off 
                                 field4    = if_abap_behv=>mk-on ) ). 
 
    up_tab = VALUE #( ( key_field = 2 
                        field1 = `set_9` 
                        field2 = `set_10` 
                        field3 = 208 
                        field4 = 209 
                        %control = VALUE #( 
                                    key_field = if_abap_behv=>mk-on 
                                    field1    = if_abap_behv=>mk-on 
                                    field2    = if_abap_behv=>mk-off 
                                    field3    = if_abap_behv=>mk-on 
                                    field4    = if_abap_behv=>mk-off ) 
                       ) 
                       ( key_field = 3 
                         field1 = `set_11` 
                         field2 = `set_12` 
                         field3 = 210 
                         field4 = 211 
                         %control = VALUE #( 
                                     key_field = if_abap_behv=>mk-on 
                                     field1    = if_abap_behv=>mk-off 
                                     field2    = if_abap_behv=>mk-on 
                                     field3    = if_abap_behv=>mk-off 
                                     field4    = if_abap_behv=>mk-on ) 
                       ) ). 
 
    UPDATE demo_tab_root_3 FROM @up_wa 
      INDICATORS SET STRUCTURE %control MAPPING FROM ENTITY. 
 
    UPDATE demo_tab_root_3 FROM TABLE @up_tab 
      INDICATORS SET STRUCTURE %control MAPPING FROM ENTITY. 
 
    out->write_doc( `Database table entries after UPDATE statements ` && 
                  `with the addition INDICATORS SET STRUCTURE:` ). 
    display_dbtab( ). 
 
    "MODIFY 
    DATA mod_tab TYPE TABLE FOR CREATE demo_managed_root_map. 
    DATA mod_wa TYPE STRUCTURE FOR CREATE demo_managed_root_map. 
 
    mod_wa = VALUE #( key_field = 1 
                      field1 = `mod_1` 
                      field2 = `mod_2` 
                      field3 = 300 
                      field4 = 301 ). 
 
 
    mod_tab = VALUE #( ( key_field = 4 
                         field1 = `mod_3` 
                         field2 = `mod_4` 
                         field3 = 302 
                         field4 = 303 ) 
                       ( key_field = 5 
                         field1 = `mod_5` 
                         field2 = `mod_6` 
                         field3 = 304 
                         field4 = 305 ) ). 
 
    MODIFY demo_tab_root_3 FROM @mod_wa MAPPING FROM ENTITY. 
    MODIFY demo_tab_root_3 FROM TABLE @mod_tab MAPPING FROM ENTITY. 
 
    out->write_doc( `Database table entries after MODIFY statements:` ). 
    display_dbtab( ). 
 
    "DELETE 
    DATA del_tab TYPE TABLE FOR DELETE demo_managed_root_map. 
    DATA del_wa TYPE STRUCTURE FOR DELETE demo_managed_root_map. 
 
    del_wa = VALUE #( key_field = 1  ). 
 
    del_tab = VALUE #( ( key_field = 4 ) 
                       ( key_field = 5 ) ). 
 
    DELETE demo_tab_root_3 FROM @del_wa MAPPING FROM ENTITY. 
    DELETE demo_tab_root_3 FROM TABLE @del_tab MAPPING FROM ENTITY. 
 
    out->write_doc( `Database table entries after DELETE statements:` ). 
    display_dbtab( ). 
  ENDMETHOD. 
  METHOD display_dbtab. 
    SELECT * FROM demo_tab_root_3 INTO TABLE @DATA(itab). 
    SORT itab BY key_field ASCENDING. 
    out->write( itab ). 
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

The example shows the four ABAP SQL statements [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), and [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) with the addition `MAPPING FROM ENTITY`. For each statement, a structure and an internal table are filled with sample values. Both structure and internal table are typed with the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR`](abaptype_structure_for.md) and [`TYPE TABLE FOR`](abaptype_table_for.md) respectively. After the statements, a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement is used to retrieve the entries from a database table and insert them into an internal table to visualize the effect of the ABAP SQL statements.

The example for `UPDATE` also shows the addition [`INDICATORS SET STRUCTURE`](../../abap-programming-language/abap-database-access/abapupdate_set_indicator.md).

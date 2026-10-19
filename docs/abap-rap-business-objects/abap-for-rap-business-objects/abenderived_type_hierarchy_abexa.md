---
title: "Using TYPE TABLE/TYPE STRUCTURE FOR HIERARCHY"
source_file: abenderived_type_hierarchy_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > TYPE TABLE FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using TYPE TABLE/TYPE STRUCTURE FOR HIERARCHY

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [actions](../../abap-glossary/abenrap_action_glosry.md) whose [`deep` input parameters](../rap-behavior-definitions/abenbdl_action_input_param.md) and [`deep` output parameters](../rap-behavior-definitions/abenbdl_action_output_para.md) use the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR HIERARCHY`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR HIERARCHY`](abaptype_structure_for.md) with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

**Data model**

The CDS data model consists of the [root entity](../../abap-glossary/abenroot_entity_glosry.md) `DEMO_MANAGED_HIERARCHY`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_HIERARCHY
  as select from demo_tab_root_6
  {
    key id,
        char1,
        char2,
        num1,
        num2
  }
```

Furthermore, the example uses the following abstract entities:

- `DEMO_ABSTRACT_ROOT` (root abstract entity)

- `DEMO_HIER_ABS_ITEM1`

- `DEMO_HIER_ABS_ITEM2`

- `DEMO_HIER_ABS_SCALAR` ([scalar type](../rap-behavior-definitions/abenbdl_define_beh_abstract.md))

- `DEMO_ABSTRACT_ROOT_2` (root abstract entity)

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_HIERARCHY` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_hierarchy unique;
strict(2);

define behavior for DEMO_MANAGED_HIERARCHY
persistent table demo_tab_root_6
lock master
authorization master ( none )

{
  create;
  update;
  delete;

  field ( readonly, numbering : managed ) id;

  // flat
  static action action_flat_param parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  // structure as input parameter
  static action action_deep_param deep parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  // table as input parameter
  static action action_deep_table_param deep table
    parameter DEMO_ABSTRACT_ROOT result [1..*] $self;

  static action storeHData deep parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  static action returnHData deep result [1] DEMO_ABSTRACT_ROOT;

}
```

**Note:** Using the notation `numbering : managed` for the key field, the value of the key field gets automatically created for each RAP BO instance.

Further BDEFs for root abstract entities that are relevant for the example:

- `DEMO_ABSTRACT_ROOT`

- `DEMO_ABSTRACT_ROOT_2`

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_HIERARCHY`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_HIERARCHY=====CCIMP` of the behavior pool.

The following methods are relevant for the example:

- `action_flat_param`

  The method loops at the flat input parameter. In the loop, the components of a structure are filled with values from the input parameter. These values are also changed within the loop. This change includes adding characters to the character fields and a calculation for the numeric fields. The output parameter `result` returns the changed instances. Furthermore, the instances are added to an internal table that is typed with the BDEF derived type [`TYPE TABLE FOR CREATE`](abaptype_table_for.md). This internal table with RAP BO instances is used as input for a [RAP create operation](../../abap-glossary/abenrap_create_operation_glosry.md).

- `action_deep_param`

  The method loops at the deep input parameter which includes a structure of type `TYPE STRUCTURE FOR HIERARCHY`. In the loop, the components of a structure are filled with selected values from the abstract entities. Similar to the previous method, these values are changed. The structure is added to the output parameter `result` and to an internal table on whose bases a RAP create operation is carried out.

- `action_deep_table_param`

  The method loops at the deep input parameter which includes a table of type `TYPE TABLE FOR HIERARCHY`. In the loop, the components of a structure are filled with selected values from the abstract entities. Similar to the previous methods, these values are changed. The structure is added to the output parameter `result` and to an internal table on whose bases a RAP create operation is carried out.

- `returnhdata`

  The method returns hierarchy data. The focus of this method is the use of variables that are typed with either `TYPE TABLE FOR HIERARCHY` or `TYPE STRUCTURE FOR HIERARCHY`. It visualizes how the BDEF derived type component [`%param`](abapderived_types_param.md), which is contained in the output parameter `result`, might be set up, i. e. the component itself can contain subcomponents of type `TYPE TABLE FOR HIERARCHY` and `TYPE STRUCTURE FOR HIERARCHY`. The variables, i. e. the structures and internal tables, are filled with demo data. This data is added to the output parameter `result`.

- `storehdata`

  The method loops at the deep input parameter which includes a structure of type `TYPE STRUCTURE FOR HIERARCHY`. In the loop, an internal table, which is typed with `TYPE TABLE FOR CREATE`, is filled with selected values from the abstract entities. A RAP create operation is carried out creating those instances that have been added to the internal table. Furthermore, the instances are added to the output parameter `result`.

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
CLASS cl_demo_rap_der_types_hrrchy DEFINITION 
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
CLASS cl_demo_rap_der_types_hrrchy IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: TYPE TABLE/STRUCTURE FOR HIERARCHY` ). 
 
    "Prepare input parameter for BDEF derived types ...FOR HIERARCHY... 
    DATA: 
      "Derived types for abstract root entity 
      ls_hier_abs_root 
        TYPE STRUCTURE FOR HIERARCHY demo_abstract_root, 
      lt_hier_abs_root 
        TYPE TABLE FOR HIERARCHY demo_abstract_root, 
      "Derived types for abstract entities 
      ls_hier_abs_item1 
        TYPE STRUCTURE FOR HIERARCHY demo_hier_abs_item1, 
      lt_hier_abs_item2 
        TYPE TABLE FOR HIERARCHY demo_hier_abs_item2, 
      ls_struc 
         TYPE demo_abstract_root. 
 
    "Add hierarchy data. Fill structures and tables. 
    "Create entries for structure to be used as input parameter 
    "for action action_deep_param. 
    ls_struc = VALUE #( char1 = 'f' 
                        char2 = 'para' 
                        num1 = 1 
                        num2 = 2 ). 
 
    ls_hier_abs_item1 = VALUE #( char1 = 'd' 
                                 char2 = 'para' 
                                 num1 = 3 
                                 num2 = 4 
                                 _root2 = VALUE #( 
                                            char1 = 'demo' 
                                            char2 = 'demo' 
                                            num1 = 5 
                                            num2 = 6 ) 
                                 %control = VALUE #( 
                                  char1 = if_abap_behv=>mk-on 
                                  char2 = if_abap_behv=>mk-on 
                                  num1 = if_abap_behv=>mk-on 
                                  num2 = if_abap_behv=>mk-on 
                                  _root2 = if_abap_behv=>mk-on ) 
                                ). 
 
    lt_hier_abs_item2 = VALUE #( %control = VALUE #( 
                                  char1 = if_abap_behv=>mk-on 
                                  char2 = if_abap_behv=>mk-on 
                                  num1 = if_abap_behv=>mk-on 
                                  num2 = if_abap_behv=>mk-on ) 
                                 ( char1 = 'd' 
                                   char2 = 'para' 
                                   num1 = 7 
                                   num2 = 8 ) 
                                 ( char1 = 'd' 
                                   char2 = 'para' 
                                   num1 = 9 
                                   num2 = 10 ) 
                                ). 
 
    ls_hier_abs_root = VALUE #( char1 = ls_struc-char1 
                                char2 = ls_struc-char2 
                                num1 = ls_struc-num1 
                                num2 = ls_struc-num2 
                                _item1 = ls_hier_abs_item1 
                                _item2 = lt_hier_abs_item2 
                                _scalar = 'scalar' 
                                %control = VALUE #( 
                                  char1 = if_abap_behv=>mk-on 
                                  char2 = if_abap_behv=>mk-on 
                                  num1 = if_abap_behv=>mk-on 
                                  num2 = if_abap_behv=>mk-on 
                                  _item1 = if_abap_behv=>mk-on 
                                  _item2 = if_abap_behv=>mk-on 
                                  _scalar = if_abap_behv=>mk-on ) ). 
 
    "Create entries for internal table to be used as input parameter 
    "for action action_deep_table_param. 
    DO 2 TIMES. 
      APPEND ls_hier_abs_root TO lt_hier_abs_root. 
    ENDDO. 
 
********************************************************************** 
    "Executing action_flat_param 
    MODIFY ENTITY demo_managed_hierarchy 
         EXECUTE action_flat_param 
         FROM VALUE #( ( %cid = 'cid_flat' 
                         %param = ls_struc ) ) 
        RESULT FINAL(lt_result1) 
        MAPPED FINAL(ls_mapped1) 
        REPORTED FINAL(ls_reported1) 
        FAILED FINAL(ls_failed1). 
 
    out->write_html( `<b>Executing action ` 
                     && `<i>action_flat_param</i></b>` 
      )->write_doc( `action_flat_param: Action result` 
      )->write( lt_result1 ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_6 INTO TABLE @FINAL(db_tab1). 
 
    out->write_doc( `Database table entries:` 
      )->write( db_tab1 
      )->line( ). 
 
 
********************************************************************** 
    "Executing action_deep_param 
    MODIFY ENTITY demo_managed_hierarchy 
       EXECUTE action_deep_param 
       FROM VALUE #( ( %cid = 'cid_deep_param' 
       "Note: %param is here typed with TYPE STRUCTURE FOR HIERARCHY 
                       %param = ls_hier_abs_root ) ) 
        RESULT FINAL(lt_result2) 
        MAPPED FINAL(ls_mapped2) 
        REPORTED FINAL(ls_reported2) 
        FAILED FINAL(ls_failed2). 
 
    out->write_html( `<b>Executing action ` 
                    && `<i>action_deep_param</i></b>` 
     )->write_doc( `action_deep_param: Action result` 
     )->write( lt_result2 ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_6 INTO TABLE @FINAL(db_tab2). 
 
    out->write_doc( `Database table entries:` 
      )->write( db_tab2 
      )->line( ). 
 
********************************************************************** 
    "Executing action_deep_table_param 
    MODIFY ENTITY demo_managed_hierarchy 
      EXECUTE action_deep_table_param 
         FROM VALUE #( ( %cid = 'cid_deep_table_param' 
         "Note: %param is here typed with TYPE TABLE FOR HIERARCHY 
                         %param = lt_hier_abs_root ) ) 
        RESULT FINAL(lt_result3) 
        MAPPED FINAL(ls_mapped3) 
        REPORTED FINAL(ls_reported3) 
        FAILED FINAL(ls_failed3). 
 
    out->write_html( `<b>Executing action ` 
                    && `<i>action_deep_table_param</i></b>` 
     )->write_doc( `action_deep_table_param: Action result` 
     )->write( lt_result3 ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_6 INTO TABLE @FINAL(db_tab3). 
    out->write_doc( `Database table entries:` 
      )->write( db_tab3 
      )->line( ). 
 
********************************************************************** 
    "Executing returnHData / storeHData 
    MODIFY ENTITY demo_managed_hierarchy 
      EXECUTE returnhdata FROM VALUE #( ( %cid = 'cid_returnHData' ) ) 
        RESULT FINAL(lt_result4) 
        MAPPED FINAL(ls_mapped4) 
        REPORTED FINAL(ls_reported4) 
        FAILED FINAL(ls_failed4). 
 
    out->write_html( `<b>Executing actions ` 
        && `<i>returnHData</i> and <i>storeHData</i></b>` 
     )->write_doc( `returnHData: Action result` 
     )->write( lt_result4 ). 
 
    MODIFY ENTITY demo_managed_hierarchy 
       EXECUTE storehdata FROM CORRESPONDING #( lt_result4 ) 
      RESULT FINAL(lt_result5) 
      MAPPED FINAL(ls_mapped5) 
      REPORTED FINAL(ls_reported5) 
      FAILED FINAL(ls_failed5). 
 
    out->write_doc( `storeHData: Action result` 
     )->write( lt_result5 ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_6 INTO TABLE @FINAL(db_tab4). 
    out->write_doc( `Database table entries:` 
      )->write( db_tab4 ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_6. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The class includes multiple ABAP EML [`MODIFY`](abapmodify_entity_entities.md) requests executing actions. Before the actions are carried out, the input parameters for those actions is prepared. In this case, multiple internal tables and structures that are typed with the BDEF derived types `TYPE TABLE FOR HIERARCHY` or `TYPE STRUCTURE FOR HIERARCHY` respectively are created. The structures and internal tables are filled with demo values to provide input parameters for the actions that have deep parameters. In case of the action `action_deep_param`, the input parameter is a structure. In case of the action `action_deep_table_param`, the input parameter is an internal table. The value assignment just visualizes the hierarchy data and possible components of the BDEF derived types, i. e. multiple types with `FOR HIERARCHY` can occur in those BDEF derived types.

The following ABAP EML `MODIFY` requests executing actions are covered in the example:

1.  Executing action `action_flat_param`

    A content ID [`%cid`](abapderived_types_cid.md) and a flat parameter `%param` are provided as input parameter. A [`COMMIT ENTITIES`](abapcommit_entities.md) statement saves the RAP BO instances to the database. The result of the action is output based on the method implementation mentioned above. The database table entries are retrieved using a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement and displayed as well.

2.  Executing action `action_deep_param`

    A content ID [`%cid`](abapderived_types_cid.md) and a deep parameter `%param` are provided as input parameter. Here, `%param` is a structure. A [`COMMIT ENTITIES`](abapcommit_entities.md) statement saves the RAP BO instances to the database. The result of the action is output based on the method implementation mentioned above. The database table entries are retrieved using a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement and output as well.

3.  Executing action `action_deep_table_param`

    A content ID [`%cid`](abapderived_types_cid.md) and a deep parameter `%param` are provided as input parameter. Here, `%param` is an internal table. A [`COMMIT ENTITIES`](abapcommit_entities.md) statement saves the RAP BO instances to the database. The result of the action is output based on the method implementation mentioned above. The database table entries are displayed, too.

4.  Executing actions `returnhdata` and `storehdata`

    A content ID [`%cid`](abapderived_types_cid.md) is provided as input parameter for the `returnhdata` method. The method returns data based on the method implementation mentioned above. This data is used as input parameter for the `storehdata` method which includes a RAP create operations that create RAP BO instances. A [`COMMIT ENTITIES`](abapcommit_entities.md) statement saves the RAP BO instances to the database. The result of both actions is displayed as well as the database table entries.

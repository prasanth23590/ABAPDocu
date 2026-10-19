---
title: "ABAP EML - GET PERMISSIONS, only_clause"
source_file: abenget_perm_only_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS > Examples for ABAP EML GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - GET PERMISSIONS, only_clause

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates all variants of the `only_clause` with a simple managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_MANAGED_ROOT_3` and its child entity `DEMO_MANAGED_CHILD_3`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT_3
  as select from demo_tab_root_2
  composition [1..1] of DEMO_MANAGED_CHILD_3 as _child
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
define view entity DEMO_MANAGED_CHILD_3
  as select from demo_tab_child_2
  association to parent DEMO_MANAGED_ROOT_3 as _parent 
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_3` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_3 unique;
strict;

define behavior for DEMO_MANAGED_ROOT_3
persistent table DEMO_TAB_ROOT_2
lock master
//global + instance authorization
authorization master ( global, instance )
{
  create;
  //dynamic global feature control
  update( features : global );
  delete;
  //dynamic instance feature control
  association _child { create( features : instance ); }
  //static feature control
  field ( readonly ) data_field1_root;
  //static feature control
  field ( mandatory ) data_field2_root;
  field ( readonly:update ) key_field;
  //dynamic instance feature control
  field ( features : instance ) data_field3_root, data_field4_root;

  action action;
}

define behavior for DEMO_MANAGED_CHILD_3 alias child
persistent table DEMO_TAB_CHILD_2
lock dependent by _parent
authorization dependent by _parent
{
  field ( readonly ) key_field;
  update;
  delete;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_3`. The actual implementation takes place in the `BP_DEMO_MANAGED_ROOT_3========CCIMP`.

The following methods are relevant for this example:

- `get_instance_features`

  The method returns information on whether certain fields (`data_field3_root` and `data_field4_root`) are read-only or can be modified based on certain conditions. Additionally, information is returned if the creation of instances for an associated entity (`_child`) is enabled or disabled. As a prerequisite in the BDEF, the two fields and the associated entity have the required notation `( features: instance )`.

- `get_global_features`

  The method returns information on whether update operations on entities are allowed or not based on a certain condition, that is, updating is only allowed within a certain time span. As a prerequisite in the BDEF, `update` has the required notation `( features: global )`.

- `get_global_authorizations`

  The method is implemented in a way that create and delete operations are only enabled for users with the appropriate authorizations. In the interest of having a simple demo, the example goes without an authorization object which is, for example, a way to handle the authorization granting in production applications. The variable `auth_flag` represents the authorization that is granted or not. In this case, the permission is not granted. As a prerequisite in the BDEF, the notation `authorization master ( global )` exists. In this example, instance authorizations are also covered, hence, the notation is `authorization master ( global, instance )` in the BDEF.

- `get_instance_authorizations`

  The method returns information on whether delete operations are allowed on instances. In this example, the deletion is not allowed if `data_field2_root` has a particular value. As a prerequisite in the BDEF, the notation `authorization master ( instance )` exists. In this example, global authorizations are also covered, hence, the notation is `authorization master ( global, instance )` in the BDEF.

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
CLASS cl_demo_rap_eml_get_perm_only DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF ls_result_inst, 
             key_field        TYPE i, 
             update           TYPE abp_behv_op_perm, 
             delete           TYPE abp_behv_op_perm, 
             assoc            TYPE abp_behv_op_perm, 
             _key             TYPE abp_behv_field_perm, 
             data_field1_root TYPE abp_behv_field_perm, 
             data_field2_root TYPE abp_behv_field_perm, 
             data_field3_root TYPE abp_behv_field_perm, 
             data_field4_root TYPE abp_behv_field_perm, 
           END OF ls_result_inst, 
           BEGIN OF ls_result_global, 
             create           TYPE abp_behv_op_perm, 
             update           TYPE abp_behv_op_perm, 
             delete           TYPE abp_behv_op_perm, 
             assoc            TYPE abp_behv_op_perm, 
             _key             TYPE abp_behv_field_perm, 
             data_field1_root TYPE abp_behv_field_perm, 
             data_field2_root TYPE abp_behv_field_perm, 
             data_field3_root TYPE abp_behv_field_perm, 
             data_field4_root TYPE abp_behv_field_perm, 
           END OF ls_result_global, 
           tt_result_inst   TYPE TABLE OF ls_result_inst, 
           tt_result_global TYPE TABLE OF ls_result_global, 
           str_type         TYPE STRUCTURE FOR 
                         PERMISSIONS RESULT demo_managed_root_3, 
           inst_tab         TYPE str_type-instances, 
           global_str       TYPE str_type-global. 
    DATA: 
      lt_result_inst   TYPE tt_result_inst, 
      lt_result_global TYPE tt_result_global, 
      request          TYPE STRUCTURE FOR 
                         PERMISSIONS REQUEST demo_managed_root_3. 
    METHODS: 
      initialize_dbtabs, 
      fill_dbtabs, 
      output_tabs IMPORTING i_tab TYPE inst_tab 
                            g_str TYPE global_str. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_get_perm_only IMPLEMENTATION. 
  METHOD main. 
 
    "Set permissions request parameter. 
    request = VALUE #( 
        %create                 = if_abap_behv=>mk-on 
        %update                 = if_abap_behv=>mk-on 
        %assoc-_child           = if_abap_behv=>mk-on 
        %delete                 = if_abap_behv=>mk-on 
        %field-key_field        = if_abap_behv=>mk-on 
        %field-data_field1_root = if_abap_behv=>mk-on 
        %field-data_field2_root = if_abap_behv=>mk-on 
        %field-data_field3_root = if_abap_behv=>mk-on 
        %field-data_field4_root = if_abap_behv=>mk-on 
                ). 
 
    out->begin_section( `GET PERMISSIONS: Variants for only_clause` ). 
 
*********************************************************************** 
 
    "ONLY GLOBAL 
    out->next_section( `ONLY GLOBAL` ). 
 
    GET PERMISSIONS ONLY GLOBAL ENTITY demo_managed_root_3 
      REQUEST request 
      RESULT FINAL(result1) 
      FAILED FINAL(failed1) 
      REPORTED FINAL(reported1). 
 
    output_tabs( i_tab = result1-instances g_str = result1-global ). 
 
********************************************************************** 
 
    "ONLY GLOBAL FEATURES 
    out->next_section( `ONLY GLOBAL FEATURES` ). 
 
    GET PERMISSIONS ONLY GLOBAL FEATURES ENTITY demo_managed_root_3 
      REQUEST request 
      RESULT FINAL(result2) 
      FAILED FINAL(failed2) 
      REPORTED FINAL(reported2). 
 
    output_tabs( i_tab = result2-instances g_str = result2-global ). 
 
********************************************************************** 
 
    "ONLY GLOBAL AUTHORIZATION 
    out->next_section( `ONLY GLOBAL AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY GLOBAL AUTHORIZATION 
      ENTITY demo_managed_root_3 
      REQUEST request 
      RESULT FINAL(result3) 
      FAILED FINAL(failed3) 
      REPORTED FINAL(reported3). 
 
    output_tabs( i_tab = result3-instances g_str = result3-global ). 
 
********************************************************************** 
 
    "ONLY INSTANCE 
    out->next_section( `ONLY INSTANCE` ). 
 
    GET PERMISSIONS ONLY INSTANCE ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result4) 
      FAILED FINAL(failed4) 
      REPORTED FINAL(reported4). 
 
    output_tabs( i_tab = result4-instances g_str = result4-global ). 
 
********************************************************************** 
 
    "ONLY INSTANCE FEATURES 
    out->next_section( `ONLY INSTANCE FEATURES` ). 
 
    GET PERMISSIONS ONLY INSTANCE FEATURES ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result5) 
      FAILED FINAL(failed5) 
      REPORTED FINAL(reported5). 
 
    output_tabs( i_tab = result5-instances g_str = result5-global ). 
 
********************************************************************** 
 
    "ONLY INSTANCE AUTHORIZATION 
    out->next_section( `ONLY INSTANCE AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY INSTANCE AUTHORIZATION 
      ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result6) 
      FAILED FINAL(failed6) 
      REPORTED FINAL(reported6). 
 
    output_tabs( i_tab = result6-instances g_str = result6-global ). 
 
********************************************************************** 
 
    "ONLY FEATURES 
    out->next_section( `ONLY FEATURES` ). 
 
    GET PERMISSIONS ONLY FEATURES ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result7) 
      FAILED FINAL(failed7) 
      REPORTED FINAL(reported7). 
 
    output_tabs( i_tab = result7-instances g_str = result7-global ). 
 
*********************************************************************** 
 
    "ONLY AUTHORIZATION 
    out->next_section( `ONLY AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY AUTHORIZATION ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result8) 
      FAILED FINAL(failed8) 
      REPORTED FINAL(reported8). 
 
    output_tabs( i_tab = result8-instances g_str = result8-global ). 
 
********************************************************************** 
 
    "ONLY dyn_tab 
    out->next_section( `ONLY dyn_var` ). 
 
    GET PERMISSIONS ONLY (if_abap_behv=>permissions_only-authorization) 
     ENTITY demo_managed_root_3 
     FROM VALUE #( ( %key-key_field = 1 ) 
                   ( %key-key_field = 2 ) ) 
     REQUEST request 
     RESULT FINAL(result9) 
     FAILED FINAL(failed9) 
     REPORTED FINAL(reported9). 
 
    output_tabs( i_tab = result9-instances g_str = result9-global ). 
 
  ENDMETHOD. 
  METHOD fill_dbtabs. 
    MODIFY demo_tab_root_2 FROM TABLE @( VALUE #( 
      ( key_field = 1 
        data_field1_root = 'aaa' 
        data_field2_root = 'A' 
        data_field3_root = 15 
        data_field4_root = 3 ) 
      ( key_field = 2 
        data_field1_root = 'bbb' 
        data_field2_root = 'B' 
        data_field3_root = 5 
        data_field4_root = 10 ) 
      ( key_field = 3 
        data_field1_root = 'ccc' 
        data_field2_root = 'B' 
        data_field3_root = 20 
        data_field4_root = 2 ) 
      ) ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_2. 
    DELETE FROM demo_tab_child_2. 
  ENDMETHOD. 
  METHOD output_tabs. 
    out->write( `Entries in INSTANCE table:` ). 
    LOOP AT i_tab ASSIGNING FIELD-SYMBOL(<ls_res_inst>). 
      APPEND VALUE #( 
         key_field        = <ls_res_inst>-key_field 
         update           = <ls_res_inst>-%update 
         delete           = <ls_res_inst>-%delete 
         assoc            = <ls_res_inst>-%assoc-_child 
         _key             = <ls_res_inst>-%field-key_field 
         data_field1_root = <ls_res_inst>-%field-data_field1_root 
         data_field2_root = <ls_res_inst>-%field-data_field2_root 
         data_field3_root = <ls_res_inst>-%field-data_field3_root 
         data_field4_root = <ls_res_inst>-%field-data_field4_root 
                    ) TO lt_result_inst. 
    ENDLOOP. 
    IF lt_result_inst IS INITIAL. 
      out->write( `No entries for INSTANCE table.` ). 
    ELSE. 
      out->write( lt_result_inst ). 
    ENDIF. 
 
    out->write( `Entries in GLOBAL structure:` ). 
 
    APPEND VALUE #( 
         create           = g_str-%create 
         update           = g_str-%update 
         delete           = g_str-%delete 
         assoc            = g_str-%assoc-_child 
         _key             = g_str-%field-key_field 
         data_field1_root = g_str-%field-data_field1_root 
         data_field2_root = g_str-%field-data_field2_root 
         data_field3_root = g_str-%field-data_field3_root 
         data_field4_root = g_str-%field-data_field4_root 
                ) TO lt_result_global. 
 
    out->write( lt_result_global ). 
 
    CLEAR lt_result_inst. 
    CLEAR lt_result_global. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
    fill_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

The example covers all variants of `only_clause` using the short form of the `GET PERMISSIONS` statement.

As a first step, the database tables that are used in the example are emptied and filled again with demo values as a basis for the example. Request parameters for an entity are then specified. In this case, all fields, operations and one associated entity (the child entity) are enabled. These parameters are used in all `GET PERMISSIONS` statements. All statements use the same input keys (except those statements where specifying the keys is not allowed) and include response parameters that are not used in the example.

The result of the individual `GET PERMISSIONS` statements is displayed on the output screen. For that purpose, internal tables are set up that contain the values from the `instance` table and `global` structure.

Notes on the result, i. e. the entries in the output tables:

- `ONLY GLOBAL`

  There are no entries in the `instance` table, hence, no table is displayed. The `global` structure includes the global authorization (the value `02`, i. e. `IF_ABAP_BEHV=>PERM-O-UNAUTHORIZED`, for the create and delete operation is displayed) and global feature controls (the value of `update` either shows `00` for enabled or `01` for disabled). Furthermore, static information is available, too: The `key_field` (here `_key`) and the field `data_field2_root` show the value `01` (i. e. `mandatory`), the field `data_field1_root` shows the value `02` (i. e. `readonly`) as defined in the BDEF.

- `ONLY GLOBAL FEATURES`

  There are no entries in the `instance` table, hence, no table is displayed. The `global` structure includes the global feature control and static information (see the details of `ONLY GLOBAL`).

- `ONLY GLOBAL AUTHORIZATION`

  There are no entries in the `instance` table, hence, no table is displayed. The `global` structure includes global authorization. The value `02`, i. e. `IF_ABAP_BEHV=>PERM-O-UNAUTHORIZED`, for the create and delete operation is displayed.

- `ONLY INSTANCE`

  The `instance` table includes instance-based authorization and instance-based feature control plus static information. According to the method `get_instance_features`, the value of `assoc` is `01` for the instance with key `1` denoting that the create-by-association operation is disabled in the context of this instance. In contrast to that, the operation is allowed for the instance with key `2` (the value is `00`). The read-only field `data_field1_root` shows the value `02`, i. e.`IF_ABAP_BEHV=>PERM-F-READ_ONLY`. `data_field3_root` and `data_field4_root` show the values of the result after calling the `get_instance_features` method. The instance with the key `2` shows the value `02` for `delete` as a result of calling the method `get_instance_authorizations`. The `global` structure includes the static information as outlined in `ONLY GLOBAL`.

- `ONLY INSTANCE FEATURES`

  The `instance` table includes instance-based feature control. It shows the same values for both `instance` table and `global` structure as in `ONLY INSTANCE` except for the instance-based authorization part (i. e. the instance with the key `2` does not include the result of the delete operation here).

- `ONLY INSTANCE AUTHORIZATION`

  The `instance` table includes instance-based authorization. The instance with the key `2` shows the value `02` for delete as a result of calling the method `get_instance_authorizations`. The instance with the key `1` is not included at all in the result. The `global` structure does not include any relevant values.

- `ONLY FEATURES`

  The `instance` table includes instance-based feature control plus static information (see the details of `ONLY INSTANCE` except for the instance-based authorization part). The `global` structure includes the global feature control and static information (see the details of `ONLY GLOBAL` except for the global authorization part).

- `ONLY AUTHORIZATION`

  The `instance` table includes instance-based authorization (see the details of `ONLY INSTANCE AUTHORIZATION`). The `global` structure includes the global authorization (see the details of `ONLY GLOBAL AUTHORIZATION`).

- `ONLY dyn_spec`

  The result is the same as for `ONLY AUTHORIZATION`. The variant `ONLY AUTHORIZATION` is specified dynamically using the enumeration value of type `T_PERMISSIONS_ONLY` of interface `IF_ABAP_BEHV`.

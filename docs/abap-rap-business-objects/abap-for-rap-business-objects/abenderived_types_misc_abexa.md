---
title: "BDEF Derived Type Components in the Context of Requesting Permissions"
source_file: abenderived_types_misc_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BDEF Derived Type Components in the Context of Requesting Permissions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the various [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) components with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) in the context of requesting permissions using multiple [`GET PERMISSIONS`](abapget_permissions.md) statements with variants of the [`ONLY` clause](abapget_permissions_only_clause.md):

- [`%action`](abapderived_types_action.md)

- [`%assoc`](abapderived_types_assoc.md)

- [`%create`](abapderived_types_create.md)

- [`%delete`](abapderived_types_delete.md)

- [`%features`](abapderived_types_features.md)

- [`%field`](abapderived_types_field.md)

- [`%op`](abapderived_types_op.md)

- [`%perm`](abapderived_types_perm.md)

**Data model**

The CDS data model consists of the [root entity](../../abap-glossary/abenroot_entity_glosry.md) `DEMO_MANAGED_ROOT_PERM` and its [child entity](../../abap-glossary/abenchild_entity_glosry.md) `DEMO_MANAGED_CHILD_PERM`. The child entity is not used in the example.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_MANAGED_ROOT_REPORTED
  as select from demo_tab_root_5
  composition [1..*] of DEMO_MANAGED_CHILD_REPORTED as _child
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_PERM` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_perm unique;
strict;

define behavior for DEMO_MANAGED_ROOT_PERM
persistent table DEMO_TAB_ROOT_5
lock master
authorization master ( global, instance )
{
  create;
  //dynamic global feature control
  update( features : global );
  delete;
  //dynamic instance feature control
  association _child { create( features : instance ); }
  //static feature control
  field ( readonly ) field1;
  field ( readonly:update ) key_field;
  //static feature control
  field ( mandatory ) field2;
  //dynamic instance feature control
  field ( features : instance ) field3, field4;

  action( features : global ) action;
}

define behavior for DEMO_MANAGED_CHILD_PERM
persistent table DEMO_TAB_CHILD_5
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly:update ) key_field, key_field_child;
  association _parent;
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_PERM`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_PERM=====CCIMP` of the behavior pool.

The following methods are relevant for this example:

- `get_instance_features`

  The method returns information on whether certain fields are read-only or can be modified based on certain conditions. Additionally, information is returned if the creation of instances for an associated entity (`_child`) is enabled or disabled. As a prerequisite in the BDEF, the two fields and the associated entity have the required notation `( features: instance )`. In the context of this method, the component `%features` is used.

- `get_global_features`

  The method returns information on whether update operations on entities and the execution of an action are allowed or not based on a certain condition, that is, updating and executing the action is only allowed within a certain time span. As a prerequisite in the BDEF, `update` and the action have the required notation `( features: global )`.

- `get_global_authorizations`

  The method is implemented in a way that create and delete operations are only enabled for users with the appropriate authorizations. In the interest of having a simple demo, the example goes without an authorization object which is, for example, a way to handle the authorization granting in production applications. The variable `auth_flag` represents the authorization that is granted or not. In this case, the permission is not granted. As a prerequisite in the BDEF, the notation `authorization master ( global )` exists. In this example, instance authorizations are also covered, hence, the notation is `authorization master ( global, instance )` in the BDEF.

- `get_instance_authorizations`

  The method returns information on whether delete operations and executions of an action are allowed on instances. In this example, deletion and action execution are not allowed if a field has a particular value. As a prerequisite in the BDEF, the notation `authorization master ( instance )` exists. In this example, global authorizations are also covered, hence, the notation is `authorization master ( global, instance )` in the BDEF. In the context of this method, the component `%op` is used.

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
CLASS cl_demo_rap_drvd_types_perm DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      request     TYPE STRUCTURE FOR 
                    PERMISSIONS REQUEST demo_managed_root_perm, 
      perm_result TYPE STRUCTURE FOR 
                    PERMISSIONS RESULT demo_managed_root_perm. 
    METHODS: 
      initialize_dbtabs, 
      fill_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_perm IMPLEMENTATION. 
  METHOD main. 
 
    "Set permissions request parameter. 
    request = VALUE #( 
        %create          = if_abap_behv=>mk-on 
        %update          = if_abap_behv=>mk-on 
        %delete          = if_abap_behv=>mk-on 
        %assoc-_child    = if_abap_behv=>mk-on 
        %action-action   = if_abap_behv=>mk-on 
        %field-key_field = if_abap_behv=>mk-on 
        %field-field1 = if_abap_behv=>mk-on 
        %field-field2 = if_abap_behv=>mk-on 
        %field-field3 = if_abap_behv=>mk-on 
        %field-field4 = if_abap_behv=>mk-on 
                ). 
 
    out->begin_section( `GET PERMISSIONS: Variants for only_clause` ). 
 
*********************************************************************** 
 
    "ONLY GLOBAL 
    out->next_section( `ONLY GLOBAL` ). 
 
    GET PERMISSIONS ONLY GLOBAL ENTITY demo_managed_root_perm 
      REQUEST request 
      RESULT FINAL(result_only_global) 
      FAILED FINAL(failed1) 
      REPORTED FINAL(reported1). 
 
    out->write( result_only_global ). 
 
********************************************************************** 
 
    "ONLY GLOBAL FEATURES 
    out->next_section( `ONLY GLOBAL FEATURES` ). 
 
    GET PERMISSIONS ONLY GLOBAL FEATURES ENTITY demo_managed_root_perm 
      REQUEST request 
      RESULT FINAL(result_only_global_feat) 
      FAILED FINAL(failed2) 
      REPORTED FINAL(reported2). 
 
    out->write( result_only_global_feat ). 
 
********************************************************************** 
 
    "ONLY GLOBAL AUTHORIZATION 
    out->next_section( `ONLY GLOBAL AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY GLOBAL AUTHORIZATION 
      ENTITY demo_managed_root_perm 
      REQUEST request 
      RESULT FINAL(result_global_auth) 
      FAILED FINAL(failed3) 
      REPORTED FINAL(reported3). 
 
    out->write( result_global_auth ). 
 
********************************************************************** 
 
    "ONLY INSTANCE 
    out->next_section( `ONLY INSTANCE` ). 
 
    GET PERMISSIONS ONLY INSTANCE ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result_only_inst) 
      FAILED FINAL(failed4) 
      REPORTED FINAL(reported4). 
 
    out->write( result_only_inst ). 
 
********************************************************************** 
 
    "ONLY INSTANCE FEATURES 
    out->next_section( `ONLY INSTANCE FEATURES` ). 
 
    GET PERMISSIONS ONLY INSTANCE FEATURES ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result_only_inst_feat) 
      FAILED FINAL(failed5) 
      REPORTED FINAL(reported5). 
 
    out->write( result_only_inst_feat ). 
 
********************************************************************** 
 
    "ONLY INSTANCE AUTHORIZATION 
    out->next_section( `ONLY INSTANCE AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY INSTANCE AUTHORIZATION 
      ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result_only_inst_auth) 
      FAILED FINAL(failed6) 
      REPORTED FINAL(reported6). 
 
    out->write( result_only_inst_auth ). 
 
********************************************************************** 
 
    "ONLY FEATURES 
    out->next_section( `ONLY FEATURES` ). 
 
    GET PERMISSIONS ONLY FEATURES ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 )  ) 
      REQUEST request 
      RESULT FINAL(result_only_feat) 
      FAILED FINAL(failed7) 
      REPORTED FINAL(reported7). 
 
    out->write( result_only_feat ). 
 
*********************************************************************** 
 
    "ONLY AUTHORIZATION 
    out->next_section( `ONLY AUTHORIZATION` ). 
 
    GET PERMISSIONS ONLY AUTHORIZATION ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result_only_auth) 
      FAILED FINAL(failed8) 
      REPORTED FINAL(reported8). 
 
    out->write( result_only_auth ). 
 
*********************************************************************** 
 
    "ONLY AUTHORIZATION 
    out->next_section( `ONLY AUTHORIZATION (focus on %perm` && 
      ` component group)` ). 
 
    GET PERMISSIONS ONLY AUTHORIZATION ENTITY demo_managed_root_perm 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT perm_result 
      FAILED FINAL(failed9) 
      REPORTED FINAL(reported9). 
 
    TYPES: BEGIN OF perm_struc, 
             key             TYPE i, 
             update          TYPE abp_behv_op_perm, 
             delete          TYPE abp_behv_op_perm, 
             action          TYPE abp_behv_op_perm, 
             assoc           TYPE abp_behv_op_perm, 
             field_key_field TYPE abp_behv_field_perm, 
             field_field1    TYPE abp_behv_field_perm, 
             field_field2    TYPE abp_behv_field_perm, 
             field_field3    TYPE abp_behv_field_perm, 
             field_field4    TYPE abp_behv_field_perm, 
           END OF perm_struc. 
 
    DATA perm_tab TYPE TABLE OF perm_struc WITH EMPTY KEY. 
 
    LOOP AT perm_result-instances ASSIGNING FIELD-SYMBOL(<fs>). 
      APPEND VALUE #( 
         key = <fs>-%key-key_field 
         update = <fs>-%perm-%update 
         delete = <fs>-%perm-%delete 
         action = <fs>-%perm-%action-action 
         assoc = <fs>-%perm-%assoc-_child 
         field_key_field = <fs>-%perm-%field-key_field 
         field_field1 = <fs>-%perm-%field-field1 
         field_field2 = <fs>-%perm-%field-field2 
         field_field3 = <fs>-%perm-%field-field3 
         field_field4 = <fs>-%perm-%field-field4 
                     ) TO perm_tab. 
 
    ENDLOOP. 
 
    out->write( perm_tab ). 
  ENDMETHOD. 
  METHOD fill_dbtabs. 
    MODIFY demo_tab_root_5 FROM TABLE @( VALUE #( 
      ( key_field = 1 
        field1 = 'aaa' 
        field2 = 'A' 
        field3 = 15 
        field4 = 3 ) 
      ( key_field = 2 
        field1 = 'bbb' 
        field2 = 'B' 
        field3 = 5 
        field4 = 10 ) 
      ( key_field = 3 
        field1 = 'ccc' 
        field2 = 'B' 
        field3 = 20 
        field4 = 2 ) 
      ) ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
    DELETE FROM demo_tab_child_5. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
    fill_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

The example covers most variants of `only_clause` using the short form of the `GET PERMISSIONS` statement.

As a first step, the database table that is used in the example is emptied and filled again with demo values as a basis for the example. Request parameters for an entity are then specified. In this case, all fields, [standard](../../abap-glossary/abencrud_glosry.md) and [nonstandard operations](../rap-behavior-definitions/abenbdl_nonstandard.md), and an associated entity (the child entity) are enabled. These parameters are used in all `GET PERMISSIONS` statements. All statements use the same input keys (except those statements where specifying the keys is not allowed) and include response parameters that are not used in the example.

The result of the individual `GET PERMISSIONS` statements is displayed in the output showing both `instance` table and `global` structure (see [`TYPE STRUCTURE FOR PERMISSIONS RESULT`](abaptype_structure_for.md)).

Notes on the result, i. e. the entries in the output tables:

- `ONLY GLOBAL`

  There are no entries in the `instance` table. The `global` structure includes the global authorization (the value *02*, i. e. `IF_ABAP_BEHV=>PERM-O-UNAUTHORIZED`, for the create and delete operation), and global feature controls (the values of `%update` and `%action-action` either show `00` for enabled or `01` for disabled). Furthermore, static information is available, too: The fields `%field-key_field` and the field `%field-field2` show the value `01` (i. e. `mandatory`), the field `%field-field1` shows the value `02` (i. e. `readonly`) as defined in the BDEF.

- `ONLY GLOBAL FEATURES`

  There are no entries in the `instance` table. The `global` structure includes the global feature control and static information (see the details above for `ONLY GLOBAL`).

- `ONLY GLOBAL AUTHORIZATION`

  There are no entries in the `instance` table. The `global` structure includes information on global authorization. The value *02*, i. e. `IF_ABAP_BEHV=>PERM-O-UNAUTHORIZED`, for the create and delete operation is displayed.

- `ONLY INSTANCE`

  The `instance` table includes information on instance-based authorization and instance-based feature control plus static information. According to the method `get_instance_features`, the value of `%assoc-_child` is *01* for the instance with key *1* denoting that the create-by-association operation is disabled in the context of this instance. In contrast to that, the operation is allowed for the instance with key *2* (the value is *00*). The read-only field `field-field1` shows the value *02*, i. e.`IF_ABAP_BEHV=>PERM-F-READ_ONLY`. `%field-field3` and `field-field4` show the values of the result after calling the `get_instance_features` method. The instance with the key *2* shows the value *02* for `%delete` as a result of calling the method `get_instance_authorizations`. The `global` structure includes the static information as outlined above for `ONLY GLOBAL`.

- `ONLY INSTANCE FEATURES`

  The `instance` table includes information on instance-based feature control. It shows the same values for both `instance` table and `global` structure as above for `ONLY INSTANCE` except for the instance-based authorization part (i. e. the instance with the key *2* does not include the result of the delete operation here).

- `ONLY INSTANCE AUTHORIZATION`

  The `instance` table includes information on instance-based authorization. The instance with the key *2* shows the value *02* for delete as a result of calling the method `get_instance_authorizations`. The instance with the key *1* is not included at all in the result. The `global` structure does not include any relevant values.

- `ONLY FEATURES`

  The `instance` table includes information on instance-based feature control plus static information (see the details above for `ONLY INSTANCE` except for the instance-based authorization part). The `global` structure includes the global feature control and static information (see the details above for `ONLY GLOBAL` except for the global authorization part).

- `ONLY AUTHORIZATION`

  The `instance` table includes information on instance-based authorization (see the details above for `ONLY INSTANCE AUTHORIZATION`). The `global` structure includes the information on global authorization (see the details above for `ONLY GLOBAL AUTHORIZATION`).

- `ONLY AUTHORIZATION` (focus on `%perm` component group)

  The implementation in the class serves the purpose of visualizing the `%perm` component group that is contained in the permission result of `GET PERMISSIONS` statements and how subcomponents of the result might be referred to. The result is of type [`TYPE STRUCTURE FOR PERMISSIONS RESULT`](abaptype_structure_for.md). In the example, a structure type is set up containing the instance key as well as the subcomponents of `%perm`. An internal table is declared that is filled with the permission result from the `instance` table. The output shows this internal table. The outcome of the permission result corresponds to the entries in the `instance` table from the previous example with `ONLY AUTHORIZATION`.

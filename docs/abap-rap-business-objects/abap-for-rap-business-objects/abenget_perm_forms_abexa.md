---
title: "ABAP EML - GET PERMISSIONS, Short and Long Forms"
source_file: abenget_perm_forms_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS > Examples for ABAP EML GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - GET PERMISSIONS, Short and Long Forms

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the short and long forms of the `GET PERMISSIONS` statement using the addition `ONLY INSTANCE FEATURES`.

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

For the above RAP behavior definition, one ABP is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_3`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_3========CCIMP` of the behavior pool.

The following method is relevant in this example:

- `get_instance_features`

  All variants of `GET PERMISSIONS` used in the example request the permissions for instance features. The method is implemented in a way that returns information on whether certain fields (`data_field3_root` and `data_field4_root`) are read-only or can be modified based on certain conditions. Additionally, information is returned if the creation of instances for an associated entity (`_child`) is disabled or enabled. As a prerequisite in the BDEF, the two fields and the associated entity have the required notation: ` association _child { create( features : instance ); } field ( features : instance ) data_field3_root, data_field4_root;`

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
CLASS cl_demo_rap_eml_get_permission DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      request       TYPE STRUCTURE FOR 
                      PERMISSIONS REQUEST demo_managed_root_3, 
      request_child TYPE STRUCTURE FOR 
                      PERMISSIONS REQUEST demo_managed_child_3. 
    METHODS: 
      initialize_dbtabs, 
      fill_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_get_permission IMPLEMENTATION. 
  METHOD main. 
 
    fill_dbtabs( ). 
 
    "Setting permissions request parameters 
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
 
    request_child = VALUE #( 
        %update                  = if_abap_behv=>mk-on 
        %delete                  = if_abap_behv=>mk-on 
        %field-key_field         = if_abap_behv=>mk-on 
        %field-data_field1_child = if_abap_behv=>mk-on 
        %field-data_field2_child = if_abap_behv=>mk-on 
        %field-data_field3_child = if_abap_behv=>mk-on 
        %field-data_field4_child = if_abap_behv=>mk-on 
                ). 
 
    out->begin_section( 
`GET PERMISSIONS variants using the addition ONLY INSTANCE FEATURES` 
                       ). 
 
********************************************************************** 
    "Short form 
    out->next_section( 
                   `GET PERMISSIONS: Short Form ` 
                       ). 
 
    GET PERMISSIONS ONLY INSTANCE FEATURES ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST  request 
      RESULT   FINAL(result_short) 
      FAILED   FINAL(failed_short) 
      REPORTED FINAL(reported_short). 
 
    out->write( result_short ). 
 
    IF failed_short IS NOT INITIAL. 
      out->write( failed_short ). 
    ENDIF. 
 
    IF reported_short IS NOT INITIAL. 
      out->write( reported_short ). 
    ENDIF. 
 
 
*********************************************************************** 
 
    "Long form 
    out->next_section( 
                   `GET PERMISSIONS: Long Form ` 
                       ). 
 
    GET PERMISSIONS ONLY INSTANCE FEATURES OF demo_managed_root_3 
      ENTITY demo_managed_root_3 
        FROM VALUE #( ( %key-key_field = 3 ) 
                      ( %key-key_field = 4 ) ) 
        REQUEST request 
        RESULT  FINAL(result_long_root) 
      ENTITY child 
        FROM VALUE #( ( %key-key_field = 3 ) 
                      ( %key-key_field = 4 ) ) 
        REQUEST request_child 
        RESULT  FINAL(result_long_child) 
      FAILED   FINAL(failed_long) 
      REPORTED FINAL(reported_long). 
 
    out->write( result_long_root ). 
 
    out->write( result_long_child ). 
 
    IF failed_long IS NOT INITIAL. 
      out->write( failed_long ). 
    ENDIF. 
 
    IF reported_long IS NOT INITIAL. 
      out->write( reported_long ). 
    ENDIF. 
 
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
       data_field2_root = 'A' 
       data_field3_root = 4 
       data_field4_root = 16 ) 
     ( key_field = 4 
       data_field1_root = 'ddd' 
       data_field2_root = 'B' 
       data_field3_root = 20 
       data_field4_root = 2 ) 
     ( key_field = 5 
       data_field1_root = 'eee' 
       data_field2_root = 'A' 
       data_field3_root = 1 
       data_field4_root = 17 ) 
     ( key_field = 6 
       data_field1_root = 'fff' 
       data_field2_root = 'B' 
       data_field3_root = 21 
       data_field4_root = 4 ) 
     ) ). 
 
    MODIFY demo_tab_child_2 FROM TABLE @( VALUE #( 
        ( key_field = 1 
          data_field1_child = 'ggg' 
          data_field2_child = 'A' 
          data_field3_child = 15 
          data_field4_child = 3 ) 
        ( key_field = 2 
          data_field1_child = 'hhh' 
          data_field2_child = 'B' 
          data_field3_child = 5 
          data_field4_child = 10 ) 
        ( key_field = 3 
          data_field1_child = 'iii' 
          data_field2_child = 'B' 
          data_field3_child = 20 
          data_field4_child = 2 ) 
        ( key_field = 4 
          data_field1_child = 'jjj' 
          data_field2_child = 'B' 
          data_field3_child = 20 
          data_field4_child = 2 ) 
        ( key_field = 5 
          data_field1_child = 'kkk' 
          data_field2_child = 'B' 
          data_field3_child = 20 
          data_field4_child = 2 ) 
        ( key_field = 6 
          data_field1_child = 'lll' 
          data_field2_child = 'B' 
          data_field3_child = 20 
          data_field4_child = 2 ) 
        ) ). 
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

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

Using the short and long form of the `GET PERMISSIONS` statement, permissions are requested for specific instances of an entity. The addition `ONLY INSTANCE FEATURES` is used in each of the statements to get the permissions, as the name implies, for the instance feature controls only.

As a first step, the database tables that are used in the example are emptied and filled again with demo values as a basis for the example. Request parameters for the root and child entity are then specified. In this case, all fields, operations and one associated entity (the child entity) are enabled. These parameters are used in all `GET PERMISSIONS` statements.

**Short form**

- The `GET PERMISSIONS` statement considers certain instances with keys that are specified after the keyword `FROM`. The `request` parameter has been specified before. The result parameter is of type `TYPE STRUCTURE FOR PERMISSIONS RESULT` and created inline. Response parameters are also specified, however, they are not used in the example.

- When executing the class and when the compiler reaches the `GET PERMISSIONS` statements, the method `get_instance_features` is called that fills the `result` accordingly.

- Notes on the result, i. e. the content in the output tables:

  - Entries in the `instance` table: The entries for the instance with key *1* show that the field `assoc` has the value *01*. According to the implementation, a create-by-association operation is disabled in this case. The entries for both instances with the keys *1* and *2* show the value *02* (that is, read-only) for the data field `data_field1_root` since it was defined as `readonly` in the BDEF. It is a static feature control also displayed in this context (see the [Guidelines for the Permission Result](abapget_permissions_rules.md)). The entries for `data_field3_root` and `data_field4_root` are determined by the `get_instance_features` method. The value *00* is available if the permission is unrestricted, *02* if the permissions is read-only.

  - Entries in the `global` structure: The result also contains static information (see the [Guidelines for the Permission Result](abapget_permissions_rules.md)). In this example, it is as follows: The key `key_field` shows the value *20* (that is, `readonly:update`) and the field `data_field2_root` shows the value *01* (i. e. `mandatory`), the field `data_field1_root` shows the value *02* (i. e. `readonly`) as defined in the BDEF.

**Long form**

- The `GET PERMISSIONS` statement includes requests for the root entity and the child entity individually.

- Result for the root entity:

  It is the same request as in the short form on the root entity, yet using different keys. Consequently, the output is similar to the one of the short form. Since the values of the instances are different, the values of `data_field3_root` and `data_field4_root` are arranged differently in the result after calling the implemented method.

- Result for the child entity:

  Similar to above, request parameters have been specified before, certain instances with specified keys are considered (following the keyword `FROM`) and the result parameter is declared inline. Response parameters are declared, too, but not relevant in the example. Notes on the result, i. e. the content in the output tables for the child entity:

  - Entries in the `instance` table: The key field of the child entity has the value *02* (i. e. unauthorized) which means a create-by-association operations is disabled in the context of the particular instance.

  - Entries in the `global` structure: The result also contains static information. Hence, the field for the key of the child entity shows the value *02* (i. e. read-only) as defined in the BDEF (`readonly`).

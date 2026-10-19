---
title: "Example for Message-Related BDEF Derived Type Components"
source_file: abenderived_types_reported_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Examples for BDEF Derived Type Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for Message-Related BDEF Derived Type Components

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of the following message-related [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) components with a [managed](../rap-behavior-definitions/abenbdl_impl_type.md) [RAP BO](../../abap-glossary/abenrap_bo_glosry.md):

- [`%element`](abapderived_types_element.md)

- [`%global`](abapderived_types_global.md)

- [`%msg`](abapderived_types_msg.md)

- [`%other`](abapderived_types_other.md)

- [`%own`](abapderived_types_own.md)

- [`%path`](abapderived_types_path.md)

- [`%state_area`](abapderived_types_state_area.md)

## More Information

See more details on message handling in the Development Guide for the ABAP RESTful Application Programming Model, section [Messages](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ac74189b5cae49c1b091f04393bac069?version=sap_cross_product_abap).

**Data model**

The CDS data model consists of the [root entity](../../abap-glossary/abenroot_entity_glosry.md) `DEMO_MANAGED_ROOT_REPORTED` and its [child entity](../../abap-glossary/abenchild_entity_glosry.md) `DEMO_MANAGED_CHILD_REPORTED`.

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

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_MANAGED_CHILD_REPORTED
  as select from demo_tab_child_5
  association to parent DEMO_MANAGED_ROOT_REPORTED 
  as _parent on $projection.key_field = _parent.key_field
  {
        _parent,
    key key_field,
    key key_field_child,
        ch_field1,
        ch_field2,
        ch_field3,
        ch_field4
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_MANAGED_ROOT_REPORTED` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_managed_root_reported unique;
strict(2);

define behavior for DEMO_MANAGED_ROOT_REPORTED
persistent table DEMO_TAB_ROOT_5
lock master
authorization master ( global )
{
  create;
  update;
  delete;
  association _child { create; }
  field(readonly:update) key_field;
}

define behavior for DEMO_MANAGED_CHILD_REPORTED
persistent table DEMO_TAB_CHILD_5
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) key_field;
  association _parent;
  validation ValidateNum on save { field ch_field1; create; }
  field(readonly:update) key_field_child;

}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_REPORTED`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_MANAGED_ROOT_REPORTED=CCIMP` of the behavior pool.

The following methods are relevant for the example:

- `get_global_authorizations`

  The method is implemented in a way that RAP create, update and delete operations are only enabled for users with the appropriate authorizations. In the interest of having a simple demo, the example goes without an authorization object which is, for example, a way to handle the authorization granting in production applications. The variable `auth_flag` represents the authorization that is granted or not. In this case, the permission for the operations is granted and the [`reported`](abaptype_response_for.md) response parameter is filled by adding a message to the `%msg` component. Furthermore, the components [`%create`](abapderived_types_create.md), [`%update`](abapderived_types_update.md) and [`%delete`](abapderived_types_delete.md) are filled in case the respective `requested_authorizations` parameter is marked as enabled. The `%global` component is marked as enabled, too, because the message is a [RAP transition message](../../abap-glossary/abenrap_trans_mes_glosry.md) and, thus, related to a specific entity of the business object. For demonstration purposes, a RAP unbound message is added to the `%other` component in the context of this method.

- `validatenum`:

  It contains the method implementation for a [validation](../rap-behavior-definitions/abenbdl_validations.md). The validation checks whether the value of a number of a RAP BO instance field in the child entity is between the values of two numbers of two fields in the root entity. If this is not the case, the validation fails and the `failed` and `reported` response parameters are filled. Since `reported` is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md), the `%own` component is available and used in the example, although it is optional here, to refer to the child entity. The `%path`, `%element` and `%state_area` components are also filled. Before looping at the RAP BO instances, the state area is invalidated. For demonstration purposes, a RAP unbound message is added to the `%other` component in the context of this method.

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
CLASS cl_demo_rap_drvd_types_repo DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      reported_late  TYPE RESPONSE FOR REPORTED LATE 
        demo_managed_root_reported, 
      reported_early TYPE RESPONSE FOR REPORTED EARLY 
        demo_managed_root_reported. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_drvd_types_repo IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo for BDEF derived type components ` && 
    `relating to REPORTED messages` 
    )->line( 
    )->next_section( `RAP create operation` ). 
 
    MODIFY ENTITY demo_managed_root_reported 
       CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
          WITH VALUE #( 
            ( %cid = 'cid1' %key-key_field = 1 
              field1 = 'aaa' field2 = 'bbb' field3 = 10 field4 = 20 ) 
            ( %cid = 'cid2' %key-key_field = 2 
              field1 = 'ccc' field2 = 'ddd' field3 = 20 field4 = 40 ) 
            ( %cid = 'cid3' %key-key_field = 3 
              field1 = 'eee' field2 = 'fff' field3 = 30 field4 = 60 ) 
            ( %cid = 'cid4' %key-key_field = 4 
              field1 = 'ggg' field2 = 'hhh' field3 = 40 field4 = 80 ) 
            ( %cid = 'cid5' %key-key_field = 5 
              field1 = 'iii' field2 = 'jjj' field3 = 50 field4 = 100 ) 
            ) 
           MAPPED FINAL(map) 
           FAILED FINAL(fail) 
           REPORTED reported_early. 
 
    out->write( reported_early ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
    FROM demo_tab_root_5 
    ORDER BY key_field 
    INTO TABLE @FINAL(root_tab). 
 
    out->write_html( 
        `<b>Database table entries ` && 
        `after the operations</b>` 
       )->write( root_tab 
       )->line( 
       )->next_section( `RAP create-by-association operation (1)` ). 
 
    MODIFY ENTITY demo_managed_root_reported 
       CREATE BY \_child FIELDS ( key_field_child ch_field1 
              ch_field2 ch_field3 ch_field4 ) WITH VALUE #( 
            ( %key-key_field = 1 
              %target = VALUE #( 
                       ( %cid = 'cid_child1' 
                         key_field_child = 10 
                         ch_field1 = 'kkk' 
                         ch_field2 = 'lll' 
                         ch_field3 = 15 
                         ch_field4 = 30 
                     ) ) ) 
            ( %key-key_field = 2 
              %target = VALUE #( 
                       ( %cid = 'cid_child2' 
                         key_field_child = 20 
                         ch_field1 = 'mmm' 
                         ch_field2 = 'nnn' 
                         ch_field3 = 25 
                         ch_field4 = 50 
                     ) ) ) 
          ( %key-key_field = 3 
              %target = VALUE #( 
                       ( %cid = 'cid_child3' 
                         key_field_child = 30 
                         ch_field1 = 'ooo' 
                         ch_field2 = 'ppp' 
                         ch_field3 = 35 
                         ch_field4 = 70 
                     ) ) ) 
                     ) 
           MAPPED FINAL(map2) 
           FAILED FINAL(fail2) 
           REPORTED reported_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_managed_root_reported 
      REPORTED reported_late. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write( reported_late ). 
 
    SELECT key_field, key_field_child, ch_field1, ch_field2, 
      ch_field3, ch_field4 
      FROM demo_tab_child_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(child_tab). 
 
    out->write_html( 
            `<b>Database table entries ` && 
            `after the operations</b>` 
      )->write( child_tab 
      )->line( 
      )->next_section( `RAP create-by-association operation (2)` ). 
 
    MODIFY ENTITY demo_managed_root_reported 
       CREATE BY \_child FIELDS ( key_field_child ch_field1 
              ch_field2 ch_field3 ch_field4 ) WITH VALUE #( 
            ( %key-key_field = 4 
              %target = VALUE #( 
                       ( %cid = 'cid_child4' 
                         key_field_child = 40 
                         ch_field1 = 'qqq' 
                         ch_field2 = 'rrr' 
                         ch_field3 = 90 
                         ch_field4 = 100 
                     ) ) ) 
            ( %key-key_field = 5 
              %target = VALUE #( 
                       ( %cid = 'cid_child5' 
                         key_field_child = 50 
                         ch_field1 = 'sss' 
                         ch_field2 = 'ttt' 
                         ch_field3 = 110 
                         ch_field4 = 120 
                     ) ) ) ) 
           MAPPED FINAL(map3) 
           FAILED FINAL(fail3) 
           REPORTED reported_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_managed_root_reported 
      REPORTED reported_late. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write( reported_late ). 
 
    SELECT key_field, key_field_child, ch_field1, ch_field2, 
      ch_field3, ch_field4 
      FROM demo_tab_child_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(child_tab2). 
 
    out->write_html( 
        `<b>Database table entries ` && 
        `after the operations</b>` 
       )->write( child_tab2 
       )->line( 
       )->next_section( `REPORTED EARLY response for RAP ` && 
                        `read-by-association operation` ). 
 
    READ ENTITY demo_managed_root_reported 
           BY \_child FROM VALUE #( 
               ( %tky-key_field = 4 ) 
               ( %tky-key_field = 5 ) ) 
           RESULT FINAL(result) 
              FAILED FINAL(fail4) 
              REPORTED reported_early. 
 
    out->write( reported_early ). 
 
    out->line( 
      )->next_section( `RAP create-by-association operation (3)` ). 
 
    ROLLBACK ENTITIES. 
 
    MODIFY ENTITY demo_managed_root_reported 
          CREATE BY \_child FIELDS ( key_field_child ch_field1 
              ch_field2 ch_field3 ch_field4 ) WITH VALUE #( 
               ( %key-key_field = 4 
                 %target = VALUE #( 
                          ( %cid = 'cid_child6' 
                            key_field_child = 40 
                            ch_field1 = 'uuu' 
                            ch_field2 = 'vvv' 
                            ch_field3 = 50 
                            ch_field4 = 100 
                        ) ) ) 
               ( %key-key_field = 5 
                 %target = VALUE #( 
                          ( %cid = 'cid_child7' 
                            key_field_child = 50 
                            ch_field1 = 'www' 
                            ch_field2 = 'xxx' 
                            ch_field3 = 60 
                            ch_field4 = 120 
                        ) ) ) 
                        ) 
              MAPPED FINAL(map5) 
              FAILED FINAL(fail5) 
              REPORTED reported_early. 
 
    COMMIT ENTITIES RESPONSE OF demo_managed_root_reported 
      REPORTED reported_late. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    out->write( reported_early ). 
    out->write( reported_late ). 
 
 
    SELECT key_field, key_field_child, ch_field1, ch_field2, 
      ch_field3, ch_field4 
      FROM demo_tab_child_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(child_tab3). 
 
    out->write_html( 
            `<b>Database table entries ` && 
            `after the operations</b>` 
           )->write( child_tab3 ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
    DELETE FROM demo_tab_child_5. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The class includes multiple ABAP EML requests:

1.  **ABAP EML create request**:

    Multiple RAP BO instances are created for the root entity. A [`COMMIT ENTITIES`](abapcommit_entities.md) triggers the saving of the instances to the database. Apart from an internal table showing the database table entries, the output shows the `REPORTED EARLY` response that, among other things, includes the `%global` component that is marked as enabled, and the content of the `%other` component.

2.  **First ABAP EML create-by-association request**:

    Multiple RAP BO instances are created for the child entity. All are purposely specified in a way so that the validation does not fail. Hence, all entries are saved to the database table following a `COMMIT ENTITIES` statement. The entries are shown in an internal table in the output. Besides this, `REPORTED LATE` responses are displayed. Since the validation is successful, there are no entries in the `reported` parameter for the RAP BO entities. For demo purposes, another RAP unbound message that has been added to `%other` when calling the `validatenum` method is displayed.

3.  **Second ABAP EML create-by-association request**:

    Two RAP BO instances are created for the child entity. All are purposely specified in a way so that the validation fails. Hence, the entries are not saved to the database table following a `COMMIT ENTITIES` statement. The entries of the database table are shown in an internal table in the output and do not show any changes. Also here, `REPORTED LATE` responses are displayed in a table. Since the validation fails, the `reported` parameter shows entries. Among them, there are entries to visualize the content of the `%path` and `%element` components. The `%state_area` component is initial in this context. A read operation that follows this create-by-association operation is required to visualize an entry. The RAP unbound message in `%other` is displayed, too.

4.  **ABAP EML read-by-association request**:

    A read-by-association operation is executed on the previously failed instances. The entries of the `REPORTED EARLY` response is displayed in an internal table. The sole purpose of this operation is to visualize the `%state_area` component that shows an entry.

5.  **Third ABAP EML create-by-association request**:

    A [`ROLLBACK ENTITIES`](abaprollback_entities.md) statement before the create-by-association request rolls back all changes of the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). Then, two RAP BO instances are created for the child entity using the same keys as previously. All are purposely specified in a way so that the validation does not fail. Hence, the entries are saved to the database table following a `COMMIT ENTITIES` statement. The entries of the database table are shown in an internal table. Both `REPORTED EARLY` and `REPORTED LATE` responses are displayed in an internal table, too, however, they do not show any entries for the child entity. The RAP unbound messages in `%other` contained in `REPORTED EARLY` and `REPORTED LATE` are displayed.

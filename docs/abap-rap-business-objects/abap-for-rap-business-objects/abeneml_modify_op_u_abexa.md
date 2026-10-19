---
title: "ABAP EML - MODIFY, Standard Operations (Unmanaged)"
source_file: abeneml_modify_op_u_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > Examples for ABAP EML MODIFY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - MODIFY, Standard Operations (Unmanaged)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates all [standard operations](../../abap-glossary/abencrud_glosry.md) to modify and read from a simple unmanaged [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). The following operations are covered:

- `CREATE`

- `CREATE BY` (create-by-association operation)

- `UPDATE`

- `DELETE`

- `READ`

- `READ BY` (read-by-association operation)

In an unmanaged RAP scenario - as opposed to managed RAP scenarios - the developer is responsible for the implementation of the standard operations. This simplified example is not a real life scenario and rather focuses on the technical side by showing how the methods of an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) might be user-implemented taking the handling of the transactional buffer in a managed scenario as a role model in a simplified way. This implementation can, for example, be called using [ABAP EML](../../abap-glossary/abeneml_glosry.md) outside of the behavior pool.

The transactional buffer of the unmanaged RAP BO in the example is constituted by internal tables for the sake of having a self-contained example reducing the complexity. The tables act as a memory area into which data from the [persistent database tables](../../abap-glossary/abenrap_persistent_table_glosry.md) are read and from which data is saved back to the database tables after triggering the saving of modified instances (with a `COMMIT ENTITIES` statement).

**Note**

The code is meant to give an idea about the principles of an unmanaged RAP scenario, the fact that everything must be user-implemented and the significance of the transactional buffer that can be accessed by [ABAP EML](../../abap-glossary/abeneml_glosry.md), and should therefore not be reused in a production scenario.

**Data model**

The CDS data model consists of the root entity DEMO_UNMANAGED_ROOT_2 and its child entity DEMO_UNMANAGED_CHILD_2.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity demo_unmanaged_root_2
  as select from demo_tab_root_3
  composition [1..*] of DEMO_UNMANAGED_CHILD_2 as _child
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
define view entity DEMO_UNMANAGED_CHILD_2
  as select from demo_tab_child_3
  association to parent demo_unmanaged_root_2 
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

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UNMANAGED_ROOT_2` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class bp_demo_unmanaged_root_2 unique;
strict(2);

define behavior for demo_unmanaged_root_2
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  field ( readonly:update ) key_field;
}

define behavior for DEMO_UNMANAGED_CHILD_2 alias child
lock dependent by _parent
authorization dependent by _parent
{
  field ( readonly:update ) key_field, key_field_child;
  association _parent;
}
```

The behavior definition is the basis of the implementation. It defines what can be implemented in the behavior pool.

**Behavior implementation**

For the above RAP behavior definition, one ABP is created. The global class of the behavior pool is `BP_DEMO_UNMANAGED_ROOT_2`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UNMANAGED_ROOT_2======CCIMP` of the behavior pool:

- `lcl_buffer` constitutes the transactional buffer. It includes internal tables to handle the data.

- `lhc_demo_unmanaged_root_2` is the handler class of the behavior pool. The methods of this class implement all standard operations including an error handling.

- `lsc_demo_unmanaged_root_2` is the saver class of the behavior pool. The methods of this class implement the actual modification of the persistent data.

**Details of the ABP**

- `lcl_buffer`

  In this local class, two internal tables are constructed that serve as transactional buffer: `root_buffer` as the transactional buffer for the root entity, and `child_buffer` for the child entity to also cover the create- and read-by-association operations. The underlying structured data types are built in a way that simplifies the handling of the buffers. `gty_buffer`, as the structured data type for `root_buffer`, contains all the key and data fields of the root entity's underlying CDS view with the same type. Plus, the structure includes the components `cid` to hold the content ID that might be provided by an instance and, for a more comfortable processing of saving and deleting instances, it includes two fields (`changed` and `deleted`) acting as flags. These flags are set in the course of modify operations, i. e. if an instance is created or changed, the `changed` receives an `X`. If an instance gets deleted, `deleted` gets the flag `X`. If no operation takes place for an entity, both fields remain initial. Likewise, the structured data type for the child entity (`gty_buffer_child`) is constructed. It also contains all the key and data fields of the child entity's underlying CDS view with the same type (which is in this example very similar to the root entity). This structure contains the components `cid_ref` for by-association operations and `cid_target` for the content ID of child instances in the `%target` structure. The latter is not used in the example. Furthermore, the component `created` is included. Its purpose is the same as `changed`, however, in this case, it is only relevant to cover create-by-association operations. Only those instances whose `created` field is marked with an `X` should be saved to the database table of the child entity.

- Methods `prep_root_buffer` and `prep_child_buffer`

  These two methods are meant to prepare the transactional buffers for the root and child entity and fill them with data from the underlying database table, especially if the buffer tables are cleared once the save sequence gets triggered by a `COMMIT ENTITIES` statement in the ABAP class. The principle of internal tables as transactional buffer is the following: Once an EML call requests data (to be read or modified) with a specific key, it is checked whether the transactional buffer already holds the requested data, otherwise it is checked if the data is available in the [persistent database table](../../abap-glossary/abenrap_persistent_table_glosry.md). If it exists there, the line with the specified key is read from the database table into the transactional buffer using a `SELECT` statement. The following is done in the individual methods for the operations to avoid double entries: If the data does not exist at all (for example, it got deleted), the `FAILED` and `REPORTED` structures should be filled with information about which data sets could not be read or modified. The `prep_child_buffer` method is relevant for the by-association operations. Not only must the availability of the line with the specified key in the root buffer be checked but also the availability of the line in the child buffer. If the line exists in the underlying database table of the child entity, the data gets read into the child buffer using a `SELECT` statement as well.

- Method `create`

  After preparing the root buffer with the provided input parameters (`entities`), a `LOOP AT` statement further processes the transactional buffer with the individual instances that come in as input parameters. There are certain conditions to be met before an instance can actually be created. If the conditions are not met for a particular instance, the result is an entry in the `FAILED` and `REPORTED` structures for the failed instance. The gist is that those instances being present in the transactional buffer and meeting the conditions receive a flag in the `changed` field and can finally be created. Consequently, the instances are saved to the database table following a `COMMIT ENTITIES` statement in the ABAP class triggering the save sequence. The checks also take the significance of the flags in the `%control` structure into consideration, i. e. if a data field is unmarked using the constant `mk-off` of interface `ABP_BEHV_FLAG`, this particular field should not be created with the provided value.

- Method `update`

  Same as the method above, after preparing the root buffer with the provided input parameters (`entities`), a `LOOP AT` statement further processes the transactional buffer with the individual instances that come in as input parameters. Also here, there are certain conditions to be met before an instance can be updated. If the conditions are not met for a particular instance, an entry gets created in the `FAILED` and `REPORTED` structures for the failed instance. The checks are implemented in the way that existing values of a data field should not be overwritten if it is explicitly unmarked in the `%control` structure. Same as above, a changed instance receives a flag. Furthermore, the `IF` statements are implemented for two scenarios. It might so happen that an EML request includes only the keys or only `%cid_ref`. In the latter case, a potentially provided key is ignored since the reference to a particular `%cid` is the principal reference.

- Method `delete`

  This method is implemented similarly to the `update` method, for example, it considers the two scenarios when only key or only `%cid_ref` are provided. If an instance is to be deleted, it receives a flag for the `deleted` field. The `changed` field gets initialized. `%control` is not applicable here.

- Method `read`

  After preparing the root buffer with the provided input parameters (`keys`), a `LOOP AT` statement is used for a detailed preparation and filling of the read `result` table according to the keys that come in as input parameters and considering the flags for the fields in the `%control` structure. If a data field is unmarked, this particular field should not be read and included in the read result. The key must always be read and returned.

- Method `rba_child`

  As an initial step in the method for read-by association operations, both root and child buffers must be prepared. Same as in the `read` method, the `LOOP AT` statement is used for a detailed preparation and filling of the read `result` table according to the keys that come in as input parameters and considering the flags for the fields in the `%control` structure. If a data field is unmarked, this particular field should not be read and included in the read result. The key must always be read and returned.

- Method `cba_child`

  As an initial step in the method for create-by association operations, both root and child buffers must be prepared. The conditions for filling the child buffer within the `LOOP AT` statement include checks for two scenarios. It might so happen that an EML request includes only the keys or only `%cid_ref`. In the latter case, a potentially provided key is ignored since the reference to a particular `%cid` is the principal reference. The flags in the `%control` structure for the data fields are considered, too. If the conditions are met for an instance to be created in the child entity, the instance receives a flag for the `created` field.

- Class `lsc_demo_unmanaged_root`

  The `finalize` method deletes all the content IDs from the transactional buffer since they must not be used during the save phase. However, it is not relevant for the example. The `save` method includes statements that save the instances from the transactional buffer, i. e. from the internal tables `root_buffer` and `child_buffer`, to the database tables (`demo_tab_root_3` and `demo_tab_child_3`). Among the statements, there is one code block dealing with create and update operations. Here, an internal helper table is created to store those instances that have a flag for the `changed` field. This helper table is then used for an ABAP SQL `MODIFY` statement that finally changes the database tables with only those instances a change is intended for. Another block is there for the deletion. Similarly, an internal helper table comprises those instances having a flag for `deleted`. The saving of instances via create-by-association operations is handled separately in the example since the instances from the child buffer must be considered (those instances with a flag for `created`) and not the ones from the root buffer as it is the case in the two preceding code blocks. The `cleanup` method clears the buffer tables.

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
CLASS cl_demo_rap_eml_u_operations DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed   TYPE RESPONSE FOR FAILED   demo_unmanaged_root_2, 
      reported TYPE RESPONSE FOR REPORTED demo_unmanaged_root_2, 
      init_str TYPE string VALUE IS INITIAL, 
      init_i   TYPE i VALUE IS INITIAL. 
    METHODS: 
      initialize_dbtabs, 
      display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_u_operations IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
            `Standard Operations with an Unmanaged RAP BO` 
       )->line( ). 
 
    out->next_section( `CREATE Operations` ). 
 
    MODIFY ENTITY demo_unmanaged_root_2 
     CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 1 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 2 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_4' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 3 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 4 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3' 
          key_field = 3 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_5' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_6' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 5 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 6 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid4' 
          key_field = 4 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_7' 
          %control-field1 = if_abap_behv=>mk-off 
          field2 = 'create_8' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 7 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 8 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid5' 
          key_field = 5 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_9' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_10' 
          %control-field2 = if_abap_behv=>mk-off 
          field3 = 9 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 10 
          %control-field4 = if_abap_behv=>mk-on ) ) 
     CREATE BY \_child FROM VALUE #( 
        "Instances only providing %cid_ref. 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( 
           ( %cid = 'cid_child1' 
             key_field_child = 1 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_1' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_2' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 11 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 12 
             %control-field4 = if_abap_behv=>mk-on ) 
           ( %cid = 'cid_child2' 
             key_field_child = 2 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_3' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_4' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 13 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 14 
             %control-field4 = if_abap_behv=>mk-on ) ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( 
           ( %cid = 'cid_child3' 
             key_field_child = 3 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_5' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_6' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 15 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 16 
             %control-field4 = if_abap_behv=>mk-on ) 
           ( %cid = 'cid_child4' 
             key_field_child = 4 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_7' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_8' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 17 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 18 
             %control-field4 = if_abap_behv=>mk-on ) ) ) 
         ( %cid_ref = 'cid3' 
             %target = VALUE #( 
           ( %cid = 'cid_child5' 
             key_field_child = 5 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_9' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_10' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 19 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 20 
             %control-field4 = if_abap_behv=>mk-on ) ) ) 
        "Instances only providing the key. 
        ( key_field = 4 
          %target = VALUE #( 
           ( %cid = 'cid_child6' 
             key_field_child = 6 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_11' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_12' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 21 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 22 
             %control-field4 = if_abap_behv=>mk-on ) 
           ( %cid = 'cid_child7' 
             key_field_child = 7 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_13' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_14' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 23 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 24 
             %control-field4 = if_abap_behv=>mk-on ) ) ) 
        ( key_field = 5 
          %target = VALUE #( 
           ( %cid = 'cid_child8' 
             key_field_child = 8 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_15' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_16' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 25 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 26 
             %control-field4 = if_abap_behv=>mk-on ) 
            ( %cid = 'cid_child9' 
             key_field_child = 9 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1 = 'cba_17' 
             %control-field1 = if_abap_behv=>mk-on 
             field2 = 'cba_18' 
             %control-field2 = if_abap_behv=>mk-on 
             field3 = 27 
             %control-field3 = if_abap_behv=>mk-on 
             field4 = 28 
             %control-field4 = if_abap_behv=>mk-on )  ) ) 
              ) 
        FAILED   failed 
        REPORTED reported. 
 
    out->write_html( '<u><b><i>Responses:</i></b></u>' ). 
    display_responses(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_3 
      ORDER BY key_field 
      INTO TABLE @FINAL(create). 
    SELECT * FROM demo_tab_child_3 
      ORDER BY key_field 
      INTO TABLE @FINAL(create_by_assoc). 
 
    out->write_html( 
'<u><b><i>Database table entries after the operations:</i></b></u>' 
       )->write( create 
       )->write( create_by_assoc 
       )->line( 
       )->next_section( `UPDATE Operations` ). 
 
    MODIFY ENTITY demo_unmanaged_root_2 
      CREATE FROM VALUE #( 
        ( %cid  = 'cid6' 
          key_field = 6 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_11' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_12' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 29 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 30 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid  = 'cid7'                            "Error 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_13' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_14' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 31 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 32 
          %control-field4 = if_abap_behv=>mk-on ) 
          ) 
      UPDATE FROM VALUE #( 
        "Instances only providing the key. 
        ( key_field = 1 
          field1 = 'update_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_2' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 33 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 34 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 2 
          field2 = 'update_3' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 35 
          %control-field3 = if_abap_behv=>mk-off 
          field4 = 36 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 3 
          field1 = 'update_4' 
          %control-field1 = if_abap_behv=>mk-on 
          field3 = 37 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 38 
          %control-field4 = if_abap_behv=>mk-off ) 
        ( key_field = 4 
          field1 = 'update_5' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = init_str 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = init_i 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 40 
          %control-field4 = if_abap_behv=>mk-off ) 
        ( key_field = 5 
          field1 = 'update_7' 
          %control-field1 = if_abap_behv=>mk-off 
          field2 = 'update_8' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 41 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 42 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 7                                       "Error 
          field1 = 'update_9' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_10' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 43 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 44 
          %control-field4 = if_abap_behv=>mk-on ) 
        "Instances only providing %cid_ref. 
        ( %cid_ref = 'cid6' 
          field1 = 'update_11' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_12' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 45 
          %control-field3 = if_abap_behv=>mk-off 
          field4 = 46 
          %control-field4 = if_abap_behv=>mk-on ) ) 
        FAILED   failed 
        REPORTED reported. 
 
    out->write_html( '<u><b><i>Responses:</i></b></u>' ). 
    display_responses(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_3 
      ORDER BY key_field 
      INTO TABLE @FINAL(update). 
 
    out->write_html( 
'<u><b><i>Database table entries after the operation:</i></b></u>' 
       )->write( update 
       )->line( 
       )->next_section( `DELETE Operations` ). 
 
    MODIFY ENTITY demo_unmanaged_root_2 
      CREATE FROM VALUE #( 
        ( %cid = 'cid8' 
          key_field = 8 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'create_15' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'create_16' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 47 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 48 
          %control-field4 = if_abap_behv=>mk-on ) 
           ) 
      UPDATE FROM VALUE #( 
        ( key_field = 9                               "Error 
          field1 = 'update_13' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_14' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 49 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 50 
          %control-field4 = if_abap_behv=>mk-on ) 
           ) 
      DELETE FROM VALUE #( ( key_field = 5 ) 
                           ( key_field = 6 ) 
                           ( key_field = 7 )          "Error 
                           ( %cid_ref = 'cid8' ) 
                         ) 
      FAILED   failed 
      REPORTED reported. 
 
    out->write_html( '<u><b><i>Responses:</i></b></u>' ). 
    display_responses(  ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_3 
      ORDER BY key_field 
      INTO TABLE @FINAL(delete). 
 
    out->write_html( 
  '<u><b><i>Database table entries after the operation:</i></b></u>' 
         )->write( delete 
         )->line( 
         )->next_section( `READ Operations` ). 
 
    READ ENTITY demo_unmanaged_root_2 
     FROM VALUE #( 
        ( key_field = 1 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 2 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 3 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-off 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 4 
          %control-field1 = if_abap_behv=>mk-off 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 5                                      "Error 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 6                                      "Error 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
             ) 
      RESULT   FINAL(read_result) 
      FAILED   failed 
      REPORTED reported. 
 
    out->write_html( 
      '<u><b><i>Read operations on root entity</i></b></u>' 
      )->write_html( '<b>Responses:</b>' ). 
    display_responses(  ). 
 
    out->write_html( 
     '<b>Read result:</b>' 
      )->write( read_result ). 
 
    READ ENTITY demo_unmanaged_root_2 
     BY \_child FROM VALUE #( 
        ( key_field = 1 
          %control-key_field_child = if_abap_behv=>mk-on 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 2 
          %control-key_field_child = if_abap_behv=>mk-on 
          %control-field1 = if_abap_behv=>mk-off 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 3 
          %control-field1 = if_abap_behv=>mk-on 
          %control-key_field_child = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-off 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 7                                       "Error 
          %control-key_field_child = if_abap_behv=>mk-on 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( key_field = 8                                       "Error 
          %control-key_field_child = if_abap_behv=>mk-on 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ) 
         RESULT FINAL(read_by_assoc) 
         FAILED failed 
         REPORTED reported. 
 
    out->write_html( 
      '<u><b><i>Read operations on child entity</i></b></u>' 
    )->write_html( '<b>Responses:</b>' ). 
    display_responses(  ). 
 
    out->write_html( 
     '<b>Read result:</b>' 
      )->write( read_by_assoc ). 
 
  ENDMETHOD. 
  METHOD display_responses. 
    IF failed IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed ). 
    ELSE. 
      out->write_doc( `No FAILED response.` ). 
    ENDIF. 
 
    IF reported IS NOT INITIAL. 
      out->write_doc( `REPORTED response:` 
        )->write( reported ). 
    ELSE. 
      out->write_doc( `No REPORTED response.` ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_3. 
    DELETE FROM demo_tab_child_3. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) from an ABAP class. The main focus of the example is to demonstrate simple EML calls that access the transactional buffer and modify [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) of root and child entity or read and return them respectively. All standard operations are covered: `CREATE`, `CREATE BY`, `UPDATE`, `DELETE`, `READ` and `READ BY`. Using `COMMIT ENTITIES` statements, the saving of the changed instances is triggered. To demonstrate the successful saving of the particular instances, an internal table is displayed which is filled with the current data sets contained in the [persistent database table](../../abap-glossary/abenrap_persistent_table_glosry.md) (using a `SELECT` statement). Furthermore, the modify and read operations include the `FAILED` and `REPORTED` structures. The example covers cases where instances cannot be changed or read on purpose. To display the responses of failed instances in the output window, the `display_responses` method comprises the construction and filling of internal tables to hold the returned information for failed instances. The information displayed for the failed instances is based on the individual ABP method calls that are responsible for filling the response structures. The information provided is intentionally kept simple and limited.

The `FAILED` tables that are displayed comprise the fail cause (there is no particular logic implemented to diversify the fail cause), content ID and key of the affected instance as well as the affected operation or association (which is indicated by the entry `01`). The `REPORTED` tables that are displayed comprise information about the severity of the incident, content ID and key as well as a custom message.

**Note:**

- Some fields are intentionally not filled to emphasize the significance of the `%control` structure, i. e. if a field is unmarked, it is not considered for the operation. That is why the keyword `FROM` is used following the keyword for the operation throughout the example since `%control` must be filled explicitly in that case.

- The modify operations focusing on `UPDATE` and `DELETE` include additional `CREATE` operations for instances holding a content ID. In doing so, the `UPDATE` and `DELETE` operations can also demonstrate the use of `%cid` and `%cid_ref`.

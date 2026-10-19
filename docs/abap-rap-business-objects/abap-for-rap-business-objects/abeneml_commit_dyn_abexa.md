---
title: "ABAP EML - COMMIT ENTITIES, Dynamic Form"
source_file: abeneml_commit_dyn_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES > Examples for ABAP EML COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - COMMIT ENTITIES, Dynamic Form

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the dynamic form of the `COMMIT ENTITIES` statement.

**Data model**

The CDS data model consists of two simple root entities:

- `DEMO_MANAGED_ROOT_2`

- `DEMO_MANAGED_ASSOC_CUSTOM`

They are not related to each other and are only used to have responses for more than one root entity in the example. Associations and child entities are of no relevance in this example.

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) of entity `DEMO_MANAGED_ROOT_2` contains the following notation for the validation `validate_field` in the body:

`validation validate_field on save { field data_field4_root; }`

Likewise, the entity `DEMO_MANAGED_ASSOC_CUSTOM` contains the following notation for the validation `validate_field` in the body:

`validation validate_field on save { field data_field4_assoc; }`

**Behavior implementation**

For both of the above RAP behavior definitions, there are [ABAP behavior pools (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) available. The actual implementation takes place in the `BP_DEMO_MANAGED_ROOT_2========CCIMP` of ABP `BP_DEMO_MANAGED_ROOT_2` and `BP_DEMO_MANAGED_ASSOC_CUSTOM==CCIMP` of ABP `BP_DEMO_MANAGED_ASSOC_CUSTOM` respectively.

The method `validate_field` has the following logic:

- First, all instances of the entities with the provided keys are read into an internal table using the keyword `READ ENTITIES`.

- It is then checked whether the number of a certain data field is higher than the value that is allowed. In case of entity `DEMO_MANAGED_ROOT_2`, the data field `data_field4_root` should not be higher than 50. In case of entity `DEMO_MANAGED_ASSOC_CUSTOM`, the data field `data_field4_assoc` should not be higher than 10000. If the values are higher, the `FAILED` and `REPORTED` structures are filled with information for the respective failed entry.

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
CLASS cl_demo_rap_eml_commit_2 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      root_name1 TYPE abp_root_entity_name 
                      VALUE 'DEMO_MANAGED_ASSOC_CUSTOM', 
      root_name2 TYPE abp_root_entity_name 
                      VALUE 'DEMO_MANAGED_ROOT_2'. 
    METHODS initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_commit_2 IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
                    `COMMIT Variant: COMMIT ENTITIES RESPONSE OF` 
                   ). 
 
    "Fill table dyn_tab with those root entity names from which 
    "responses should be retrieved. 
    FINAL(dyn_tab) = VALUE abp_entity_name_tab( ( root_name1 ) 
                                                ( root_name2 ) ). 
 
    "First round of modify operations with valid entries. 
    "Entries are created for two root entities. 
    MODIFY ENTITIES OF demo_managed_root_2 
      ENTITY demo_managed_root_2 
        CREATE FIELDS ( key_field data_field1_root data_field2_root 
            data_field3_root data_field4_root ) WITH VALUE #( 
          ( %cid = 'cid1' key_field = 1 
            data_field1_root = 'aaa' data_field2_root = 'bbb' 
            data_field3_root = 10 data_field4_root = 11 ) 
          ( %cid = 'cid2' key_field = 2 
            data_field1_root = 'ccc' data_field2_root = 'ddd' 
            data_field3_root = 12 data_field4_root = 13 ) 
              ). 
 
    MODIFY ENTITIES OF demo_managed_assoc_custom 
      ENTITY demo_managed_assoc_custom 
        CREATE FIELDS ( key_field data_field1_assoc 
            data_field2_assoc data_field3_assoc data_field4_assoc ) 
            WITH VALUE #( 
          ( %cid = 'cid3' key_field = 3 
            data_field1_assoc = 'eee' data_field2_assoc = 'fff' 
            data_field3_assoc = 14 data_field4_assoc = 15 ) 
          ( %cid = 'cid4' key_field = 4 
            data_field1_assoc = 'ggg' data_field2_assoc = 'hhh' 
            data_field3_assoc = 16 data_field4_assoc = 17 ) 
              ). 
 
    COMMIT ENTITIES 
     RESPONSES OF dyn_tab 
      FAILED   FINAL(failed1) 
      REPORTED FINAL(reported1). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_2 
      INTO TABLE @FINAL(lt_com_responses_of). 
    SELECT * FROM demo_tab_assoc_2 
      INTO TABLE @FINAL(lt_com_responses_of2). 
 
    out->write_doc( 
    `1st modify operation for entity 1: Result with valid entries:` 
               )->write( lt_com_responses_of 
               )->write_doc( 
    `1st modify operation for entity 2: Result with valid entries:` 
               )->write( lt_com_responses_of2 
               ). 
 
    out->write_doc( `Commit responses:` ). 
 
    IF failed1 IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed1 ). 
    ELSE. 
      out->write_doc( `No FAILED response.` ). 
    ENDIF. 
 
    IF reported1 IS NOT INITIAL. 
      out->write_doc( `REPORTED response:` 
        )->write( reported1 ). 
    ELSE. 
      out->write_doc( `No REPORTED response.` ). 
    ENDIF. 
 
    initialize_dbtabs( ). 
 
********************************************************************** 
 
    out->line( ). 
 
    "Second round of modify operations with invalid entries. 
    MODIFY ENTITIES OF demo_managed_root_2 
          ENTITY demo_managed_root_2 
            CREATE FIELDS ( key_field data_field1_root data_field2_root 
            data_field3_root data_field4_root ) WITH VALUE #( 
            ( %cid = 'cid5' key_field = 5 
              data_field1_root = 'iii' data_field2_root = 'jjj' 
              data_field3_root = 18 data_field4_root = 19 ) 
            ( %cid = 'cid6' key_field = 6 
              data_field1_root = 'iii' data_field2_root = 'jjj' 
              data_field3_root = 20 data_field4_root = 51 ) 
            ( %cid = 'cid7' key_field = 7 
              data_field1_root = 'kkk' data_field2_root = 'lll' 
              data_field3_root = 21 data_field4_root = 52 ) 
                  ). 
 
    MODIFY ENTITIES OF demo_managed_assoc_custom 
          ENTITY demo_managed_assoc_custom 
            CREATE FIELDS ( key_field data_field1_assoc 
            data_field2_assoc data_field3_assoc data_field4_assoc ) 
            WITH VALUE #( 
            (  %cid = 'cid8' key_field = 8 
               data_field1_assoc = 'mmm' data_field2_assoc = 'nnn' 
               data_field3_assoc = 22 data_field4_assoc = 23 ) 
            (  %cid = 'cid9' key_field = 9 
               data_field1_assoc = 'mmm' data_field2_assoc = 'nnn' 
               data_field3_assoc = 24 data_field4_assoc = 10001 ) 
            (  %cid = 'cid10' key_field = 10 
               data_field1_assoc = 'ooo' data_field2_assoc = 'ppp' 
               data_field3_assoc = 25 data_field4_assoc = 10002 ) 
                  ). 
 
    COMMIT ENTITIES 
     RESPONSES OF dyn_tab 
      FAILED   FINAL(failed2) 
      REPORTED FINAL(reported2). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_2 
      INTO TABLE @FINAL(lt_com_responses_inval). 
    SELECT * FROM demo_tab_assoc_2 
      INTO TABLE @FINAL(lt_com_responses_inval2). 
 
    out->write_doc( 
    `2nd modify operation for entity 1 - ` && 
    `no saved entries due to invalid entries:` 
               )->write( lt_com_responses_inval 
               )->write_doc( 
    `2nd modify operation for entity 2 - ` && 
    `no saved entries due to invalid entries:` 
               )->write( lt_com_responses_inval2 
               ). 
 
    out->write_doc( `Commit responses:` ). 
 
    IF failed2 IS NOT INITIAL. 
      out->write_doc( `FAILED response:` 
        )->write( failed2 ). 
    ELSE. 
      out->write_doc( `No FAILED response.` ). 
    ENDIF. 
 
    IF reported2 IS NOT INITIAL. 
      out->write_doc( `REPORTED response:` 
        )->write( reported2 ). 
    ELSE. 
      out->write_doc( `No REPORTED response.` ). 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_2. 
    DELETE FROM demo_tab_assoc_2. 
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

- Two `MODIFY` operations for two different root entities are carried out within one [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) to create several instances using the keyword `CREATE`.

- For these newly created instances, the validations are successful and they are saved to the database using `COMMIT ENTITIES`. The saved data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations and the successful saving to the database. Afterwards, the database tables are emptied using the method `initialize_dbtabs( )`.

- `COMMIT ENTITIES RESPONSE OF ...`

Two rounds of `MODIFY` operations are carried out on two different entities, one round with valid entries, the other containing invalid entries. Validations always accept or reject data changes per RAP transaction. Therefore, if the validation fails only for one instance, the complete content of the transactional buffer is rejected. In case of a failed validation, the `FAILED` and `REPORTED` structures are filled with information on the failed instances.

- The internal table `dyn_tab` is set up to hold those root entities for which responses should be retrieved.

- First round: `MODIFY` operations are carried out on two root entities using the keyword `CREATE` to create new instances. The `COMMIT ENTITIES RESPONSES OF ...` statement includes the `FAILED` and `REPORTED` responses for both of the root entities since `dyn_tab` was specified accordingly. Upon committing, the validation method in the ABP is called. Since all instances are valid, all of them are saved to the database table. There are no `FAILED` and `REPORTED` responses. The saved data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations and the successful saving to the database. Afterwards, the database is emptied.

- Second round: Same as before, `MODIFY` operations are carried out on the two root entities using the keyword `CREATE` to create new instances, yet with entries for which the validation will fail (the number of the fourth data field is higher than the allowed value in the validation method).

  For each entity, there is one valid entry and two invalid entries. Also here, the `COMMIT ENTITIES RESPONSES OF ...` statement includes the `FAILED` and `REPORTED` responses for both of the root entities as the internal table `dyn_tab` was specified accordingly. Upon committing, the validation method in the respective ABP is called. The methods ensure that the response structures are filled with information on those instances for which the validation failed. Due to the fact that invalid entries exist, these instances are not saved to database as well as those instances with valid entries. All instances of the whole RAP transaction are not saved. All data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations. Consequently, there are no data sets to be displayed because of the failed saving. Two internal tables are created to display parts of the accumulated `FAILED` responses for all root entities specified in `dyn_tab` and parts of the accumulated `REPORTED` responses. **Note:** No further data changes are possible as long as the invalid instances are not corrected. An invalid entity instance must either be corrected using an `UPDATE` operation, or it must be deleted using the `ROLLBACK ENTITIES` statement. Otherwise, no further data changes are possible.

---
title: "ABAP EML - COMMIT ENTITIES, Short and Long Form"
source_file: abencommit_entities_sh_lo_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > COMMIT ENTITIES > Examples for ABAP EML COMMIT ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - COMMIT ENTITIES, Short and Long Form

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates two variants of the `COMMIT ENTITIES` statement: the short version without responses and long form with responses. It covers several `MODIFY` operations for creating instances for two root entities in a simplified managed scenario. The saving of these instances is triggered by `COMMIT ENTITIES` statements.

For the purpose of showing entries in the `FAILED` and `REPORTED` structures in the context of the long version, a validation is implemented in the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) that causes the saving of certain entries to fail and fills the response structures.

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

- Consequently, once the validation method is called and the save sequence is triggered upon committing, the saving of all instances to the database table fails including those instances for which the validation did not fail. See more information on validations in the [RAP BDL Documentation](../rap-behavior-definitions/abenbdl_validations.md).

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
CLASS cl_demo_rap_eml_commit_1 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_commit_1 IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 
                    `COMMIT Variants` 
        )->begin_section( 
                    `COMMIT Variant: COMMIT ENTITIES.` 
                  ). 
 
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
        CREATE FIELDS ( key_field data_field1_assoc data_field2_assoc 
            data_field3_assoc data_field4_assoc ) WITH VALUE #( 
          ( %cid = 'cid3' key_field = 3 
            data_field1_assoc = 'eee' data_field2_assoc = 'fff' 
            data_field3_assoc = 14 data_field4_assoc = 15 ) 
          ( %cid = 'cid4' key_field = 4 
            data_field1_assoc = 'ggg' data_field2_assoc = 'hhh' 
            data_field3_assoc = 16 data_field4_assoc = 17 ) 
              ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_2 
      INTO TABLE @FINAL(lt_entity_1). 
    SELECT * FROM demo_tab_assoc_2 
      INTO TABLE @FINAL(lt_entity_2). 
 
    out->write_doc( 
    `Result of modify operations on two entities:` 
               )->write( lt_entity_1 
               )->write( lt_entity_2 
               )->line( 
               )->begin_section( 
                  `COMMIT Variant: COMMIT ENTITIES RESPONSE OF ...` 
               )->write_text( `First round of modify operations ` && 
                              `on two entities with valid entries:` ). 
 
    initialize_dbtabs( ). 
 
    "COMMIT ENTITIES RESPONSE OF 
    "First round of modify operations with valid entries. 
    "Entries are created for two root entities. 
    MODIFY ENTITIES OF demo_managed_root_2 
      ENTITY demo_managed_root_2 
        CREATE FIELDS ( key_field data_field1_root data_field2_root 
            data_field3_root data_field4_root ) WITH VALUE #( 
          ( %cid = 'cid5' key_field = 5 
            data_field1_root = 'iii' data_field2_root = 'jjj' 
            data_field3_root = 18 data_field4_root = 19 ) 
          ( %cid = 'cid6' key_field = 6 
            data_field1_root = 'kkk' data_field2_root = 'lll' 
            data_field3_root = 20 data_field4_root = 21 ) 
              ). 
 
    MODIFY ENTITIES OF demo_managed_assoc_custom 
      ENTITY demo_managed_assoc_custom 
        CREATE FIELDS ( key_field data_field1_assoc data_field2_assoc 
            data_field3_assoc data_field4_assoc ) WITH VALUE #( 
          ( %cid = 'cid7' key_field = 7 
            data_field1_assoc = 'mmm' data_field2_assoc = 'nnn' 
            data_field3_assoc = 22 data_field4_assoc = 23 ) 
          ( %cid = 'cid8' key_field = 8 
            data_field1_assoc = 'ooo' data_field2_assoc = 'ppp' 
            data_field3_assoc = 24 data_field4_assoc = 25 ) 
              ). 
 
    "COMMIT ENTITIES statement, long version. 
    "Responses are retrieved per root entity. 
    COMMIT ENTITIES 
      RESPONSE OF demo_managed_root_2 
        FAILED   FINAL(failed1a) 
        REPORTED FINAL(reported1a) 
      RESPONSE OF demo_managed_assoc_custom 
        FAILED   FINAL(failed2a) 
        REPORTED FINAL(reported2a). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_2 
      INTO TABLE @FINAL(lt2_entity_1). 
    SELECT * FROM demo_tab_assoc_2 
      INTO TABLE @FINAL(lt2_entity_2). 
 
    out->write_doc( 
    `1st modify operation for entity 1. Result with valid entries:` 
               )->write( lt2_entity_1 ). 
 
    IF failed1a IS NOT INITIAL. 
      out->write_doc( `FAILED response for entity 1:` 
        )->write( failed1a ). 
    ELSE. 
      out->write_doc( `No FAILED response for entity 1.` ). 
    ENDIF. 
 
    IF reported1a IS NOT INITIAL. 
      out->write_doc( `REPORTED response for entity 1:` 
        )->write( reported1a ). 
    ELSE. 
      out->write_doc( `No REPORTED response for entity 1.` ). 
    ENDIF. 
 
    out->write_doc( 
`1st modify operation for entity 2. Result with valid entries:` 
          )->write( lt2_entity_2 
          ). 
 
    IF failed2a IS NOT INITIAL. 
      out->write_doc( `FAILED response for entity 2:` 
        )->write( failed2a ). 
    ELSE. 
      out->write_doc( `No FAILED response for entity 2.` ). 
    ENDIF. 
 
    IF reported2a IS NOT INITIAL. 
      out->write_doc( `REPORTED response for entity 2:` 
        )->write( reported2a ). 
    ELSE. 
      out->write_doc( `No REPORTED response for entity 2.` ). 
    ENDIF. 
 
    initialize_dbtabs( ). 
 
    out->line( 
    )->write_text( `Second round of modify operations ` && 
                   `on two entities with invalid entries:` ). 
 
    "Second round of modify operations with invalid entries. 
    MODIFY ENTITIES OF demo_managed_root_2 
          ENTITY demo_managed_root_2 
            CREATE FIELDS ( key_field data_field1_root data_field2_root 
            data_field3_root data_field4_root ) WITH VALUE #( 
            ( %cid = 'cid9' key_field = 9 
              data_field1_root = 'qqq' data_field2_root = 'rrr' 
              data_field3_root = 26 data_field4_root = 27 ) 
            ( %cid = 'cid10' key_field = 10 
              data_field1_root = 'sss' data_field2_root = 'ttt' 
              data_field3_root = 28 data_field4_root = 51 ) 
            ( %cid = 'cid11' key_field = 11 
              data_field1_root = 'uuu' data_field2_root = 'vvv' 
              data_field3_root = 29 data_field4_root = 52 ) 
                  ). 
 
    MODIFY ENTITIES OF demo_managed_assoc_custom 
          ENTITY demo_managed_assoc_custom 
            CREATE FIELDS ( key_field data_field1_assoc 
            data_field2_assoc data_field3_assoc data_field4_assoc ) 
            WITH VALUE #( 
            (  %cid = 'cid12' key_field = 12 
               data_field1_assoc = 'www' data_field2_assoc = 'xxx' 
               data_field3_assoc = 30 data_field4_assoc = 31 ) 
            (  %cid = 'cid13' key_field = 13 
               data_field1_assoc = 'yyy' data_field2_assoc = 'zzz' 
               data_field3_assoc = 32 data_field4_assoc = 10001 ) 
            (  %cid = 'cid14' key_field = 14 
               data_field1_assoc = 'aaa' data_field2_assoc = 'bbb' 
               data_field3_assoc = 33 data_field4_assoc = 10002 ) 
                  ). 
 
    "COMMIT ENTITIES statement, long version. 
    "Responses are retrieved per root entity. 
    COMMIT ENTITIES 
      RESPONSE OF demo_managed_root_2 
        FAILED   FINAL(failed1b) 
        REPORTED FINAL(reported1b) 
      RESPONSE OF demo_managed_assoc_custom 
        FAILED   FINAL(failed2b) 
        REPORTED FINAL(reported2b). 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT * FROM demo_tab_root_2 
      INTO TABLE @FINAL(lt3_entity_1). 
    SELECT * FROM demo_tab_assoc_2 
      INTO TABLE @FINAL(lt3_entity_2). 
 
    out->write_doc( 
    `2nd modify operation for entity 1. ` && 
    `No saved entries due to invalid entries:` 
               )->write( lt3_entity_1 ). 
 
    IF failed1b IS NOT INITIAL. 
      out->write_doc( `FAILED response for entity 1:` 
        )->write( failed1b ). 
    ELSE. 
      out->write_doc( `No FAILED response for entity 1.` ). 
    ENDIF. 
 
    IF reported1b IS NOT INITIAL. 
      out->write_doc( `REPORTED response for entity 1:` 
        )->write( reported1b ). 
    ELSE. 
      out->write_doc( `No REPORTED response for entity 1.` ). 
    ENDIF. 
 
    out->write_doc( 
         `2nd modify operation for entity 2. ` && 
         `No saved entries due to invalid entries:` 
          )->write( lt3_entity_2 
          ). 
 
    IF failed2b IS NOT INITIAL. 
      out->write_doc( `FAILED response for entity 2:` 
        )->write( failed2b ). 
    ELSE. 
      out->write_doc( `No FAILED response for entity 2.` ). 
    ENDIF. 
 
    IF reported2b IS NOT INITIAL. 
      out->write_doc( `REPORTED response for entity 2:` 
        )->write( reported2b ). 
    ELSE. 
      out->write_doc( `No REPORTED response for entity 2.` ). 
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

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class and shows an example for both, short and long version of the `COMMIT ENTITIES` statement:

- `COMMIT ENTITIES.`

  Two `MODIFY` operations for two different root entities are carried out within one [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) to create several instances using the keyword `CREATE`. These newly created instances are saved to the database tables when triggering the save phase with the `COMMIT ENTITIES.` statement. It is just about saving the created entries, responses are not of interest. The saved data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations and the successful saving to the database. Afterwards, the database tables are emptied.

- `COMMIT ENTITIES RESPONSE OF ...`

  Two rounds of `MODIFY` operations are carried out on two different entities, one round with valid entries, the other containing invalid entries. Due to the implemented validation, it is ensured that no instance from the transactional buffer is saved if the validation fails for one or more of the instances created within the RAP transaction. In case of a failed validation, the `FAILED` and `REPORTED` structures are filled with information on the failed instances. First round: `MODIFY` operations are carried out on two root entities using the keyword `CREATE` to create new instances. The `COMMIT ENTITIES RESPONSE OF ...` statement includes the `FAILED` and `REPORTED` responses for both of the root entities. Upon committing, the validation method in the ABP is called. Since all instances are valid, all of them are saved to the database table. There are no `FAILED` and `REPORTED` responses. The saved data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations and the successful saving to the database. Afterwards, the database is emptied. Second round: Same as before, `MODIFY` operations are carried out on the two root entities using the keyword `CREATE` to create new instances, yet with entries for which the validation will fail (the number of the fourth data field is higher than the allowed value in the validation method). For each entity, there is one valid entry and two invalid entries. Also here, the `COMMIT ENTITIES RESPONSE OF ...` statement includes the `FAILED` and `REPORTED` responses for both of the root entities. Upon committing, the validation method in the respective ABP is called. The methods ensure that the response structures are filled with information on those instances for which the validation failed. Due to the fact that invalid entries exist, these instances are not saved to the database as well as those instances with valid entries. All instances of the whole RAP transaction are not saved. All data sets are then read from the database tables into internal tables to display the outcome of the `MODIFY` operations. Consequently, there are no data sets to be displayed because the saving failed for all instances. Two internal tables are created and displayed per entity that show parts of the `FAILED` and `REPORTED` responses returned for those instances for which the validation failed. **Note:** No further data changes are possible as long as the invalid instances are not corrected. An invalid entity instance must either be corrected using an `UPDATE` operation, or it must be deleted using the `ROLLBACK ENTITIES` statement. Otherwise, no further data changes are possible.

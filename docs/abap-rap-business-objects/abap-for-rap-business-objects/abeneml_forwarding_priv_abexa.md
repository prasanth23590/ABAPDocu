---
title: "Using the FORWARDING PRIVILEGED Addition with an ABAP EML Statement"
source_file: abeneml_forwarding_priv_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - PRIVILEGED"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using the FORWARDING PRIVILEGED Addition with an ABAP EML Statement

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates ABAP EML `MODIFY` statements executing [actions](../../abap-glossary/abenrap_action_glosry.md) with the addition `FORWARDING PRIVILEGED` using a managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). The following ABAP repository objects are used in the example:

**Data models**

- `DEMO_MANAGED_PRIVILEGED`

- `DEMO_MANAGED_PRIVILEGED_T`

**Behavior definitions**

- `DEMO_MANAGED_PRIVILEGED`

- `DEMO_MANAGED_PRIVILEGED_T`

**Behavior implementations**

- `BP_DEMO_MANAGED_PRIVILEGED`: `BP_DEMO_MANAGED_PRIVILEGED====CCIMP`

- `BP_DEMO_MANAGED_PRIVILEGED_T`: `BP_DEMO_MANAGED_PRIVILEGED_T==CCIMP`

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
CLASS cl_demo_rap_eml_forwarding_prv DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS: 
      constructor, 
      fill_dbtab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_forwarding_prv IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demonstrating the FORWARDING PRIVILEGED ` && 
    `addition` 
    )->line( 
    )->write_doc( `Executing an action that includes an EML request ` && 
    `with FORWARDING PRIVILEGED in the implementation` 
    )->write_doc( `--------- EML request without PRIVILEGED ---------` 
    ). 
 
    MODIFY ENTITY demo_managed_privileged 
      EXECUTE forwarding_privileged 
      FROM VALUE #( ( key_field = 1 ) 
                    ( key_field = 2 ) ) 
      FAILED FINAL(f1) 
      REPORTED FINAL(r1). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ELSE. 
      SELECT key_field, field1, field2 FROM demo_tab_root_3 
      WHERE key_field BETWEEN 1 AND 2 
      ORDER BY key_field 
      INTO TABLE @DATA(itab). 
 
      out->write( itab ). 
    ENDIF. 
 
    out->write_doc( `--------- EML request with PRIVILEGED ---------` ). 
 
    MODIFY ENTITY PRIVILEGED demo_managed_privileged 
      EXECUTE forwarding_privileged 
      FROM VALUE #( ( key_field = 3 ) 
                    ( key_field = 4 ) ) 
      FAILED FINAL(f2) 
      REPORTED FINAL(r2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ELSE. 
      SELECT key_field, field1, field2 FROM demo_tab_root_3 
      WHERE key_field BETWEEN 3 AND 4 
      ORDER BY key_field 
      INTO TABLE @itab. 
 
      out->write( itab ). 
    ENDIF. 
 
    out->line( 
     )->write_doc( `Executing an action that includes EML requests ` && 
        `depending on the result of the importing parameter ` && 
        `PRIVILEGED when calling cl_abap_behv_aux=>get_current_context` 
     )->write_doc( `The FORWARDING PRIVILEGED addition is a ` && 
     `shortcut to such an implementation.` 
     )->write_doc( `--------- EML request without PRIVILEGED ---------` 
     ). 
 
    MODIFY ENTITY demo_managed_privileged 
      EXECUTE forwarding_privileged_aux 
      FROM VALUE #( ( key_field = 5 ) 
                    ( key_field = 6 ) ) 
      FAILED FINAL(f3) 
      REPORTED FINAL(r3). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ELSE. 
      SELECT key_field, field1, field2 FROM demo_tab_root_3 
      WHERE key_field BETWEEN 5 AND 6 
      ORDER BY key_field 
      INTO TABLE @itab. 
 
      out->write( itab ). 
    ENDIF. 
 
    out->write_doc( `--------- EML request with PRIVILEGED ---------` ). 
 
    MODIFY ENTITY PRIVILEGED demo_managed_privileged 
      EXECUTE forwarding_privileged_aux 
      FROM VALUE #( ( key_field = 7 ) 
                    ( key_field = 8 ) ) 
      FAILED FINAL(f4) 
      REPORTED FINAL(r4). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ELSE. 
      SELECT key_field, field1, field2 FROM demo_tab_root_3 
      WHERE key_field BETWEEN 7 AND 8 
      ORDER BY key_field 
      INTO TABLE @itab. 
 
      out->write( itab ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    fill_dbtab( ). 
  ENDMETHOD. 
  METHOD fill_dbtab. 
    DELETE FROM demo_tab_root_3. 
    MODIFY demo_tab_root_3 FROM TABLE @( VALUE #( 
      ( key_field = 1 ) 
      ( key_field = 2 ) 
      ( key_field = 3 ) 
      ( key_field = 4 ) 
      ( key_field = 5 ) 
      ( key_field = 6 ) 
      ( key_field = 7 ) 
      ( key_field = 8 ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The source code above uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class. There are two ABAP EML modify requests:

- First, a demo database table is filled with entries to work with in the example. Only the key field is filled.

- The example includes four ABAP EML requests executing two different actions based on the created keys.

- The first two ABAP EML requests execute the `forwarding_privileged` action. One statement executes the action with, the other without the `PRIVILEGED` addition. The implementation of the `forwarding_privileged` action in the ABAP behavior pool includes an ABAP EML request executing an action (`act`) of another RAP BO (whose root view entity is based on the same database table). This statement uses the `FORWARDING PRIVILEGED` addition, which, as the name implies, forwards the privileged access. The implementation of the `act` action includes calling the `GET_CURRENT_CONTEXT` method of the `CL_ABAP_BEHV_AUX` class, with which context information is retrieved. To visualize the (not) forwarded privileged access, fields of the RAP BO instances are updated with flags and text that indicate the (not) forwarded privileged access.

- The next two ABAP EML requests execute the `forwarding_privileged_aux` action. One statement executes the action with, the other without the `PRIVILEGED` addition. As above, the implementation of the `forwarding_privileged_aux` action in the ABAP behavior pool includes an ABAP EML request executing an action (`act`) of another RAP BO. In this case, the method is implemented in a way that basically corresponds to the functionality of a statement that uses the `FORWARDING PRIVILEGED` addition. After all action executions, a [`COMMIT ENTITIES`](abapcommit_entities.md) statement is executed to persist the RAP BO instances to the database. Then, the data is retrieved from the database table and output to demonstrate the effect of the implementations.

---
title: "ABAP SQL - Locator, Copy Column"
source_file: abendb_copy_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Streaming and Locators > ABAP SQL - Examples of LOB Handles"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Locator, Copy Column

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how column content can be copied using [locators](../../abap-glossary/abenlocator_glosry.md).

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
CLASS cl_demo_db_copy DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_db_copy IMPLEMENTATION. 
  METHOD main. 
 
    DATA: 
      source TYPE c LENGTH 255 
             VALUE '/SAP/PUBLIC/BC/ABAP/mime_demo/ABAP_Docu_Logo.gif', 
      target TYPE c LENGTH 255 
             VALUE 'picture_copy'. 
 
    DATA wa TYPE demo_blob_table LOCATOR FOR ALL COLUMNS. 
 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = source 
     )->request(   CHANGING field = target ). 
 
    SELECT SINGLE picture 
           FROM demo_blob_table 
           WHERE name = @source 
           INTO @wa-picture. 
 
    IF sy-subrc <> 0. 
      out->write( 
        'Nothing found, run DEMO_DB_WRITER first!' ). 
      RETURN. 
    ENDIF. 
 
    wa-name = target. 
    INSERT demo_blob_table FROM @wa. 
 
    IF sy-subrc = 0. 
      out->write( 
        'You can run DEMO_DB_READER with new name now' ). 
    ELSE. 
      out->write( 
        'Target already exists' ). 
    ENDIF. 
 
    wa-picture->close( ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `main` [derives](../abap-declarations/abaptypes_lob_handle.md) an [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) from the structure of the DDIC database table `DEMO_BLOB_TABLE`, where the component `PICTURE` is declared as an [LOB handle component](../../abap-glossary/abenlob_handle_component_glosry.md) for a locator. This locator is then [created](abenselect_into_lob_handles.md) in a `SELECT` statement.

A new value is then assigned to the key field of the LOB handle structure and the LOB handle structure is used as a work area in an `INSERT` statement. As a result, the content of the column to which the locator is linked is [copied](abenium_lob.md) to the corresponding column of the new row without the content having to be transported to the ABAP class.

If data previously written in the executable writer stream example is read, this is the data of a figure in the GIF format. By specifying the new name, the copied figure can be displayed using the example for reader streams.

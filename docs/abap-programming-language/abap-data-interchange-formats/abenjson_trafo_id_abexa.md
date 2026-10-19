---
title: "JSON - Identity Transformation with JSON Writer as Target"
source_file: abenjson_trafo_id_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Identity Transformation with JSON Writer as Target

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various XML sources for [identity transformations](../../abap-glossary/abenid_trafo_glosry.md) with a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) as a target.

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
CLASS cl_demo_call_trafo_id_json DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_call_trafo_id_json IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 
      `Identity Transformation for JSON Writer` ). 
    DATA json_writer TYPE REF TO cl_sxml_string_writer. 
 
    out->begin_section( 
      `Source JSON String` ). 
    FINAL(json) = cl_abap_conv_codepage=>create_out( )->convert( 
                   `{"TEXT":"Hello JSON!"}` ). 
    json_writer = cl_sxml_string_writer=>create( 
                    type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE XML json 
                           RESULT XML json_writer. 
    out->write_json( json_writer->get_output( ) ). 
 
    out->next_section( 
      `Source JSON Reader` ). 
    FINAL(json_reader) = cl_sxml_string_reader=>create( json ). 
    json_writer = cl_sxml_string_writer=>create( 
                    type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE XML json_reader 
                           RESULT XML json_writer. 
    out->write_json( json_writer->get_output( ) ). 
 
    out->next_section( 
      `Source JSON-XML` ). 
    FINAL(xml_json) = cl_abap_conv_codepage=>create_out( )->convert( 
     `<object><str name="TEXT">Hello JSON!</str></object>` ). 
    json_writer = cl_sxml_string_writer=>create( 
                    type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE XML xml_json 
                           RESULT XML json_writer. 
    out->write_json( json_writer->get_output( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` is filled three times with XML sources. These sources can be passed to the [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) specified as an XML target:

- Valid JSON data in a byte string.

- A [JSON reader](../../abap-glossary/abenjson_reader_glosry.md) that points to this byte string.

- XML data in a byte string in [JSON XML format](../../abap-glossary/abenjson_xml_glosry.md).

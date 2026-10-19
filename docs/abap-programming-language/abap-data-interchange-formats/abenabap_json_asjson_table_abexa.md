---
title: "JSON - asJSON for Internal Tables"
source_file: abenabap_json_asjson_table_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - asJSON for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [asJSON](abenabap_asjson_abap_types_table.md) for internal tables.

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
CLASS cl_demo_asjson_tables DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asjson_tables IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF struct, 
             day  TYPE string, 
             date TYPE d, 
           END OF struct. 
    DATA itab TYPE STANDARD TABLE OF struct. 
    itab = VALUE #( 
     ( day = 'Yesterday' 
         date = cl_demo_date_time=>get_user_date( ) - 1 ) 
     ( day = 'Today' 
         date = cl_demo_date_time=>get_user_date( ) ) 
     ( day = 'Tomorrow' 
         date = cl_demo_date_time=>get_user_date( ) + 1 ) ). 
 
    "Transformation to JSON 
    out->begin_section( 'asJSON' ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE itab = itab 
                           RESULT XML writer. 
    FINAL(json) = writer->get_output( ). 
    out->write_json( json ). 
 
    "JSON-XML 
    out->next_section( 'asJSON-XML' ). 
    FINAL(reader) = cl_sxml_string_reader=>create( json ). 
    FINAL(xml_writer) = cl_sxml_string_writer=>create( ). 
    reader->next_node( ). 
    reader->skip_node( xml_writer ). 
    DATA(xml) = xml_writer->get_output( ). 
    out->write_xml( xml ). 
 
    "asXML 
    out->next_section( 'asXML' ). 
    CALL TRANSFORMATION id SOURCE itab = itab 
                           RESULT XML xml. 
    out->write_xml( xml ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, for which a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) is specified as the XML target, is called to create the [asJSON](../../abap-glossary/abenasjson_glosry.md) representation of an internal table.

For comparison, the [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation of the JSON data and the [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the ABAP data is also shown.

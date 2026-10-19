---
title: "JSON - Object Components in JSON-XML"
source_file: abenabap_json_xml_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Object Components in JSON-XML

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the two alternatives for object components in [JSON-XML](abenabap_json_xml.md).

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
CLASS cl_demo_json_xml_object_mmbrs DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_json_xml_object_mmbrs IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 'Render' ). 
    "JSON-XML without and with members 
    FINAL(json_xml) = 
      `<object>` && 
      `<str name="text">abcd</str>` && 
      `<bool name="flag">true</bool>` && 
      `<member name="number">` && 
      `<num>111</num>` && 
      `</member>` && 
      `<member name="content">` && 
      `<null />` && 
      `</member>` && 
      `</object>`. 
 
    out->begin_section( 
        'JSON-XML without and with member elements' 
      )->write_xml( json_xml ). 
    "Render JSON data 
    out->next_section( 'JSON' ). 
    FINAL(reader) = cl_sxml_string_reader=>create( 
      input = cl_abap_conv_codepage=>create_out( 
                )->convert( json_xml ) ). 
    FINAL(json_writer) = cl_sxml_string_writer=>create( 
                          type = if_sxml=>co_xt_json ) . 
    TRY. 
        reader->next_node( ). 
        reader->skip_node( json_writer ). 
      CATCH cx_sxml_parse_error INTO FINAL(error). 
        out->write_text( error->get_text( ) ). 
    ENDTRY. 
    FINAL(json) = json_writer->get_output( ). 
    out->write_json( json 
      )->end_section( 
      )->next_section( 'Parse' ). 
 
    "Parse JSON data without setting the member option 
    out->begin_section( 'JSON-XML without member elements' ). 
    FINAL(reader1) = cl_sxml_string_reader=>create( input = json ). 
    FINAL(xml_writer1) = cl_sxml_string_writer=>create( ). 
    TRY. 
        reader1->next_node( ). 
        reader1->skip_node( xml_writer1 ). 
      CATCH cx_sxml_parse_error INTO FINAL(error1). 
        out->write_text( error1->get_text( ) ). 
    ENDTRY. 
    out->write_xml( xml_writer1->get_output( ) ). 
 
    "Parse JSON data with setting the member option 
    out->next_section( 'JSON-XML with member elements' ). 
    FINAL(reader2) = cl_sxml_string_reader=>create( input = json ). 
    reader2->set_option( if_sxml_reader=>co_opt_sep_member ). 
    FINAL(xml_writer2) = cl_sxml_string_writer=>create( ). 
    TRY. 
        reader2->next_node( ). 
        reader2->skip_node( xml_writer2 ). 
      CATCH cx_sxml_parse_error INTO FINAL(error2). 
        out->write_text( error2->get_text( ) ). 
    ENDTRY. 
    out->write_xml( xml_writer2->get_output( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The string `json_xml` is filled with XML data in valid [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) and displayed. The element `<object>` contains elements that embody JSON object components directly and `<member>` elements that wrap these components.

A [JSON reader](../../abap-glossary/abenjson_reader_glosry.md) parses the string `json_xml` by calling the method `SKIP_NODE` in a single action and passes the XML data to a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) created with the type `IF_SXML=>CO_XT_JSON`. The output of this writer is passed to the string `json`, which then contains valid JSON data. The writer has implemented both kinds of the object components with the same result.

The string `json` is parsed with two further XML readers. The first parses with standard setting and the setting applies the option `IF_SXML_READER=>CO_OPT_SEP_MEMBER`. In the JSON-XML result of the first reader, no object component has a `<member>` element; in the JSON-XML results of the second reader, every object component is represented with a `<member>` element.

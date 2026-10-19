---
title: "sXML - Modifying XML Data"
source_file: abensxml_reader_writer_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Modifying XML Data

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads, modifies, and writes to XML data.

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
CLASS cl_demo_sxml_reader_writer DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_reader_writer IMPLEMENTATION. 
  METHOD main. 
    FINAL(xml) = 
     cl_abap_conv_codepage=>create_out( )->convert( 
       `<text>` && 
       `<line>aaaa</line>` && 
       `<line>bbbb</line>` && 
       `<line>cccc</line>` && 
       `</text>` ). 
 
    out->begin_section( 'Original XML-Data' 
      )->write_xml( xml ). 
 
    FINAL(reader) = cl_sxml_string_reader=>create( xml ). 
    FINAL(writer) = CAST if_sxml_writer( 
                          cl_sxml_string_writer=>create( ) ). 
    DO. 
      FINAL(node) = reader->read_next_node( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      IF node IS INSTANCE OF if_sxml_value_node. 
        FINAL(value_node) = CAST if_sxml_value_node( node ). 
        IF value_node->value_type = if_sxml_value=>co_vt_text. 
          value_node->set_value( 
            to_upper( value_node->get_value( ) ) ). 
        ENDIF. 
      ENDIF. 
      writer->write_node( node ). 
    ENDDO. 
 
    out->next_section( 'Modified XML-Data' 
      )->write_xml( 
        CAST cl_sxml_string_writer( writer )->get_output( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a loop, XML data is [parsed using object-oriented methods](abenabap_sxml_lib_parse_oo.md). If the node has a character-like value, the value in the associated object is transformed to uppercase letters. All read nodes and any modified nodes are [rendered using object-oriented methods](abenabap_sxml_lib_render_oo.md) in the same loop. The result is XML data in which all literal text elements are in uppercase letters. See also the corresponding executable example for the iXML Library.

## Hint

Any parts of XML data can be modified in a similar way. For example, the functions [`to_mixed`](../abap-processing-internal-data/abencase_functions.md), [`from_mixed`](../abap-processing-internal-data/abencase_functions.md) can be used to convert the names of XML elements between different naming conventions.

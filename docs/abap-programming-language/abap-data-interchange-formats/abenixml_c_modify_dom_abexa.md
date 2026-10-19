---
title: "iXML - Modify XML Documents"
source_file: abenixml_c_modify_dom_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Modify XML Documents

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Modifies XML documents in DOM representation.

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
CLASS cl_demo_ixml_cld_modify_elmnts DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS xml_source. 
    DATA xml_string TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_modify_elmnts IMPLEMENTATION. 
  METHOD main. 
    xml_source( ). 
 
    DATA(xml) = 
     cl_abap_conv_codepage=>create_out( )->convert( 
       source = xml_string ). 
 
    FINAL(o) = out->begin_section( 'Original XML Data' 
      )->write_xml( xml ). 
 
    FINAL(ixml) = cl_ixml_core=>create( ). 
    FINAL(stream_factory) = ixml->create_stream_factory( ). 
    FINAL(document) = ixml->create_document( ). 
    IF ixml->create_parser( 
      document = document 
      stream_factory = stream_factory 
      istream = stream_factory->create_istream_xstring( string = xml ) 
      )->parse( ) <> 0. 
      RETURN. 
    ENDIF. 
 
    DATA(renderer) = ixml->create_renderer( document = document 
                           ostream  = 
                           stream_factory->create_ostream_xstring( 
                           string = xml ) 
    ). 
 
    FINAL(iterator) = document->create_iterator( ). 
    DO. 
      FINAL(node) = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      IF node->get_type( ) = if_ixml_node=>co_node_text. 
        node->set_value( to_upper( node->get_value( ) ) ). 
      ENDIF. 
    ENDDO. 
 
    CLEAR xml. 
    renderer->render( ). 
 
    out->next_section( 'Modified XML Data' 
      )->write_xml( xml ). 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
     `<text>` && 
      `<line>aaaa</line>` && 
      `<line>bbbb</line>` && 
      `<line>cccc</line>` && 
      `</text>`. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is parsed to a DOM object. An iterator is used to iterate across all nodes of the document. If the element is a text element, its content is transformed to uppercase. The modified document is rendered and displayed. See also the corresponding executable example for [sXML Library](abensxml_reader_writer_abexa.md).

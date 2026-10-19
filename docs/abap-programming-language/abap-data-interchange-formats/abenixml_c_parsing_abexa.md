---
title: "iXML - Parse to DOM"
source_file: abenixml_c_parsing_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Parse to DOM

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Parses simple XML data to a DOM representation.

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
CLASS cl_demo_ixml_cloud_parsing DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS xml_source. 
    METHODS process_dom 
      IMPORTING document TYPE REF TO if_ixml_node. 
    METHODS process_errors 
      IMPORTING parser TYPE REF TO if_ixml_parser_core. 
    DATA xml_string TYPE string. 
    DATA xml_xstring TYPE xstring. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cloud_parsing IMPLEMENTATION. 
  METHOD main. 
    xml_source( ). 
 
    FINAL(ixml) = cl_ixml_core=>create( ). 
    FINAL(stream_factory) = ixml->create_stream_factory( ). 
    FINAL(document) = ixml->create_document( ). 
    FINAL(istream) = 
      stream_factory->create_istream_xstring( string = xml_xstring ). 
    FINAL(parser) = ixml->create_parser( 
                      document       = document 
                      stream_factory = stream_factory 
                      istream        = istream 
                    ). 
 
    IF parser->parse( ) <> 0. 
      process_errors( parser ). 
    ELSE. 
      process_dom( document ). 
    ENDIF. 
 
    process_dom( document ). 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
      `<?xml version="1.0"?>` && 
      `<order number="4711">` && 
      `<head>` && 
      `<status>confirmed</status>` && 
      `<date format="mm-dd-yyyy">07-19-2012</date>` && 
      `</head>` && 
      `<body>` && 
      `<item units="2" price="17.00">Part No. 0110</item>` && 
      `<item units="1" price="10.50">Part No. 1609</item>` && 
      `<item units="5" price="12.30">Part No. 1710</item>` && 
      `</body>` && 
      `</order>`. 
 
    CALL TRANSFORMATION id 
      SOURCE XML xml_string 
      RESULT XML xml_xstring. 
  ENDMETHOD. 
  METHOD process_dom. 
    IF document IS INITIAL. 
      RETURN. 
    ENDIF. 
    out->begin_section( 'DOM Tree' ). 
    FINAL(iterator) = document->create_iterator( ). 
    DATA(node) = iterator->get_next( ). 
    WHILE NOT node IS INITIAL. 
      FINAL(indent) = node->get_height( ) * 2. 
      CASE node->get_type( ). 
        WHEN if_ixml_node=>co_node_element. 
          FINAL(attributes) = node->get_attributes( ). 
          out->write( |Element:{ repeat( val = ` ` 
                                         occ = indent + 2  ) 
                              }{ node->get_name( ) }| ). 
          IF NOT attributes IS INITIAL. 
            DO attributes->get_length( ) TIMES. 
              FINAL(attr) = attributes->get_item( sy-index - 1 ). 
              out->write( |Attribute:{ repeat( val = ` ` 
                                               occ = indent ) 
                                     }{ attr->get_name( ) } = { 
                                        attr->get_value( ) } | ). 
            ENDDO. 
          ENDIF. 
        WHEN if_ixml_node=>co_node_text OR 
        if_ixml_node=>co_node_cdata_section. 
          out->write( |Text:{ repeat( val = ` ` occ = indent + 5 ) 
                           }{ node->get_value( ) }| ). 
      ENDCASE. 
      node = iterator->get_next( ). 
    ENDWHILE. 
  ENDMETHOD. 
  METHOD process_errors. 
    DO parser->num_errors( 
          min_severity = if_ixml_parse_error_core=>co_warning ) TIMES. 
      IF parser->get_error( 
           index = sy-index - 1 
           min_severity =  if_ixml_parse_error_core=>co_warning 
             )->get_severity( ) = if_ixml_parse_error_core=>co_warning. 
        out->write_text( parser->get_error( 
          index = sy-index - 1 
          min_severity = if_ixml_parse_error_core=>co_warning 
            )->get_reason( ) ). 
      ELSE. 
        out->write_text( parser->get_error( 
          index = sy-index - 1 
          min_severity = if_ixml_parse_error_core=>co_warning 
            )->get_reason( ) ). 
      ENDIF. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is first transformed to an input stream object and then imported into a DOM object using a parser object. If parsed successfully, the nodes of the DOM object are compiled as output texts in the method `process_dom`.

An [iterator](abenabap_ixml_lib_c_dom_iterat_r.md) is used to access the nodes. Each element is [checked](abenabap_ixml_lib_c_dom_direct_r.md) to see whether it has attributes. Existing attributes are then read.

If the XML data has errors, for example because a closing tag was renamed, the method `process_errors` is executed, and the appropriate error message is displayed.

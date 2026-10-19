---
title: "iXML - Sequential Parsing"
source_file: abenixml_c_sequential_pars_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Sequential Parsing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Parses simple XML data sequentially.

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
CLASS cl_demo_ixml_cloud_pars_sqntl DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS xml_source. 
    METHODS handle_errors 
      IMPORTING parser TYPE REF TO if_ixml_parser_core. 
    DATA xml_string TYPE string. 
    DATA xml_xstring TYPE xstring. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cloud_pars_sqntl IMPLEMENTATION. 
  METHOD main. 
    xml_source( ). 
 
    FINAL(ixml)           = cl_ixml_core=>create( ). 
    FINAL(stream_factory) = ixml->create_stream_factory( ). 
 
    FINAL(istream)        = stream_factory->create_istream_xstring( 
       string = xml_xstring ). 
 
    FINAL(document)       = ixml->create_document( ). 
    FINAL(parser)         = ixml->create_parser( 
                             stream_factory = stream_factory 
                             istream        = istream 
                             document       = document ). 
 
    parser->set_event_subscription( 
      events = if_ixml_event=>co_event_element_pre + 
               if_ixml_event=>co_event_element_post ). 
 
    DO. 
      FINAL(event) = parser->parse_event( ). 
      IF event IS INITIAL. 
        EXIT. 
      ENDIF. 
      FINAL(name)  = event->get_name( ). 
      FINAL(value) = event->get_value( ). 
      out->write( |{ name } { value }| ). 
      FINAL(xml_string) = ``. 
      ixml->create_renderer( 
        document = document 
        ostream  = stream_factory->create_ostream_xstring( 
                    string = xml_xstring ) 
         )->render( ). 
      out->write_xml( xml_string )->line( ). 
    ENDDO. 
 
    IF parser->num_errors( ) > 0. 
      handle_errors( parser ). 
      RETURN. 
    ENDIF. 
  ENDMETHOD. 
  METHOD handle_errors. 
    DO parser->num_errors( ) TIMES. 
      FINAL(error)  = parser->get_error( index = sy-index - 1 ). 
      FINAL(reason) = error->get_reason( ). 
      ... 
    ENDDO. 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
      `<texts>`              && 
      `  <text1>aaa</text1>` && 
      `  <text2>bbb</text2>` && 
      `</texts>`. 
 
    CALL TRANSFORMATION id 
      SOURCE XML xml_string 
      RESULT XML xml_xstring. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is first transformed to an input stream object and this object is then processed in a loop using a parser object until the method `PARSE_EVENT` returns an initial value. To define the sequences, the events `CO_EVENT_ELEMENT_PRE` and `CO_EVENT_ELEMENT_POST` of the interface are registered before the loop. These events are raised before and after the parsing of an element. The loop produces the name and value of the current element. The current DOM representation of the XML document is rendered in each loop pass and is also displayed.

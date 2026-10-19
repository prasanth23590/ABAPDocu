---
title: "iXML - Access to Attributes"
source_file: abenixml_c_attributes_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Access to Attributes

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses the attributes of the elements in a DOM.

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
CLASS cl_demo_ixml_cld_acc_attribute DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS xml_source. 
    DATA xml_string TYPE string. 
    DATA xml_xstring TYPE xstring. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_acc_attribute IMPLEMENTATION. 
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
 
    FINAL(rc) = parser->parse( ). 
 
    IF rc IS NOT INITIAL. 
      ... "Error handling 
      RETURN. 
    ENDIF. 
 
    FINAL(element) = document->get_root_element( ). 
    DATA(child) = element->get_first_child( ). 
 
    DATA(attributes) = child->get_attributes( ). 
    DO attributes->get_length( ) TIMES. 
      DATA(attribute) = attributes->get_item( sy-index - 1 ). 
      out->write( |{ attribute->get_name( ) } | && 
                  |{ attribute->get_value( ) }| ). 
    ENDDO. 
 
    out->line( ). 
    child = child->get_next( ). 
 
    attributes = child->get_attributes( ). 
    attribute = attributes->get_named_item_ns( name = 'format' ). 
    out->write( |{ attribute->get_name( ) } | && 
                |{ attribute->get_value( ) }| ). 
    attribute = attributes->get_named_item_ns( name = 'level' ). 
    out->write( |{ attribute->get_name( ) } | && 
                |{ attribute->get_value( ) }| ). 
 
    out->line( ). 
    child = child->get_next( ). 
 
    attribute = CAST if_ixml_element( child 
                       )->get_attribute_node_ns( name = 'format' ). 
    out->write( |{ attribute->get_name( ) } | && 
                |{ attribute->get_value( ) }| ). 
    out->write( |level { CAST if_ixml_element( 
                   child )->get_attribute_ns( name = 'level' ) }| ). 
 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
     `<texts>`                                        && 
     `  <text1 format="bold"   level="1">aaa</text1>` && 
     `  <text2 format="italic" level="2">bbb</text2>` && 
     `  <text3 format="arial"  level="3">ccc</text3>` && 
     `</texts>`. 
 
    CALL TRANSFORMATION id 
      SOURCE XML xml_string 
      RESULT XML xml_xstring. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is first transformed to an input stream object and the object is then imported into a DOM object using a parser object. If parsed successfully, the root node and its subnodes are read. Various methods for accessing the attributes of subnodes are displayed.

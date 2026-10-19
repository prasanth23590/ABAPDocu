---
title: "iXML - Iterator for Nodes"
source_file: abenixml_c_node_iterator_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Iterator for Nodes

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses the nodes in DOM using an iterator.

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
CLASS cl_demo_ixml_cld_node_iterator DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS xml_source. 
    DATA xml_string TYPE string. 
    DATA xml_xstring TYPE xstring. 
    METHODS iterate 
      IMPORTING iterator TYPE REF TO if_ixml_node_iterator. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_node_iterator IMPLEMENTATION. 
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
 
    DATA(iterator) = document->create_iterator( ). 
    iterate( iterator ). 
    out->line( ). 
 
    FINAL(element) = document->get_root_element( ). 
    iterator = element->create_iterator( ). 
    iterate( iterator ). 
    out->line( ). 
 
    FINAL(child) = element->get_first_child( ). 
    iterator = child->create_iterator( ). 
    iterate( iterator ). 
  ENDMETHOD. 
  METHOD iterate. 
    DO. 
      FINAL(node) = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      IF node->get_type( ) <> if_ixml_node=>co_node_element. 
        CONTINUE. 
      ENDIF. 
      out->write( |{ node->get_name( ) } | && 
                  |{ node->get_value( ) }| ). 
    ENDDO. 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
     `<texts>`                              && 
     `  <text1 format="bold">aaa</text1>`   && 
     `  <text2 format="italic">bbb</text2>` && 
     `</texts>`. 
 
    CALL TRANSFORMATION id 
      SOURCE XML xml_string 
      RESULT XML xml_xstring. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is first transformed to an input stream object and the object is then imported into a DOM object using a parser object. If parsed successfully, iterators are created for the entire document, the root node, and a subnode of the root node and iterations are performed across its nodes. By selecting the node type, only XML elements are respected in the output.

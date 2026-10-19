---
title: "iXML - Iterator for Node List"
source_file: abenixml_c_node_list_itrtr_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Iterator for Node List

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses the nodes in a node list in DOM using an iterator.

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
CLASS cl_demo_ixml_cld_node_list_itr DEFINITION 
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
CLASS cl_demo_ixml_cld_node_list_itr IMPLEMENTATION. 
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
 
    FINAL(nodes) = document->get_root_element( )->get_children( ). 
    FINAL(iterator) = nodes->create_iterator( ). 
 
    DO. 
      FINAL(node) = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      out->write_text( |{ node->get_name( ) } | && 
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

XML data is first transformed to an input stream object and the object is then imported into a DOM object using a parser object. If parsed successfully, an iterator is created for the subnodes of the root node and used for iterations.

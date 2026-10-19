---
title: "iXML - DOM Representation"
source_file: abenixml_c_dom_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - DOM Representation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

DOM representation of XML data.

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
CLASS cl_demo_ixml_cloud_dom DEFINITION 
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
CLASS cl_demo_ixml_cloud_dom IMPLEMENTATION. 
  METHOD main. 
    FINAL(o) = out->begin_section( `XML-Data` ). 
    xml_source( ). 
    out->write_xml( xml_xstring ). 
 
    out->next_section( `XML-Document in DOM-Format` ). 
    TYPES: BEGIN OF t_node, 
             gid    TYPE i, 
             type   TYPE i, 
             prefix TYPE string, 
             name   TYPE string, 
             value  TYPE string, 
           END OF t_node. 
    DATA node_tab TYPE STANDARD TABLE OF t_node. 
 
    FINAL(ixml)           = cl_ixml_core=>create( ). 
    FINAL(document)       = ixml->create_document( ). 
    TRY. 
        CALL TRANSFORMATION id SOURCE XML xml_xstring 
                                  RESULT XML document. 
      CATCH cx_transformation_error. 
        RETURN. 
    ENDTRY. 
    FINAL(iterator) = document->create_iterator( ). 
    DO. 
      DATA(node) = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      APPEND VALUE #( 
        gid     = node->get_gid( ) 
        type    = node->get_type( ) 
        prefix  = node->get_namespace_prefix( ) 
        name    = node->get_name( ) 
        value   = node->get_value( ) ) TO node_tab. 
    ENDDO. 
    out->write_data( node_tab ). 
 
    TYPES: BEGIN OF t_attribute, 
             name  TYPE string, 
             value TYPE string, 
           END OF t_attribute. 
    DATA attribute_tab TYPE STANDARD TABLE OF t_attribute. 
    iterator->reset( ). 
    DO. 
      node = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      FINAL(attributes) = node->get_attributes( ). 
      IF attributes IS INITIAL OR attributes->get_length( ) = 0. 
        CONTINUE. 
      ENDIF. 
      CLEAR attribute_tab. 
      DO. 
        FINAL(attribute) = attributes->get_item( sy-index - 1 ). 
        IF attribute IS INITIAL. 
          EXIT. 
        ENDIF. 
        APPEND VALUE #( 
          name  = attribute->get_name( ) 
          value = attribute->get_value( ) ) TO attribute_tab. 
      ENDDO. 
      out->begin_section( |Attributes of GID { node->get_gid( ) }| 
        )->write_data( attribute_tab 
        )->end_section( ). 
    ENDDO. 
  ENDMETHOD. 
  METHOD xml_source. 
    xml_string = 
      `<?xml version="1.0"?>` && 
      `<order number="4711"` && 
      ` xmlns:demo="http://www.sap.com/abapdemos">` && 
      `<!-- Head and body of order -->` && 
      ` <demo:head>` && 
      ` <demo:status>confirmed</demo:status>` && 
      ` <demo:date format="mm-dd-yyyy">07-19-2012</demo:date>` && 
      ` </demo:head>` && 
      ` <demo:body>`  && 
      ` <demo:item units="2" price="17.00">Part No. 0110</demo:item>` && 
      ` <demo:item units="1" price="10.50">Part No. 1609</demo:item>` && 
      ` <demo:item units="5" price="12.30">Part No. 1710</demo:item>` && 
      ` </demo:body>` && 
      `</order>`. 
 
    CALL TRANSFORMATION id 
      SOURCE XML xml_string 
      RESULT XML xml_xstring. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is transformed to its DOM representation using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`. An [iterator](abenabap_ixml_lib_c_dom_iterat_r.md) is used to read all DOM nodes and pass their most important properties to an internal table and then output them. A second iteration reads the attributes of elements, whose internal table is also output.

## Hint

The GID is a unique internal indexing of a node.

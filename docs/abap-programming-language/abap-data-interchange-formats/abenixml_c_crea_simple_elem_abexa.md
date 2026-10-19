---
title: "iXML - Create Simple Elements"
source_file: abenixml_c_crea_simple_elem_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Create Simple Elements

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creates single elements in DOM.

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
CLASS cl_demo_ixml_cld_create_smpl_e DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_create_smpl_e IMPLEMENTATION. 
  METHOD main. 
    FINAL(ixml)     = cl_ixml_core=>create( ). 
    FINAL(document) = ixml->create_document( ). 
 
    FINAL(root) = document->create_simple_element_ns( 
                   prefix = 'asx' 
                   name = 'abap' 
                   parent = document ). 
    root->set_attribute_ns( prefix = 'xmlns' 
                            name = 'asx' 
                            value = 'http://www.sap.com/abapxml' ). 
    root->set_attribute_ns( name =  'version' 
                            value = '1.0' ). 
 
    FINAL(node1) = document->create_simple_element_ns( 
                    prefix = 'asx' 
                    name = 'values' 
                    parent = root ). 
 
    document->create_simple_element_ns( 
                name = 'TEXT' 
                value = 'Hello XML' 
                parent = node1 ). 
 
    DATA xml_xstring TYPE xstring. 
    ixml->create_renderer( document = document 
                           ostream  = ixml->create_stream_factory( 
                                        )->create_ostream_xstring( 
                                             string = xml_xstring ) 
                                               )->render( ). 
    out->write_xml( xml_xstring ). 
 
    DATA result TYPE string. 
    CALL TRANSFORMATION id SOURCE XML xml_xstring 
                           RESULT  text = result. 
    out->write_data( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

As in the executable example [Creating Nodes](abenixml_c_crea_elem_abexa.md), but using the method `CREATE_SIMPLE_ELEMENT_NS` to create elements with content and insert them.

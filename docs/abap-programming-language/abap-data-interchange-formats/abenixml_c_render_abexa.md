---
title: "iXML - Rendering"
source_file: abenixml_c_render_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Rendering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Renders XML documents to DOM representation.

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
CLASS cl_demo_ixml_cld_render DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_render IMPLEMENTATION. 
  METHOD main. 
 
    DATA source_tab TYPE TABLE OF i. 
    source_tab = VALUE #( FOR j = 1 UNTIL j > 10 
                        ( ipow( base = 2 exp = j ) ) ). 
    FINAL(ixml) = cl_ixml_core=>create( ). 
    FINAL(stream_factory) = ixml->create_stream_factory( ). 
    FINAL(document) = ixml->create_document( ). 
    CALL TRANSFORMATION id SOURCE text = `Powers of 2` 
                                  numbers = source_tab 
                           RESULT XML document. 
    DO 7 TIMES. 
      document->find_from_name_ns( name = 'item' )->remove_node( ). 
    ENDDO. 
 
    out->begin_section( 
      `Renderer for complete document` ). 
    DATA xml_xstring TYPE xstring. 
    ixml->create_renderer( document = document 
                           ostream  = 
                           stream_factory->create_ostream_xstring( 
                                             string = xml_xstring ) 
                         )->render( ). 
    out->write_xml( xml_xstring ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is created in asXML format using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) and written directly to an XML document in DOM representation. The method `REMOVE_NODE` is used to remove some nodes and the content of the modified document is rendered in the following way:

- A renderer is created for the entire document and its method `RENDER` is executed, producing complete XML data.

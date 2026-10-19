---
title: "sXML - Token-Based Rendering"
source_file: abensxml_rendering_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Token-Based Rendering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[Token-based](abenabap_sxml_lib_render_token.md) writing of simple XML data.

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
CLASS cl_demo_sxml_token_writer DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_token_writer IMPLEMENTATION. 
  METHOD main. 
    FINAL(writer) = 
      CAST if_sxml_writer( cl_sxml_string_writer=>create(  ) ). 
    TRY. 
        writer->open_element( name = 'texts' 
                              nsuri = 'http://www.sap.com/abapdemos' 
                              prefix = 'demo' ). 
        writer->open_element( name = 'text' 
                              nsuri = 'http://www.sap.com/abapdemos' ). 
        writer->write_attribute( name = 'format' value = 'bold' ). 
        writer->write_attribute( name = 'level'  value = '1' ). 
        writer->write_value( 'aaaa' ). 
        writer->close_element( ). 
        writer->open_element( name = 'text' 
                              nsuri = 'http://www.sap.com/abapdemos' ). 
        writer->write_attribute( name = 'format' value = 'italic' ). 
        writer->write_attribute( name = 'level'  value = '2' ). 
        writer->write_value( 'bbbb' ). 
        writer->close_element( ). 
        writer->close_element( ). 
      CATCH cx_sxml_state_error INTO FINAL(error). 
        out->write_text( error->get_text( ) ). 
        RETURN. 
    ENDTRY. 
    FINAL(xml) = 
      CAST cl_sxml_string_writer( writer )->get_output(  ). 
    out->write_xml( xml ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example shows how XML data can be created using the methods `OPEN_ELEMENT`, `WRITE_ATTRIBUTE`, `WRITE_VALUE`, `CLOSE_ELEMENT`, of the interface `IF_SXML_WRITER`.

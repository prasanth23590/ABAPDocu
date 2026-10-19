---
title: "sXML - Object-Oriented Rendering"
source_file: abensxml_oo_rendering_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Object-Oriented Rendering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[Object-oriented](abenabap_sxml_lib_render_oo.md) writing of simple XML data.

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
CLASS cl_demo_sxml_oo_writer DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_oo_writer IMPLEMENTATION. 
  METHOD main. 
    FINAL(writer) = 
      CAST if_sxml_writer( cl_sxml_string_writer=>create(  ) ). 
 
    DATA open_element TYPE REF TO if_sxml_open_element. 
    DATA value TYPE REF TO if_sxml_value_node. 
    TRY. 
        open_element = writer->new_open_element( 
                         name = 'texts' 
                         nsuri = 'http://www.sap.com/abapdemos' 
                         prefix = 'demo' ). 
        writer->write_node( open_element ). 
        open_element = writer->new_open_element( 
                         name = 'text' 
                         nsuri = 'http://www.sap.com/abapdemos' ). 
        open_element->set_attribute( name = 'format' 
                                     value = 'bold' ). 
        open_element->set_attribute( name = 'level' 
                                     value = '1' ). 
        writer->write_node( open_element ). 
        value = writer->new_value( ). 
        value->set_value( 'aaaa' ). 
        writer->write_node( value ). 
        writer->write_node( writer->new_close_element( ) ). 
        open_element = writer->new_open_element( 
                         name = 'text' 
                         nsuri = 'http://www.sap.com/abapdemos' ). 
        open_element->set_attribute( name = 'format' 
                                     value = 'italic' ). 
        open_element->set_attribute( name = 'level' 
                                     value = '2' ). 
        writer->write_node( open_element ). 
        value = writer->new_value( ). 
        value->set_value( 'bbbb' ). 
        writer->write_node( value ). 
        writer->write_node( writer->new_close_element( ) ). 
        writer->write_node( writer->new_close_element( ) ). 
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

This example shows how XML data can be created using the methods for the object-oriented rendering of the interface `IF_SXML_WRITER`.

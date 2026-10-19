---
title: "sXML - Defining XML Header"
source_file: abensxml_writer_header_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Defining XML Header

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines an XML header.

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
CLASS cl_demo_sxml_header DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_header IMPLEMENTATION. 
  METHOD main. 
    FINAL(writer) = CAST if_sxml_writer( 
                      cl_sxml_string_writer=>create( ) ). 
 
    writer->set_option( 
      option = if_sxml_writer=>co_opt_xml_header 
      value  = if_sxml_writer=>co_opt_val_without_encoding ). 
 
    writer->open_element( name = 'document' ). 
    writer->open_element( name = 'header' ). 
    CASE writer->get_option( 
      option = if_sxml_writer=>co_opt_xml_header ). 
      WHEN if_sxml_writer=>co_opt_val_full. 
        writer->write_attribute( name = 'version' value = '1.0' ). 
        writer->write_attribute( name = 'encoding' value = 'utf-8' ). 
      WHEN if_sxml_writer=>co_opt_val_without_encoding. 
        writer->write_attribute( name = 'version' value = '1.0' ). 
      WHEN OTHERS. 
    ENDCASE. 
    writer->close_element( ). 
    writer->close_element( ). 
 
    DATA(result) = cl_abap_conv_codepage=>create_in( )->convert( 
                   CAST cl_sxml_string_writer( 
                     writer )->get_output( ) ). 
 
    out->write_xml( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the usage of the header option for the [sXML writer](abenabap_sxml_lib_render.md). Here, the value is set to `co_opt_val_without_encoding`.

---
title: "sXML - Transformation to XML Writer"
source_file: abensxml_trafo_into_writer_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Transformation to XML Writer

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Transformation of ABAP data to an XML writer.

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
CLASS cl_demo_sxml_trafo_into_writer DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_trafo_into_writer IMPLEMENTATION. 
  METHOD main. 
    FINAL(user_date) = cl_demo_date_time=>get_user_date( ). 
    FINAL(writer) = 
      CAST if_sxml_writer( cl_sxml_string_writer=>create(  ) ). 
    writer->open_element( name = 'document' ). 
    writer->open_element( name = 'head' ). 
    writer->open_element( name = 'author' ). 
    writer->write_value( CONV string( sy-uname ) ). 
    writer->close_element( ). 
    writer->open_element( name = 'date' ). 
    writer->write_value( CONV string( user_date ) ). 
    writer->close_element( ). 
    writer->close_element( ). 
    writer->open_element( name = 'body' ). 
    DO 10 TIMES. 
      CALL TRANSFORMATION id SOURCE number  = sy-index 
                             RESULT XML writer. 
    ENDDO. 
    writer->close_element( ). 
    writer->close_element( ). 
    FINAL(xml) = 
      CAST cl_sxml_string_writer( writer )->get_output(  ). 
    out->write_xml( xml ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An XML writer is filled with XML data that is split into the parts `head` and `body`. The data content of the element `body` is taken directly from an internal table using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`.

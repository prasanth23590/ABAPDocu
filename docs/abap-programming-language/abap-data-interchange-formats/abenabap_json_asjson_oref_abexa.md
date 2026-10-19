---
title: "JSON - asJSON for Object References"
source_file: abenabap_json_asjson_oref_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - asJSON for Object References

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

## Source Code

``` abap
* CCDEF 
INTERFACE intf. 
  DATA attr TYPE string. 
ENDINTERFACE. 
CLASS serializable DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_serializable_object. 
    INTERFACES intf DATA VALUES attr = 'Interface Attribute'. 
    DATA attr1 TYPE string VALUE `Attribute 1`. 
    DATA attr2 TYPE string VALUE `Attribute 2`. 
  PRIVATE SECTION. 
    CONSTANTS serializable_class_version TYPE i VALUE 1. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_asjson_oref DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asjson_oref IMPLEMENTATION. 
  METHOD main. 
    FINAL(oref) = NEW serializable( ). 
 
    "Transformation to JSON 
    out->begin_section( 'asJSON'  ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE oref = oref 
                           RESULT XML writer. 
    FINAL(json) = writer->get_output( ). 
    out->write_json( json ). 
 
    "JSON-XML 
    out->next_section( 'asJSON-XML' ). 
    FINAL(reader) = cl_sxml_string_reader=>create( json ). 
    FINAL(xml_writer) = cl_sxml_string_writer=>create( ). 
    reader->next_node( ). 
    reader->skip_node( xml_writer ). 
    DATA(xml) = xml_writer->get_output( ). 
    out->write_xml( xml ). 
 
    "asXML 
    out->next_section( 'asXML' ). 
    CALL TRANSFORMATION id SOURCE oref = oref 
                           RESULT XML xml. 
    out->write_xml( xml ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, for which a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) is specified as the XML target, is called to create the [asJSON](../../abap-glossary/abenasjson_glosry.md) representation of a reference variable that points to an instance.

For comparison, the [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation of the JSON data and the [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the ABAP data is also shown.

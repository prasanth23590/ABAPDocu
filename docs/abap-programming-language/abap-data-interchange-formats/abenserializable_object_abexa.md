---
title: "Adjusted Serialization and Deserialization"
source_file: abenserializable_object_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types > asXML - Mapping of Reference Variables and Objects > asXML - Instances of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Adjusted Serialization and Deserialization

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the adjusted serialization and deserialization of objects.

## Source Code

``` abap
* CCDEF 
INTERFACE intf. 
  METHODS get_attr RETURNING VALUE(attr) TYPE string. 
ENDINTERFACE. 
CLASS cls_unsafe DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES: if_serializable_object, 
      intf. 
  PRIVATE SECTION. 
    DATA attr TYPE string VALUE 'Private'. 
ENDCLASS. 
 
CLASS cls_safe DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES: if_serializable_object, 
      intf. 
  PRIVATE SECTION. 
    DATA attr TYPE string VALUE 'Private'. 
    METHODS: serialize_helper EXPORTING attr TYPE string, 
    deserialize_helper IMPORTING attr TYPE string. 
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
CLASS cl_demo_serializable_object DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS serialize_deserialize CHANGING iref TYPE REF TO intf. 
ENDCLASS. 
 
* CCIMP 
CLASS cls_unsafe IMPLEMENTATION. 
  METHOD intf~get_attr. 
    attr = me->attr. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS cls_safe IMPLEMENTATION. 
  METHOD serialize_helper. 
    attr = me->attr. 
  ENDMETHOD. 
  METHOD deserialize_helper. 
  ENDMETHOD. 
  METHOD intf~get_attr. 
    attr = me->attr. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_serializable_object IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 'Unsafe Class' ). 
    DATA(iref_unsafe) = CAST intf( NEW cls_unsafe( ) ). 
    serialize_deserialize( CHANGING iref = iref_unsafe ). 
 
    out->next_section( 'Safe Class' ). 
    DATA(iref_safe) = CAST intf( NEW cls_safe( ) ). 
    serialize_deserialize( CHANGING iref = iref_safe ). 
 
  ENDMETHOD. 
  METHOD serialize_deserialize. 
    DATA xml_string TYPE string. 
    DATA json_string TYPE string. 
    out->write_data( iref->get_attr( ) 
      )->begin_section( 'asXML' ). 
    CALL TRANSFORMATION id SOURCE oref = iref 
                           RESULT XML xml_string. 
    out->write_xml( xml_string ). 
    REPLACE PCRE '(<ATTR>)([^<]+)(</ATTR>)' IN xml_string 
                                            WITH '$1Public$3'. 
    IF sy-subrc = 0. 
      CALL TRANSFORMATION id SOURCE XML xml_string 
                             RESULT oref = iref. 
      out->write_data( iref->get_attr( ) ). 
    ENDIF. 
    out->next_section( 'asJSON' ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
                     type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE oref = iref 
                           RESULT XML writer. 
    json_string = cl_abap_conv_codepage=>create_in( )->convert( 
                                      writer->get_output( ) ). 
    out->write_json( json_string ). 
    REPLACE PCRE '("ATTR":")([^"]+)(")' IN json_string 
                                        WITH '$1Nonsense$3'. 
    IF sy-subrc = 0. 
      CALL TRANSFORMATION id SOURCE XML json_string 
                             RESULT oref = iref. 
      out->write_data( iref->get_attr( ) ). 
    ENDIF. 
    out->end_section( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, objects in two classes are serialized to [asXML](../../abap-glossary/abenasxml_glosry.md) and to [asJSON](../../abap-glossary/abenasjson_glosry.md), and then deserialized.

The object of the class `cl_unsafe` is processed by default. The example shows that the standard behavior allows an object in a class to be created for which a private attribute receives a value set from outside, both for asXML and for asJSON After deserialization, the value of the private attribute `attr` in the new class does not match the value defined in the class.

The object of the class `cl_safe` is processed in an adjusted way. The example demonstrates how the methods `SERIALIZE_HELPER` and `DESERIALIZE_HELPER` can be used to prevent unwanted manipulation of attributes. The private attribute `attr` is serialized using `SERIALIZE_HELPER` but is not deserialized in `DESERIALIZE_HELPER`.

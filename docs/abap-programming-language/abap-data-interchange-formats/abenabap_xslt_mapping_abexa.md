---
title: "asXML - Mapping of UUIDs"
source_file: abenabap_xslt_mapping_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of UUIDs

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the mapping of UUIDs to XML schema data types.

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
CLASS cl_demo_abap_xml_schema_map DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_xml_schema_map IMPLEMENTATION. 
  METHOD main. 
 
    DATA: uuid      TYPE xsduuid_char, 
          uuid1     TYPE xsduuid_char, 
          uuid2     TYPE xsduuid_char, 
          exc_trafo TYPE REF TO cx_transformation_error, 
          exc_prev  TYPE REF TO cx_root. 
 
    FIELD-SYMBOLS <uuid> TYPE sysuuid_c32. 
 
    TRY. 
        uuid = cl_uuid_factory=>create_system_uuid( 
          )->create_uuid_c32( ). 
        ASSIGN uuid TO <uuid>. 
        CALL TRANSFORMATION id SOURCE uuid1 = uuid 
                                      uuid2 = <uuid> 
                               RESULT XML FINAL(xml_xstring). 
        out->write_xml( xml_xstring ). 
      CATCH cx_uuid_error. 
        RETURN. 
      CATCH cx_transformation_error. 
        RETURN. 
    ENDTRY. 
 
    TRY. 
        CALL TRANSFORMATION demo_uuid SOURCE XML xml_xstring 
                                      RESULT uuid1 = uuid1 
                                             uuid2 = uuid2. 
      CATCH cx_transformation_error INTO exc_trafo. 
        out->write( exc_trafo->get_text( ) ). 
        IF exc_trafo->previous IS NOT INITIAL. 
          exc_prev = exc_trafo->previous. 
          out->write( exc_prev->get_text( ) ). 
        ENDIF. 
    ENDTRY. 
    out->write( `UUID1 = ` && uuid1 ). 
    out->write( `UUID2 = ` && uuid2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, a [UUID](../../abap-glossary/abenuuid_glosry.md) is created and passed to the predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` with the data types `XSDUUID_CHAR` and `SYSUUID_C32`. The UUID of the type `XSDUUID_CHAR` is recognized as such and converted to the associated [XML schema data type](abenabap_xslt_asxml_schema.md). However, the UUID of the type `SYSUUID_C32` is interpreted as a regular text field and passed unconverted in accordance with the associated rules for the [mapping of elementary ABAP types](abenabap_xslt_asxml_elementary.md).

When the new XML data is deserialized using the Simple Transformation `DEMO_UUID`, an attempt is made to convert both nodes to ABAP UUIDs of type `XSDUUID_CHAR`. This only works for the first node, which exists in the correct XML schema data type. In the case of the second node, which exists as unformatted text, an exception is raised.

The example shows that it is possible to work with XML schema data types without having to use self-programmed conversions. However, it also shows that when using XML schema data types it is important to pay attention to the correct mapping of data types.

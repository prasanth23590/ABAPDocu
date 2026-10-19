---
title: "asXML - Mapping of XML Fragments"
source_file: abenasxml_fragments_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of XML Fragments

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the mapping of XML fragments.

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
CLASS cl_demo_asxml_fragment DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS prepare_fragment 
      RETURNING VALUE(xml) TYPE xstring. 
    METHODS serialize 
      IMPORTING source        TYPE any 
                node          TYPE string 
                trafo         TYPE string 
                text          TYPE string 
      RETURNING VALUE(result) TYPE xstring. 
    METHODS deserialize 
      IMPORTING source TYPE xstring 
                node   TYPE string 
                trafo  TYPE string 
                text   TYPE string 
      EXPORTING result TYPE any. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_fragment IMPLEMENTATION. 
  METHOD main. 
    DATA: xstr    TYPE xstring, 
          xsdstr  TYPE xsdany, 
          xmlstr1 TYPE xstring, 
          xmlstr2 TYPE xstring. 
 
    xstr = prepare_fragment( ). 
 
    xmlstr1 = serialize( 
      source = xstr 
      node   = 'ROOT' 
      trafo  = 'ID' 
      text =  'XSLT-Serialization of XML-Fragment from XSTRING' ). 
 
    xsdstr = xstr. 
 
    xmlstr1 = serialize( 
      source = xsdstr 
      node   = 'ROOT' 
      trafo  = 'ID' 
      text =  'XSLT-Serialization of XML-Fragment from XSDANY' & 
              ' into node ROOT' ). 
 
    xmlstr2 = serialize( 
      source = xsdstr 
      node   = 'X' 
      trafo  = 'ID' 
      text =  'XSLT-Serialization of XML-Fragment from XSDANY' & 
              ' into node X' ). 
 
 
    deserialize( 
      EXPORTING 
        source = xmlstr1 
        node   = 'ROOT' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node ROOT' & 
                 ' into XSTRING' 
      IMPORTING result = xstr ). 
    deserialize( 
      EXPORTING 
        source = xmlstr2 
        node   = 'X' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node X' & 
                 ' into XSTRING' 
      IMPORTING result = xstr ). 
 
    deserialize( 
      EXPORTING 
        source = xmlstr1 
        node   = 'ROOT' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node ROOT' & 
                 ' into XSDANY' 
      IMPORTING result = xsdstr ). 
    deserialize( 
      EXPORTING 
        source = xmlstr2 
        node   = 'X' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node X' & 
                 ' into XSDANY' 
      IMPORTING result = xsdstr ). 
 
    deserialize( 
      EXPORTING 
        source = xmlstr1 
        node   = 'X' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node ROOT' & 
                 ' into XSDANY using node X' 
      IMPORTING result = xsdstr ). 
    deserialize( 
      EXPORTING 
        source = xmlstr2 
        node   = 'ROOT' 
        trafo  = 'ID' 
        text   = 'XSLT-Deserialization of XSLT-result with node X' & 
                 ' into XSDANY using node ROOT' 
      IMPORTING result = xsdstr ). 
 
  ENDMETHOD. 
  METHOD deserialize. 
    FINAL(result_tab) = VALUE abap_trans_resbind_tab( 
     ( name = node value = REF #( result ) ) ). 
    TRY. 
        out->begin_section( text ). 
        CALL TRANSFORMATION (trafo) 
          SOURCE XML source 
          RESULT (result_tab) 
          OPTIONS clear = 'all'. 
        IF result IS NOT INITIAL. 
          out->write_xml( result ). 
        ELSE. 
          out->write_text( 'Initial' ). 
        ENDIF. 
      CATCH cx_transformation_error. 
        out->write_text( 'Error' ). 
    ENDTRY. 
    out->end_section( ). 
  ENDMETHOD. 
  METHOD prepare_fragment. 
    out->begin_section( 
      )->begin_section( 'XML-Fragment' ). 
    xml = cl_abap_conv_codepage=>create_out( )->convert( 
      `<?xml version="1.0" encoding="utf-8" ?>` && 
      `<X>`            && 
      `Text`           && 
      `<X1>Text1</X1>` && 
      `<X2>Text1</X2>` && 
      `</X>` ). 
    out->write_xml( xml 
      )->end_section( ). 
  ENDMETHOD. 
  METHOD serialize. 
    FINAL(source_tab) = VALUE abap_trans_srcbind_tab( 
     ( name = node value = REF #( source ) ) ). 
    TRY. 
        out->begin_section( text ). 
        CALL TRANSFORMATION (trafo) 
          SOURCE (source_tab) 
          RESULT XML result. 
        out->write_xml( result ). 
      CATCH cx_transformation_error. 
        out->write_text( 'Error' ). 
    ENDTRY. 
    out->end_section( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the serialization and deserialization of XML fragments and their representation in asXML using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`.

- First, an XML fragment with the root element *X* is created in a variable `xstr` with the type `xstring` and the result is displayed.

- The fragment is serialized from the variable `xstr` of type `xstring` to an element `ROOT` as the XML schema type `xsd:base64Binary` in accordance with the rules for the [mapping of elementary data types](abenabap_xslt_asxml_elementary.md).

- On the other hand, a serialization of the fragment from the variable `xsdstr` of type `XSDANY` adds the attribute `asx:root` with the content *X*, that is, the name of the root element of the XML fragment) to the element `ROOT` and represents the remaining content of the fragment in an unchanged way.

- A further serialization of the fragment from the variable `xsdstr` produces the element *X*. This has the same name as the root element of the XML fragment and so the attribute is not added.

- Any attempt to deserialize the fragment content to an ABAP variable of type `xstring` fails for both serialization results, since the attribute specified for `NODE` when mapping elementary data types is not supported or because no valid asXML format exists for the target variable.

- Deserializations to variables of type `XSDANY` are possible in both cases, however, and create the original XML fragment again in the variable.

- If a nonexistent element is addressed in deserializations, no deserialization is performed as usual.

For information about serializations and deserializations of XML fragments using [Simple Transformations](abenabap_st.md), see the executable example [ST, Mapping of XML Fragments](abenst_xsdany_abexa.md).

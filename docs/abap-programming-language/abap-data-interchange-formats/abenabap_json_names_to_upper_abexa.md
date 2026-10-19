---
title: "JSON - Transforming Names"
source_file: abenabap_json_names_to_upper_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Transforming Names

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Transforms the names of JSON objects to uppercase letters.

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
CLASS cl_demo_json_names_to_upper DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS: 
      json_names_to_upper_pr 
        IMPORTING in       TYPE xstring 
        RETURNING VALUE(o) TYPE xstring, 
      json_names_to_upper_tr 
        IMPORTING in       TYPE xstring 
        RETURNING VALUE(o) TYPE xstring. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_json_names_to_upper IMPLEMENTATION. 
  METHOD main. 
    DATA: BEGIN OF struc, 
            col1 TYPE i, 
            col2 TYPE i, 
          END OF struc. 
 
    FINAL(json) = cl_abap_conv_codepage=>create_out( )->convert( 
                   `{"struc":{"col1":1,"col2":2}}` ). 
 
    out->begin_section( 'Original JSON' 
      )->write_json( json ). 
 
    CALL TRANSFORMATION id SOURCE XML json RESULT struc = struc. 
 
    out->next_section( 'Deserialized JSON' 
      )->write( struc ). 
 
    FINAL(asjson) = json_names_to_upper_pr( json ). 
 
    ASSERT asjson = json_names_to_upper_tr( json ). 
 
    out->begin_section( 'Modified JSON' 
      )->write_json( asjson ). 
 
    CALL TRANSFORMATION id SOURCE XML asjson RESULT struc = struc. 
 
    out->next_section( 'Deserialized JSON' 
      )->write( struc ). 
  ENDMETHOD. 
  METHOD json_names_to_upper_pr. 
    FINAL(reader) = cl_sxml_string_reader=>create( in ). 
    FINAL(writer) = CAST if_sxml_writer( 
      cl_sxml_string_writer=>create( type = if_sxml=>co_xt_json ) ). 
    DO. 
      FINAL(node) = reader->read_next_node( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      IF node->type = if_sxml_node=>co_nt_element_open. 
        FINAL(attributes)  = CAST if_sxml_open_element( 
                                   node )->get_attributes( ). 
        LOOP AT attributes ASSIGNING FIELD-SYMBOL(<attribute>). 
          IF <attribute>->qname-name = 'name'. 
            <attribute>->set_value( 
              to_upper( <attribute>->get_value( ) ) ). 
          ENDIF. 
        ENDLOOP. 
      ENDIF. 
      writer->write_node( node ). 
    ENDDO. 
    o = CAST cl_sxml_string_writer( writer )->get_output( ) . 
  ENDMETHOD. 
  METHOD json_names_to_upper_tr. 
    FINAL(writer) = 
      cl_sxml_string_writer=>create( type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION demo_json_xml_to_upper 
                        SOURCE XML in 
                        RESULT XML writer. 
    o = writer->get_output( ) . 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates how the names of [JSON data](abenjson_oview.md) objects can be transformed to uppercase letters, so that they can be bound to the corresponding ABAP data in deserializations using the statement `CALL TRANSFORMATION` for example. Two transformation methods are demonstrated:

- Parsing and rendering in the method `json_names_to_upper_pr`

  - This transforms the JSON data to [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md).

  - The result is parsed using an [XML reader](../../abap-glossary/abenxml_reader_glosry.md).

  - The attributes with the name `name` are transformed to uppercase letters as in the executable example [Modifying XML Data](abensxml_reader_writer_abexa.md).

  - The result is rendered back to JSON using a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md).

- Calling a transformation in the method `json_names_to_upper_tr`

  - The XSL transformation `DEMO_JSON_XML_TO_UPPER`, written for this purpose, is used to transform the object names in [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) to uppercase letters and places the result in a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md).

  - The modified JSON data is read from the writer.

The statement `ASSERT` guarantees that the results of both transformations are the same. After the transformation, the data is deserialized successfully to the ABAP structure. The method used in practice depends on performance and the volume of data expected.

The XSL transformation used `DEMO_JSON_XML_TO_UPPER` is as follows:

``` abap
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
               xmlns:sap="http://www.sap.com/sapxsl" version="1.0"> 
  <xsl:template match="@* | node()"> 
    <xsl:copy> 
      <xsl:apply-templates select="@* | node()"/> 
    </xsl:copy> 
  </xsl:template> 
  <xsl:template match="@*"> 
    <xsl:attribute name="name"> 
      <xsl:value-of select="sap:upper-case(.)"/> 
    </xsl:attribute> 
  </xsl:template> 
</xsl:transform>
```

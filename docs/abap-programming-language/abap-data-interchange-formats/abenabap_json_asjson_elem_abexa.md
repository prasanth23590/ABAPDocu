---
title: "JSON - asJSON for Elementary Object Types"
source_file: abenabap_json_asjson_elem_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - asJSON for Elementary Object Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [asJSON](abenabap_asjson_abap_types_elem.md) for all elementary ABAP types.

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
CLASS cl_demo_asjson_elmntry_types DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asjson_elmntry_types IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      i          TYPE i            VALUE -123, 
      int8       TYPE int8         VALUE -123, 
      p          TYPE p DECIMALS 2 VALUE `-1.23`, 
      decfloat16 TYPE decfloat16   VALUE `123E+1`, 
      decfloat34 TYPE decfloat34   VALUE `-3.140000E+02`, 
      f          TYPE f            VALUE `-3.140000E+02`, 
      c          TYPE c LENGTH 3   VALUE ` Hi`, 
      string     TYPE string       VALUE ` Hello `, 
      n          TYPE n LENGTH 6   VALUE `001234`, 
      x          TYPE x LENGTH 3   VALUE `ABCDEF`, 
      xstring    TYPE xstring      VALUE `456789AB`, 
      d          TYPE d            VALUE `20020204`, 
      t          TYPE t            VALUE `201501`, 
      utclong    TYPE utclong      VALUE `2002-02-04T20:15:01,1234567`. 
 
    "Transformation to JSON 
    out->begin_section( 'asJSON'  ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    DATA stab TYPE abap_trans_srcbind_tab. 
    stab = VALUE #( 
      ( name = 'I'          value = REF #( i ) ) 
      ( name = 'INT8'       value = REF #( int8 ) ) 
      ( name = 'P'          value = REF #( p ) ) 
      ( name = 'DECFLOAT16' value = REF #( decfloat16 ) ) 
      ( name = 'DECFLOAT34' value = REF #( decfloat34 ) ) 
      ( name = 'F'          value = REF #( f ) ) 
      ( name = 'C'          value = REF #( c ) ) 
      ( name = 'STRING'     value = REF #( string ) ) 
      ( name = 'N'          value = REF #( n ) ) 
      ( name = 'X'          value = REF #( x ) ) 
      ( name = 'XSTRING'    value = REF #( xstring ) ) 
      ( name = 'D'          value = REF #( d ) ) 
      ( name = 'T'          value = REF #( t ) ) 
      ( name = 'UTCLONG'    value = REF #( utclong ) ) ) . 
    CALL TRANSFORMATION id SOURCE (stab) 
                           RESULT  XML writer. 
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
    CALL TRANSFORMATION id SOURCE (stab) 
                           RESULT  XML xml. 
    out->write_xml( xml ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, for which a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) is specified as the XML target, is called to create the [asJSON](../../abap-glossary/abenasjson_glosry.md) representation of all elementary ABAP types.

For comparison, the [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation of the JSON data and the [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the ABAP data is also shown.

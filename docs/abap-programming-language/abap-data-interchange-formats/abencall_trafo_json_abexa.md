---
title: "JSON Transformations"
source_file: abencall_trafo_json_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > CALL TRANSFORMATION > CALL TRANSFORMATION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON Transformations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the possible JSON sources and targets of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

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
CLASS cl_demo_call_trafo_json DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS sxml_writer_for_json. 
    METHODS transformation_id_result 
      RETURNING VALUE(json) TYPE string. 
    METHODS transformation_id_source 
      IMPORTING json TYPE string. 
    METHODS st_result 
      RETURNING VALUE(json_x) TYPE xstring. 
    METHODS st_source 
      IMPORTING json_st TYPE xstring. 
    METHODS xslt_result 
      RETURNING VALUE(json) TYPE string. 
    METHODS xslt_source 
      IMPORTING json TYPE string. 
    DATA int TYPE i. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_call_trafo_json IMPLEMENTATION. 
  METHOD main. 
    sxml_writer_for_json( ). 
    DATA(json) = transformation_id_result( ). 
    transformation_id_source( json ). 
    DATA(json_st) = st_result( ). 
    st_source( json_st ). 
    DATA(json_xslt) = xslt_result( ). 
    xslt_source( json_xslt ). 
  ENDMETHOD. 
  METHOD st_result. 
    CALL TRANSFORMATION demo_st_json_trafo 
      SOURCE var = 0 
      RESULT JSON json_x. 
    DATA(json) = cl_abap_conv_codepage=>create_in( codepage = `utf-8` 
                   )->convert( json_x ). 
 
    out->begin_section( `Simple Transformation Result` 
       )->end_section( ). 
    out->write( json ). 
  ENDMETHOD. 
  METHOD sxml_writer_for_json. 
    FINAL(sxml_writer) = cl_sxml_string_writer=>create( 
                           type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id 
      SOURCE var = 0 
      RESULT XML sxml_writer. 
    DATA(json) = cl_abap_conv_codepage=>create_in( codepage = `utf-8` 
                   )->convert( sxml_writer->get_output( ) ). 
 
    out->begin_section( `sXML Writer for JSON` 
      )->end_section( ). 
    out->write( json ). 
  ENDMETHOD. 
  METHOD transformation_id_result. 
    CALL TRANSFORMATION id 
      SOURCE var = 0 
      RESULT JSON json. 
 
    out->begin_section( `Transformation ID Result` 
      )->end_section( ). 
    out->write( json ). 
  ENDMETHOD. 
  METHOD transformation_id_source. 
    CALL TRANSFORMATION id 
      SOURCE JSON json 
      RESULT var = int. 
 
    out->begin_section( `Transformation ID Source` 
      )->end_section( ). 
    out->write( int ). 
  ENDMETHOD. 
  METHOD st_source. 
    CALL TRANSFORMATION demo_st_json_trafo 
      SOURCE JSON json_st 
      RESULT var = int. 
 
    out->begin_section( `Simple Transformation Source` 
      )->end_section( ). 
    out->write( int ). 
  ENDMETHOD. 
  METHOD xslt_result. 
    CALL TRANSFORMATION demo_xslt_json_trafo 
      SOURCE var = 0 
      RESULT JSON json. 
 
    out->begin_section( `XSL Transformation Result` 
      )->end_section( ). 
    out->write( json ). 
  ENDMETHOD. 
  METHOD xslt_source. 
    CALL TRANSFORMATION demo_xslt_json_trafo 
      SOURCE JSON json 
      RESULT var = int. 
 
    out->begin_section( `XSL Transformation Source` 
      )->end_section( ). 
    out->write( int ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

First, JSON is returned as result using the [sXML](abenabap_sxml_lib.md) writer. Using the sXML writer, the result is first returned as XML and must be converted to JSON. Using JSON directly as source and result in the statement `CALL TRANSFORMATION` makes this step redundant.

The following examples show the use of `JSON` for the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md), [Simple Transformations](abenabap_st.md), and [XSL Transformations](abenabap_xslt.md).

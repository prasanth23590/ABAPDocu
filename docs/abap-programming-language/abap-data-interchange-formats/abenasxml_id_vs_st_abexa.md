---
title: "asXML - Transformation ID vs. Simple Transformation"
source_file: abenasxml_id_vs_st_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Transformation ID vs. Simple Transformation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the differences between the transformation `ID` and a Simple Transformation.

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
CLASS cl_demo_asxml_id_vs_st DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_id_vs_st IMPLEMENTATION. 
  METHOD main. 
    DATA: str TYPE string, 
          xml TYPE string, 
          len TYPE i. 
 
    out->begin_section( 'XSLT ID' ). 
    str = `     `. 
    len = strlen( str ). 
    out->write_text( |String length before: { len }| ). 
    CALL TRANSFORMATION id SOURCE node = str 
                           RESULT XML xml. 
    out->write_xml( xml ). 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT node = str. 
    len = strlen( str ). 
    out->write_text( |String length after: { len }| ). 
 
    out->next_section( 'ST tt:copy' ). 
    str = `     `. 
    len = strlen( str ). 
    out->write_text( |String length before: { len }| ). 
    CALL TRANSFORMATION demo_asxml_copy SOURCE root = str 
                                        RESULT XML xml. 
    out->write_xml( xml ). 
    CALL TRANSFORMATION demo_asxml_copy SOURCE XML xml 
                                        RESULT root = str. 
    len = strlen( str ). 
    out->write_text( |String length after: { len }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A text string with five blanks is serialized and deserialized in a [Simple Transformation](abenabap_st.md) `DEMO_ASXML_COPY` using the predefined [identity transformation `ID`](abenabap_xslt_id.md) and the statement [`tt:copy`](abenst_tt_copy.md). The transformation `ID` contains the statement `<xsl:strip-space elements="*"/>`, which means that the blanks are ignored in deserializations and the text string then has the length 0. After deserializations with the Simple Transformation, the blanks exist in the text string.

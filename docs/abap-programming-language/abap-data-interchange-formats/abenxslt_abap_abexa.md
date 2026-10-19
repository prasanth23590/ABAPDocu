---
title: "XSL Transformations Using ABAP Method Calls"
source_file: abenxslt_abap_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL Transformations Using ABAP Method Calls

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how ABAP methods can be called from within a transformation.

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
CLASS cl_demo_xslt_abap DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS save 
      IMPORTING element TYPE csequence 
                line    TYPE numeric. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xslt_abap IMPLEMENTATION. 
  METHOD main. 
    DATA xml_result TYPE string. 
 
    FINAL(xml_source) = `<root>` && 
                        `<text/>` && 
                        `</root>`. 
 
    CALL TRANSFORMATION demo_xslt_abap 
      PARAMETERS object = me 
      SOURCE XML xml_source 
      RESULT XML xml_result. 
 
  ENDMETHOD. 
  METHOD save. 
    out->write( |This is element { element } in line { line }.| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, the string defined in `xml_source` is transformed. The XSL transformation `DEMO_XSLT_ABAP` has the following form:

``` abap
<xsl:transform 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:sap="http://www.sap.com/sapxsl" version="1.0"> 
 
  <xsl:output indent="yes" method="xml" omit-xml-declaration="yes"/> 
 
  <xsl:strip-space elements="*"/> 
 
  <xsl:param name="OBJECT"/> 
 
  <xsl:template match="*"> 
    <sap:call-external method="save" name="OBJECT"> 
      <sap:callvalue param="ELEMENT" select="name()"/> 
      <sap:callvalue param="LINE" select="sap:line()"/> 
    </sap:call-external> 
    <xsl:apply-templates select="*"/> 
  </xsl:template> 
 
</xsl:transform>
```

Using the [`sap:call-external` instruction](abenabap_xslt_abap_calls.md), the ABAP method `save` is called and the values of `ELEMENT` and `LINE` are passed to the `save` method.

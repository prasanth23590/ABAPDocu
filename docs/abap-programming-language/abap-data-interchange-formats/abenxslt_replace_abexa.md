---
title: "XSL Transformations Using Replace"
source_file: abenxslt_replace_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL Transformations Using Replace

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the usage of the function `replace()` in an XSL transformation.

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
CLASS cl_demo_xslt_replace DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xslt_replace IMPLEMENTATION. 
  METHOD main. 
    DATA xml_result TYPE string. 
 
    FINAL(xml_source) = `<root>` && 
      `<html>` && 
      `<p>` && 
      `1 \n` && 
      `2.` && 
      `</p>` && 
      `</html>` && 
      `</root>`. 
 
    CALL TRANSFORMATION demo_xslt_replace 
      SOURCE XML xml_source 
      RESULT XML xml_result. 
 
    out->write_json( xml_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, the string defined in `xml_source` is transformed. The XSL transformation `DEMO_XSLT_REPLACE` has the following form:

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl"> 
 
<xsl:output method="xml" omit-xml-declaration="yes" indent="yes"/> 
 
<xsl:template match="node()|@*"> 
  <xsl:copy> 
    <xsl:apply-templates select="node()|@*"/> 
  </xsl:copy> 
</xsl:template> 
 
<xsl:template match="root"> 
  <xsl:apply-templates/> 
</xsl:template> 
 
<xsl:template match="html"> 
  <object> 
    <array name="HTML"> 
      <object> 
        <xsl:for-each select="child::node()"> 
          <str name="{name()}"><xsl:value-of select="."/></str> 
        </xsl:for-each> 
      </object> 
    </array> 
  </object> 
</xsl:template> 
 
<xsl:template match="text()[contains(., '\')]"> 
  <xsl:value-of select="replace(., '\\', '\\\\')"/> 
</xsl:template> 
 
</xsl:transform>
```

Using the function `replace()`, the backslash character is replaced by two backslash characters. The XML is transformed to [JSON XML](abenabap_json_xml.md) and the final output is in JSON format.

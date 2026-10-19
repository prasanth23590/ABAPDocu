---
title: "XSL Transformations Using Tokenize"
source_file: abenxslt_tokenize_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL Transformations Using Tokenize

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the usage of the function `tokenize()` in an XSL transformation.

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
CLASS cl_demo_xslt_tokenize DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xslt_tokenize IMPLEMENTATION. 
  METHOD main. 
    DATA xml_result TYPE string. 
 
    FINAL(xml_source) = `<root>` && 
      `<pets>` && 
      `<dog name="Rupert the Dog" color="grey"/>` && 
      `<dog name="Ralph" color="brown"/>` && 
      `<cat name="Marvin the Cat" color="white"/>` && 
      `<cat name="Garfield the Cat" color="orange"/>` && 
      `<cat name="Fluffy" color="black"/>` && 
      `</pets>` && 
      `</root>`. 
 
    CALL TRANSFORMATION demo_xslt_tokenize 
      SOURCE XML xml_source 
      RESULT XML xml_result. 
 
    out->write( xml_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, the string defined in `xml_source` is transformed. The XSL transformation `DEMO_XSLT_TOKENIZE` has the following form:

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl"> 
 
<xsl:output method="html" omit-xml-declaration="yes" indent="yes"/> 
 
<xsl:template match="/"> 
  <xsl:apply-templates select="root/pets/cat"/> 
  <xsl:apply-templates select="root/pets/dog"/> 
</xsl:template> 
 
<xsl:template match="dog"> 
  <dog nickname="{sap:tokenize(@name, '\s+')[1]}" position="{position()}"> 
    <xsl:for-each select="sap:tokenize(@name)"> 
      <token><xsl:copy/></token> 
    </xsl:for-each> 
  </dog> 
</xsl:template> 
 
<xsl:template match="cat"> 
  <cat name="{@name}" position="{position()}"> 
    <xsl:for-each select="sap:tokenize(@name)"> 
      <token><xsl:copy/></token> 
    </xsl:for-each> 
  </cat> 
</xsl:template> 
 
</xsl:transform>
```

Using the function `tokenize()`, the string of each `name` attribute of a `cat` element is split into its tokens. As no pattern is specified, a whitespace is implicitly assumed as the separator.

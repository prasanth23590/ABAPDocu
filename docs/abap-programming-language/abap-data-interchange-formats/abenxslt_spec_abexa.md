---
title: "XSL Transformations"
source_file: abenxslt_spec_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL Transformations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a simple XML to HTML transformation. The output contains a paragraph.

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
CLASS cl_demo_xslt_hello_world DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xslt_hello_world IMPLEMENTATION. 
  METHOD main. 
    DATA xml_result TYPE string. 
 
    FINAL(xml_source) = `<root>` && 
                        `<text>Hello World!</text>` && 
                        `</root>`. 
 
    CALL TRANSFORMATION demo_xslt_hello_world 
      SOURCE XML xml_source 
      RESULT XML xml_result. 
 
    out->write( xml_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, the string defined in `xml_source` is transformed. The XSL transformation `DEMO_XSLT_HELLO_WORLD` has the following form:

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl"> 
 
<xsl:output method="html" omit-xml-declaration="yes" indent="yes"/> 
 
<xsl:strip-space elements="*"/> 
 
<xsl:template match="/"> 
    <html> 
        <head> 
            <style> 
                <xsl:call-template name="style"/> 
            </style> 
        </head> 
        <body> 
            <xsl:apply-templates select="root"/> 
        </body> 
    </html> 
</xsl:template> 
 
<xsl:template match="root"> 
    <p><xsl:value-of select="/."/></p> 
</xsl:template> 
 
<xsl:template name="style"> 
    body { 
      font-family: Arial; 
    } 
</xsl:template> 
 
</xsl:transform>
```

Apart from the HTML construct, a template defining CSS is called.

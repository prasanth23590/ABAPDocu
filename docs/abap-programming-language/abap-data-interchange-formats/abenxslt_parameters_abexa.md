---
title: "XSL Transformations Using Parameters"
source_file: abenxslt_parameters_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL Transformations Using Parameters

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the usage of parameters in an XSL transformation.

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
CLASS cl_demo_xslt_parameters DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xslt_parameters IMPLEMENTATION. 
  METHOD main. 
    DATA xml_result TYPE string. 
    DATA(doc_time) = cl_demo_date_time=>get_system_time( ). 
    DATA time LIKE doc_time. 
 
    FINAL(xml_source) = `<root>` && 
                        `<greeting></greeting>` && 
                        `<text>XML!</text>` && 
                        `</root>`. 
 
    CALL TRANSFORMATION demo_xslt_parameters 
      PARAMETERS time = doc_time 
      SOURCE XML xml_source 
      RESULT XML xml_result. 
 
    out->write( xml_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the ABAP class, the string defined in `xml_source` is transformed. Using the addition [`PARAMETERS`](abapcall_transformation.md), the data object `doc_time` is bound to the parameter `time`. The XSL transformation `DEMO_XSLT_PARAMETERS` has the following form:

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl"> 
 
<xsl:output method="xml" omit-xml-declaration="yes" indent="yes"/> 
 
<xsl:strip-space elements="*"/> 
 
<xsl:param name="TIME" sap:type="number"/> 
 
<xsl:template match="/"> 
    <xsl:apply-templates select="root"/> 
</xsl:template> 
 
<xsl:template match="root"> 
    <xsl:if test="$TIME &lt; 43200"> 
        <xsl:value-of select="string('Good morning')"/> 
    </xsl:if> 
    <xsl:if test="$TIME &gt; 43200"> 
        <xsl:value-of select="string('Good afternoon')"/> 
    </xsl:if> 
    <xsl:value-of select="concat(', ', ./text)"/> 
</xsl:template> 
 
</xsl:transform>
```

The parameter `time` must be specified as a top-level element in the XSLT program in uppercase letters. To compare the system time with another time, the type must be specified.

---
title: "Transformation of XML Element Names"
source_file: abencall_trafo_upper_lower_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > CALL TRANSFORMATION > CALL TRANSFORMATION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Transformation of XML Element Names

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the transformation of letters in XML element names.

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
CLASS cl_demo_trafo_upper_lower DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_trafo_upper_lower IMPLEMENTATION. 
  METHOD main. 
    DATA: BEGIN OF simple_struc, 
            int_col1 TYPE i VALUE 111, 
            int_col2 TYPE i VALUE 222, 
          END OF simple_struc. 
 
    out->begin_section( `Serialization` ). 
 
    CALL TRANSFORMATION id 
                        SOURCE simple_struc = simple_struc 
                        RESULT XML FINAL(asxml). 
    out->begin_section( `ID` 
      )->write_xml( asxml ). 
 
    CALL TRANSFORMATION demo_id_upper_lower 
                        PARAMETERS mode = 'LO' 
                        SOURCE simple_struc = simple_struc 
                        RESULT XML FINAL(xml_lower). 
    out->next_section( `DEMO_ID_UPPER_LOWER` 
      )->write_xml( xml_lower ). 
 
    CALL TRANSFORMATION demo_id_from_to_mixed 
                        PARAMETERS mode = 'TO' 
                        SOURCE simple_struc = simple_struc 
                        RESULT XML FINAL(xml_camel). 
    out->next_section( `DEMO_ID_FROM_TO_MIXED` 
      )->write_xml( xml_camel ). 
 
 
    out->end_section( 
      )->next_section( `Deserialization` ). 
 
    CLEAR simple_struc. 
    CALL TRANSFORMATION id 
                        SOURCE XML xml_lower 
                        RESULT simple_struc = simple_struc. 
    out->begin_section( `ID for XML_LOWER` 
      )->write( simple_struc ). 
 
    CLEAR simple_struc. 
    CALL TRANSFORMATION id 
                        SOURCE XML xml_camel 
                        RESULT simple_struc = simple_struc. 
    out->next_section( `ID for XML_CAMEL` 
      )->write( simple_struc ). 
 
    CLEAR simple_struc. 
    CALL TRANSFORMATION demo_id_upper_lower 
                        SOURCE XML xml_lower 
                        RESULT simple_struc = simple_struc. 
    out->next_section( `DEMO_ID_UPPER_LOWER for XML_LOWER` 
      )->write( simple_struc ). 
 
    CLEAR simple_struc. 
    CALL TRANSFORMATION demo_id_from_to_mixed 
                        SOURCE XML xml_camel 
                        RESULT simple_struc = simple_struc. 
    out->next_section( `DEMO_ID_FROM_TO_MIXED for XML_CAMEL` 
      )->write( simple_struc ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In deserializations of XML data to ABAP data, the XML elements to be deserialized must generally be written in uppercase letters to be identified. This example shows ways of transforming elements written in other ways using user-defined XSL transformations.

- A structure, `simple_struc`, is serialized using different XSL transformations.

  - The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` creates [asXML](../../abap-glossary/abenasxml_glosry.md) with XML element names in uppercase letters.

  - The user-defined XSL transformation `DEMO_ID_UPPER_LOWER` transforms the XML element names created by the serialization to lowercase letters, if the correct parameter passing is used.

  - The user-defined XSL transformation `DEMO_ID_FROM_TO_MIXED` transforms the XML element names created by the serialization to Mixed Case Style (also known as Camel Case Style), if the appropriate parameter passing is used. To do this, an ABAP method is called from the transformation and this method itself calls the built-in function [`to_mixed`](../abap-processing-internal-data/abencase_functions.md).

- Deserializations of the transformed asXML data with the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` do not find the structure or the components.

- Deserializations of the transformed asXML data with the user-defined XSL transformations, on the other hand, are successful.

  - `DEMO_ID_UPPER_LOWER` also transforms lowercase letters to uppercase letters.

  - `DEMO_ID_FROM_TO_MIXED` also calls a method for [`to_mixed`](../abap-processing-internal-data/abencase_functions.md). This simple example transformation is not, however, symmetrical in all cases.

Instead of transformations, parsers and renderers can be used, as demonstrated in the executable example for [JSON](abenabap_json_names_to_upper_abexa.md). The serial processing used here can be useful when dealing with large volumes of data.

The transformations used are as follows:

**`DEMO_ID_UPPER_LOWER`**

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl" 
  xmlns:asx="http://www.sap.com/abapxml"> 
 
  <xsl:variable name="smallcase" select="'abcdefghijklmnopqrstuvwxyz'"/> 
  <xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'"/> 
 
<xsl:param name="MODE" select="'UP'"/> 
 
<xsl:template match="*"> 
  <xsl:element name="{sap:if($MODE='LO', 
         translate(name(),$uppercase, $smallcase ), 
         translate(name(),$smallcase, $uppercase ))}"> 
    <xsl:copy-of select="@*"/> 
    <xsl:apply-templates select="node()"/> 
  </xsl:element> 
</xsl:template> 
 
<xsl:template match="asx:*"> 
  <xsl:copy> 
    <xsl:copy-of select="@*"/> 
    <xsl:apply-templates select="node()"/> 
  </xsl:copy> 
</xsl:template> 
 
<xsl:template match="text() | processing-instruction() | comment()"> 
  <xsl:copy/> 
</xsl:template> 
 
</xsl:transform>
```

**`DEMO_ID_FROM_TO_MIXED`**

``` abap
<xsl:transform version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
  xmlns:sap="http://www.sap.com/sapxsl" 
  xmlns:asx="http://www.sap.com/abapxml" 
  xmlns:f="FCT" exclude-result-prefixes="f"> 
 
<sap:external-function name="f:toCC" kind="class" 
 class="CL_DEMO_XSLT_FROM_TO_MIXED" method="TO_CAMEL_CASE"> 
  <sap:argument param="IN"  type="string"/> 
  <sap:result   param="OUT" type="string"/> 
</sap:external-function> 
 
<sap:external-function name="f:fromCC" kind="class" 
 class="CL_DEMO_XSLT_FROM_TO_MIXED" method="FROM_CAMEL_CASE"> 
  <sap:argument param="IN"  type="string"/> 
  <sap:result   param="OUT" type="string"/> 
</sap:external-function> 
 
<xsl:param name="MODE" select="'FROM'"/> 
 
 
<xsl:template match="*"> 
  <xsl:element name="{sap:if($MODE='TO', 
                      f:toCC(name()), 
                      f:fromCC(name()))}"> 
    <xsl:copy-of select="@*"/> 
    <xsl:apply-templates select="node()"/> 
  </xsl:element> 
</xsl:template> 
 
<xsl:template match="asx:*"> 
  <xsl:copy> 
    <xsl:copy-of select="@*"/> 
    <xsl:apply-templates select="node()"/> 
  </xsl:copy> 
</xsl:template> 
 
<xsl:template match="text() | processing-instruction() | comment()"> 
  <xsl:copy/> 
</xsl:template> 
 
</xsl:transform>
```

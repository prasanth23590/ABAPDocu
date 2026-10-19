---
title: "Transformation of XML Syntax Characters"
source_file: abencall_trafo_escaping_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > CALL TRANSFORMATION > CALL TRANSFORMATION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Transformation of XML Syntax Characters

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the serialization of characters from the XML syntax using various transformations.

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
CLASS cl_demo_transformation_escpng DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_transformation_escpng IMPLEMENTATION. 
  METHOD main. 
    DATA xml TYPE string. 
 
    FINAL(text) = `<>&"`. 
 
    out->begin_section( `Text` 
      )->write( text 
 
      )->next_section( `XSLT` 
 
      )->begin_section( `<xsl:output method="text" />` ). 
    CALL TRANSFORMATION demo_escaping_text SOURCE text = text 
                                           RESULT XML xml. 
    out->write( xml 
 
      )->next_section( `<xsl:output method="xml" />` ). 
    CALL TRANSFORMATION demo_escaping_xml SOURCE text = text 
                                          RESULT XML xml. 
    out->write( xml 
 
      )->next_section( `<xsl:output method="html" />` ). 
    CALL TRANSFORMATION demo_escaping_html SOURCE text = text 
                                           RESULT XML xml. 
    out->write( xml 
 
      )->next_section( `<xsl:output method="html" />` ). 
    CALL TRANSFORMATION demo_escaping_js SOURCE text = text 
                                         RESULT XML xml. 
    out->write( xml 
      )->end_section( 
 
      )->next_section( `ST` ). 
    CALL TRANSFORMATION demo_escaping_st SOURCE text = text 
                                         RESULT XML xml. 
    out->write( xml ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Four XSLT programs with different output methods are called and an ST program for serializing a text string containing the syntax characters *\<\>&"*. The results are as follows:

- No replacements are made in the results of the XSL transformation `DEMO_ESCAPING_TEXT` with the output method *text*.

- In the results of the XSL transformation `DEMO_ESCAPING_XML` with the output method *xml*, the syntax characters *\<*, *\>*, and *&* are replaced by *&lt;*, *\>*, and *&*.

- In the results of the XSL transformation `DEMO_ESCAPING_HTML` with the output method *html*, the syntax characters *\<*, *\>*, and *&* are replaced by *&lt;*, *\>*, and *&*.

- In the results of the XSL transformation `DEMO_ESCAPING_JS` with the output method *html*, the syntax characters are not replaced because they are part of JavaScript.

The result of the Simple Transformation `DEMO_ESCAPING_ST` matches the XSL transformation with the output method *xml*. Also, the text string is output here as an attribute in which the syntax character *"* is replaced by *"*.

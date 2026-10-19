---
title: "sXML - Deserialization with XML Reader"
source_file: abensxml_trafo_from_reader_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Deserialization with XML Reader

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deserializes ABAP data from an XML reader.

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
CLASS cl_demo_sxml_trafo_from_reader DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_trafo_from_reader IMPLEMENTATION. 
  METHOD main. 
 
    FINAL(xml) = cl_abap_conv_codepage=>create_out( )->convert( 
      `<document>` && 
      `  <head>` && 
      `    <author>KELLERH</author>` && 
      `    <date>20120824</date>` && 
      `  </head>` && 
      `  <body>` && 
      `    <asx:abap` && 
      `      xmlns:asx="http://www.sap.com/abapxml" version="1.0">` && 
      `      <asx:values>` && 
      `        <TABLE>` && 
      `          <item>1</item>` && 
      `          <item>2</item>` && 
      `          <item>3</item>` && 
      `        </TABLE>` && 
      `      </asx:values>` && 
      `    </asx:abap>` && 
      `  </body>` && 
      `</document>` ). 
 
    FINAL(reader) = 
      CAST if_sxml_reader( cl_sxml_string_reader=>create( xml ) ). 
 
    WHILE reader->name <> 'body'. 
      reader->next_node( ). 
    ENDWHILE. 
 
    DATA itab TYPE TABLE OF i. 
    CALL TRANSFORMATION id SOURCE XML reader 
                           RESULT table = itab. 
    out->write( itab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An XML string reader parses the XML data of a byte string until it reaches the element `<body>`. The element `<header>` is not analyzed further. The reader located at the element opening of `<body>` is used as an XML source for the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`. The content of `<body>` is in asXML format for an internal table, which means it can be deserialized to such a table.

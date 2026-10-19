---
title: "asXML - Mapping of Qualified Names"
source_file: abenasxml_qnames_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Qualified Names

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the mapping of XML schema data types for qualified names.

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
CLASS cl_demo_asxml_qname DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_qname IMPLEMENTATION. 
  METHOD main. 
    DATA: name1  TYPE string, 
          name2  TYPE string, 
          qname1 TYPE xsdqname, 
          qname2 TYPE xsdqname. 
 
    DATA xmlstring TYPE string. 
 
    name1 = qname1 = '{test_uri}Value1'. 
    name2 = qname2 = '{test_uri}Value2'. 
 
    out->begin_section( 'Serialization of Strings' ). 
    CALL TRANSFORMATION id SOURCE test1 = name1 
                                  test2 = name2 
                           RESULT XML xmlstring. 
    out->write_xml( xmlstring ). 
 
    out->next_section( 'Serialization of XSDQNAME' ). 
    CALL TRANSFORMATION id SOURCE test1 = qname1 
                                  test2 = qname2 
                           RESULT XML xmlstring. 
    out->write_xml( xmlstring ). 
 
    out->next_section( 'Source for Deserialization' ). 
    xmlstring = 
    `<?xml version="1.0" encoding="utf-8" ?>`   && 
    `<asx:abap `                                && 
      `xmlns:asx="http://www.sap.com/abapxml" ` && 
      `xmlns:demox="my_uri"  version="1.0">`    && 
    `<asx:values >`                             && 
    `<TEST1>demox:Value1</TEST1>`               && 
    `<TEST2>Value2</TEST2>`                     && 
    `</asx:values>`                             && 
    `</asx:abap>`. 
    out->write_xml( xmlstring ). 
 
    out->next_section( 'Deserialization' ). 
    CALL TRANSFORMATION id SOURCE XML xmlstring 
                           RESULT test1 = name1 
                                  test2 = name2. 
    CALL TRANSFORMATION id SOURCE XML xmlstring 
                           RESULT test1 = qname1 
                                  test2 = qname2. 
    out->write( 
      |{ name1  WIDTH = 20 }{ name2  WIDTH = 20 }| & |\n| & 
      |{ qname1 WIDTH = 20 }{ qname2 WIDTH = 20 }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, only two serializations of ABAP data objects are performed to asXML format whose content corresponds to the *{URI}name* format. In the first serialization, the data objects have the type `string`. In the second they have the type `XSDQNAME`. In the first case, the content is passed unchanged, but in the second case it is interpreted as a qualified name and the associated namespace declarations are created.

Next, XML data is created, which contains one element with a namespace prefix and one without a namespace prefix. This data is deserialized to ABAP data objects with the type `string` and the type `XSDQNAME`. The element with a namespace prefix is deserialized to the data object with the type `string` unchanged. However, when deserializing to the data object of the type `XSDQNAME`, a conversion to the format *{URI}name* takes place. The element with no namespace prefix is deserialized unchanged in both cases, since only the empty standard namespace exists.

---
title: "asXML - Mapping of Anonymous Data Objects"
source_file: abenasxml_data_object_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Anonymous Data Objects

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the mapping of anonymous data objects.

## Source Code

``` abap
* CCDEF 
CLASS serializable DEFINITION. 
  PUBLIC SECTION. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_asxml_data_object DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_data_object IMPLEMENTATION. 
  METHOD main. 
    DATA dref   TYPE REF TO decfloat34. 
    DATA xmlstr TYPE xstring. 
 
    CREATE DATA dref. 
    dref->* = '1.23456'. 
    CALL TRANSFORMATION id SOURCE dref = dref 
                           RESULT XML xmlstr. 
 
    out->write_xml( xmlstr ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The anonymous data object referenced by `dref` is mapped to a subelement of the element `heap`. An XML reference mechanism is used to associate this subelement with the reference variables in the element `values`. The element name is the XML schema type name `precisionDecimal` of the built-in ABAP type `decfloat34` from the namespace `abap="http://www.sap.com/abapxml/types/built-in"`.

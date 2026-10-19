---
title: "enum, Deserialization"
source_file: abenenum_deserialization_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Enumerated Objects (enum)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# enum, Deserialization

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a dynamically created XML file is deserialized to an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md).

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
CLASS cl_demo_deserialize_enums_v5 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_deserialize_enums_v5 IMPLEMENTATION. 
  METHOD main. 
    DATA input TYPE c LENGTH 3 VALUE 'XL'. 
    cl_demo_input=>new( )->request( CHANGING field = input ). 
    input = to_upper( input ). 
 
    TYPES: 
      BEGIN OF ENUM size, 
        s, m, l, xl, xxl, 
      END OF ENUM size. 
 
    FINAL(xml) = 
      cl_abap_conv_codepage=>create_out( )->convert( 
        `<asx:abap version="1.0"` && 
        ` xmlns:asx="http://www.sap.com/abapxml">` && 
        `  <asx:values>` && 
        `  <ENUM>` && input && `</ENUM>` && 
        `  </asx:values>` && 
        `</asx:abap>` ) ##no_text. 
 
    DATA size TYPE size. 
    TRY. 
        CALL TRANSFORMATION id 
                            SOURCE XML xml 
                            RESULT enum = size. 
      CATCH cx_transformation_error INTO FINAL(exc). 
        out->write( exc->previous->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    out->write( |Name:  { size 
                           }\nValue: { CONV i( size ) }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A byte string is composed in such a way that it represents an XML file in asXML format for an enumerated object of the enumerated type `size` and is deserialized as such. Any invalid entries raise an exception.

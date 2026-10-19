---
title: "XSL - Identity Transformation to asXML Format"
source_file: abenxslt_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Serialization from and Deserialization to ABAP > XSL - Identity Transformation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - Identity Transformation to asXML Format

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the serialization of ABAP data to the [asXML format](abenabap_xslt_asxml.md).

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
CLASS cl_demo_xsl_transformation DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_serializable_object. 
  PROTECTED SECTION. 
    DATA carriers TYPE TABLE OF scarr. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    METHODS constructor. 
  PRIVATE SECTION. 
    DATA lines TYPE i. 
    METHODS: 
    serialize_helper 
    EXPORTING count TYPE i, 
    deserialize_helper 
    IMPORTING count TYPE i. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    SELECT * 
    FROM scarr 
    INTO TABLE @carriers 
    UP TO 2 ROWS. 
  ENDMETHOD. 
  METHOD serialize_helper. 
    count = lines( carriers ). 
  ENDMETHOD. 
  METHOD deserialize_helper. 
    lines = count. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xsl_transformation IMPLEMENTATION. 
  METHOD main. 
    DATA buffer TYPE xstring. 
 
    TYPES oref  TYPE REF TO object. 
    DATA: dref1 TYPE REF TO oref, 
          date  TYPE d, 
          time  TYPE t, 
          dref2 LIKE dref1. 
 
    dref1    = NEW #( ). 
    dref1->* = NEW c2( ). 
 
    FINAL(user_date) = cl_demo_date_time=>get_system_date( ). 
    FINAL(user_time) = cl_demo_date_time=>get_system_time( ). 
    CALL TRANSFORMATION id 
                        SOURCE xmldat = user_date 
                               xmltim = user_time 
                               ref  = dref1 
                        RESULT XML DATA(xmlstr). 
    EXPORT obj = xmlstr TO DATA BUFFER buffer. 
 
    out->write_xml( xmlstr ). 
 
    IMPORT obj = xmlstr FROM DATA BUFFER buffer. 
    CALL TRANSFORMATION id 
                        SOURCE XML xmlstr 
                        RESULT xmldat = date 
                               xmltim = time 
                               ref = dref2. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Serialization of data objects to a string `xmlstr` using the [identity transformation](abenabap_xslt_id.md) `ID`. A date field `date`, a time field `time`, and a data reference variable `dref1` are serialized. The data reference variable points to an anonymous object reference variable, which in turn points to an object of the class `c2`. Objects serialized in this way can be stored persistently, for example in a [data cluster](../../abap-glossary/abendata_cluster_glosry.md). After the objects are imported from where they are stored, they are deserialized to other data objects. Following deserialization, `dref2` points to another anonymous reference variable, such as `dref1`. This [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) and the instance of the class `c2` to which it points are created during deserialization.

The [XML](../../abap-glossary/abenxml_glosry.md) document created during serialization is in [asXML](../../abap-glossary/abenasxml_glosry.md) format. It has approximately the content described below. In this description, line breaks and indents have been added. The element `values` contains the asXML representations of the three passed data objects. In the names `X-MLDAT` and `X-MLTIM`, *xml* is replaced by *X-ML*. The attribute `href` of the element `REF` uses the key *d1* to refer to the representation of the associated [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) in the element `heap`. This uses the key *o3* to refer to the representation of the instance of the class `c2`, which is also in the element `heap`. This representation is divided into the object parts for the classes `c1` and `c2`. The object part for `c1` contains the representation of the double-row structured internal table `carriers`. The object part for `c2` contains the representation for the output parameter `count` of the method `SERIALIZE_HELPER`.

``` abap
<?xml version="1.0" encoding="iso-8859-1" ?> 
<asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0"> 
  <asx:values> 
    <X-MLDAT>2003-04-15</X-MLDAT> 
    <X-MLTIM>14:57:53</X-MLTIM> 
    <REF href="#d1" /> 
  </asx:values> 
  <asx:heap 
       xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
       xmlns:abap="http://www.sap.com/abapxml/types/built-in" 
       xmlns:cls="http://www.sap.com/abapxml/classes/global" 
       xmlns:dic="http://www.sap.com/abapxml/types/dictionary"> 
    <abap:refObject href="#o3" id="d1" /> 
    <prg:C2 
      xmlns:prg="http://www.sap.com/abapxml/classes/program/XMLTST" 
      id="o3"> 
      <local.C1> 
        <CARRIERS> 
          <SCARR> 
            <MANDT>000</MANDT> 
            <CARRID>AA</CARRID> 
            <CARRNAME>American Airlines</CARRNAME> 
            <CURRCODE>USD</CURRCODE> 
            <URL>http://www.aa.com</URL> 
          </SCARR> 
          <SCARR> 
            <MANDT>000</MANDT> 
            <CARRID>AB</CARRID> 
            <CARRNAME>Air Berlin</CARRNAME> 
            <CURRCODE>DEM</CURRCODE> 
            <URL>http://www.airberlin.de</URL> 
          </SCARR> 
        </CARRIERS> 
      </local.C1> 
      <local.C2> 
        <COUNT>2</COUNT> 
      </local.C2> 
    </prg:C2> 
  </asx:heap> 
</asx:abap> 
 
```

For further executable examples, see [asXML, Examples of Mappings](abenasxml_abexas.md)

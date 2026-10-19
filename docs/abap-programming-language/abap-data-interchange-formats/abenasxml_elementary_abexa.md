---
title: "asXML - Mapping of Elementary Data Types"
source_file: abenasxml_elementary_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Elementary Data Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the mapping of elementary data types.

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
CLASS cl_demo_asxml_elementary DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_elementary IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      i          TYPE i            VALUE -123, 
      int8       TYPE int8         VALUE -123, 
      p          TYPE p DECIMALS 2 VALUE `-1.23`, 
      decfloat16 TYPE decfloat16   VALUE `123E+1`, 
      decfloat34 TYPE decfloat34   VALUE `-3.140000E+02`, 
      f          TYPE f            VALUE `-3.140000E+02`, 
      c          TYPE c LENGTH 3   VALUE ` Hi`, 
      string     TYPE string       VALUE ` Hello `, 
      n          TYPE n LENGTH 6   VALUE `001234`, 
      x          TYPE x LENGTH 3   VALUE `ABCDEF`, 
      xstring    TYPE xstring      VALUE `456789AB`, 
      d          TYPE d            VALUE `20020204`, 
      t          TYPE t            VALUE `201501`, 
      utclong    TYPE utclong      VALUE `2002-02-04T20:15:01,1234567`. 
 
    DATA stab TYPE abap_trans_srcbind_tab. 
    stab = VALUE #( 
      ( name = 'I'          value = REF #( i ) ) 
      ( name = 'INT8'       value = REF #( int8 ) ) 
      ( name = 'P'          value = REF #( p ) ) 
      ( name = 'DECFLOAT16' value = REF #( decfloat16 ) ) 
      ( name = 'DECFLOAT34' value = REF #( decfloat34 ) ) 
      ( name = 'F'          value = REF #( f ) ) 
      ( name = 'C'          value = REF #( c ) ) 
      ( name = 'STRING'     value = REF #( string ) ) 
      ( name = 'N'          value = REF #( n ) ) 
      ( name = 'X'          value = REF #( x ) ) 
      ( name = 'XSTRING'    value = REF #( xstring ) ) 
      ( name = 'D'          value = REF #( d ) ) 
      ( name = 'T'          value = REF #( t ) ) 
      ( name = 'UTCLONG'    value = REF #( utclong ) ) ) . 
    CALL TRANSFORMATION id SOURCE (stab) 
                           RESULT XML FINAL(xmlstr). 
 
    out->write_xml( xmlstr ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The statement `CALL TRANSFORMATION` binds the data objects of all elementary ABAP types to elements. The `values` subelement contains these elements. The content of these elements is determined by mapping the bound elementary ABAP data objects.

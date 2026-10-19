---
title: "ST - Mapping of XML Fragments"
source_file: abenst_xsdany_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for XML Fragments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Mapping of XML Fragments

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the mapping of XML fragments using ST.

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
CLASS cl_demo_st_xsdany DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS prepare_fragment 
      RETURNING VALUE(xml) TYPE xsdany. 
    METHODS serialize 
      IMPORTING source        TYPE xsdany 
                trafo         TYPE string 
                text          TYPE string 
      RETURNING VALUE(result) TYPE xstring. 
    METHODS deserialize 
      IMPORTING source TYPE xstring 
                trafo  TYPE string 
                text   TYPE string. 
    METHODS invoke_deserialization 
      IMPORTING source TYPE xstring 
                text   TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_xsdany IMPLEMENTATION. 
  METHOD main. 
 
    FINAL(xsdstr) = prepare_fragment( ). 
 
    FINAL(xmlstr1) = serialize( 
      source = xsdstr 
      trafo  = 'DEMO_ST_XSDANY' 
      text =  'ST-Serialization of XML-Fragment' ). 
    FINAL(xmlstr2) = serialize( 
      source = xsdstr 
      trafo  = 'DEMO_ST_XSDANY_LAX' 
      text =  'Lax ST-Serialization of XML-Fragment' ). 
    FINAL(xmlstr3) = serialize( 
      source = xsdstr 
      trafo  = 'DEMO_ST_XSDANY_NO_ROOT' 
      text =  'noRoot-ST-Serialization of XML-Fragment' ). 
    FINAL(xmlstr4) = serialize( 
      source = xsdstr 
      trafo  = 'DEMO_ST_XSDANY_LAX_NO_ROOT' 
      text =  'Lax noRoot-ST-Serialization of XML-Fragment' ). 
    out->line( ). 
 
    invoke_deserialization( source = xmlstr1 
                            text   = `` ). 
    invoke_deserialization( source = xmlstr2 
                            text   = `lax ` ). 
    invoke_deserialization( source = xmlstr3 
                            text   = `noRoot-` ). 
    invoke_deserialization( source = xmlstr4 
                            text   = `lax noRoot-` ). 
 
  ENDMETHOD. 
  METHOD deserialize. 
    DATA result TYPE xsdany. 
    TRY. 
        out->begin_section( text ). 
        CALL TRANSFORMATION (trafo) 
          SOURCE XML source 
          RESULT root = result 
          OPTIONS clear = 'all'. 
        IF result IS NOT INITIAL. 
          out->write_xml( result ). 
        ELSE. 
          out->write_text( 'Initial' ). 
        ENDIF. 
      CATCH cx_transformation_error. 
        out->write_text( 'Error' ). 
    ENDTRY. 
    out->end_section( ). 
  ENDMETHOD. 
  METHOD invoke_deserialization. 
    deserialize( 
  EXPORTING 
    source = source 
    trafo  = 'DEMO_ST_XSDANY' 
    text   = `ST-Deserialization of ` 
             && text && `ST-result` ). 
    deserialize( 
      EXPORTING 
        source = source 
        trafo  = 'DEMO_ST_XSDANY_LAX' 
        text   = `Lax ST-Deserialization of ` 
                 && text && `ST-result` ). 
    deserialize( 
      EXPORTING 
        source = source 
        trafo  = 'DEMO_ST_XSDANY_NO_ROOT' 
        text   = `noRoot-ST-Deserialization of ` 
                 && text && `ST-result` ). 
    deserialize( 
      EXPORTING 
        source = source 
        trafo  = 'DEMO_ST_XSDANY_LAX_NO_ROOT' 
        text   = `Lax noRoot-ST-Deserialization of ` 
                 && text && `ST-result` ). 
    out->line( ). 
  ENDMETHOD. 
  METHOD prepare_fragment. 
    out->begin_section( 'XML-Fragment' ). 
    xml = cl_abap_conv_codepage=>create_out( )->convert( 
          `<?xml version="1.0" encoding="utf-8" ?>` && 
          `<X>`              && 
            `Text`           && 
            `<X1>Text1</X1>` && 
            `<X2>Text1</X2>` && 
          `</X>` ). 
    out->write_xml( xml )->line( ). 
  ENDMETHOD. 
  METHOD serialize. 
    TRY. 
        out->begin_section( text ). 
        CALL TRANSFORMATION (trafo) 
          SOURCE root = source 
          RESULT XML result. 
        out->write_xml( result ). 
      CATCH cx_transformation_error. 
        out->write_text( 'Error' ). 
    ENDTRY. 
    out->end_section( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The following transformations are called in this example:

- `DEMO_ST_XSDANY`

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <node> 
      <tt:value ref="ROOT"/> 
    </node> 
  </tt:template> 
</tt:transform>
```

- `DEMO_ST_XSDANY_LAX`

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <node tt:lax="on"> 
      <tt:value ref="ROOT"/> 
    </node> 
  </tt:template> 
</tt:transform>
```

- `DEMO_ST_XSDANY_NO_ROOT`

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <node> 
      <tt:value option="noRootAttr" ref="ROOT"/> 
    </node> 
  </tt:template> 
</tt:transform>
```

- `DEMO_ST_XSDANY_LAX_NO_ROOT`

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <node tt:lax="on"> 
      <tt:value option="noRootAttr" ref="ROOT"/> 
    </node> 
  </tt:template> 
</tt:transform>
```

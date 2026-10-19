---
title: "ST - Option for Invalid Values"
source_file: abenst_noerror_option_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for Elementary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Option for Invalid Values

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how ABAP types are mapped using invalid values.

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
CLASS cl_demo_st_noerror_option DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS call_transformation 
      CHANGING writer TYPE REF TO cl_sxml_string_writer. 
    DATA: 
      num      TYPE n LENGTH 8, 
      pack     TYPE p LENGTH 8, 
      boolean  TYPE xsdboolean, 
      date     TYPE xsddate_d, 
      time     TYPE xsdtime_t, 
      langu    TYPE xsdlanguage, 
      currcode TYPE xsdcurrcode, 
      unitcode TYPE xsdunitcode. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_noerror_option IMPLEMENTATION. 
  METHOD main. 
    FIELD-SYMBOLS <hex> TYPE x. 
 
    FINAL(d_placeholder) = `  1234  `. 
    FINAL(date_placeholder) = 'XXXXXXXX'. 
    FINAL(time_placeholder) = 'XXXXXX'. 
    FINAL(unitcode_placeholder) = '&#x00A7;&#x00A7;&#x00A7;&#x00A7;&#x00A7;' ##STRING_OK. 
 
    num = CONV d( d_placeholder ). 
    pack = -1234. 
    ASSIGN pack TO <hex> CASTING. 
    REPLACE SECTION OFFSET 7 LENGTH 1 OF <hex> WITH 
            CONV xstring( '40' ) IN BYTE MODE. 
    boolean = '1'. 
    date = date_placeholder. 
    time = time_placeholder. 
    langu = '&#x00A7;' ##STRING_OK. 
    currcode = '&#x00A7;&#x00A7;&#x00A7;&#x00A7;&#x00A7;' ##STRING_OK. 
    unitcode = unitcode_placeholder. 
 
    TRY. 
        CALL TRANSFORMATION demo_st_noerror_option 
          SOURCE n           = num 
                 p           = pack 
                 boolean     = boolean 
                 xsddate_d   = date 
                 xsdtime_t   = time 
                 xsdlanguage = langu 
                 xsdcurrcode = currcode 
                 xsdunitcode = unitcode 
          RESULT XML FINAL(xml). 
      CATCH cx_transformation_error INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    out->write_xml( xml ). 
  ENDMETHOD. 
  METHOD call_transformation. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example passes various types of ABAP data to the transformation `DEMO_ST_NOERROR_OPTION` and provides the result for XML. The transformation applies the option [`noError`](abenst_option_format.md) to the ABAP data:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="N"/> 
  <tt:root name="P"/> 
  <tt:root name="BOOLEAN"/> 
  <tt:root name="XSDDATE_D"/> 
  <tt:root name="XSDTIME_T"/> 
  <tt:root name="XSDLANGUAGE"/> 
  <tt:root name="XSDCURRCODE"/> 
  <tt:root name="XSDUNITCODE"/> 
  <tt:template> 
    <array> 
      <object> 
        <str name="n"> 
          <tt:value option="noError" ref="N"/> 
        </str> 
        <str name="p"> 
          <tt:value option="noError" ref="P"/> 
        </str> 
        <bool name="boolean"> 
          <tt:value option="noError" ref="BOOLEAN"/> 
        </bool> 
        <str name="xsddate_d"> 
          <tt:value option="noError" ref="XSDDATE_D"/> 
        </str> 
        <str name="xsdtime_t"> 
          <tt:value option="noError" ref="XSDTIME_T"/> 
        </str> 
        <str name="xsdlanguage"> 
          <tt:value option="noError" ref="XSDLANGUAGE"/> 
        </str> 
        <str name="xsdcurrcode"> 
          <tt:value option="noError" ref="XSDCURRCODE"/> 
        </str> 
        <str name="xsdunitcode"> 
          <tt:value option="noError" ref="XSDUNITCODE"/> 
        </str> 
      </object> 
    </array> 
  </tt:template> 
</tt:transform>
```

The transformation creates [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) to represent both XML and JSON. The example passes an invalid value to the transformation for each of the types used. If the option [`noError`](abenst_option_format.md) were not specified, each of the invalid types would raise an exception.

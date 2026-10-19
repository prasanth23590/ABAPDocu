---
title: "asXML - Deserializing Structure Components"
source_file: abenabap_asxml_asjson_empty_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Examples of Mappings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Deserializing Structure Components

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the deserialization of empty and missing structure components.

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
CLASS cl_demo_asxml_asjson_strct_cps DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_asjson_strct_cps IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `ABAP Structure` ). 
    CONSTANTS: 
      BEGIN OF struct, 
        text0   TYPE string VALUE ``, 
        text1   TYPE string VALUE `Text1`, 
        text2   TYPE string VALUE `Text2`, 
        text3   TYPE string VALUE `Text3`, 
        number0 TYPE i VALUE 0, 
        number1 TYPE i VALUE 111, 
        number2 TYPE i VALUE 222, 
        number3 TYPE i VALUE 333, 
      END OF struct. 
    DATA(examples) = struct. 
    out->write_data( examples ). 
 
    out->next_section( `Structure serialized to asXML` ). 
    DATA xml TYPE string. 
 
    CALL TRANSFORMATION id SOURCE examples = examples 
                           RESULT XML xml. 
    out->write_xml( xml ). 
 
    out->next_section( `Structure serialized to asJSON` ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
                      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE examples = examples 
                           RESULT XML writer. 
    DATA(json) = cl_abap_conv_codepage=>create_in( )->convert( 
                   writer->get_output( ) ). 
    out->write_json( json ). 
 
    out->next_section( `Modified asXML` ). 
    REPLACE `<TEXT2>Text2</TEXT2>` IN xml WITH `<TEXT2 />`. 
    REPLACE `<TEXT3>Text3</TEXT3>` IN xml WITH ``. 
    REPLACE `<NUMBER2>222</NUMBER2>` IN xml WITH `<NUMBER2 />`. 
    REPLACE `<NUMBER3>333</NUMBER3>` IN xml WITH ``. 
    out->write_xml( xml ). 
 
    out->next_section( 
      `ABAP Structure after Deserialization of asXML` ). 
    examples = struct. 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT examples = examples. 
    out->write_data( examples ). 
 
    out->next_section( `Modified asJSON` ). 
    REPLACE `"TEXT2":"Text2",` IN json WITH `"TEXT2":""`. 
    REPLACE `"TEXT3":"Text3"` IN json WITH ``. 
    REPLACE `"NUMBER2":222,` IN json WITH `"NUMBER2":0`. 
    REPLACE `"NUMBER3":333` IN json WITH ``. 
    out->write_json( json ). 
 
    out->next_section( 
      `ABAP Structure after Deserialization of asJSON` ). 
    examples = struct. 
    CALL TRANSFORMATION id SOURCE XML json 
                           RESULT examples = examples. 
    out->write_data( examples ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A structure is transformed using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` into its [asXML](../../abap-glossary/abenasxml_glosry.md) and [asJSON](../../abap-glossary/abenasjson_glosry.md) representations. In the asXML representation, the values of two elements and two complete elements are removed. In JSON, values cannot be removed. In the asJSON representation, the values of two object components are initialized and two object components are removed.

After deserialization into the original ABAP structure, the components to which empty XML elements are assigned are initial. Components, for which no XML element or no JSON object component exist retain their previous value.

---
title: "Deserializing Empty Elements"
source_file: abenabap_deserl_empt_elem_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > CALL TRANSFORMATION > CALL TRANSFORMATION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Deserializing Empty Elements

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the deserialization of empty elements.

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
CLASS cl_demo_asxml_asjson_empty_vls DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_asjson_empty_vls IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `asXML` ). 
    DATA elem TYPE i VALUE 111. 
    DATA: BEGIN OF struc, 
            col TYPE i VALUE 111, 
          END OF struc. 
    DATA itab TYPE TABLE OF i. 
    itab = VALUE #( ( 111 ) ). 
    out->begin_section( `ABAP Data Objects` 
      )->write_data( elem 
      )->write_data( struc 
      )->write_data( itab ). 
 
    out->next_section( 
      `ABAP Data Objects serialized to asXML` ). 
    DATA xml TYPE string. 
    CALL TRANSFORMATION id SOURCE elem = elem 
                                  struc = struc 
                                  itab = itab 
                           RESULT XML xml. 
    out->write_xml( xml ). 
 
    out->next_section( `Modified asXML` ). 
    REPLACE `<ELEM>111</ELEM>` IN xml WITH `<ELEM />`. 
    REPLACE `<STRUC><COL>111</COL></STRUC>` IN xml WITH `<STRUC />`. 
    REPLACE `<ITAB><item>111</item></ITAB>` IN xml WITH `<ITAB />`. 
    out->write_xml( xml ). 
 
    out->next_section( 
      `ABAP Data Objects after Deserialization of asXML` ). 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT elem = elem 
                                  struc = struc 
                                  itab = itab. 
    out->write_data( elem 
      )->write_data( struc 
      )->write_data( itab 
      )->end_section( ). 
 
    out->next_section( 
      `ABAP Data Objects after Deserialization with Clearing` ). 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT elem = elem 
                                  struc = struc 
                                  itab = itab 
                          OPTIONS clear = 'all'. 
    out->write_data( elem 
      )->write_data( struc 
      )->write_data( itab 
      )->end_section( ). 
 
    out->next_section( `asJSON` ). 
    elem = 111. 
    struc-col = 111. 
    itab = VALUE #( ( 111 ) ). 
    out->begin_section( `ABAP Data Objects` 
      )->write_data( elem 
      )->write_data( struc 
      )->write_data( itab ). 
 
    out->next_section( 
      `ABAP Data Objects serialized to asJSON` ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
                     type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE elem = elem 
                                  struc = struc 
                                  itab = itab 
                           RESULT XML writer. 
    DATA(json) = cl_abap_conv_codepage=>create_in( )->convert( 
                   writer->get_output( ) ). 
    out->write_json( json ). 
 
    out->next_section( `Modified asJSON` ). 
    REPLACE `"ELEM":111` IN json WITH `"ELEM":0`. 
    REPLACE `"COL":111` IN json WITH ``. 
    REPLACE `111` IN json WITH ``. 
    out->write_json( json ). 
 
    out->next_section( 
      `ABAP Data Objects after Deserialization of asJSON` ). 
    CALL TRANSFORMATION id SOURCE XML json 
                           RESULT elem = elem 
                                  struc = struc 
                                  itab = itab. 
    out->write_data( elem 
      )->write_data( struc 
      )->write_data( itab ). 
 
    out->next_section( 
      `ABAP Data Objects after Deserialization with Clearing` ). 
    CALL TRANSFORMATION id SOURCE XML json 
                           RESULT elem = elem 
                                  struc = struc 
                                  itab = itab 
                          OPTIONS clear = 'all'. 
    out->write_data( elem 
      )->write_data( struc 
      )->write_data( itab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An elementary data object, a structure and an internal table are transformed using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` to their [asXML](../../abap-glossary/abenasxml_glosry.md) and [asJSON](../../abap-glossary/abenasjson_glosry.md) representations. In the asXML representation, the values of all elements are removed. In the asJSON representation, only the components from objects and arrays can be removed.

After deserialization to the original ABAP data objects, the elementary data object and the internal table are initial. However, the empty element in the structure is interpreted as a missing component and the structure component retains its previous value. If the transformation option [`clear`](abapcall_transformation_options.md) is used with the value *all*, all ABAP data objects are initialized.

## Hint

The modification of XML and JSON data using string processing shown here is only for the sake of clarity in the example. In production programs, the APIs of [class libraries for XML](abenabap_xml_libs.md) should be used for this.

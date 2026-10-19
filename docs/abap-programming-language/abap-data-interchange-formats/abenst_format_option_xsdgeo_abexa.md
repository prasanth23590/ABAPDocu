---
title: "ST - Formatting Options for Spatial Data"
source_file: abenst_format_option_xsdgeo_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules > ST - option, Mapping Rules for Elementary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Formatting Options for Spatial Data

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the `XSDGEO` domain is mapped using formatting options.

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
CLASS cl_demo_st_format_option_geo DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_format_option_geo IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: 
      BEGIN OF town, 
        name     TYPE string, 
        location TYPE xsdgeo, 
      END OF town. 
 
    FINAL(json) = `{"Town":{"Name":"Walldorf",` && 
      `"Location":{"type":"Point","coordinates":[49.3063,8.6423]}}}`. 
 
    DATA walldorf TYPE town. 
    CALL TRANSFORMATION demo_st_format_option_geo 
      SOURCE XML json 
      RESULT town = walldorf. 
 
    DATA(ewkb_walldorf) = VALUE town( 
      name = walldorf-name location = walldorf-location ). 
 
    FINAL(json_writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    FINAL(xml_writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_xml10 ). 
 
    CALL TRANSFORMATION demo_st_format_option_geo 
      SOURCE town = ewkb_walldorf 
      RESULT XML json_writer. 
 
    FINAL(json_result) = cl_abap_conv_codepage=>create_in( )->convert( 
      json_writer->get_output( ) ). 
 
    out->begin_section( `geoJSON result` ). 
    out->write_json( json_result ). 
 
    CALL TRANSFORMATION demo_st_format_option_geo 
      SOURCE town = ewkb_walldorf 
      RESULT XML xml_writer. 
 
    FINAL(xml_result) = cl_abap_conv_codepage=>create_in( )->convert( 
      xml_writer->get_output( ) ). 
 
    out->next_section( `XML result` ). 
    out->write_xml( xml_result ). 
    out->end_section( ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example passes ABAP data to the transformation `DEMO_ST_FORMAT_OPTION_GEO` and provides the result in geoJSON and XML format.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="TOWN"/> 
  <tt:template> 
    <object> 
      <object name="Town" tt:ref="TOWN"> 
          <str name = "Name"> 
            <tt:value ref="NAME"/> 
          </str> 
          <object name = "Location"> 
            <tt:value ref="LOCATION" option="format(geo=4326)"/> 
          </object> 
      </object> 
    </object> 
  </tt:template> 
</tt:transform>
```

In this example, `geo=4326` is used, which represents the WGS 84 standard representation.

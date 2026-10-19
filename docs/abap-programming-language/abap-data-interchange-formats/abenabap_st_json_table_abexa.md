---
title: "JSON - Simple Transformation for Internal Tables"
source_file: abenabap_st_json_table_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Simple Transformation for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the Simple Transformation of an internal table to [JSON data](abenjson_oview.md).

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
CLASS cl_demo_st_json_table DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_json_table IMPLEMENTATION. 
  METHOD main. 
    "Internal table as source of transformation 
    out->begin_section( 'Internal Table' ). 
    DATA: BEGIN OF carrier_wa, 
            carrid   TYPE scarr-carrid, 
            carrname TYPE scarr-carrname, 
            url      TYPE scarr-url, 
          END OF carrier_wa, 
          carrier_tab LIKE TABLE OF carrier_wa. 
    SELECT * 
           FROM scarr 
           INTO CORRESPONDING FIELDS OF TABLE @carrier_tab. 
    out->write_data( carrier_tab ). 
 
    "Simple Transformation to JSON 
    out->next_section( 'JSON' ). 
    DATA(json_writer) = cl_sxml_string_writer=>create( 
                          type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION demo_st_json_table 
                        SOURCE carriers = carrier_tab 
                        RESULT XML json_writer. 
    FINAL(json) = json_writer->get_output( ). 
    out->write_json( json ). 
 
    "Simple Transformation to JSON-XML 
    out->next_section( 'JSON-XML' ). 
    CALL TRANSFORMATION demo_st_json_table 
                        SOURCE carriers = carrier_tab 
                        RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
 
    "Assert symmetry of transformation 
    DATA result_tab LIKE carrier_tab. 
    CALL TRANSFORMATION demo_st_json_table 
                        SOURCE XML json 
                        RESULT carriers = result_tab. 
    ASSERT result_tab = carrier_tab. 
 
    "Assert that results of transformation and JSON-Writer are the same 
    FINAL(xml_reader) = cl_sxml_string_reader=>create( xml ). 
    json_writer = cl_sxml_string_writer=>create( 
                    type = if_sxml=>co_xt_json ). 
    xml_reader->next_node( ). 
    xml_reader->skip_node( json_writer ). 
    ASSERT json_writer->get_output( ) = json. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An internal table `carrier_tab` is filled with data from the database table `SCARR` and is transformed twice using the Simple Transformation `DEMO_ST_JSON_TABLE`. The ST program is as follows:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="CARRIERS"/> 
  <tt:template> 
    <array> 
      <tt:loop ref=".CARRIERS"> 
        <object> 
          <str name="Carrier-Id"> 
            <tt:value ref="$ref.carrid"/> 
          </str> 
          <str name="Carrier"> 
            <tt:value ref="$ref.carrname"/> 
          </str> 
          <str name="URL"> 
            <tt:value ref="$ref.url"/> 
          </str> 
        </object> 
      </tt:loop> 
    </array> 
  </tt:template> 
</tt:transform>
```

The transformation is written in such a way that the new XML data has a valid [JSON XML](abenabap_json_xml.md) format.

- When the transformation is called for the first time, a[JSON writer](abenabap_json_sxml.md) is specified as the result. The JSON data can be retrieved directly from this result and added to the `json` string, where the data can be output.

- When the transformation is called for the second time, an inline declared byte string `xml` is specified as the result. This usually creates XML data in XML 1.0 format. The output shows that it is the JSON XML created by the transformation.

Finally, a demonstration that:

- The Simple Transformation is symmetrical. To do this, the JSON data is passed to the transformation. The result matches the source table.

- An additional [JSON writer](abenabap_json_sxml.md) creates the same JSON data in `xml` from the JSON-XML, as when the transformation is called. Specifying a JSON writer as the result of a transformation means that JSON-XML does not need to be explicitly handled in the ABAP class.

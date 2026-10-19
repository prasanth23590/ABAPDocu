---
title: "JSON - Simple Transformation for Name Attributes"
source_file: abenabap_st_json_table_attr_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Simple Transformation for Name Attributes

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates a Simple Transformation used to create name attributes in [JSON data](abenjson_oview.md).

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
CLASS cl_demo_st_json_table_attrbts DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_st_json_table_attrbts IMPLEMENTATION. 
  METHOD main. 
    "Internal table as source of transformation 
    out->begin_section( 'Internal Table' ). 
    DATA: BEGIN OF carrier_wa, 
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
    FINAL(json_writer) = cl_sxml_string_writer=>create( 
                          type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION demo_st_json_table_attributes 
                        SOURCE carriers = carrier_tab 
                        RESULT XML json_writer. 
    FINAL(json) = json_writer->get_output( ). 
    out->write_json( json ). 
 
    "Simple Transformation to JSON-XML 
    out->next_section( 'JSON-XML' ). 
    CALL TRANSFORMATION demo_st_json_table_attributes 
                        SOURCE carriers = carrier_tab 
                        RESULT XML FINAL(xml). 
    out->write_xml( xml ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in a similar way to the [executable example](abenabap_st_json_table_abexa.md) for an internal table, but the values of the attributes `name` of the elements `object` in JSON-XML are also filled from the internal table in the Simple Transformation `DEMO_ST_JSON_TABLE_ATTRIBUTES`. The ST program is as follows:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="CARRIERS"/> 
  <tt:template> 
    <array> 
      <tt:loop ref=".CARRIERS"> 
        <object> 
          <str> 
            <tt:attribute name="name"> 
              <tt:value ref="$ref.carrname"/> 
            </tt:attribute> 
            <tt:value ref="$ref.url"/> 
          </str> 
        </object> 
      </tt:loop> 
    </array> 
  </tt:template> 
</tt:transform>
```

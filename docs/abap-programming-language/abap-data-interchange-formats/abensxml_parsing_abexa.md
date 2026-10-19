---
title: "sXML - Token-Based Parsing"
source_file: abensxml_parsing_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Token-Based Parsing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simple [token-based](abenabap_sxml_lib_parse_iterative.md) reading of XML data.

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
CLASS cl_demo_sxml_token_reader DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS get_node_type 
      IMPORTING node_type_int           TYPE if_sxml_node=>node_type 
      RETURNING VALUE(node_type_string) TYPE string. 
    METHODS get_value_type 
      IMPORTING value_type_int           TYPE if_sxml_value=>value_type 
      RETURNING VALUE(value_type_string) TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_token_reader IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `XML-Data` ). 
    FINAL(xml) = cl_abap_conv_codepage=>create_out( )->convert( 
     `<?xml version="1.0"?>` && 
     `<order number="4711"` && 
     ` xmlns:demo="http://www.sap.com/abapdemos">` && 
     ` <!-- Head and body of order -->` && 
     ` <demo:head>` && 
     ` <demo:status>confirmed</demo:status>` && 
     ` <demo:date format="mm-dd-yyyy">07-19-2012</demo:date>` && 
     ` </demo:head>` && 
     ` <demo:body>`  && 
     ` <demo:item units="2" price="17.00">Part No. 0110</demo:item>` && 
     ` <demo:item units="1" price="10.50">Part No. 1609</demo:item>` && 
     ` <demo:item units="5" price="12.30">Part No. 1710</demo:item>` && 
     ` </demo:body>` && 
     `</order>` ). 
    out->write_xml( xml ). 
 
    out->next_section( `Parsed Nodes of the XML-Data` ). 
    DATA: BEGIN OF node, 
            node_type  TYPE string, 
            prefix     TYPE string, 
            name       TYPE string, 
            nsuri      TYPE string, 
            value_type TYPE string, 
            value      TYPE string, 
          END OF node, 
          nodes LIKE TABLE OF node. 
    FINAL(reader) = cl_sxml_string_reader=>create( xml ). 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          APPEND VALUE #( 
            node_type  = get_node_type( reader->node_type ) 
            prefix     = reader->prefix 
            name       = reader->name 
            nsuri      = reader->nsuri 
            value_type = get_value_type( reader->value_type ) 
            value      = reader->value ) TO nodes. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open. 
            DO. 
              reader->next_attribute( ). 
              IF reader->node_type <> if_sxml_node=>co_nt_attribute. 
                EXIT. 
              ENDIF. 
              APPEND VALUE #( 
                node_type  = `attribute` 
                prefix     = reader->prefix 
                name       = reader->name 
                nsuri      = reader->nsuri 
                value      = reader->value ) TO nodes. 
            ENDDO. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO FINAL(parse_error). 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
 
    out->write( nodes ). 
  ENDMETHOD. 
  METHOD get_node_type. 
    CASE node_type_int. 
      WHEN if_sxml_node=>co_nt_initial. 
        node_type_string = `CO_NT_INITIAL`. 
*      WHEN if_sxml_node=>co_nt_comment. 
*        node_type_string = `CO_NT_COMMENT`. 
      WHEN if_sxml_node=>co_nt_element_open. 
        node_type_string = `CO_NT_ELEMENT_OPEN`. 
      WHEN if_sxml_node=>co_nt_element_close. 
        node_type_string = `CO_NT_ELEMENT_CLOSE`. 
      WHEN if_sxml_node=>co_nt_value. 
        node_type_string = `CO_NT_VALUE`. 
      WHEN if_sxml_node=>co_nt_attribute. 
        node_type_string = `CO_NT_ATTRIBUTE`. 
*      WHEN if_sxml_node=>co_nt_pi. 
*        node_type_string = `CO_NT_FINAL`. 
      WHEN OTHERS. 
        node_type_string = `Error`. 
    ENDCASE. 
  ENDMETHOD. 
  METHOD get_value_type. 
    CASE value_type_int. 
      WHEN 0. 
        value_type_string = `Initial`. 
      WHEN if_sxml_value=>co_vt_none . 
        value_type_string = `CO_VT_NONE`. 
      WHEN if_sxml_value=>co_vt_text. 
        value_type_string = `CO_VT_TEXT`. 
      WHEN if_sxml_value=>co_vt_raw. 
        value_type_string = `CO_VT_RAW`. 
      WHEN if_sxml_value=>co_vt_any. 
        value_type_string = `CO_VT_ANY`. 
      WHEN OTHERS. 
        value_type_string = `Error`. 
    ENDCASE. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates how the two methods `NEXT_NODE` and `NEXT_ATTRIBUTE` of a string reader can be used to read all existing information in XML data in a nested loop. The outer loop iterates across all nodes of the XML data and the inner loop iterates across any existing list of XML attributes of an element. The relevant information is taken from the attributes of the reader, appended to an internal table, and output as a result.

## Hint

The class `CL_DEMO_SXML_PARSE_XML` implements the token-based parsing shown here for any XML data that can be entered.

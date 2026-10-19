---
title: "sXML - Steps in Token-Based Parsing"
source_file: abensxml_parsing_steps_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Steps in Token-Based Parsing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various steps in [token-based parsing](abenabap_sxml_lib_parse_iterative.md).

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
CLASS cl_demo_sxml_token_rdr_steps DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA parser TYPE REF TO if_sxml_reader. 
    DATA: BEGIN OF wa, 
            method    TYPE string, 
            node_type TYPE string, 
            name      TYPE string, 
            value     TYPE string, 
          END OF wa, 
          output LIKE TABLE OF wa. 
    METHODS parse 
      IMPORTING method TYPE string. 
    METHODS get_node_type 
      IMPORTING node_type_int           TYPE if_sxml_node=>node_type 
      RETURNING VALUE(node_type_string) TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_token_rdr_steps IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `XML-Data` ). 
    FINAL(xml) = `<x a="aval" b="bval"><y c="cval">yval</y></x>`. 
    out->write_xml( xml ). 
 
    out->next_section( `Parser Methods` ). 
 
    parser = cl_sxml_string_reader=>create( 
               cl_abap_conv_codepage=>create_out( )->convert( xml ) ). 
 
    parse( 'NEXT_NODE' ). 
    parse( 'NEXT_ATTRIBUTE' ). 
    parse( 'NEXT_ATTRIBUTE' ). 
    parse( 'CURRENT_NODE' ). 
    parse( 'NEXT_ATTRIBUTE' ). 
    parse( 'NEXT_NODE' ). 
    parse( 'NEXT_ATTRIBUTE' ). 
    parse( 'NEXT_NODE' ). 
    parse( 'PUSH_BACK' ). 
    parse( 'NEXT_ATTRIBUTE' ). 
    parse( 'PUSH_BACK' ). 
    parse( 'SKIP_NODE' ). 
    parse( 'NEXT_NODE' ). 
 
    out->write( output ). 
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
  METHOD parse. 
    CALL METHOD parser->(method). 
    APPEND VALUE #( 
      method     = method 
      node_type  = get_node_type( parser->node_type ) 
      name       = parser->name 
      value      = parser->value ) TO output. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Using simple XML data, this example demonstrates how possible steps work, alongside `NEXT_NODE` and `NEXT_ATTRIBUTE`, in [token-based parsing](abenabap_sxml_lib_parse_iterative.md) with an XML reader from [sXML Library](abenabap_sxml_lib.md).

- The method `CURRENT_NODE` resets an iteration across an attribute list back to its start.

- The method `PUSH_BACK` first branches an iteration from a value node to the associated element opening and from there to the element opening of the superelement.

- The method `SKIP_NODE` then parses all subnodes up to the end of element of the XML data.

In this example, the demonstration methods process a known XML data structure. A further [executable example](abensxml_parsing_methods_abexa.md) demonstrates the methods without the entire structure of XML data being known in advance.

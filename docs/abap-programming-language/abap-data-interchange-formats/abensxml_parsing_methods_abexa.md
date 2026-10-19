---
title: "sXML - Methods for Token-Based Parsing."
source_file: abensxml_parsing_methods_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Methods for Token-Based Parsing.

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how various methods are used in [token-based parsing](abenabap_sxml_lib_parse_iterative.md).

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
CLASS cl_demo_sxml_token_rdr_mthds DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS get_node_type 
      IMPORTING node_type_int           TYPE if_sxml_node=>node_type 
      RETURNING VALUE(node_type_string) TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_token_rdr_mthds IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `XML-Data` ). 
    FINAL(xml) = cl_abap_conv_codepage=>create_out( )->convert( 
     `<?xml version="1.0"?>` && 
     `<items>` && 
     `<item1 a1="11" b1="12" c1="13">1</item1>`  && 
     `<item2 a2="21" b2="22" c2="23">2</item2>`  && 
     `<item3 a3="31" b3="32" c3="33"><subItems>` && 
     `<subItem1>31</subItem1>` && 
     `<subItem2>32</subItem2>` && 
     `<subItem3>33</subItem3>` && 
     `</subItems></item3>` && 
     `<item4 a4="AA==" b4="AQ==" c4="Ag==">4</item4>` && 
     `</items>` ). 
    out->write_xml( xml ). 
 
    "Parsing all nodes 
    out->next_section( 
      `Parsing all Nodes of the XML-Data` ). 
    DATA: BEGIN OF node, 
            node_type TYPE string, 
            name      TYPE string, 
            value     TYPE string, 
          END OF node, 
          nodes LIKE TABLE OF node. 
    DATA(reader) = cl_sxml_string_reader=>create( xml ). 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          APPEND VALUE #( 
            node_type  = get_node_type( reader->node_type ) 
            name       = reader->name 
            value      = reader->value ) TO nodes. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open. 
            DO. 
              reader->next_attribute( ). 
              IF reader->node_type <> if_sxml_node=>co_nt_attribute. 
                EXIT. 
              ENDIF. 
              APPEND VALUE #( 
                node_type  = `attribute` 
                name       = reader->name 
                value      = reader->value ) TO nodes. 
            ENDDO. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO DATA(parse_error). 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
    out->write_data( nodes ). 
 
    "Push back node 
    out->next_section( `Push Back one Node` ). 
    reader = cl_sxml_string_reader=>create( xml ). 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_value AND 
             reader->value = 2. 
            reader->push_back( ). 
            DO. 
              reader->next_attribute( ). 
              IF reader->node_type <> if_sxml_node=>co_nt_attribute. 
                EXIT. 
              ENDIF. 
              out->write( 
                       |{ reader->name } { reader->value }| ). 
            ENDDO. 
            reader->next_node( ). 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO parse_error. 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
 
    "Handling attributes 
    out->next_section( `Handling Attributes` ). 
    reader = cl_sxml_string_reader=>create( xml ). 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open. 
            IF reader->name = 'item2'. 
              reader->get_attribute_value( 'b2' ). 
              out->begin_section( `Query one Attribute` 
                )->write( |{ reader->name } { reader->value }| 
                )->end_section( ). 
            ENDIF. 
            DO. 
              reader->next_attribute( ). 
              IF reader->node_type <> if_sxml_node=>co_nt_attribute. 
                EXIT. 
              ENDIF. 
              IF reader->value = '33'. 
                out->begin_section( `Reset Node` ). 
                reader->current_node( ). 
                DO. 
                  reader->next_attribute( ). 
                  IF reader->node_type <> if_sxml_node=>co_nt_attribute. 
                    EXIT. 
                  ENDIF. 
                  out->write( |{ reader->name } { reader->value }| ). 
                ENDDO. 
                out->end_section( ). 
                EXIT. 
              ENDIF. 
              IF reader->name = 'a4'. 
                out->begin_section( `Reading Raw Values` ). 
              ENDIF. 
              TRY. 
                  reader->next_attribute_value( 
                    if_sxml_value=>co_vt_raw ). 
                  out->write( |{ reader->name 
                             } { reader->value 
                             } { reader->value_raw }| ). 
                CATCH cx_sxml_parse_error INTO parse_error. 
                  CONTINUE. 
              ENDTRY. 
            ENDDO. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO parse_error. 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
 
    "Skip node 
    out->next_section( `Skipping a Node and Getting the Subtree` ). 
    reader = cl_sxml_string_reader=>create( xml ). 
    DATA(writer) = CAST if_sxml_writer( 
      cl_sxml_string_writer=>create(  ) ). 
    DATA level TYPE i. 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open. 
            level += 1. 
          ELSEIF reader->node_type = if_sxml_node=>co_nt_element_close. 
            level -= 1. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open AND 
             level > 2. 
            reader->skip_node( writer ). 
            level -= 1. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO parse_error. 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
    DATA(xml_sub) = 
       CAST cl_sxml_string_writer( writer )->get_output(  ). 
    out->write_xml( xml_sub ). 
 
    "Skip node 
    out->next_section( `Skipping a Node and Getting the Subelements` ). 
    reader = cl_sxml_string_reader=>create( xml ). 
    writer = CAST if_sxml_writer( 
      cl_sxml_string_writer=>create(  ) ). 
    writer->open_element( name = 'subElements' ). 
    CLEAR level. 
    TRY. 
        DO. 
          reader->next_node( ). 
          IF reader->node_type = if_sxml_node=>co_nt_final. 
            EXIT. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open. 
            level += 1. 
          ELSEIF reader->node_type = if_sxml_node=>co_nt_element_close. 
            level -= 1. 
          ENDIF. 
          IF reader->node_type = if_sxml_node=>co_nt_element_open AND 
             level > 3. 
            reader->skip_node( writer ). 
            level -= 1. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO parse_error. 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
    writer->close_element( ). 
    xml_sub = 
       CAST cl_sxml_string_writer( writer )->get_output(  ). 
    out->write_xml( xml_sub ). 
 
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
ENDCLASS.
```

## Example Description

A string of XML data is parsed multiple times:

- In the first parsing, all data is read as usual in a nested loop using the methods `NEXT_NODE` and `NEXT_ATTRIBUTES`.

- In the second parsing, the method `PUSH_BACK` is used to reset the parser to the element opening for each value node with a specific value and to read the attributes here.

- The third parsing demonstrates various ways of reading XML data.

  - First, a specific attribute is read for an element with a specific name using `GET_ATTRIBUTE_VALUE`.

  - Then an iteration runs across all attributes of all elements without evaluating the elements until a specific value occurs. If the value occurs, the method `CURRENT_NODE` is used to reset the parser to the start of the current attribute list and the list is evaluated.

  - Finally, the method `NEXT_ATTRIBUTE_VALUE` is used to read the value of each attribute as raw data stored in [Base64](../../abap-glossary/abenbase64_glosry.md) format. The data is displayed only if this is successful.

- In the fourth and fifth parsings, the method `SKIP_NODE` demonstrates why the hierarchy level of the current node is saved in the helper variable `level`.

  - In the first case, the element opening of `subitems` is exited using `SKIP_NODE`. The entire subtree introduced using `subitems` is parsed and placed in an XML writer. The results are then displayed.

  - In the second case, the element openings of all subelements of `subitems` are exited and these are parsed and their content is placed in an XML writer. These elements are located at the same level, which means the associated element opening and the end of element must be added to the writer explicitly.

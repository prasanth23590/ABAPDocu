---
title: "sXML - Object-Oriented Parsing"
source_file: abensxml_oo_parsing_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Object-Oriented Parsing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simple [object-oriented](abenabap_sxml_lib_parse_oo.md) reading of XML data.

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
CLASS cl_demo_sxml_oo_reader DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sxml_oo_reader IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `XML-Data` ). 
    FINAL(xml) = cl_abap_conv_codepage=>create_out( )->convert( 
     `<?xml version="1.0"?>` && 
     `<order number="4711"` && 
     ` xmlns:demo="http://www.sap.com/abapdemos">` && 
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
    DATA: BEGIN OF node_wa, 
            node_type TYPE string, 
            prefix    TYPE string, 
            name      TYPE string, 
            nsuri     TYPE string, 
            value     TYPE string, 
            value_raw TYPE xstring, 
          END OF node_wa, 
          nodes LIKE TABLE OF node_wa. 
    FINAL(reader) = cl_sxml_string_reader=>create( xml ). 
    TRY. 
        DO. 
          CLEAR node_wa. 
          FINAL(node) = reader->read_next_node( ). 
          IF node IS INITIAL. 
            EXIT. 
          ENDIF. 
 
          CASE node->type. 
            WHEN if_sxml_node=>co_nt_element_open. 
              FINAL(open_element) = CAST if_sxml_open_element( node ). 
              node_wa-node_type = `open element`. 
              node_wa-prefix    = open_element->prefix. 
              node_wa-name      = open_element->qname-name. 
              node_wa-nsuri     = open_element->qname-namespace. 
              FINAL(attributes)  = open_element->get_attributes( ). 
              APPEND node_wa TO nodes. 
              LOOP AT attributes INTO FINAL(attribute). 
                node_wa-node_type = `attribute`. 
                node_wa-prefix    = attribute->prefix. 
                node_wa-name      = attribute->qname-name. 
                node_wa-nsuri     = attribute->qname-namespace. 
                IF attribute->value_type = if_sxml_value=>co_vt_text. 
                  node_wa-value = attribute->get_value( ). 
                ELSEIF attribute->value_type = 
                                   if_sxml_value=>co_vt_raw. 
                  node_wa-value_raw = attribute->get_value_raw( ). 
                ENDIF. 
                APPEND node_wa TO nodes. 
              ENDLOOP. 
              CONTINUE. 
            WHEN if_sxml_node=>co_nt_element_close. 
              FINAL(close_element) = CAST if_sxml_close_element( node ). 
              node_wa-node_type   = `close element`. 
              node_wa-prefix      = close_element->prefix. 
              node_wa-name        = close_element->qname-name. 
              node_wa-nsuri       = close_element->qname-namespace. 
              APPEND node_wa TO nodes. 
              CONTINUE. 
            WHEN if_sxml_node=>co_nt_value. 
              FINAL(value_node) = CAST if_sxml_value_node( node ). 
              node_wa-node_type   = `value`. 
              IF value_node->value_type = if_sxml_value=>co_vt_text. 
                node_wa-value = value_node->get_value( ). 
              ELSEIF value_node->value_type = if_sxml_value=>co_vt_raw. 
                node_wa-value_raw = value_node->get_value_raw( ). 
              ENDIF. 
              APPEND node_wa TO nodes. 
              CONTINUE. 
            WHEN OTHERS. 
              node_wa-node_type   = `Error`. 
              APPEND node_wa TO nodes. 
              EXIT. 
          ENDCASE. 
 
        ENDDO. 
      CATCH cx_sxml_parse_error INTO FINAL(parse_error). 
        out->write_text( parse_error->get_text( ) ). 
    ENDTRY. 
 
    out->write( nodes ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example has the same basic functions as the [executable example](abensxml_parsing_abexa.md) for token-based parsing. Instead of the method `NEXT_NODE`, however, the method `READ_NEXT_NODE` is used here, and its return value is analyzed. Depending on the current node type, a downcast is performed to a suitable interface and attributes and methods are used to read the attributes of the current node.

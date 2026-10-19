---
title: "Access to XML Using Class Libraries"
source_file: abenxml_access_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Access to XML Using Class Libraries

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates parsing and rendering using an example class.

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
CLASS cl_demo_cl_xml_access DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cl_xml_access IMPLEMENTATION. 
  METHOD main. 
    DATA(index) = 1. 
    cl_demo_input=>new( )->request( CHANGING field = index ). 
 
    SELECT FROM scarr 
           FIELDS * 
           INTO TABLE @FINAL(itab) UP TO 3 ROWS. 
    CALL TRANSFORMATION id SOURCE itab = itab 
                        RESULT XML FINAL(xml). 
 
    out->next_section( 'Original XML' 
    )->write_xml( xml ). 
 
    TRY. 
        FINAL(nodes) = cl_demo_xml_access=>parse_xml( xml ). 
      CATCH cx_demo_xml_access. 
        out->write( 'Exception in parsing' ). 
        RETURN. 
    ENDTRY. 
 
    out->next_section( 'Node Table' 
     )->write_data( nodes ). 
 
    TRY. 
        cl_demo_xml_access=>get_tree_nodes( 
          EXPORTING nodes = nodes 
                    index = index 
          IMPORTING subtree =     FINAL(subtree) 
                    descendants = FINAL(descendants) 
                    ancestors   = FINAL(ancestors) 
                    siblings    = FINAL(siblings)  ). 
 
        out->next_section( |Subtree starting with node { index }| 
        )->write_data( subtree 
        )->next_section( |Descendants of node { index }| 
        )->write_data( descendants 
        )->next_section( |Ancestors of node { index }| 
        )->write_data( ancestors 
        )->next_section( |Siblings of node { index }| 
        )->write_data( siblings ). 
      CATCH cx_demo_xml_access. 
        out->write( 'Exception in hierarchy data' ). 
        RETURN. 
    ENDTRY. 
 
    TRY. 
        out->next_section( 'Rendered XML' )->write_xml( 
          cl_demo_xml_access=>render_xml( nodes ) ). 
      CATCH cx_demo_xml_access. 
        out->write( 'Exception in rendering' ). 
        RETURN. 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example class `CL_DEMO_XML_ACCESS` wraps methods of the [sXML Library](../../abap-glossary/abensxml_library_glosry.md).

- Method `PARSE_XML` allows the parsing of the relevant data of an XML file from a byte string into an internal table whose structure is defined in that class.

- Method `RENDER_XML` allows the rendering of the data from such a node table into an XML file in a byte string.

- Method `GET_HIERARCHY_DATA` allows retrieving information about the hierarchical relations between the XML nodes stored in the internal table. For that, the internal table is accessed with [hierarchy functions](../../abap-glossary/abenhierarchy_function_glosry.md) of ABAP SQL.

As an example, an XML file is accessed that results from a transformation of an internal table into [asXML](../../abap-glossary/abenasxml_glosry.md) format by using the predefined identity transformation [`ID`](abenabap_xslt_id.md).

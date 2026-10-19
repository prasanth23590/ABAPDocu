---
title: "iXML - Access Using Names"
source_file: abenixml_c_node_names_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Access Using Names

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Accesses elements of a DOM using the name.

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
CLASS cl_demo_ixml_cld_acc_names DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_acc_names IMPLEMENTATION. 
  METHOD main. 
 
    DATA source_tab TYPE TABLE OF i. 
    source_tab = VALUE #( FOR j = 1 UNTIL j > 10 
                        ( ipow( base = 2 exp = j ) ) ). 
    FINAL(ixml) = cl_ixml_core=>create( ). 
    FINAL(document) = ixml->create_document( ). 
    CALL TRANSFORMATION id SOURCE text = `Powers of 2` 
                                  numbers = source_tab 
                           RESULT XML document. 
 
    FINAL(element)  = document->find_from_name_ns( name = 'TEXT' ). 
    IF element IS NOT INITIAL. 
      out->write_data( element->get_value( ) ). 
    ENDIF. 
 
    FINAL(elements) = 
      document->get_elements_by_tag_name( name = 'item' ). 
    DATA target_tab LIKE source_tab. 
    DO elements->get_length( ) TIMES. 
      FINAL(node) = elements->get_item( sy-index - 1 ). 
      APPEND node->get_value( ) TO target_tab. 
    ENDDO. 
 
    out->write( target_tab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is created in asXML format using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) and written directly to an XML document in DOM representation.

In the XML document, first the element `TEXT` is searched for and then its value displayed. All elements `item` are then collected and their values appended to an internal table in a loop and then output.

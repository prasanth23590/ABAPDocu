---
title: "iXML - Iterator Filters"
source_file: abenixml_c_filter_itrtr_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Iterator Filters

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filtered access to nodes in DOM using an iterator.

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
CLASS cl_demo_ixml_cld_filter_itr DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ixml_cld_filter_itr IMPLEMENTATION. 
  METHOD main. 
    DATA source_tab TYPE TABLE OF i. 
    source_tab = VALUE #( FOR j = 1 UNTIL j > 10 
                        ( ipow( base = 2 exp = j ) ) ). 
    FINAL(ixml) = cl_ixml_core=>create( ). 
    FINAL(document) = ixml->create_document( ). 
    CALL TRANSFORMATION id SOURCE text = `Powers of 2` 
                                  numbers = source_tab 
                           RESULT XML document. 
 
    FINAL(iterator) = document->create_iterator_filtered( 
                      document->create_filter_and( 
                        filter1 = document->create_filter_node_type( 
                          node_types = if_ixml_node=>co_node_element ) 
                        filter2 = document->create_filter_name_ns( 
                          name = 'item' ) ) ). 
 
    DATA target_tab LIKE source_tab. 
    DO. 
      FINAL(node) = iterator->get_next( ). 
      IF node IS INITIAL. 
        EXIT. 
      ENDIF. 
      APPEND node->get_value( ) TO target_tab. 
    ENDDO. 
 
    out->write( target_tab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

XML data is created in asXML format using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) and written directly to an XML document in DOM representation. An iterator is created for the entire document that is linked with a filter. The filter is an *and* join between two filters and selects by node type and name. The iterator only returns the selected nodes.

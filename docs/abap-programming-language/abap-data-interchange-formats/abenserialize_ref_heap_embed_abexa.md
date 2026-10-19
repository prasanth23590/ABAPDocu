---
title: "Serialization to Heap or Embedded"
source_file: abenserialize_ref_heap_embed_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types > asXML - Mapping of Reference Variables and Objects > asXML - Anonymous Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Serialization to Heap or Embedded

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates serializations of an anonymous data object to [asXML](../../abap-glossary/abenasxml_glosry.md) and to [asJSON](../../abap-glossary/abenasjson_glosry.md).

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
CLASS cl_demo_asxml_heap_embedded DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asxml_heap_embedded IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Serialization of Data Reference Variable` ). 
 
    DATA dref TYPE REF TO string. 
    dref = NEW #( `contents` ). 
 
    out->begin_section( `Contents in Heap` 
      )->begin_section( `asXML` ). 
    CALL TRANSFORMATION id SOURCE dref = dref 
                           RESULT XML FINAL(xml_heap). 
    out->write_xml( xml_heap 
      )->next_section( `asJSON` ). 
    FINAL(writer_heap) = cl_sxml_string_writer=>create( 
                          type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref 
                           RESULT XML writer_heap. 
    out->write_json( writer_heap->get_output( ) 
      )->end_section( ). 
 
    out->next_section( `Contents Embedded` 
      )->begin_section( `asXML` ). 
    CALL TRANSFORMATION id SOURCE dref = dref 
                           RESULT XML FINAL(xml_embedded) 
                           OPTIONS data_refs = `embedded`. 
    out->write_xml( xml_embedded 
      )->next_section( `asJSON` ). 
    FINAL(writer_embedded) = cl_sxml_string_writer=>create( 
                          type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE dref = dref 
                           RESULT XML writer_embedded 
                           OPTIONS data_refs = `embedded`. 
    out->write_json( writer_embedded->get_output( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` is used to serialize an anonymous data object to [asXML](../../abap-glossary/abenasxml_glosry.md) and to [asJSON](../../abap-glossary/abenasjson_glosry.md), once with and once without the transformation option [`data_refs = `embedded\`\`](abapcall_transformation_options.md).

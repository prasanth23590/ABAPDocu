---
title: "JSON - asJSON in General"
source_file: abenabap_hello_json_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - asJSON in General

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [asJSON](abenabap_asjson_general.md) for a text string.

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
CLASS cl_demo_json_elementary_trafo DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_json_elementary_trafo IMPLEMENTATION. 
  METHOD main. 
    DATA(text) = `Hello JSON, I'm ABAP!`. 
    out->write_data( text ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE text = text 
                           RESULT XML writer. 
    FINAL(json) = writer->get_output( ). 
    out->write_json( json ). 
 
    out->line( ). 
 
    text = `{"TEXT":"Hello ABAP, I'm JSON!"}`. 
    out->write_json( text ). 
    CALL TRANSFORMATION id SOURCE XML text 
                           RESULT text = text. 
    out->write_data( text ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, for which a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) is specified as the XML target, serializes a text string to [JSON](../../abap-glossary/abenjson_glosry.md). The output shows the [asJSON](../../abap-glossary/abenasjson_glosry.md) representation of the text string.

The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` then deserializes JSON data in asJSON format to a text string.

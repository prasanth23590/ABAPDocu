---
title: "JSON - Rendering"
source_file: abenabap_json_token_writer_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Rendering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the rendering of [JSON data](abenjson_oview.md).

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
CLASS cl_demo_json_token_writer DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA writer TYPE REF TO if_sxml_writer. 
    METHODS write_element IMPORTING name  TYPE string 
                                    attr  TYPE string OPTIONAL 
                                    value TYPE string OPTIONAL 
                          RAISING   cx_sxml_state_error. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_json_token_writer IMPLEMENTATION. 
  METHOD main. 
    writer = 
      CAST if_sxml_writer( 
             cl_sxml_string_writer=>create( 
               type = if_sxml=>co_xt_json  ) ). 
    TRY. 
        write_element( name  = 'object' ). 
        write_element( name  = 'str'    attr = 'order' 
                       value = '4711' ). 
        writer->close_element( ). 
        write_element( name  = 'object' attr = 'head' ). 
        write_element( name  = 'str'    attr = 'status' 
                       value = 'confirmed' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'date' 
                       value = '07-19-2012' ). 
        writer->close_element( ). 
        writer->close_element( ). 
        write_element( name  = 'object' attr = 'body' ). 
        write_element( name  = 'object' attr = 'item' ). 
        write_element( name  = 'str'    attr = 'units' 
                       value = '2' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'price' 
                       value = '17.00' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'Part No.' 
                       value = '0110' ). 
        writer->close_element( ). 
        writer->close_element( ). 
        write_element( name  = 'object' attr = 'item' ). 
        write_element( name  = 'str'    attr = 'units' 
                       value = '1' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'price' 
                       value = '10.50' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'Part No.' 
                       value = '1609' ). 
        writer->close_element( ). 
        writer->close_element( ). 
        write_element( name  = 'object' attr = 'item' ). 
        write_element( name  = 'str'    attr = 'units' 
                       value = '5' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'price' 
                       value = '12.30' ). 
        writer->close_element( ). 
        write_element( name  = 'str'    attr = 'Part No.' 
                       value = '1710' ). 
        writer->close_element( ). 
        writer->close_element( ). 
        writer->close_element( ). 
        writer->close_element( ). 
      CATCH cx_sxml_state_error INTO FINAL(error). 
        out->write( error->get_text( ) ). 
        RETURN. 
    ENDTRY. 
    FINAL(json) = 
      CAST cl_sxml_string_writer( writer )->get_output(  ). 
    out->write_json( json ). 
  ENDMETHOD. 
  METHOD write_element. 
    writer->open_element( name = name ). 
    IF attr IS NOT INITIAL. 
      writer->write_attribute( name = 'name' value = attr ). 
    ENDIF. 
    IF value IS NOT INITIAL. 
      writer->write_value( value = value ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An [XML string writer](abenabap_sxml_lib_render.md) from [XML Library](abenabap_sxml_lib.md) is created as a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) with the type `IF_SXML=>CO_XT_JSON`. [Token-based rendering](abenabap_sxml_lib_render_token.md) methods are used to fill the writer with XML elements that create a valid [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation. The result is a string with valid [JSON data](abenjson_oview.md).

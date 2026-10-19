---
title: "asJSON - Mapping of Enumerated Types"
source_file: abenabap_asjson_abap_types_enum.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of Enumerated Types

The asJSON representation of [enumerated types](../../abap-glossary/abenenum_type_glosry.md) corresponds to their [asXML representation](abenabap_xslt_asxml_enum.md). This means that, in asJSON, the content of an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) is represented by the uppercase name of the [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) with a maximum of 30 characters, and this value is represented as a character-like [elementary data object](abenabap_asjson_abap_types_elem.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization of an internal table with enumerated values by JSON.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM color STRUCTURE col, 
    red, blue, green, 
  END OF ENUM color STRUCTURE col. 
 
DATA colors TYPE SORTED TABLE OF color 
            WITH UNIQUE KEY table_line. 
 
DO. 
  ASSIGN col-(sy-index) TO FIELD-SYMBOL(<fs>). 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  colors = VALUE #( BASE colors ( <fs> ) ). 
ENDDO. 
 
FINAL(writer) = cl_sxml_string_writer=>create( 
     type = if_sxml=>co_xt_json ). 
CALL TRANSFORMATION id SOURCE colors = colors 
                       RESULT XML writer. 
 
out->write_json( writer->get_output( ) ). 
 
out->display( ).
```

The output is:

``` abap
{ 
 "COLORS": 
 [ 
  "RED", 
  "BLUE", 
  "GREEN" 
 ] 
}
```

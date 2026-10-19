---
title: "JSON - asJSON for Additional XML Schema Data Types"
source_file: abenabap_json_asjson_xsd_abexa.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - asJSON for Additional XML Schema Data Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [asJSON](abenabap_asjson_abap_types_table.md) for additional [XML Schema Data Types](abenabap_asjson_schema.md).

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
CLASS cl_demo_asjson_other_xsd_types DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_asjson_other_xsd_types IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      BEGIN OF examples, 
        BEGIN OF boolean, 
          ab_true   TYPE abap_bool 
                    VALUE abap_true, 
          ab_false  TYPE abap_bool 
                    VALUE abap_false, 
          xsd_true  TYPE xsdboolean 
                    VALUE abap_true, 
          xsd_false TYPE xsdboolean 
                    VALUE abap_false, 
        END OF boolean, 
        BEGIN OF date, 
          ab_date  TYPE d 
                   VALUE `20121001`, 
          xsd_date TYPE xsddate_d 
                   VALUE `20121001`, 
        END OF date, 
        BEGIN OF datetime, 
          ab_utclong            TYPE utclong 
                                VALUE `2012-07-27 17:03:34.1234`, 
          ab_timestamp          TYPE timestamp 
                                VALUE `20120727170334`, 
          ab_timestampl         TYPE timestampl 
                                VALUE `20120727170334.1234`, 
          xsd_datetime_z        TYPE xsddatetime_z 
                                VALUE `20120727170334`, 
          xsd_datetime_long_z   TYPE xsddatetime_long_z 
                                VALUE `20120727170334.1234`, 
          xsd_datetime_offset   TYPE xsddatetime_offset 
                                VALUE `20120727170334+140`, 
          xsd_datetime_local    TYPE xsddatetime_local 
                                VALUE `20120727170334`, 
          xsd_datetime_local_dt TYPE xsddatetime_local_dt 
                                VALUE `20120727170334`, 
        END OF datetime, 
        BEGIN OF language, 
          ab_language  TYPE sy-langu 
                       VALUE `D`, 
          xsd_language TYPE xsdlanguage 
                       VALUE `D`, 
        END OF language, 
        BEGIN OF uuid, 
          ab_uuid_raw   TYPE x LENGTH 16 
                       VALUE `005056A207C81ED1BFC6B69E72F50550`, 
          ab_uuid_char  TYPE c LENGTH 32 
                       VALUE `005056A207C81ED1BFC6B69E72F50550`, 
          xsd_uuid_raw  TYPE xsduuid_raw 
                       VALUE `005056A207C81ED1BFC6B69E72F50550`, 
          xsd_uuid_char TYPE xsduuid_char 
                       VALUE `005056A207C81ED1BFC6B69E72F50550`, 
        END OF uuid, 
      END OF examples. 
 
    "Transformation to JSON 
    out->begin_section( 'asJSON'  ). 
    FINAL(writer) = cl_sxml_string_writer=>create( 
      type = if_sxml=>co_xt_json ). 
    CALL TRANSFORMATION id SOURCE examples = examples 
                           RESULT  XML writer. 
    FINAL(json) = writer->get_output( ). 
    out->write_json( json ). 
 
    "JSON-XML 
    out->next_section( 'asJSON-XML' ). 
    FINAL(reader) = cl_sxml_string_reader=>create( json ). 
    FINAL(xml_writer) = cl_sxml_string_writer=>create( ). 
    reader->next_node( ). 
    reader->skip_node( xml_writer ). 
    DATA(xml) = xml_writer->get_output( ). 
    out->write_xml( xml ). 
 
    "asXML 
    out->next_section( 'asXML' ). 
    CALL TRANSFORMATION id SOURCE examples = examples 
                           RESULT  XML xml. 
    out->write_xml( xml ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A call of the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, for which a [JSON](../../abap-glossary/abenjson_writer_glosry.md) writer is specified as an XML target, creates the [asJSON](../../abap-glossary/abenasjson_glosry.md) representation of a structure. The structure components are typed with regular ABAP types and typed with special [domains](abenabap_xslt_asxml_schema.md) for XML schema data types. The time stamp type `utclong` is formatted by default using `yyyy-mm-ddThh:mm:ss.fffffffZ`. [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) in packed numbers, on the other hand, require special domains.

For comparison, the [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation of the JSON data and the [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the ABAP data is also shown.

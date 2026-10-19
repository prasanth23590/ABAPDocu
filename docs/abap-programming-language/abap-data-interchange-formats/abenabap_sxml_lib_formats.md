---
title: "sXML - Formats"
source_file: abenabap_sxml_lib_formats.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Formats

The formats supported by sXML Library are represented by the constants of the `IF_SXML` interface:

- XML 1.0 (constant `IF_SXML=>CO_XT_XML10`)

  Standard XML in accordance with [W3C](http://www.w3.org/XML/). XML data is represented in a specific character format using a character string (standard is Unicode character format UTF-8). Raw data whose binary content is to be stored is represented by a [Base64](../../abap-glossary/abenbase64_glosry.md) representation.

- Binary XML (constant `IF_SXML=>CO_XT_BINARY`)

  SAP-specific binary format for XML data in which redundant information is suppressed. The XML data is not represented as generally readable character strings and the only character set allowed is UTF-8. Special XML readers and XML writers that understand the format are required to parse and render XML data to [Binary XML](../../abap-glossary/abenbinary_xml_glosry.md). sXML can be used to create these objects.

- JSON (constant `IF_SXML=>CO_XT_JSON`)

  JavaScript Object Notation in accordance with [json.org](http://www.json.org/). [JSON](../../abap-glossary/abenjson_glosry.md) is not XML but JSON data can be represented using XML data. Once mapping of this type is the SAP-specific [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md). The format JSON in sXML Library means that an XML writer of this format transforms valid JSON-XML data to JSON data and an XML reader detects JSON data and parses it as if it were JSON-XML data. All methods for [handling JSON in ABAP](abenabap_json.md) are based on readers and writers like these.

When an [XML writer](abenabap_sxml_lib_render.md) is created, the format created by the writer is defined as follows:

- For all formats , the factory methods `CREATE` of the writers for the different storage types have an input parameter `TYPE` to which the value of the constants above can be passed. The XML 1.0 format is used by default. The character format can be passed to the input parameter `ENCODING`, where the default value is UTF-8. This creates the XML declaration. Writers for Binary XML only accept the default value.

When an [XML reader](abenabap_sxml_lib_parse.md) is created, it itself detects the format of the data passed to the parameter `INPUT` of the factory method `CREATE`. The same reader classes can be used for all formats .

## Hints

- The attribute `TYPE` declared in the interface `IF_SXML` contains the type of every XML reader and XML writer or the format it is processing. The possible values of the attribute correspond to those of the constants `CO_XT_...` of the interface.

- XML readers and XML writers of the required formats can be used to transform an XML format to another format.

- An XML writer to which the character format *UTF16BE* or *UTF16LE* was passed to the parameter `ENCODING` uses the byte order mark (BOM) required by the XML standard as the prefix for the written XML data.

## Executable Examples

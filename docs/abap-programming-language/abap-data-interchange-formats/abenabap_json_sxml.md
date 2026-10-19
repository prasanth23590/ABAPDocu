---
title: "JSON - Parsing and Rendering"
source_file: abenabap_json_sxml.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Parsing and Rendering

The processing of [JSON](abenjson_oview.md) data in ABAP is integrated in the [sXML](../../abap-glossary/abensxml_library_glosry.md) Library. Here, JSON is supported as a separate [format](abenabap_sxml_lib_formats.md), with [JSON-XML](../../abap-glossary/abenjson_glosry.md) used as an intermediate step.

- [Parsing JSON Data](abenabap_json_sxml.md#parsing-json-data)

- [Rendering of JSON Data](abenabap_json_sxml.md#rendering-of-json-data)

## Parsing JSON Data

When creating with the method `CREATE`, XML data and [JSON data](abenjson_oview.md) can be passed to each [XML reader](abenabap_sxml_lib_parse.md) in the sXML Library (except for XOP readers) that is based on the corresponding [classes and interfaces](abenabap_sxml_lib_reader.md). The reader recognizes the JSON format and becomes a JSON reader. A JSON reader handles JSON data as if it were passed XML data that contains the [JSON-XML representation](abenabap_json_xml.md) of the JSON data.

When parsed, invalid JSON data raises an exception of the class `CX_SXML_PARSE_ERROR` that should be caught in each parser step.

### Hints

- A JSON reader can, like all XML readers, be used as the source of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md), which allows direct serialization of JSON data to ABAP data objects.

- When JSON data is parsed, escape characters `\` in front of [special characters](abenjson_oview.md) in character-like values are removed automatically.

- By default, the [JSON-XML](abenabap_json_xml.md) representation is created internally, where the object components of the JSON data are not nested in an element `<member>`. To create the longer variant with `<member>` elements, the method `SET_OPTION` of the interface `IF_SXML_READER` can be used to set the option `IF_SXML_READER=>CO_OPT_SEP_MEMBER`.

### Executable Example

[JSON, Parse](abenabap_json_oo_reader_abexa.md)

## Rendering of JSON Data

The method `CREATE` can be used to create each [XML writer](abenabap_sxml_lib_render.md) in sXML Library (except for XOP writers) that is based on the appropriate [classes and interfaces](abenabap_sxml_lib_writer.md) as a JSON writer. Here, the associated constant of the interface `IF_SXML` must be passed to the input parameter `TYPE`.

`cl_sxml_..._writer=>create( type = if_sxml=>co_xt_json ).`

A JSON writer of this type can, like any sXML writer, be provided with XML data using [token-based](abenabap_sxml_lib_render_token.md) and [object-oriented rendering](abenabap_sxml_lib_render_oo.md) methods. This XML data must be a valid [JSON-XML representation](abenabap_json_xml.md) of [JSON data](abenjson_oview.md). The object components of JSON data can be written to a writer in either JSON-XML notation, that is, with or without a `<member>` element.

The writer transforms the entered JSON-XML representation to JSON format and provides the result depending on the writer type.

No invalid JSON data is created and instead an exception of the class `CX_SXML_STATE_ERROR` is raised, which must be caught in each writer step.

### Hints

- When JSON data is rendered, [special characters](abenjson_oview.md) in character-like values are prefixed automatically with the escape character `\`.

- A JSON writer can, like all XML writers, be used as the target of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md), which allows direct serialization of ABAP data objects to JSON data.

### Executable Example

[JSON, Render](abenabap_json_token_writer_abexa.md)

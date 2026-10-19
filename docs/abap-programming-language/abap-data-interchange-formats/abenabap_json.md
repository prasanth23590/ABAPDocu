---
title: "ABAP and JSON"
source_file: abenabap_json.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP and JSON

This section describes how [JSON](../../abap-glossary/abenjson_glosry.md) data can be created and read in ABAP. The main topics are

- processing and creating JSON data using parsers and renderers created and used using the APIs of the [sXML Library](../../abap-glossary/abensxml_library_glosry.md).

- the direct transformation of ABAP data to JSON format (serialization) and reading of data in JSON format to ABAP data objects (deserialization) using transformations that exist as programs in the repository.

ABAP provides the following technologies for handling JSON:

- [Readers and writers for JSON](abenabap_json_lib_object_types.md)

- [Transformations for JSON](abenabap_json_trafos.md)

The readers and writers for JSON enable the parsing and rendering of general XML data, while transformations are used mostly to serialize ABAP data to JSON and deserialize JSON data to ABAP. The technologies are linked by the fact that objects of the reader and writer can serve as the source and target of transformations.

The handling of [JSON data](abenjson_oview.md) in ABAP is based on the following principles:

- A [JSON-XML](abenabap_json_xml.md) format maps JSON data to XML.

- XML readers and XML writers in sXML Library support JSON-XML and can be used as [parsers and renderers](abenabap_json_sxml.md) of JSON data.

- [JSON readers](abenabap_json_lib_reader.md) and [JSON writers](abenabap_json_lib_writer.md) support JSON-XML and can be used as parsers and renderer of JSON data.

- Direct [transformations](abenabap_json_trafos.md) can be performed [between ABAP and JSON](abenabap_json_trafos.md). Here, a canonical JSON representation of ABAP data called [asJSON](abenabap_asjson.md) can be used for the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`.

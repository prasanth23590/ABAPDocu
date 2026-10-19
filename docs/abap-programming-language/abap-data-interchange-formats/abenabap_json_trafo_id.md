---
title: "JSON - Identity Transformation"
source_file: abenabap_json_trafo_id.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Identity Transformation

The predefined [identity transformation](abenabap_xslt_id.md) `ID` is executed internally so that all requirements for [JSON transformations](abenabap_json_trafos.md) are met. The following combinations are possible:

- [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) as XML target

  - ABAP data objects as source

    The ABAP data is serialized directly to its canonical JSON format [asJSON](../../abap-glossary/abenasjson_glosry.md). In this concept, the ABAP data is serialized first to its canonical XML format [asXML](../../abap-glossary/abenasxml_glosry.md). This is then transformed to an [asJSON-XML](../../abap-glossary/abenasjson_xml_glosry.md) representation and passed to the writer.

  - XML data as XML source

    The XML source must be in JSON-XML format and is passed to the writer directly.

  - JSON data or JSON reader as XML source

    The JSON-XML data is passed to the writer directly.

- JSON data or [JSON reader](../../abap-glossary/abenjson_reader_glosry.md) as XML source

  - ABAP data objects as target

    The JSON data must be in an [asJSON](../../abap-glossary/abenasjson_glosry.md) format that matches the ABAP data objects. The JSON data is deserialized directly to the ABAP data objects. Conceptually, an asJSON-XML representation of the asJSON data is processed that is first transformed to asXML and then deserialized to the ABAP data objects.

  - XML data as XML target

    The JSON-XML data is passed to the XML target directly.

  - JSON writer as XML target

    The JSON-XML data is passed to the writer directly.

When XML data is specified as an XML source or XML target, this covers all data that can be specified behind `XML` in `CALL TRANSFORMATION`, except for JSON data and JSON readers and writers.

## Hints

- If the identity transformation `ID` is used to serialize ABAP data to JSON and deserialize JSON data to ABAP, [asJSON, the canonical JSON representation](abenabap_asjson.md) of ABAP data, is applied.

- Copies of the XSL transformation `ID` made from the repository to other XSLT programs are not handled like `ID` internally and cannot be used like ID for JSON data.

## Executable Examples

- See [Identity Transformation with JSON Writer as Target](abenjson_trafo_id_abexa.md) for the various ways of specifying JSON data as an XML source.

- See the [asJSON](abenabap_asjson.md) examples.

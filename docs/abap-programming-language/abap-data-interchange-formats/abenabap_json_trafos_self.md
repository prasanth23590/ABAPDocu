---
title: "JSON - User-defined Transformations"
source_file: abenabap_json_trafos_self.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - User-defined Transformations

User-defined XSLT programs and Simple Transformations enable the following transformations:

- Serialization of ABAP data objects to JSON

  - An [XSL transformation](abenabap_xslt.md) accesses the [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the connected ABAP data, created internally. It must transform asXML to JSON-XML.

  - A [Simple Transformation](abenabap_st.md) accesses the connected ABAP data directly. It must create a valid JSON-XML representation.

- Deserialization from JSON to ABAP data objects:

  - An [XSL transformation](abenabap_xslt.md) must transform JSON-XML to an [asXML](../../abap-glossary/abenasxml_glosry.md) representation of the bound ABAP data objects.

  - A [Simple Transformation](abenabap_st.md) must process JSON-XML and write the data to the bound ABAP data objects.

- XSL transformations between JSON and XML or between JSON and JSON.

  - Transformations can be called between JSON-XML and any XML or between JSON-XML and JSON-XML.

## Executable Example

[Simple Transformation for Internal Tables](abenabap_st_json_table_abexa.md)

---
title: "asJSON - Mapping Additional XML Schema Data Types"
source_file: abenabap_asjson_schema.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping Additional XML Schema Data Types

In [asXML](../../abap-glossary/abenasxml_glosry.md), apart from the XML schema data types needed to map elementary ABAP types, additional XML schema data types are supported by special [domains](abenabap_xslt_asxml_schema.md) called `XSD...`.

asJSON, which is based on asXML, also supports these domains, apart from `XSDQNAME`. In serializations and deserializations from or to ABAP data objects typed with these domains, the same applies as to [asXML](abenabap_xslt_asxml_schema.md). Here, values from the domain `XSDBOOLEAN` are represented as real [Boolean JSON values](abenjson_oview.md) in asJSON.

## Hint

By specifying [`format`](abenst_option_format.md) in the attribute [`option`](abenst_option.md) of the ST statement [`tt:value`](abenst_tt_value_elementary.md), formats of this type can also be applied to ABAP data objects that are not typed with a domain of this type. In JSON, furthermore, the `option` attribute also makes it possible to convert ABAP data fields and [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) to UNIX time stamps (ticks) in the JSON format for OData.

## Executable Example

[asJSON for Additional XML Schema Data Types](abenabap_json_asjson_xsd_abexa.md)

---
title: "asJSON - Canonical JSON Representation"
source_file: abenabap_asjson.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Canonical JSON Representation

The canonical JSON representation asJSON is the format of [JSON](../../abap-glossary/abenjson_glosry.md) data that is produced by a serialization of ABAP data using the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`, or that is required for a deserialization using the identity transformation.

asJSON is based closely on [asXML](abenabap_xslt_asxml.md). Conceptually, an asJSON representation is produced by a restructuring of the asXML representation of this ABAP data to a [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation, while keeping all value content. This means the same basic rules apply as for asXML. In particular, XML schema data types for the mapping of ABAP data types are also used in asJSON.

Description of the asJSON format:

- [General asJSON Format](abenabap_asjson_general.md)

- [Mapping of ABAP Data Types](abenabap_asjson_abap_types.md)

## Hints

- asJSON only occurs in the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID`. In particular, asJSON is not generally needed for user-defined transformations for JSON data. [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) is used directly instead.

- A JSON-XML representation of asJSON is known as [asJSON-XML](../../abap-glossary/abenasjson_xml_glosry.md). asJSON-XML is not used as an intermediate format in transformations, but the asJSON-XML linked with an asJSON representation can be created to analyze it and compare it with asXML.

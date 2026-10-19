---
title: "Canonical XML Representation (asXML)"
source_file: abenabap_xslt_asxml.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Canonical XML Representation (asXML)

The canonical [XML](../../abap-glossary/abenxml_glosry.md) representation asXML is the format of XML data that results from a serialization of ABAP data using [XSLT programs](../../abap-glossary/abenxsl_transformation_glosry.md) as an intermediate format, or that is required for a deserialization using XSLT. This format is also known as ABAP Serialization XML.

The canonical XML representation supports all ABAP data types. The elementary ABAP data types are mapped to a set of XML schema data types. Conversely, special domains are available for further XML schema data types.

The asXML format is significant in the following cases:

- The mapping of elementary ABAP data types to XML schema data types and vice versa.

- In the case of user-defined [XSL](../../abap-glossary/abenxsl_transformation_glosry.md) transformations of ABAP data to an XML format, the asXML format of the serialization result must be known.

- External XML data whose content is to be deserialized into ABAP data must be transformed to asXML format.

- The asXML mapping of elementary ABAP data types to XML schema data types and vice versa is also used in [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md)

Description of the asXML format:

- [General asXML Format](abenabap_xslt_asxml_general.md)

- [Mapping of ABAP Data Types](abenabap_xslt_asxml_named.md)

- [Mapping Additional XML Schema Data Types](abenabap_xslt_asxml_schema.md)

- [Mapping of XML Fragments](abenabap_xslt_asxml_fragment.md)

## Hint

The asXML format of serialized ABAP data or objects can be created and examined using the predefined [identity transformation `ID`](abenabap_xslt_id.md). This transformation is not, however, symmetrical with respect to text strings that contain only blanks. A symmetrical transformation that creates the asXML format of ABAP data (excluding reference variables) can be created using the [`ST`](abenabap_st.md) statement [`tt:copy`](abenst_tt_copy.md).

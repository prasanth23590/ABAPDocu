---
title: "ABAP and XML"
source_file: abenabap_xml.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP and XML

This section describes how [XML](../../abap-glossary/abenxml_glosry.md) data can be created and read in ABAP. The main topics are

- processing and creating XML data using parsers and renderers that are created and used using the APIs of class libraries, and

- the direct transformation of ABAP data to an XML format (serialization) and reads of data in XML format to ABAP data objects (deserialization) using transformations that exist as programs in the repository.

ABAP provides the following technologies for handling [XML](abenxml_oview.md):

- [Class libraries for XML](abenabap_xml_libs.md)

- [Transformations for XML](abenabap_xml_trafos.md)

Class libraries enable the parsing and rendering of general XML data, while transformations are used mostly to serialize ABAP data to XML and deserialize XML data to ABAP. The technologies are linked by the fact that objects of the class libraries can serve as the source and target of transformations.

## Hints

- In this documentation, the term *XML data* generally indicates a character string or byte string whose value is in XML format and which can occur in various forms, such as strings or internal tables. The term *XML document* generally indicates the representation of XML data in [DOM](../../abap-glossary/abendom_glosry.md) format.

- When storing in formats other than UTF-8, it should be noted that XML data must be prefixed with a byte order (BOM), in accordance with the XML standard. This applies specifically to storing character-like data in the character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md) used by the ABAP programming language. This can mean that XML data that was written as character-like data in a Unicode system cannot be handled directly as such in a non-Unicode system.

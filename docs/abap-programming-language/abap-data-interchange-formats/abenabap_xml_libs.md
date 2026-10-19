---
title: "XML - Class Libraries"
source_file: abenabap_xml_libs.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XML - Class Libraries

The following libraries that are delivered as part of AS ABAP enable processing of XML data based on classes and interfaces:

- iXML Library

  The *integrated* XML Library provides methods for parsing XML data in XML 1.0 format to a [DOM](../../abap-glossary/abendom_glosry.md) representation, for processing a DOM representation, and for rendering a DOM representation in XML data. iXML Library supports DTDs (Document Type Definitions). There is an [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md).

- [sXML Library](abenabap_sxml_lib.md)

  The *serial* XML Library provides methods for iterative processing of XML data in various formats. An XML reader reads XML data node by node. An XML writer writes individual nodes in XML data. sXML Library supports [JSON](../../abap-glossary/abenjson_glosry.md).

Objects of these libraries can be used as the source or target of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

## Executable Example

[Access to XML using Class Libraries](abenxml_access_abexa.md)

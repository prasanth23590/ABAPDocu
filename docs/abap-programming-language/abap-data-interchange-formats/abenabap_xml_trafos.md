---
title: "XML - Transformations"
source_file: abenabap_xml_trafos.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XML - Transformations

The AS ABAP kernel contains processors for the following transformations:

- [XSL Transformations](abenabap_xslt.md)

- [Simple Transformations](abenabap_st.md)

Appropriate transformation programs can be created in the ABAP repository and called using the following statement:

- [`CALL TRANSFORMATION`](abapcall_transformation.md)

The possible transformations fulfill the following purposes:

- XSL transformations transform XML to unicode character streams that can be calculated, for example XML or HTML.

- Simple transformations serialize ABAP data to XML and deserialize XML data to ABAP.

To also access ABAP data using XSL transformations, the asXML format can be used as an intermediate format, which defines a mapping between ABAP data and XML:

- [asXML - Canonical XML Representation](abenabap_xslt_asxml.md)

The source and target of these transformations can be ABAP data objects, XML data in strings, or internal tables or objects from [class libraries for XML](abenabap_xml_libs.md).

---
title: "sXML Library"
source_file: abenabap_sxml_lib.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML Library

The sXML Library provides an API consisting of [classes and interfaces](abenabap_sxml_lib_object_types.md) for reading (validating parses) and rendering (validating writes) of XML data in different formats and from different sources or to different targets.

- [Supported Formats](abenabap_sxml_lib_formats.md)

- [Parsing](abenabap_sxml_lib_parse.md)

- [Rendering](abenabap_sxml_lib_render.md)

In contrast to the [iXML Library for ABAP Cloud](abenabap_ixml_lib_cloud.md), no document is created in [DOM format](../../abap-glossary/abendom_glosry.md) and no DTDs (Document Type Definitions) are supported. Instead, the nodes of the tree structure represented by the XML data are processed serially and only the current node can be accessed. The node can be accessed using token-based or object-oriented methods. The classes and interfaces are described in the class and interface documentation.

## Hints

- The sXML Library supports the [UTF](../../abap-glossary/abenutf_glosry.md) character representation of the Unicode character set and hence also characters from the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md).

- The sXML Library methods are also used internally in calls of [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md) using the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

- Serial processing of XML data in the sXML Library involves the [parsing](abenabap_sxml_lib_parse.md) and [rendering](abenabap_sxml_lib_render.md) of each node from front to back without a preview. This is particularly clear in the parser method `SKIP_NODE`, which skips a node, but still has to parse it with all subnodes. This characteristic can be exploited to check whether data is well-formed and to test the copying of XML data to a writer.

- In contrast to the sXML Library, the iXML Libraries create a DOM document and support DTDs.

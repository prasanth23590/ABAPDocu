---
title: "sXML - Rendering"
source_file: abenabap_sxml_lib_render.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Rendering

To create XML data using sXML Library, the content is passed to an XML writer. A writer of this type is validating, which means that invalid actions, such as attempts to add an attribute to a value node, raise an [exception](abenabap_sxml_lib_exceptions.md). An XML writer creates the XML data as a hierarchical tree-like structure where each token is represented by a node that can be assigned uniquely to a parent node (see [W3C Information Set](http://www.w3.org/TR/xml-infoset/)). An XML writer can be used to write the data in exactly the same way is read by an [XML reader](abenabap_sxml_lib_parse.md).

The [classes and interfaces](abenabap_sxml_lib_writer.md) of the sXML Library that are available for rendering XML data are organized so that there are separate XML writer classes for different requirements. These classes inherit from the abstract superclass `CL_SXML_WRITER`. The abstract superclass contains implementations of functions required by all writers and includes the interface `IF_SXML_WRITER`, which contains the components shared by all writers. This interface enables all writers to be accessed in the same way. If special components need to be accessed that are not declared in the interface, a downcast must be used on the corresponding class.

The specialized writer classes are:

- `CL_SXML_STRING_WRITER`

  Writers in this class render XML data to a byte string.

- `CL_SXML_TABLE_WRITER`

  Writers in this class render XML data to an internal table with a flat byte-like line type.

Each of these classes has a specific factory method `CREATE` for creating appropriate writers. Apart from an XOP writer, the required [format](abenabap_sxml_lib_formats.md) and the required character format of the data can be passed to each writer. The standard format is XML 1.0 format in the UTF-8 character format. Instructions on standardization and handling empty elements can be passed to the factory method if the format is suitable.

The methods of the interface `IF_SXML_WRITER` enable serial rendering of XML data. There are two basic ways to do this:

- [Token-based rendering](abenabap_sxml_lib_render_token.md)

- [Object-oriented rendering](abenabap_sxml_lib_render_oo.md)

A writer cannot be used more than once for the same XML data or for other data. The write position of a writer is updated during rendering using its methods. The actions allowed by a writer depend on the current write position. For writers that do not write to external repositories, the written XML can be read using the method `GET_OUTPUT`.

## Hints

- In a suitable write position, an XML writer from the sXML Library can be used as an XML target of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md). The output of the transformation is inserted into the output of the writer and its write position moved accordingly.

- The XML declaration can be set in the `IF_SXML_WRITER` interface using one of the following values for the option `CO_OPT_XML_HEADER`:

  - `CO_OPT_VAL_NO` (no XML header)

  - `CO_OPT_VAL_WITHOUT_ENCODING` (version)

  - `CO_OPT_VAL_FULL` (version and encoding)

    The default option is `CO_OPT_VAL_NO`. Using the option [`xml_header`](abapcall_transformation_options.md) for `CALL TRANSFORMATION` overrides the option in `IF_SXML_WRITER` if it is initial. For JSON and Binary XML, the setting of the option is ignored.

- The writers in the sXML Library do not currently support XML comments, `CDATA` sections, or processor instructions.

- If rendering produces content of elements or attributes, the characters *\<*, *\>*, *&*, *"*, and *'* are transformed automatically into the respective [XML notation](abenxml_oview.md).

## Executable Examples

- [Transformation to XML Writers](abensxml_trafo_into_writer_abexa.md)

- [XML Header](abensxml_writer_header_abexa.md)

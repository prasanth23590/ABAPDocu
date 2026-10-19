---
title: "iXML Library for ABAP Cloud"
source_file: abenabap_ixml_lib_cloud.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML Library for ABAP Cloud

- [API of the iXML Library](abenabap_ixml_lib_cloud.md#api-of-the-ixml-library)

- [Access to the iXML Library](abenabap_ixml_lib_cloud.md#access-to-the-ixml-library)

- [Services in the iXML Library](abenabap_ixml_lib_cloud.md#services-in-the-ixml-library)

## API of the iXML Library

iXML Library provides an API for handling XML documents in [DOM](../../abap-glossary/abendom_glosry.md) format. This API enables

- XML data to be parsed to DOM format,

- reads and writes to be performed on XML documents in DOM format, including creating new documents,

- XML documents in DOM format to be rendered to XML data.

In ABAP programs, the API is implemented using interfaces from the class library with the naming convention `IF_IXML_CORE...`. The access class `CL_IXML_CORE` contains factory methods for creating basic objects such as streams, parsers, documents, and renderers. These objects are then accessed using interface reference variables. The classes and interfaces are documented in the Class Builder.

### Hints

- The [classes and interfaces](abenabap_ixml_lib_c_object_types.md) in iXML Library from the package `SIXML_CORE` wrap classes and interfaces implemented in C++ that are delivered as part of the ABAP kernel.

- iXML Library supports the Unicode character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md). Characters from the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md) are supported and the same problems as in [ABAP](../abap-overview/abencharacter_sets.md) can occur.

- The DOM of the iXML Library and its associated methods are also used internally in calls of [XSL transformations](../../abap-glossary/abenxsl_transformation_glosry.md) with the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

## Access to the iXML Library

Precisely one factory object of the [access class](abenabap_ixml_lib_c_cl_ixml.md) `CL_IXML_CORE` is required for accessing iXML Library in an ABAP program. This object is created as follows:

`DATA(ixml) = cl_ixml_core=>create( ).`

The static type of the reference variable `ixml` is then the interface `IF_IXML_CORE`, which contains all factory methods required to create further objects, such as streams, XML documents, parsers, or renderers. This factory object is a singleton and can only be instantiated once in an [internal session](../../abap-glossary/abeninternal_session_glosry.md).

## Services in the iXML Library

The most important services offered by the [classes and interfaces](abenabap_ixml_lib_c_object_types.md) in iXML Library are as follows:

- [XML parser](abenabap_ixml_lib_c_parse.md)

  The XML parser analyzes the syntax of an XML file provided in an [input stream](abenabap_ixml_lib_c_input_output.md) to check whether it is correct and creates an [XML document](abenabap_ixml_lib_c_input_output.md) in a [DOM](../../abap-glossary/abendom_glosry.md) representation from this file. This document can then be accessed using interfaces. The DOM can be created as follows:

  - [Complete Parsing to DOM](abenabap_ixml_lib_c_parse_dom.md)

    The parser creates the XML document in a [DOM](../../abap-glossary/abendom_glosry.md) representation for the complete XML data in a single action and places it in the memory.

  - [Sequential Parsing](abenabap_ixml_lib_c_parse_event.md)

    The parser processes the input stream in sequential runs, where each sequence is determined by events that can be accessed using the interface `IF_IXML_EVENT`. The application can already process each sequence while the parser is running. It is possible to configure whether a complete XML document is saved in [DOM](../../abap-glossary/abendom_glosry.md) representation.

- [Access to DOM](abenabap_ixml_lib_c_dom_access.md)

  An XML document represented as [DOM](../../abap-glossary/abendom_glosry.md) is a standardized tree representation. For each logical unit of the XML document, there is a node object of an associated class that implements specialized interfaces. An ABAP program can use the interfaces to perform reads and writes to the [XML](abenabap_ixml_lib_c_input_output.md) document. The classes of the node objects are not usually used directly in the program.

- [XML renderer](abenabap_ixml_lib_c_render.md)

  The XML renderer creates XML data from an XML document saved as DOM. This document is created by parsing with and without subsequent modifications, or created as a complete new document using the methods of the DOM interface. The renderer then passes the data to an [output stream](abenabap_ixml_lib_c_input_output.md).

- [XPath evaluation](abenabap_cl_ixml_xpath.md)

  An XPath expression can be evaluated using [`CL_IXML_XPATH`](abenabap_ixml_lib_c_xpath.md).

### Hints

- One benefit of DOM is very simple access to the individual parts of an XML document. It also has the drawback, however, of increased memory consumption, which can be up to ten times the actual size of the document. It should be noted that the document itself can already use more memory for its markup than for the actual data. This memory consumption can be restricted by preventing a complete DOM from being created by sequential parsing or by parsing to data objects.

- The DOM in iXML Library also includes DTDs (Document Type Definitions).

- If XML data needs to be parsed and rendered only and no XML documents in DOM representation and no DTDs are needed, [sXML Library](abenabap_sxml_lib.md) provides an alternative with better performance than iXML Library.

- iXML only supports the XML 1.0 format, where XML data is represented by a particular character format using a character string. [sXML Library](abenabap_sxml_lib.md) supports more [formats](abenabap_sxml_lib_formats.md).

- When data is rendered as character-like XML data, this data is prefixed by the byte order mark (BOM) that is required by the XML standard.

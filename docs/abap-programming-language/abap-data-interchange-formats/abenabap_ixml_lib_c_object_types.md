---
title: "iXML - Classes and Interfaces"
source_file: abenabap_ixml_lib_c_object_types.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Classes and Interfaces

The following sections list the classes and interfaces of iXML Library according to subareas.

- [Access class](abenabap_ixml_lib_c_cl_ixml.md)

- [Streams](abenabap_ixml_lib_c_stream.md)

- [Parser](abenabap_ixml_lib_c_parser.md)

- [DOM](abenabap_ixml_lib_c_dom.md)

- [Renderer](abenabap_ixml_lib_c_renderer.md)

- [Encoding](abenabap_ixml_lib_c_encoding.md)

Not all object types in iXML Library include the interface `IF_IXML_UNKNOWN`. Reference variables of this type can point to all objects in iXML Library. The interface `IF_IXML_UNKNOWN` contains the method `QUERY_INTERFACE`, which can be used for special downcasts within iXML Library.

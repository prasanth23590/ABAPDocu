---
title: "iXML - Access to DOM"
source_file: abenabap_ixml_lib_c_dom_access.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Access to DOM

[DOM](../../abap-glossary/abendom_glosry.md) describes a tree-like representation, implemented using instances of classes, of a complete XML document in the memory. At the same time, each component of the XML file is created by a separate object. The associated [interfaces](abenabap_ixml_lib_c_dom.md) of the iXML Library can be used to access an XML document in DOM format.

- [Reads performed on DOM](abenabap_ixml_lib_c_dom_access_r.md)

- [Writes performed on DOM](abenabap_ixml_lib_c_dom_access_w.md)

## Hints

- When working with DOM, it is important to know the difference between the nodes of the DOM and the elements of the represented XML data. Each part of an XML document is represented by a separate node. A single element in XML data in DOM consists of multiple nodes for tags, content and so on, which can be accessed individually or together.

- iXML documents can be defined as an XML target, iXML documents and their nodes can be specified as an XML source for XSL transformations called using [`CALL TRANSFORMATION`](abapcall_transformation.md).

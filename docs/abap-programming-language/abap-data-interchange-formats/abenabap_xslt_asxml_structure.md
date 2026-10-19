---
title: "asXML - Mapping of Structures"
source_file: abenabap_xslt_asxml_structure.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Structures

The asXML representation of structures is significant mainly for XSL transformations. In Simple Transformations, this representation is important only when using the statement [`tt:copy`](abenst_tt_copy.md).

The components of an ABAP structure are represented in asXML as a sequence of subelements of the structure element. The content of each subelement corresponds to the canonical representation of the component value. The name of each subelement is the name of the corresponding component. In serializations, the subelements are represented in the order of the components in the structure. In deserializations of the asXML representation of a structure, the order of the subcomponents is not important and redundant XML elements are ignored. Components of the structure for which there are no subelements remain unchanged.

If the required XML element does not exist in deserializations to a structure, the structure data object retains its previous value. If an empty element is assigned to a structure, the subelements are missing for all components of the structure and the structure also remains unchanged. To initialize the structure in deserializations in these cases, the transformation option [`clear`](abapcall_transformation_options.md) with the value *all* can be used.

## Executable Examples

- [asXML, Mapping of Structures](abenasxml_structure_abexa.md)

- [Deserializing Structure Components](abenabap_asxml_asjson_empty_abexa.md)

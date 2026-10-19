---
title: "asXML - Mapping of XML Fragments"
source_file: abenabap_xslt_asxml_fragment.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of XML Fragments

asXML allows the mapping of entire XML fragments, that is, of complete elements and their subelements that exist in XML format in ABAP as the content of data objects or of parts of data objects (such as structure components or table rows). The data objects must have the type `xstring` and be declared with reference to the [DDIC domain](../../abap-glossary/abendomain_glosry.md) `XSDANY`.

- When serialized, such a data object or part of a data object must contain the [UTF-8](../../abap-glossary/abenutf8_glosry.md) representation of a complete XML fragment. The content of the root element of the XML fragment is passed unchanged to the XML element for which the data object was created. If the name of the XML element is not the same as the name of the root element of the XML fragment, the latter is used as the content of an attribute `asx:root` that is added to the XML element. No attribute is created if the names are the same.

- When deserialized, an XML element that contains the attribute `asx:root` must be assigned to such a data object or part of a data object. An XML fragment is created in the data object that has the content of the attribute as a root element and whose content is inherited unchanged from the XML element. If the attribute `asx:root` does not exist, the root element is given the name of the XML element.

The following restrictions apply:

- XML fragments whose elements do not contain attributes cannot be deserialized.

- XML fragments whose root element is in the standard namespace cannot be serialized or deserialized.

## Hints

- An XML fragment that exists in a data object of type `xstring` and that is not declared with reference to the domain `XSDANY` is formatted as the XML schema type `xsd:base64Binary` in accordance with the rules for [mapping elementary data types](abenabap_xslt_asxml_elementary.md).

- An XML element that contains the attribute `asx:root` cannot be deserialized to data objects that are not declared with reference to the domain `XSDANY`.

- The handling of XML fragments in the statement [`tt:value`](abenst_tt_value_elementary.md) is supported in [Simple Transformations](abenabap_st.md), but not in the statements [`tt:write`](abenst_tt_write.md) or [`tt:read`](abenst_tt_read.md). In `tt:value`, the mapping rule for XML fragments can be modified using certain values for the attribute [`option`](abenst_option_xsdany.md).

- XML fragments in byte strings with reference to the domain `XSDANY` are not supported in [transformations for JSON](abenabap_json_trafos.md).

## Executable Example

[asXML, Mapping of XML Fragments](abenasxml_fragments_abexa.md)

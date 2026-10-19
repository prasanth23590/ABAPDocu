---
title: "asXML - Mapping of ABAP Data Types"
source_file: abenabap_xslt_asxml_named.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of ABAP Data Types

Named data objects other than reference variables are represented in asXML as the content of the following elements:

[`<bn1>...</bn1>`](abenabap_xslt_asxml_general.md) [`<bn2>...</bn2>`](abenabap_xslt_asxml_general.md) [`...`](abenabap_xslt_asxml_general.md)

An additional area is implemented for the objects referenced by reference variables:

``` abap
`<asx:heap>` 
  `...` 
`</asx:heap>`
```

Depending on the ABAP data type, serializations map the value of named data objects to a particular XML representation and deserializations operate in the opposite direction:

- [Mapping of Elementary ABAP Types](abenabap_xslt_asxml_elementary.md)

- [Mapping of Structures](abenabap_xslt_asxml_structure.md)

- [Mapping of Internal Tables](abenabap_xslt_asxml_table.md)

- [Mapping of Enumerated Types](abenabap_xslt_asxml_enum.md)

- [Mapping of Reference Variables and Referenced Objects](abenabap_xslt_asxml_references.md)

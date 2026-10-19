---
title: "asJSON - Mapping of ABAP Data Types"
source_file: abenabap_asjson_abap_types.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of ABAP Data Types

Named data objects other than reference variables are represented in asJSON as the content of the following object components:

[`"bn1":...`](abenabap_asjson_general.md) [`"bn1":...`](abenabap_asjson_general.md) [`...`](abenabap_asjson_general.md)

An additional object is implemented for the objects referenced by reference variables:

[`"%heap":...`](abenabap_asjson_general.md)

Depending on the ABAP data type, serializations map the value of named data objects to a particular JSON representation and vice versa in deserializations:

- [Mapping of Elementary ABAP Types](abenabap_asjson_abap_types_elem.md)

- [Mapping of Structures](abenabap_asjson_abap_types_struc.md)

- [Mapping of Internal Tables](abenabap_asjson_abap_types_table.md)

- [Mapping of Enumerated Types](abenabap_asjson_abap_types_enum.md)

- [Mapping of Reference Variables and Referenced Objects](abenabap_asxml_references.md)

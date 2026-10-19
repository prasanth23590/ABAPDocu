---
title: "asJSON - Mapping of Internal Tables"
source_file: abenabap_asjson_abap_types_table.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of Internal Tables

Internal tables are represented in asJSON as [JSON arrays](abenjson_oview.md). The lines of the internal table are represented in their canonical representation as the components of the array. All table categories are allowed. Serializations do not pass any information about the table category to the JSON data. If the target field of a deserialization is a [sorted table](../../abap-glossary/abensorted_table_glosry.md), the lines are sorted accordingly.

## Hints

- An internal table that does not have an associated JSON object component in deserializations retains its previous value. If an empty array is assigned to an internal table, it is set to its type-dependent initial value, that is, it is emptied. To initialize the internal table in either case, the transformation option [`clear`](abapcall_transformation_options.md) with the value *all* can be used.

- Unlike in the [asXML representation](abenabap_xslt_asxml_table.md) of internal tables, asJSON does not require a name like `item` for the table lines.

## Executable Example

[asJSON for Internal Tables](abenabap_json_asjson_table_abexa.md)

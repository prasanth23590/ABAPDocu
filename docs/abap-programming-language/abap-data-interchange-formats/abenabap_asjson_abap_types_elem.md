---
title: "asJSON - Mapping of Elementary ABAP Types"
source_file: abenabap_asjson_abap_types_elem.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of Elementary ABAP Types

The values of elementary ABAP types are represented in asJSON using the [JSON representations](abenjson_oview.md) of character-like values and numeric values. Representations of Boolean values and zero are not used.

- The values of all numeric types (`i`, `p`, `decfloat16`, `decfloat34`, `f`) are represented directly as JSON number values.

- The values of all other types (`c`, `string`, `n`, `d`, `t`, `x`, `xstring`) are represented as character-like values in quotation marks.

The type-dependent format of a value corresponds to the [asXML representation](abenabap_xslt_asxml_named.md) of elementary types and can be taken from the tables there. The serialization and deserialization behavior listed there applies.

## Hint

An elementary ABAP data object that does not have an associated JSON object component in deserializations retains its previous value. To initialize the data object in this case, the transformation option [`clear`](abapcall_transformation_options.md) with the value *all* can be used.

## Executable Example

[asJSON for Elementary ABAP Types](abenabap_json_asjson_elem_abexa.md)

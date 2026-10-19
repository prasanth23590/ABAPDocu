---
title: "asJSON - Named Reference Variables"
source_file: abenabap_asjson_reference_var.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types > asJSON - Mapping of Reference Variables and Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Named Reference Variables

Like a regular data object, a named reference variable is represented as an object component that has special content:

`"bni":{ "%ref":"#key" }`

The content of the object component of a named reference variable is an object with exactly one object component called `%ref`. The content of the object component `%ref` is a character-like value `"#key"`, where `key` is the unique key of an object component in the object `%heap`. The object of an initial reference is empty. The `key` key of the ABAP runtime framework is set in serializations and in deserializations, any key can be used.

Otherwise the same rules apply to serializations and deserializations of named reference variables as to [asXML](abenasxml_reference_variable.md) and the same special cases must be respected.

## Executable Example

[Serializing Data References](abenserialize_dref_abexa.md)

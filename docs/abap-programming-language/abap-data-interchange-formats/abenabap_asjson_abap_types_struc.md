---
title: "asJSON - Mapping of Structures"
source_file: abenabap_asjson_abap_types_struc.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of Structures

In asJSON, an ABAP structure is represented as a [JSON object](abenjson_oview.md) whose object components represent the structure components. The content of each object component corresponds to the canonical representation of the component value. The name of each object component is the name of the corresponding structure component. In serializations, the object components are represented in the order of the components in the structure. In deserializations of the asJSON representation of a structure, the order of the object components is not important and superfluous object components are ignored. Components of the structure for which there are no object components remain unchanged.

## Hint

A structure that does not have an associated JSON object component in deserializations retains its previous value. A structure to which an empty object is assigned also remains unchanged, since this has the same effect on the structure components as a missing object component. To initialize the structure in these cases, the transformation option [`clear`](abapcall_transformation_options.md) can be used with the value *all*.

## Executable Example

[asJSON for Structures](abenabap_json_asjson_struc_abexa.md)

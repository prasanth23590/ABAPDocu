---
title: "asJSON - Mapping of Reference Variables and Objects"
source_file: abenabap_asxml_references.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Mapping of Reference Variables and Objects

As in [asXML](abenabap_xslt_asxml_references.md), a reference mechanism is used for the asJSON representation of anonymous data objects and class instances (objects), which are addressed using references in reference variables. Since [JSON](abenjson_oview.md) does not suggest any syntax for references, an SAP-specific reference mechanism based on asXML is used.

- Named reference variables are represented as object components, whose content is by default a key for the referenced objects.

- The referenced objects are stored as object components in the object [`%heap`](abenabap_asjson_general.md). This name corresponds to the key.

In addition to the value, the dynamic type of the reference variables is specified in the object components of `%heap` when serialization takes place to ensure unique deserialization.

- [asJSON - Named Reference Variables](abenabap_asjson_reference_var.md)

- [asJSON - Anonymous Data Objects](abenabap_asjson_anonym_do.md)

- [asJSON - Instances of Classes](abenabap_asjson_class_instances.md)

## Hints

- The asJSON representation of reference variables and referenced objects is only relevant for [XSL](../../abap-glossary/abenid_trafo_glosry.md) transformations and the identity transformation `ID`. Simple Transformations cannot currently be used to transform reference variables.

- For data references, the value *embedded* can be specified for the transformation option [`data_refs`](abapcall_transformation_options.md) to define embedded storage in serializations instead of storage in the `%heap` object component.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For information about the differences between serializing to `%heap` and embedded storage, see the executable example [Serializations to Heap or Embedded](abenserialize_ref_heap_embed_abexa.md).

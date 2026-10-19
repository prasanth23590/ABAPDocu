---
title: "asXML - Mapping of Reference Variables and Objects"
source_file: abenabap_xslt_asxml_references.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Reference Variables and Objects

Anonymous data objects and instances of classes (objects) are addressed in ABAP using references in reference variables only. The associated asXML format consists of

- subelements of [`values`](abenabap_xslt_asxml_general.md) for named reference variables and

- by default subelements of [`heap`](abenabap_xslt_asxml_general.md) for the referenced objects.

The reference between the reference elements and the object elements is established using an XML reference mechanism, where a referenced object in the same XML data is identified by a key. The dynamic type of the reference variables for the object elements under `heap` is specified when serialization takes place, so that deserialization is unique.

- [Named Reference Variables](abenasxml_reference_variable.md)

- [Anonymous Data&#x2028; Objects](abenasxml_anonymous_data_object.md)

- [Class Instances](abenasxml_class_instances.md)

## Hints

- The asXML representation of reference variables and referenced objects is only of relevance for [XSL](../../abap-glossary/abenid_trafo_glosry.md) transformations and the identity transformation `ID`. You cannot currently use Simple Transformations to transform reference variables.

- For data references, the value *embedded* can be specified for the transformation option [`data_refs`](abapcall_transformation_options.md) to define an embedded repository in serializations instead of the repository in the element `heap`.

## Executable Example

[asXML, Mapping of Objects](abenasxml_object_abexa.md)

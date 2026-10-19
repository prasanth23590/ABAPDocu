---
title: "asXML - Named Reference Variables"
source_file: abenasxml_reference_variable.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types > asXML - Mapping of Reference Variables and Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Named Reference Variables

A named reference variable is represented as the only attribute of the associated subelement of `values`, where the subelement has no further content.

`<bni href="#key"/>`

An attribute for a reference variable has the name `href` and the content *\#key*, where `key` is the unique key of an object in the element `heap`. An element of an initial reference does not have an attribute `href` nor any other content. The `key` key is set by the ABAP runtime framework in serializations and in deserializations, any key can be used.

The following special cases when serializing named reference variables should be noted:

- Data reference variables that point to data objects whose data type only has one technical name raise the exception `CX_REFERENCE_NOT_SERIALIZABLE` (handled using `CX_XSLT_SERIALIZATION_ERROR`). This can be avoided by specifying transformation option [`technical_types`](abapcall_transformation_options.md).

- Data reference variables that point to data objects that were not created using `CREATE DATA` (stack references) are handled like initial reference variables in serializations. This can be overridden by specifying the transformation option [`data_refs`](abapcall_transformation_options.md).

In deserializations to a reference variable, the reference variable must be the same as or more general than the dynamic type of the object that is stored in the XML document. The associated ABAP data objects or instances of a class are created in deserializations.

## Hint

Data types without names or with purely technical names are [bound data types](../../abap-glossary/abenbound_data_type_glosry.md) or data types constructed using [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md).

## Executable Example

[Serializing Data References](abenserialize_dref_abexa.md)

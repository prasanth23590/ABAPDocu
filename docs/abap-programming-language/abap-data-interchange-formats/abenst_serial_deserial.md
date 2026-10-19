---
title: "ST - Serialization and Deserialization"
source_file: abenst_serial_deserial.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Serialization and Deserialization

Serialization and deserialization are primarily based on the following schema:

- During serialization, the literal elements of templates are passed to the target XML data unchanged and the ST statements specified in between are executed.

- In deserializations, the source XML data is handled as an inbound stream and compared to the template element by element. Identically named elements (or attributes or texts) of the inbound stream are consumed if they are at the same position in the ST program or if there is a statement there that can process the element. After the successful comparison or consumption of the element, the comparison of the subsequent element starts.

Serializations and deserializations can be divided into the following topics:

- [Literal Template Content](abenst_literals.md)

- [Non-Literal Attributes](abenst_tt_attribute.md)

- [Namespaces](abenst_tt_namespace.md)

- [Transformation of ABAP Values](abenst_abap_values.md)

- [Value Assignments](abenst_assignments.md)

- [Reading and Writing Variables](abenst_variable_transformations.md)

- [Flow Control](abenst_tt_cond.md)

When a Simple Transformation is defined, it must be noted whether the serializations and deserializations are [symmetric](abenst_symmetry.md).

## Hints

- In serializations and deserializations, the XML data is processed in the form of writer streams and reader streams. When ABAP methods are called from Simple Transformations, [processing these XML streams](abenst_tt_call-method_writerreader.md) is possible.

- Serializations and deserializations are subject to the general restriction that the content of a [data root](abenst_tt_root.md) cannot be modified by serialization and only writes are possible to a data root in deserializations.

---
title: "Simple Transformations (ST)"
source_file: abenabap_st.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Simple Transformations (ST)

Simple Transformations (ST) is an SAP programming language for describing transformations between ABAP data and [XML](../../abap-glossary/abenxml_glosry.md) formats. ST is restricted to the two modes of [serialization](../../abap-glossary/abenserialization_glosry.md) (ABAP to XML) and [deserialization](../../abap-glossary/abendeserialization_glosry.md) (XML to ABAP) of ABAP data, which are most important for data integration. Transformations from ABAP to ABAP and XML to XML are not possible in ST as is the case for more general [XSLT](../../abap-glossary/abenxslt_glosry.md).

Simple Transformations are created as [ST programs](abenst_programs_structure.md). Existing ST programs can be called using the statement [`CALL TRANSFORMATION`](abapcall_transformation.md). The associated ST processor is integrated into the ABAP runtime framework.

In contrast to [XSLT](abenabap_xslt.md), the main advantages of ST programs are as follows:

- ST programs are declarative and thus easier to read.

- ST programs only have serial access to the XML data and are therefore very efficient even with large data volumes. The nodes in XML data, however, cannot be accessed in an arbitrary order.

- ST programs describe serialization and deserialization simultaneously, that is, ABAP data serialized in XML with ST can also be deserialized with the same ST program.

- Objects can be created from ABAP Objects and their methods called in ST programs.

- ST programs are restricted to the transformation of elementary and structured ABAP data, along with internal tables. The transformation of reference variables and referenced objects is not currently supported.

The following topics describe ST:

- [ST - Structure of ST Programs](abenst_programs_structure.md)

- [ST - Addressing ABAP Data](abenst_addressing.md)

- [ST - Serialization and Deserialization](abenst_serial_deserial.md)

- [ST - Modularization with Subtemplates](abenst_modularization.md)

- [ST - Reusing ST Programs](abenst_reuse.md)

- [ST - Access to ABAP Objects from ST](abenst_abap_objects.md)

- [ST - Overview of Statements](abenst_statements.md)

- [ST - Examples](abenst_abexas.md)

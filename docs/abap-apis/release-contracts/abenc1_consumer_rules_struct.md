---
title: "C1 Contract Rules for Consuming Structures"
source_file: abenc1_consumer_rules_struct.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# C1 Contract Rules for Consuming Structures

API providers can add or change non-key elements in global types as structured DDIC types or CDS entities. These types can be released APIs themselves or can be used for typing attributes or method parameters of released classes or interfaces. Also the position of non-key elements can be changed. This impacts all operations with APIs that rely on a certain number of components of a structure and on their position. Main examples are:

- [Assignments and Comparisons](abenc1_consumer_rules_struct.md#assignments-and-comparisons)

- [Unstructured Access](abenc1_consumer_rules_struct.md#unstructured-access)

- [Field Symbols](abenc1_consumer_rules_struct.md#field-symbols)

- [RFC](abenc1_consumer_rules_struct.md#rfc)

Includes

Including a released structure into another structure.

**Possible Problems**

Error, when a component is added that already exists.

**Mitigation**

Include a released structure only by renaming its components with [suffixes](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md).

## Assignments and Comparisons

Assignments and comparisons between data objects that are typed with the released structured type and data objects that are typed otherwise can occur for:

- [Logical Expressions](../../abap-programming-language/abap-program-flow-logic/abenlogexp.md)

- [Assignments](../../abap-programming-language/abap-processing-internal-data/abenvalue_assignments.md)

- [Working with internal tables](../../abap-programming-language/abap-processing-internal-data/abenitab.md)

- [ABAP SQL](../../abap-programming-language/abap-database-access/abenabap_sql.md)

- [Working with data clusters](../../abap-programming-language/abap-data-cluster/abendata_cluster.md)

**Possible Problems**

Depending on the change all kinds of errors might occur. The following allowed changes in particular can affect the rules for processing structures fundamentally:

- Adding numeric components to a formerly character-like structure.

- Adding [deep](../../abap-glossary/abendeep_glosry.md) components to a formerly [flat](../../abap-glossary/abenflat_glosry.md) structure.

- Shifting the positions of numeric or deep components to formerly character-like sections.

**Mitigation**

No assignments or comparisons between released structures and data objects that are typed otherwise. No usage of otherwise defined structures in ABAP SQL. The various `CORRESPONDING` mechanisms can be used to mitigate the problem, but they are not failsafe in all situations.

## Unstructured Access

Processing the content of a released structure without addressing single components as for example:

- [Offset/Length Specifications](../../abap-programming-language/abap-operands/abenoffset_length.md)

- [String processing](../../abap-programming-language/abap-processing-internal-data/abenabap_data_string.md) (on complete structure)

**Possible Problems**

Depending on the change (see above) all kinds of errors might occur.

**Mitigation**

No processing of released structures without accessing single

components.

## Field Symbols

Addressing released structures with [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) by using:

- [`ASSIGN`](../../abap-programming-language/abap-processing-internal-data/abapassign.md)

- `ASSIGNING` addition when [working with internal tables](../../abap-programming-language/abap-processing-internal-data/abenitab.md)

**Possible Problems**

When the addition [`CASTING`](../../abap-programming-language/abap-processing-internal-data/abapassign_casting.md) is used, deep components must appear with exactly the same type and position in the assigned structure.

**Mitigation**

No casting assignment of released structures to field symbols.

## RFC

Passing released structures to remote RFMs.

**Possible Problems**

Deep components are not supported in RFC.

**Mitigation**

No passing of released structures to remote RFMs.

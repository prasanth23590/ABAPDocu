---
title: "sorted key"
source_file: abensorted_key_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sorted key

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Unique or non-unique [table key](abentable_key_glosry.md) of an [internal table](abeninternal_table_glosry.md), in which the assignment to the table lines is managed using a [table index](abentable_index_glosry.md), the key entries of which are sorted in ascending order. A sorted key is the [primary table key](abenprimary_table_key_glosry.md) of a [sorted table](abensorted_table_glosry.md) and can be assigned to all internal tables as a [secondary table key](abensecondary_table_key_glosry.md). Sorting occurs according to the [comparison rules](../abap-programming-language/abap-program-flow-logic/abenlogexp_rules.md) for the data types of the key fields. When an internal table is accessed using a sorted key, the response time logarithmically depends on the number of table entries because the table is accessed using a binary search.

---
title: "table index"
source_file: abentable_index_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table index

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

An [index](abenindex_glosry.md) of an [internal table](abeninternal_table_glosry.md) managed by the [ABAP runtime framework](abenabap_runtime_frmwk_glosry.md). A [primary table index](abenprimary_table_index_glosry.md) is used for [index tables](abenindex_table_glosry.md) and [secondary table indexes](abensecondary_table_index_glosry.md) are used for the management of [sorted](abensorted_key_glosry.md) [secondary table keys](abensecondary_table_index_glosry.md). The line numbers of every table index start at 1 and run consecutively with no gaps up to the current number of lines in the table. If necessary, the physical index is changed to a logical index, which increases runtime demand. The logical index is created in exactly the moment in which a line is inserted before another line, the order of the table lines is changed, or if any line except for the bottom line is deleted.

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenitab_access.md)

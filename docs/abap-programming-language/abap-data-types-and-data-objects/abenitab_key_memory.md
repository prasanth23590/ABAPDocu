---
title: "itab - Line-Based Administration Costs"
source_file: abenitab_key_memory.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Line-Based Administration Costs

In addition to the basic memory requirement specified in [Memory Requirement for Deep Data Objects](abenmemory_consumption_1.md), which is created to administrate internal tables in table headers, additional memory is required for administrating each individual line, so allowing optimized access to the individual lines. This internal administration of individual lines has two variants:

- A [table index](../../abap-glossary/abentable_index_glosry.md) administrates the logical order of table lines. The additional memory requirement is 6 bytes per table line on average. **Exception:** If the logical order matches the physical order in the table body, no additional memory is required for the index.

- [Hash administration](../../abap-glossary/abenhash_algorithm_glosry.md) is used to access table lines to be accessed by hashing the associated key components. The additional memory requirement is 18 bytes per table line on average, as long as the table is not accessed using the [`DELETE`](../abap-processing-internal-data/abapdelete_itab.md) or [`SORT`](../abap-processing-internal-data/abapsort_itab.md) statements. Following this type of access, an average of 30 bytes is required per table line.

How a table line is administrated depends on the [table category](../../abap-glossary/abentable_category_glosry.md) and any existing [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). The table category determines the basic administration of the lines of an internal table (table index for [index tables](../../abap-glossary/abenindex_table_glosry.md), hash administration for [hashed tables](../../abap-glossary/abenhashed_table_glosry.md)). Each additional secondary table key introduces additional line administration (table index for [sorted keys](../../abap-glossary/abensorted_key_glosry.md), hash administration for [hash keys](../../abap-glossary/abenhash_key_glosry.md)).

Indexes are therefore created in the following cases:

- As the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) of a [standard table](../../abap-glossary/abenstandard_table_glosry.md) for managing the order created by index operations. However, the order in the index has no relation to the content of the table lines. The index is only for the optimization of index accesses. Content searches cannot be optimized and always lead to a linear search across all table lines.

- As the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) of a sorted table or as the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) of a sorted secondary table of any table for managing the order of table lines in accordance with the sorted primary or secondary table key. The order of table lines is determined by the view of the table lines defined by the sorted table keys. This defines an order for the lines of the table that can be used for optimized access by the binary search.

Hash administrations are created in the following cases:

- For the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of a hashed table or for a secondary [hash key](../../abap-glossary/abenhash_key_glosry.md) of any other table. They do not allow index access. They can only be used for optimized access with a completely specified table key.

If secondary table keys are used, additional memory costs may be incurred.

- An internal table with at least one ambiguous sorted secondary key needs an additional 8 bytes per table line for the basic costs to administrate possible duplicates. These additional basic costs are incurred only once and not for each table key.

- Additional memory costs are incurred if a secondary key must be updated following a change to the content of the internal table. These vary in size from a few bytes per table line and depend heavily on the number of changes made.

---
title: "itab - Initial Memory Requirement"
source_file: abenitab_initial_mem_req.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Initial Memory Requirement

The initial memory requirement is a type property of a [table type](../../abap-glossary/abentable_type_glosry.md) that is not part of its [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) and does not affect its compatibility to other table types.

As for all dynamic data objects, [memory](abenmemory_consumption_1.md) is requested for internal tables by inserting content. The data of an internal table is stored in the memory in blocks and the memory is requested block by block. The first block is allocated in the memory even before the table is filled with lines. This block is called the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) of an internal table

If the initial memory requirement becomes insufficient for adding more lines, further blocks are created using an internal duplication strategy until a threshold is reached. After this, all blocks are requested with a constant size between eight and 16 kilobytes.

The size of the internal memory requirement can be affected by addition [`INITIAL SIZE`](../abap-declarations/abaptypes_itab.md). Normally, this is not necessary, but can make sense for nested internal tables.

When an internal table is initialized with [`CLEAR`](../abap-processing-internal-data/abapclear.md), the initial memory requirement is not released. When an internal table is initialized with [`FREE`](../abap-processing-internal-data/abapfree_dataobject.md), the initial memory requirement is released. The latter is necessary only in case of memory bottlenecks. Normally, performance is improved by reusing the allocated memory when refilling the internal table.

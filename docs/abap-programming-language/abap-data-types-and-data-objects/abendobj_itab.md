---
title: "Internal Tables"
source_file: abendobj_itab.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Internal Tables

Internal tables provide a means of taking variable data from a fixed structure and storing it in the working memory in ABAP. An internal table is a data object that contains any lines with any data type whose total is not defined statically. The data type of an internal table is a table type. As well as the line type, the table type also defines the [table category](../../abap-glossary/abentable_category_glosry.md) and the [table key](../../abap-glossary/abentable_key_glosry.md).

Internal tables offer dynamic arrays and remove the task of program-driven dynamic memory management from the programmer (see [Memory Consumption of Deep Data Objects](abenmemory_consumption.md)). A particularly important application for internal tables is for storing and formatting data from a database table within a program. In conjunction with [structures](abendata_objects_structure.md), they are also the best way of defining complicated data structures in an ABAP program.

- [itab - Table Type](abenitab_data_type.md)

- [itab - Selection of the Table Category](abenitab_cat.md)

- [itab - Table Key](abenitab_key.md)

- [itab - Accessing Internal Tables](abenitab_access.md)

- [itab - Initial Memory Requirement](abenitab_initial_mem_req.md)

- [itab - Line-Based Administration Costs](abenitab_key_memory.md)

## Hints

- For information about the maximum size of an internal table, see [Maximum Size of Dynamic Data Objects](abenmemory_consumption_2.md).

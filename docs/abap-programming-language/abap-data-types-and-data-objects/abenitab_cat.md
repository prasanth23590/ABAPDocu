---
title: "itab - Selection of the Table Category"
source_file: abenitab_cat.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Selection of the Table Category

What category of table should be used in an individual case depends on the type of individual line access that will be used most frequently on the table. These rules are made suitably relative to tables with [secondary keys](../../abap-glossary/abensecondary_table_key_glosry.md).

- **Standard Tables**

  This table category is appropriate when the individual entries can be accessed using the [index](../../abap-glossary/abenindex_glosry.md). Access using the index is the fastest possible access to table entries. Standard tables should be filled by appending lines using [`APPEND`](../abap-processing-internal-data/abapappend.md) and implement other accesses using an index specification (`INDEX` addition of the respective statements). Since the cost of accesses to standard tables using the primary key increases linearly with the number of table entries, this type of access should only be used on standard tables if the filling of the table can be separated from the rest of the processing. If a standard table is sorted after filling, the cost of a key access with a binary search ([`BINARY SEARCH`](../abap-processing-internal-data/abapread_table_free.md)) only depends logarithmically on the number of table entries.

- **Sorted Tables**

  This table category is appropriate if the table must already be sorted at the time it is constructed. The filling of the table takes place by insertion using the [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) statement and in accordance with the sort order defined by the primary table key. The cost of key accesses depends logarithmically on the number of table entries because a binary search is performed automatically. Sorted tables are also particularly suited for partially sequential processing in a [`LOOP`](../abap-processing-internal-data/abaploop_at_itab.md), if initial parts of the table key are specified in the `WHERE` condition.

- **Hashed Tables**

  This table category is suitable when key accesses are the central operation on table entries. Hashed tables cannot be accessed using a primary table index. However, the cost per key access is always constant and independent of the number of table entries. As with database tables, the key of hashed tables is always unique. Therefore, hashed tables are suitable for creating database-like internal tables and using them accordingly.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A table `scarr_tab_down` intended for index access should be sorted by key field in descending order. This can only be a standard table. To sort in ascending order, a sorted table can and should be used, in this case `scarr_tab_up`. If only key access is required, then a hashed table like `scarr_tab_key` can be used.

``` abap
DATA scarr_tab_down 
  TYPE STANDARD TABLE OF scarr 
       WITH NON-UNIQUE KEY carrid. 
 
DATA scarr_tab_up 
  TYPE SORTED TABLE OF scarr 
       WITH UNIQUE KEY carrid. 
 
DATA scarr_tab_key 
  TYPE HASHED TABLE OF scarr 
       WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       ORDER BY carrid DESCENDING 
       INTO TABLE @scarr_tab_down. 
 
scarr_tab_up = scarr_tab_down. 
 
scarr_tab_key = scarr_tab_up. 
 
cl_demo_output=>new( 
 )->write( scarr_tab_down[ 1 ] 
 )->write( scarr_tab_up[ 1 ] 
 )->write( scarr_tab_key[ carrid = 'UA' ] 
 )->display( ).
```

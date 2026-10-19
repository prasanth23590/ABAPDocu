---
title: "itab - Duplicate Unique Keys"
source_file: abenitab_key_duplicates.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Duplicate Unique Keys

When lines are inserted into internal tables with a unique primary key or unique secondary key, duplicates can occur with respect to one or more of these keys. Depending on whether the insertion is a single record operation or a mass operation, the ABAP runtime framework reacts as follows to an attempt to insert an entry with duplicate key values:

- First, it checks whether duplicate key values would occur with respect to the primary key. The system behavior is as follows depending on the operation:

  - When single lines are inserted using the variant

    [`INSERT wa INTO TABLE itab`](../abap-processing-internal-data/abapinsert_itab_position.md) duplicate entries with respect to the primary key are ignored and `sy-subrc` is set to 4. This is often used to filter out duplicates when the table is constructed.

  - In all other cases, such as

    [`INSERT ... INTO itab INDEX idx`](../abap-processing-internal-data/abapinsert_itab_position.md)

    [`INSERT LINES OF`](../abap-processing-internal-data/abapinsert_itab_linespec.md) (bulk operation)

    [`APPEND`](../abap-processing-internal-data/abapappend.md)

    [`COLLECT`](../abap-processing-internal-data/abapcollect.md)

    [`=`](../abap-processing-internal-data/abapmove.md), [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md) (bulk operations) the runtime error `ITAB_DUPLICATE_KEY` occurs.

- A check is then made to see whether duplicate key values would occur with respect to any existing unique secondary keys. If this is the case,

  - an exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised for the statements [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) and [`APPEND`](../abap-processing-internal-data/abapappend.md) if the operation is a single record operation.

  - For all other insert and assignment operations, particularly for all mass operations, the runtime error `ITAB_DUPLICATE_KEY` occurs.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first `INSERT` statement does not insert a line and sets `sy-subrc` to the value 4. The second `INSERT` statement produces a runtime error.

``` abap
DATA itab TYPE SORTED TABLE OF i WITH UNIQUE KEY table_line. 
 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
 
INSERT 2 INTO TABLE itab. 
 
INSERT 2 INTO itab INDEX 2.
```

---
title: "itab - Duplicate Non-Unique Keys"
source_file: abenitab_key_secondary_duplicates.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Duplicate Non-Unique Keys

Non-unique table keys can produce duplicate lines with respect to these keys. This section describes the order of these duplicates when inserting into tables with non-unique sorted table keys. This order is ignored with respect to non-unique primary keys in standard tables.

- [Single Record Operations](abenitab_key_secondary_duplicates.md#single-record-operations)

- [Block Operations](abenitab_key_secondary_duplicates.md#block-operations)

- [Special Features](abenitab_key_secondary_duplicates.md#special-features)

## Single Record Operations

When individual lines are inserted where the insert position is determined using a table key, that is, in the case of

- the operations [`INSERT ... INTO TABLE ...`](../abap-processing-internal-data/abapinsert_itab_position.md) or

- in [lazy updates](../../abap-glossary/abenlazy_update_glosry.md) of sorted secondary keys

the order of the duplicates with respect to the table key of the target table is determined in accordance with the insertion order of the individual lines. The duplicate line that was last inserted into the table is sorted before all other duplicates.

## Block Operations

For block operations such as an [assignment](../abap-processing-internal-data/abapmove.md) of an internal table to another table or when inserting multiple lines using [`INSERT LINES OF`](../abap-processing-internal-data/abapinsert_itab_linespec.md), the order of duplicates with respect to a sorted key of the target table in the block is taken from the source table. If there are already one or more duplicates in the target table, the source block duplicates are inserted in their original order in front of the first duplicate in the target table.

## Special Features

Some operations have the characteristics of block operations but are executed internally as sequences of single record operations. In this case, the original order of duplicates with respect to a sorted key in the target table is not retained. This is the case for the following operations:

- Filling an internal table using [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md) from a table previously stored using [`EXPORT`](../abap-data-cluster/abapexport_data_cluster.md) and all operations that are based internally on such an import, such as posting operations.

- The deserialization of an internal table from a table previously serialized to XML using [`CALL TRANSFORMATION`](../abap-data-interchange-formats/abapcall_transformation.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following insertion is

``` abap
a a 
b z 
b y 
b x 
b b
```abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE string, 
    col2 TYPE string, 
  END OF line, 
  itab TYPE SORTED TABLE OF line 
            WITH NON-UNIQUE KEY col1. 
 
DATA(itab) = VALUE itab( 
 ( col1 = 'b' col2 = 'b' ) 
 ( col1 = 'a' col2 = 'a' ) ). 
 
FINAL(jtab) = VALUE itab( 
 ( col1 = 'b' col2 = 'x' ) 
 ( col1 = 'b' col2 = 'y' ) 
 ( col1 = 'b' col2 = 'z' ) ). 
 
INSERT LINES OF jtab INTO TABLE itab. 
 
cl_demo_output=>display( itab ).
```

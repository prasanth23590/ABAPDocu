---
title: "REPLACE IN TABLE, table_range"
source_file: abapreplace_table_range.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > REPLACE IN TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE IN TABLE, table_range

## Syntax

``` abap
... [FROM lin1 [OFFSET off1]] 
    [TO   lin2 [OFFSET off2]] ...  
```

## Description

This addition restricts the search performed by the statement [`REPLACE IN TABLE`](abapreplace_itab.md) on the table section specified in the [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) `lin1`, `off1`, `lin2`, and `off2`. The syntax and semantics are the same as for the statement [`FIND`](abapfind_table_range.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacement creates the result shown below. It should be noted that the `OFFSET` addition of `TO` defines the end of the replacement range.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 5, 
    col2 TYPE c LENGTH 5, 
  END OF line, 
  itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
DATA(itab) = VALUE itab( FOR i = 1 UNTIL i > 5 
                       ( col1 = 'abcde' col2 = 'abcde' ) ). 
 
REPLACE ALL OCCURRENCES OF `cd` 
        IN TABLE itab 
        FROM 2 OFFSET 5 
        TO   4 OFFSET 5 
        WITH 'XX'. 
 
out->write( itab ). 
 
out->display( ).
```

Result:

| **col1** | **col2** |
|----------|----------|
| `abcde`  | `abcde`  |
| `abcde`  | `abXXe`  |
| `abXXe`  | `abXXe`  |
| `abXXe`  | `abcde`  |
| `abcde`  | `abcde`  |

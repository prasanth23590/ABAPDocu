---
title: "DELETE itab, itab_line"
source_file: abapdelete_itab_line.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE itab, itab_line

## Syntax

``` abap
... { table_key  | index }.  
```

[`table_key`](abapdelete_itab_key.md) · [`index`](abapdelete_itab_index.md)

## Description

In this variant, the statement `DELETE` deletes a line specified by a table key in [`table_key`](abapdelete_itab_key.md) or a line specified by a line number [`index`](abapdelete_itab_index.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of individual lines in an internal table. The first `DELETE` statement uses the primary table key to find the line. The second `DELETE` statement deletes the line by specifying a line number, which is also determined here by accessing a key.

``` abap
DATA itab TYPE SORTED TABLE OF string 
          WITH UNIQUE KEY primary_key COMPONENTS table_line. 
 
itab = VALUE #( ( `X` ) ( `Y` ) ( `Z` ) ). 
 
DELETE TABLE itab WITH TABLE KEY 
  primary_key COMPONENTS table_line = `X`. 
 
DELETE itab INDEX 
  line_index( itab[ KEY primary_key table_line = `Z` ] ).
```

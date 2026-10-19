---
title: "REPLACE IN TABLE, options"
source_file: abapreplace_itab_options.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > REPLACE IN TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE IN TABLE, options

## Syntax

``` abap
... [VERBATIM]   
    [RESPECTING|IGNORING CASE]   
    [REPLACEMENT COUNT rcnt]   
    { {[REPLACEMENT LINE rlin]   
       [REPLACEMENT OFFSET roff]   
       [REPLACEMENT LENGTH rlen]}   
    | [RESULTS result_tab|result_wa] } ...  
```

## Description

The addition `REPLACEMENT LINE` returns the last line number in which the search pattern was found using the statement [`REPLACE IN TABLE`](abapreplace_itab.md) in `rlin`. The following can be specified for `rlin`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If no replacement is made, `rlin` retains its existing value or remains initial.

The remaining additions used for making replacements in individual table lines have the same [meaning](abapreplace_options.md) as pattern-based replacements made using [`REPLACE`](abapreplace_in_pattern.md) in elementary character strings or byte strings.

When the `RESULTS` addition is used, the line numbers of each occurrence in the component `LINE` of the table line in `result_tab` or the line number of the last occurrence are stored in `result_wa`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example performs the same replacement as the [replacement range](abapreplace_table_range.md) example. Here, the positions of the replaced occurrences are returned.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF result, 
    line   TYPE i, 
    offset TYPE i, 
    length TYPE i, 
  END OF result, 
  result_tab TYPE TABLE OF result WITH EMPTY KEY. 
 
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
        WITH 'XX' 
        RESULTS FINAL(results). 
 
out->write( CORRESPONDING result_tab( results ) ). 
 
out->display( ).
```

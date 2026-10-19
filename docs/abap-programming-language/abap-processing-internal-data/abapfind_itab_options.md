---
title: "FIND IN TABLE, options"
source_file: abapfind_itab_options.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > FIND IN TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND IN TABLE, options

## Syntax

``` abap
... [{RESPECTING|IGNORING} CASE] 
    [MATCH COUNT  mcnt] 
    { {[MATCH LINE   mlin] 
       [MATCH OFFSET moff] 
       [MATCH LENGTH mlen]} 
    | [RESULTS result_tab|result_wa] } 
    [SUBMATCHES s1 s2 ...] ...  
```

## Description

The addition `MATCH LINE` returns the number of the line in which the last substring was found using [`FIND IN TABLE`](abapfind_itab.md) in data object `mlin`. The following can be specified for `mlin`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If the substring is not found, `mlin` retains its previous value or stays initial.

The remaining additions used for searching in the individual table lines have the same [meaning](abapfind_options.md) as in the statement [`FIND`](abapfind.md) for elementary character strings and byte strings.

If the addition `RESULTS` is used, the line numbers of each occurrence in the component `LINE` of the table line in question in `result_tab` or the line number of the last occurrence are also saved to `result_wa` and the lines in `result_tab` are sorted by the columns `LINE`, `OFFSET`, and `LENGTH`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a text into an internal table in `ITF` format and search for all strings *ABAP* and *XML*. The table returned contains the positions of the occurrences. The line type of the internal table is interpreted as a single field of the type `c` despite being a structured type.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF result, 
    line   TYPE i, 
    offset TYPE i, 
    length TYPE i, 
  END OF result, 
  result_tab TYPE TABLE OF result WITH EMPTY KEY. 
 
DATA itf_tab TYPE tline_tab. 
IF cl_abap_docu_itf=>get_docu( EXPORTING id = 'SD' 
                                         object = 'ABENABAP_XML' 
                               IMPORTING itf = itf_tab ) = 0. 
 
  FIND ALL OCCURRENCES OF PCRE 'ABAP|XML' 
       IN TABLE itf_tab 
       RESPECTING CASE 
       RESULTS FINAL(results). 
 
  IF sy-subrc = 0. 
    out->write( CORRESPONDING result_tab( results ) ). 
  ENDIF. 
ENDIF. 
 
out->display( ).
```

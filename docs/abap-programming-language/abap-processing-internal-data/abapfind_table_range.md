---
title: "FIND IN TABLE, table_range"
source_file: abapfind_table_range.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > FIND IN TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND IN TABLE, table_range

## Syntax

``` abap
... [FROM lin1 [OFFSET off1]] 
    [TO   lin2 [OFFSET off2]] ...  
```

## Description

This addition limits the search in the statement [`FIND IN TABLE`](abapfind_itab.md) to the table range specified in `lin1`, `off1`, `lin2` and `off2`. Without this addition, the program searches the entire table line by line. `lin1`, `off1`, `lin2` and `off2` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`.

The table range begins in line `lin1` after the [offset](../../abap-glossary/abenoffset_glosry.md) `off1`, and ends in line `lin2` in front of the offset `off2`. If `FROM` is specified without ` OFFSET`, the range implicitly begins at the start of `lin1`. If `TO` is specified without `OFFSET`, the range ends implicitly at the end of line `lin2`.

The value of `lin1` must be greater than or equal to 1, and the value of `lin2` must be greater than or equal to the value of `lin1`, and both must refer to valid table lines. The values of `off1` and `off2` must be greater than or equal to 0 and be within the respective line length. If `lin1` and `lin2` refer to the same line, the value of `off2` must be greater than or equal to the value of `off1`. Both offsets may refer to the end of the line.

## Hint

This addition is also used in the statement [`REPLACE IN TABLE`](abapreplace_itab.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a text into an internal table in `ITF` format and search for the first string *AS* in a non-case-sensitive search. The line type of the internal table is interpreted as a single field of the type `c` despite being a structured type. The first search finds the first paragraph format *AS* in the column `tdformat`. The second search is limited to the lines of the first paragraph and finds the word `as` in the column `tdline`, if it exists here. By specifying the offset, the paragraph format is not found in the first line of the paragraph.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itf_tab TYPE tline_tab. 
IF cl_abap_docu_itf=>get_docu( EXPORTING id = 'SD' 
                                         object = 'ABENABAP_XML' 
                               IMPORTING itf = itf_tab ) = 0. 
  DELETE itf_tab FROM 18. 
  out->write( itf_tab ). 
 
  FIND FIRST OCCURRENCE OF SUBSTRING 'as' 
       IN TABLE itf_tab 
       IGNORING CASE 
       MATCH LINE DATA(mline) 
       MATCH OFFSET DATA(moff) 
       MATCH LENGTH DATA(mlen). 
  IF sy-subrc = 0. 
    out->write( |{ mline }, { moff }, { mlen }| ). 
  ENDIF. 
 
  DATA: 
    idx1 TYPE i, 
    idx2 TYPE i. 
  LOOP AT itf_tab TRANSPORTING NO FIELDS WHERE tdformat = 'AS'. 
    idx2 = COND i( WHEN idx1 IS NOT INITIAL THEN sy-tabix ). 
    IF idx2 IS NOT INITIAL. 
      EXIT. 
    ENDIF. 
    idx1 = COND i( WHEN idx1 IS INITIAL THEN sy-tabix ). 
  ENDLOOP. 
 
  FIND FIRST OCCURRENCE OF SUBSTRING 'as' 
       IN TABLE itf_tab 
       FROM idx1 OFFSET 2 TO idx2 - 1 
       IGNORING CASE 
       MATCH LINE mline 
       MATCH OFFSET moff 
       MATCH LENGTH mlen. 
  IF sy-subrc = 0. 
    out->write( |{ mline }, { moff }, { mlen }| ). 
  ENDIF. 
 
ENDIF. 
 
out->display( ).
```

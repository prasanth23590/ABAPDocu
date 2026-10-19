---
title: "LOOP AT itab, result"
source_file: abaploop_at_itab_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, result

## Syntax

``` abap
... { INTO wa }   
  | { ASSIGNING <fs> [CASTING] [ELSE UNASSIGN] }   
  | { REFERENCE INTO dref }   
  | { TRANSPORTING NO FIELDS } ...  
```

## Description

Defines the output behavior of a [`LOOP`](abaploop_at_itab.md) across an internal table. There are four alternatives for the output behavior:

- The addition `INTO` is used to assign the content of the current line to a work area `wa`.

- The addition `ASSIGNING` is used to assign the current line to a field symbol `<fs>`. No other memory area can be assigned to the field symbol within the loop and the assignment cannot be undone using [`UNASSIGN`](abapunassign.md).

- The addition `REFERENCE INTO` is used to create a reference to the current line in a reference variable. No other reference can be assigned to the reference variable within the loop and the reference variable cannot be initialized using [`CLEAR`](abapclear.md).

- The addition `TRANSPORTING NO FIELDS` specifies that only the relevant system fields are filled. This addition is only possible if the addition `WHERE` is used in the conditions [`cond`](abaploop_at_itab_cond.md) at the same time and if the addition [`GROUP BY`](abaploop_at_itab_group_by.md) is not used.

If the internal table `itab` is specified as an existing data object, the syntax and meaning of the specified [output behavior](abapread_table_outdesc.md) is the same as in the statement [`READ TABLE`](abapread_table.md), with the exception that no further [`transport_options`](abapread_table_transport_options.md) can be specified after `INTO wa`, and the same restrictions apply to modifications of key fields of the [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In particular, inline declarations for the work area, the field symbol, or the reference variable using the declaration operators [`DATA`](../abap-declarations/abendata_inline.md), [`FINAL`](../abap-declarations/abenfinal_inline.md), and [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md) are possible. The addition `ELSE UNASSIGN` sets the state of the field symbol behind `ASSIGNING` to unassigned if no loop pass was executed and `sy-subrc` is set to 4.

If a field symbol or a dereferenced reference variable is specified for the work area `wa` or the reference variable `dref`, the target data object of the field symbol or reference variable is determined in each loop pass. The current data object is used as the target area for each loop pass. This means that changes in the assignment of the field symbol or reference variable within the loop modify the target area.

If the internal table is specified as the return value of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md), a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md), or a [table expression](../../abap-glossary/abentable_expression_glosry.md), the additions `ASSIGNING` and `REFERENCE INTO` can also be specified for `LOOP`, unlike in `READ TABLE`. The internal table is only available while the loop is being processed, which means that all field symbols and reference variables that point to lines in the internal table become invalid when the loop is exited.

## Hints

- If the current line is deleted within the loop when the additions `ASSIGNING` or `REFERENCE` are used, the field symbol or reference variable is not assigned or unbound in the current loop pass afterwards.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Two `LOOP` loops are used to determine the line numbers for numbers greater than or equal to 40 and less than or equal to 60 in a sorted table of random numbers, and the addition `TRANSPORTING NO FIELDS` is used. Then, `INTO` is used to read these lines to a variable `number`. Filling the `output` table in this way demonstrates the use of `number`. It could also be done using [`INSERT LINES OF`](abapinsert_itab_linespec.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                        min  = 1 
                                        max  = 100 ). 
 
DATA itab TYPE SORTED TABLE OF i WITH NON-UNIQUE KEY table_line. 
itab = VALUE #( FOR i = 1 UNTIL i > 100 ( rnd->get_next( ) ) ). 
 
LOOP AT itab TRANSPORTING NO FIELDS WHERE table_line >= 40. 
  FINAL(idx1) = sy-tabix. 
  EXIT. 
ENDLOOP. 
 
LOOP AT itab FROM idx1 TRANSPORTING NO FIELDS WHERE table_line > 60. 
  FINAL(idx2) = sy-tabix - 1. 
  EXIT. 
ENDLOOP. 
 
DATA output TYPE TABLE OF i WITH EMPTY KEY. 
LOOP AT itab FROM idx1 TO idx2 INTO FINAL(number). 
  output = VALUE #( BASE output ( number ) ). 
ENDLOOP. 
out->write( output ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Loop across an internal table containing dates. The table lines are assigned to a structured field symbol with a corresponding casting.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF date, 
    year  TYPE c LENGTH 4, 
    month TYPE c LENGTH 2, 
    day   TYPE c LENGTH 2, 
  END OF date. 
 
DATA itab TYPE SORTED TABLE OF d WITH UNIQUE KEY table_line. 
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
itab = VALUE #( FOR i = - 3 UNTIL i > 3 ( date + i ) ). 
 
DATA output TYPE TABLE OF date WITH EMPTY KEY. 
FIELD-SYMBOLS <date> TYPE date. 
LOOP AT itab ASSIGNING <date> CASTING ELSE UNASSIGN. 
  output = VALUE #( BASE output ( <date> ) ). 
ENDLOOP. 
IF <date> IS ASSIGNED. 
  out->write( output ). 
ENDIF. 
 
out->display( ).
```

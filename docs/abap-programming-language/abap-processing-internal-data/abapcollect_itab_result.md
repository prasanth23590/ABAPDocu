---
title: "COLLECT, result"
source_file: abapcollect_itab_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > COLLECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COLLECT, result

## Syntax

``` abap
... { ASSIGNING <fs> [CASTING] }   
  | { REFERENCE INTO dref }.  
```

## Description

The addition `ASSIGNING` is used to assign the inserted or existing line to a field symbol `<fs>` and the addition `REFERENCE INTO` is used to set a reference to the line in a reference variable.

The syntax and meaning are the same as when specifying the output behavior in the statement [`READ TABLE`](abapread_table_outdesc.md) with the exception that the addition `ELSE UNASSIGN` cannot be used. The same restrictions apply regarding the modification of key fields for [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In particular, inline declarations using the declaration operators [`DATA`](../abap-declarations/abendata_inline.md), [`FINAL`](../abap-declarations/abenfinal_inline.md) and [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md) are possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `COLLECT` is executed until the column `num` reaches the value 100 for one of the three possible key values.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    key TYPE c LENGTH 1, 
    num TYPE i, 
  END OF line. 
DATA 
  itab TYPE SORTED TABLE OF line 
            WITH UNIQUE KEY key. 
DATA(t) = CONV i( cl_demo_date_time=>get_utc_time( ) ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = t 
                                        min  = 1 
                                        max  = 3 ). 
 
DO. 
  COLLECT VALUE line( key = COND #( LET r = rnd->get_next( ) IN 
                                    WHEN r = 1 THEN 'X' 
                                    WHEN r = 2 THEN 'Y' 
                                    WHEN r = 3 THEN 'Z' ) 
                      num = 1 ) INTO itab 
          ASSIGNING FIELD-SYMBOL(<fs>). 
  IF <fs>-num = 100. 
    EXIT. 
  ENDIF. 
ENDDO. 
 
out->write( itab ). 
 
out->display( ).
```

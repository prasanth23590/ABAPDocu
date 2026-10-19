---
title: "APPEND, result"
source_file: abapappend_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > APPEND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# APPEND, result

## Syntax

``` abap
... { ASSIGNING <fs> [CASTING]}   
  | { REFERENCE INTO dref }.  
```

## Description

These additions can only be used when appending single lines. If the append was successful, the addition `ASSIGNING` is used to assign the appended line to a field symbol `<fs>`; the addition `REFERENCE INTO` is used to set a reference to the appended line in a reference variable.

The syntax and meaning are the same as when specifying the output behavior in the statement [`READ TABLE`](abapread_table_outdesc.md) with the exception that the addition `ELSE UNASSIGN` cannot be used. The same restrictions apply regarding the modification of key fields for [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In particular, inline declarations using the declaration operators [`DATA`](../abap-declarations/abendata_inline.md), [`FINAL`](../abap-declarations/abenfinal_inline.md) and [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md) are possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Append two lines to an internal table and assign a field symbol to the first line and set a reference in the second line.

``` abap
DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
 
APPEND `First line`  TO itab ASSIGNING FIELD-SYMBOL(<fs>). 
APPEND `Second line` TO itab REFERENCE INTO FINAL(dref). 
 
cl_demo_output=>new( 
  )->write( <fs> 
  )->write( dref->* 
  )->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the `DO` loop, the data references in `stab` point to the random numbers up to 50 and those in `ltab` point to the random numbers greater than 50 that were appended to `itab`.

``` abap
DATA: 
  itab TYPE TABLE OF i WITH EMPTY KEY, 
  stab TYPE TABLE OF REF TO i WITH EMPTY KEY, 
  ltab TYPE TABLE OF REF TO i WITH EMPTY KEY. 
 
FINAL(rnd) = 
  cl_abap_random_int=>create( 
    seed =  CONV #( cl_demo_date_time=>get_utc_time( ) ) 
    min  = 1 
    max  = 100 ). 
 
DO 100 TIMES. 
  APPEND rnd->get_next( ) TO itab REFERENCE INTO FINAL(dref). 
  IF dref->* <= 50. 
    APPEND dref TO stab. 
  ELSE. 
    APPEND dref TO ltab. 
  ENDIF. 
ENDDO.
```

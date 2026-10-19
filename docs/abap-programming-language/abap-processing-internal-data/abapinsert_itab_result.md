---
title: "INSERT, result"
source_file: abapinsert_itab_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > INSERT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, result

## Syntax

``` abap
... { ASSIGNING <fs> [CASTING] [ELSE UNASSIGN] }   
  | { REFERENCE INTO dref }.  
```

## Description

These additions can only be used when inserting single lines. If the insertion is successful, the addition `ASSIGNING` is used to assign the inserted line to a field symbol `<fs>` or the addition `REFERENCE INTO` is used to set a reference to the inserted line in a reference variable.

The syntax and meaning are the same as when specifying the output behavior in the statement [`READ TABLE`](abapread_table_outdesc.md) and the same restrictions apply regarding the modification of key fields for [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In particular, inline declarations using the declaration operators [`DATA`](../abap-declarations/abendata_inline.md), [`FINAL`](../abap-declarations/abenfinal_inline.md) and [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md) are possible. The addition `ELSE UNASSIGN` sets the state of the field symbol behind `ASSIGNING` to unassigned if the insertion was not successful and `sy-subrc` is set to 4. Otherwise, the field symbol keeps its previous state.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See addition [`INITIAL LINE`](abapinsert_itab_linespec.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the `DO` loop, the internal table `ref_tab` contains references to each line of the internal table `itab`.

``` abap
DATA: 
  itab    TYPE SORTED TABLE OF string WITH UNIQUE KEY table_line, 
  ref_tab TYPE STANDARD TABLE OF REF TO string. 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
DO strlen( abcde ) TIMES. 
  INSERT substring( val = abcde off = sy-index - 1 len = 1 ) 
         INTO TABLE itab 
         REFERENCE INTO FINAL(dref). 
  APPEND dref TO ref_tab. 
ENDDO.
```

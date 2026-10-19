---
title: "MODIFY itab, result"
source_file: abapmodify_itab_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab > MODIFY itab, itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab, result

## Syntax

``` abap
... { ASSIGNING <fs> [CASTING] [ELSE UNASSIGN]}   
  | { REFERENCE INTO dref }.  
```

## Description

These additions are possible only when modifying [single lines](abapmodify_itab_single.md). If modified successfully, the addition `ASSIGNING` is used to assign the line to a field symbol and the addition `REFERENCE INTO` is used to set a reference to the modified line in a reference variable.

The syntax and meaning are the same as when specifying the output behavior in the statement [`READ TABLE`](abapread_table_outdesc.md) and the same restrictions apply regarding the modification of key fields for [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In particular, inline declarations using the declaration operators [`DATA`](../abap-declarations/abendata_inline.md), [`FINAL`](../abap-declarations/abenfinal_inline.md) and [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md) are possible. The addition `ELSE UNASSIGN` sets the state of the field symbol behind `ASSIGNING` to unassigned if the modification was not successful and `sy-subrc` is set to 4. Otherwise, the field symbol keeps its previous state.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of smoking seats to non-smoking seats in an internal table of flight bookings. After the loop, each line in the reference table `reftab` references a line in `itab` in which a change took place.

``` abap
DATA itab TYPE HASHED TABLE OF sbook 
          WITH UNIQUE KEY carrid connid fldate bookid. 
 
SELECT * 
       FROM sbook 
       INTO TABLE @itab. 
 
DATA reftab TYPE TABLE OF REF TO sbook WITH EMPTY KEY. 
LOOP AT itab INTO DATA(line) WHERE smoker = 'X'. 
  CLEAR line-smoker. 
  MODIFY TABLE itab FROM line TRANSPORTING smoker 
                    REFERENCE INTO FINAL(dref). 
  APPEND dref TO reftab. 
ENDLOOP.
```

---
title: "SHIFT, deleting"
source_file: abapshift_deleting.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > SHIFT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SHIFT, deleting

## Syntax

``` abap
... { {LEFT DELETING LEADING}   
    | {RIGHT DELETING TRAILING} } mask ...  
```

## Description

If these additions are used, the statement `SHIFT` shifts the content of `dobj` by one place to the left or the right as long as the content of the first or last place of `dobj` is contained in `mask`.

If the data object `dobj` is a string, it is truncated when it is shifted to the left but not lengthened when it is shifted to the right. This means the content of `mask` can also be moved out of a string to the right.

In character string processing, `mask` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). It is case-sensitive and any trailing blanks in `mask` are respected. If the content of the first or last place in `dobj` is not contained in `mask`, the content of `text` remains unchanged. In particular, nothing is shifted if `mask` is an empty string.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the shift to the right, `text` contains the value *\_\_\_\_\_I know you* and keeps its length of 15 characters.

``` abap
DATA text TYPE string VALUE `I know you know`. 
 
SHIFT text RIGHT DELETING TRAILING 'no kw'.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example removes first the trailing blank and then the leading blanks from a string. For strings without leading blanks, this sequence of statements can be used to remove trailing blanks.

``` abap
DATA txt TYPE string VALUE `XXXXX     `. 
 
SHIFT txt RIGHT DELETING TRAILING ` `. 
SHIFT txt LEFT  DELETING LEADING  ` `.
```

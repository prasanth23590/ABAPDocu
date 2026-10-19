---
title: "OVERLAY"
source_file: abapoverlay.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# OVERLAY

## Syntax

``` abap
OVERLAY text1 WITH text2 [ONLY mask].  
```

## Description

Characters in the variable `text1` are replaced by the characters in the operand `text2` that are in the same place there. `text2` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md).

If the addition `ONLY` is not specified, all blanks in `text1` are replaced. If the addition `ONLY` is specified, all characters are replaced that occur in the operand `mask`. This is case-sensitive. `mask` is also a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md).

If the lengths of `text1` and `text2` are different, `text1` is processed using the shorter length only.

The operands `text1`, `text2`, and `mask` must be character-like operands. In operands of fixed length, trailing blanks are respected. If `mask` is an empty string, no replacements are made.

## System Fields

| **`sy-subrc`** | **Meaning**                                          |
|----------------|------------------------------------------------------|
| 0              | At least one character in `text1` has been replaced. |
| 4              | No characters in `text1` have been replaced.         |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the `text` field has been assigned to the `time` field, it contains the invalid time *12\_\_00* due to the [conversion rules](abenconversion_type_c.md). As a result of the overlay with the `initial_time` constants, the two blanks are replaced by *00* and the result is the valid time *120000*.

``` abap
CONSTANTS initial_time TYPE t VALUE IS INITIAL. 
DATA: time TYPE t, 
      text TYPE c LENGTH 4. 
 
text = '12'. 
time = text. 
OVERLAY time WITH initial_time.
```

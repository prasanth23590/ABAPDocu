---
title: "TRANSLATE"
source_file: abaptranslate.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TRANSLATE

## Syntax

``` abap
TRANSLATE text {TO {UPPER|LOWER} CASE}   
             | {USING mask}.  
```

### Addition

[1. `... TO {UPPER|LOWER} CASE`](abaptranslate.md#addition-1)

[2. `... USING mask`](abaptranslate.md#addition-2)

## Overview

### Description

This statement translates the individual characters of the character-like variable `text`. Either `CASE` can be used to translate the case or `USING` can be used for a translation according to a pattern. The variable `text` must be a character-like variable.

## Addition 1

`... TO {UPPER|LOWER} CASE`

### Description

If `UPPER` is specified, all lowercase letters of the data object `text` are translated to uppercase. If `LOWER` is specified, all uppercase letters are translated to lowercase.

### Hint

To change the case of the letters in a character string in an operand position, a [case function](abencase_functions.md) can be used that includes the functions of the statement `TRANSLATE`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the translation, the variable `text` contains *CAREFUL WITH THAT AXE, EUGENE*.

``` abap
DATA text TYPE string. 
text = `Careful with that Axe, Eugene`. 
TRANSLATE text TO UPPER CASE.
```

## Addition 2

`... USING mask`

### Description

If `USING` is specified, the characters in `text` are translated in accordance with the rule specified in the data object `mask`. `mask` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) whose value is interpreted as a string of character pairs. Starting with the first pair, a search is performed in `text` for the first character in every pair and each occurrence is replaced with the second character of the pair. The search is case-sensitive. If `mask` contains a character multiple times as the first character of a pair, only the first pair is respected. A character in `text` that has already been replaced cannot be replaced again in the same `TRANSLATE` statement. Therefore, if the second character of a pair in `mask` is listed as the first character of a subsequent pair, the second pair affects only the original characters in `text`.

Trailing blanks in data objects `text` and `mask` are respected for data objects. If `mask` contains an odd number of characters, the last character is ignored. If `mask` is an empty string, no replacements are made.

### Hint

To translate a character string in an operand position, a [translate function](abentranslate_functions.md) that includes the functions of the statement `TRANSLATE` can also be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Translation of the characters *A* to *B*, *a* to *b* and back. After execution, `text` contains *Abracadabra*.

``` abap
DATA text TYPE string. 
text = `Barbcbdbarb`. 
TRANSLATE text USING 'ABBAabba'.
```

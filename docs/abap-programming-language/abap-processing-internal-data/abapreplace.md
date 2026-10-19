---
title: "REPLACE"
source_file: abapreplace.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE

## Syntax Forms

**[Pattern-Based Replacement](abapreplace_in_pattern.md)**

``` abap
1. REPLACE [{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF] pattern 
          IN [section_of] dobj WITH new 
          [IN {CHARACTER|BYTE} MODE] 
          [replace_options].
```

**[Position-Based Replacement](abapreplace_in_position.md)**

``` abap
2. REPLACE SECTION [OFFSET off] [LENGTH len] OF dobj WITH new 
                  [IN {CHARACTER|BYTE} MODE].
```

[`pattern`](abapreplace_pattern.md) · [`section_of`](abapfind_section_of.md) · [`replace_options`](abapreplace_options.md)

## Description

This statement replaces characters or bytes of the variable `dobj` with characters or bytes of the operand `new`, which is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). Here, a distinction is made between pattern-based and position-based replacements.

When the replacement is performed, an interim result without a length limit is created implicitly and passed to the data object `dobj`. If the length of the interim result is longer than the length of `dobj`, data objects of fixed length are truncated on the right. If the length of the interim result is shorter than the length of `dobj`, data objects of fixed length are padded on the right with blanks or hexadecimal zeros. Data objects of variable length are adjusted accordingly. If the interim result is truncated during the assignment, `sy-subrc` is set to 2.

In character string processing, the trailing blanks are respected for data objects `dobj` of fixed length. For `new` the closing blanks are ignored.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The simplest form of the statement `REPLACE`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `Hallo`. 
REPLACE `a` IN str WITH `e`. 
out->write( str ). 
 
out->display( ).
```

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | The search pattern or specified section was replaced by the content of `new` and the result is available in full in `dobj`.                          |
| 2              | The search pattern or specified section was replaced by the content of `new` in `dobj` and the result of the replacement was truncated on the right. |
| 4              | The search pattern in `pattern` was not found in `dobj` in the pattern-based search.                                                                 |

## Hints

- The statement [`REPLACE IN TABLE`](abapreplace_itab.md) can be used to make replacements in internal tables.

- To replace parts of a character string in an operand position, a [replace function](abenreplace_functions.md) can be used that includes some of the functions of the statement `REPLACE`.

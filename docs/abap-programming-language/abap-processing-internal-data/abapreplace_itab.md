---
title: "REPLACE IN TABLE itab"
source_file: abapreplace_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE IN TABLE itab

## Syntax

``` abap
REPLACE [{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF] pattern   
        IN TABLE itab [table_range] WITH new   
        [IN {CHARACTER|BYTE} MODE]   
        [replace_options].  
```

[`pattern`](abapreplace_pattern.md) · [`table_range`](abapreplace_table_range.md) · [`replace_options]`](abapreplace_itab_options.html)

## Description

The internal table `itab` is searched line-by-line for the character or byte strings specified by [`pattern`](abapreplace_pattern.md) and replaces any occurrences with the content of the operand `new`. `new` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md).

`itab` expects a standard table without [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). The lines in the table must be [character](../../abap-glossary/abencharlike_data_object_glosry.md)-like or [byte](../../abap-glossary/abenbyte_like_data_object_glosry.md)-like, depending on the addition `CHARACTER` or `BYTE MODE`. Byte or character strings that cover multiple table lines are not replaced.

The addition [`table_range`](abapreplace_table_range.md) can be used to restrict the search range in the table. When searching in individual table lines, the other additions operate in the same way as in the statement [`REPLACE pattern IN`](abapreplace_in_pattern.md) for elementary character or byte strings, with a further addition, [`REPLACEMENT LINE`](abapreplace_itab_options.md) that also returns the line number of an occurrence.

In string processing for line types of fixed length, trailing blanks are respected, whereas in `new` they are ignored.

If the internal table is empty, a replacement is never successful and `sy-subrc` is set to 4.

## Hints

- `REPLACE IN TABLE` can be used in tables with structured line types to replace character strings if the structure only contains [flat](../../abap-glossary/abenflat_glosry.md) [character-like](../../abap-glossary/abencharlike_data_object_glosry.md) components. Every line is then handled in the same way as a field of type `c`.

- Replacements using `REPLACE IN TABLE` give better performance than running a [`LOOP`](abaploop_at_itab.md) and using [`REPLACE`](abapreplace_in_pattern.md) to make replacements in individual lines.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | The search pattern was replaced by the content of `new` and the full result is available in the table lines.                                     |
| 2              | The search pattern was replaced by the content of `new` and the result of the replacement was truncated on the right in at least one table line. |
| 4              | The search pattern in `pattern` was not found in the internal table.                                                                             |
| 8              | The operands `pattern` or `new` do not contain interpretable double-byte characters.                                                             |

The values of `sy-tabix` and `sy-fdpos` are not changed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A simple *DM-Euro Conversion*.

``` abap
DATA menu TYPE TABLE OF string WITH EMPTY KEY. 
 
menu = value #( ( `Beer  -  3 DM` ) 
                ( `Pizza - 10 DM` ) ). 
 
REPLACE ALL OCCURRENCES OF PCRE `\b(DM)\b` 
        IN TABLE menu WITH 'EUR' 
        RESPECTING CASE.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_REPLACE_INFINITE_LOOP`

- *Cause:* Substring of length **0** creates an endless loop when searching for all occurrences.

  *Runtime error:* `REPLACE_INFINITE_LOOP`

`CX_SY_TAB_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or line specification in the addition of `FROM ... OFFSET ... TO OFFSET`.

  *Runtime error:* `INVALID_TABLE_RANGE`

`CX_SY_INVALID_REGEX`

- *Cause:* Invalid expression after the addition `PCRE|REGEX`.

  *Runtime error:* `INVALID_REGEX`

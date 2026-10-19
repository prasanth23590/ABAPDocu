---
title: "FIND IN TABLE itab"
source_file: abapfind_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND IN TABLE itab

## Syntax

``` abap
FIND [{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF] pattern 
  IN TABLE itab [table_range] 
  [IN {CHARACTER|BYTE} MODE] 
  [find_options]  .
```

[`pattern`](abapfind_pattern.md) · [`table_range`](abapfind_table_range.md) · [`find_options`](abapfind_itab_options.md)

## Description

The internal table `itab` is searched line-by-line for the character strings or byte strings specified in [`pattern`](abapfind_pattern.md). `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

`itab` must be a standard table with no [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). The lines in the table must be [character](../../abap-glossary/abencharlike_data_object_glosry.md)-like or [byte](../../abap-glossary/abenbyte_like_data_object_glosry.md)-like, depending on the addition `CHARACTER` or `BYTE MODE`. Character strings or byte strings that cover multiple table lines are not found.

The [`table_range`](abapfind_table_range.md) addition can be used to restrict the search range in the table. When making replacements in the individual table lines, the other additions generally have the same meaning as the statement [`FIND`](abapfind.md) for elementary character or byte strings. Here, a further addition [`MATCH LINE`](abapfind_itab_options.md) also returns the line number of any occurrence.

The search is terminated if the search pattern was found for the first time, or if all search patterns were found in the entire search range, or if the end of the search range was reached. The search result is communicated by setting `sy-subrc`.

In string processing for line types of fixed length, trailing blanks are respected.

If the internal table is empty, a search is never successful and `sy-subrc` is set to 4 with one exception: A search for a obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) that matches an empty string sets `sy-subrc` to 0 and behaves as if the internal table contained an empty first line by returning 1 for [`MATCH LINE`](abapfind_itab_options.md) and 0 for [`MATCH OFFSET`](abapfind_itab_options.md) and [`MATCH LENGTH`](abapfind_itab_options.md).

## Hints

- `FIND IN TABLE` can be used to search tables with structured line types for character strings, if the structure only contains [flat](../../abap-glossary/abenflat_glosry.md) [character-like](../../abap-glossary/abencharlike_data_object_glosry.md) components. Every line is then handled in the same way as a field of type `c`.

- Searching using `FIND IN TABLE` produces better performance than running a [`LOOP`](abaploop_at_itab.md) and using [`FIND`](abapfind.md) to search the individual lines.

- For searching multiple lines, the lines can be converted to a string by using the concatenation function [`concat_lines_of`](abenconcatenation_functions.md) or the statement [`CONCATENATE LINES OF`](abapconcatenate.md). It must be ensured that trailing blanks are handled correctly.

## System Fields

| **`sy-subrc`** | **Meaning**                                                     |
|----------------|-----------------------------------------------------------------|
| 0              | The search pattern was found at least once in the search range. |
| 4              | The search pattern was not found in the search range.           |

The values of `sy-tabix` and `sy-fdpos` are not changed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a text into an internal table in `ITF` format and search for the first string *ABAP* or *XML*. The positions the occurrence are written in variables. The line type of the internal table is interpreted as a single field of the type `c` despite being a structured type.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itf_tab TYPE tline_tab. 
IF cl_abap_docu_itf=>get_docu( EXPORTING id = 'SD' 
                                         object = 'ABENABAP_XML' 
                               IMPORTING itf = itf_tab ) = 0. 
 
  FIND FIRST OCCURRENCE OF PCRE 'ABAP|XML' 
       IN TABLE itf_tab 
       RESPECTING CASE 
       MATCH LINE FINAL(mline) 
       MATCH OFFSET FINAL(moff) 
       MATCH LENGTH FINAL(mlen). 
 
  IF sy-subrc = 0. 
    out->write( |{ mline }, { moff }, { mlen }| ). 
  ENDIF. 
ENDIF. 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in the addition `SECTION OF`.

  *Runtime error:* `REFI_WRONG_SECTION`

`CX_SY_TAB_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specification in the addition of `FROM ... OFFSET ... TO OFFSET`.

  *Runtime error:* `INVALID_TABLE_RANGE`

`CX_SY_INVALID_REGEX`

- *Cause:* Invalid expression after the addition `PCRE|REGEX`.

  *Runtime error:* `INVALID_REGEX`

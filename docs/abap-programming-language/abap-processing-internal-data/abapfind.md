---
title: "FIND"
source_file: abapfind.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND

## Syntax

``` abap
FIND [{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF] pattern 
  IN [section_of] dobj 
  [IN {CHARACTER|BYTE} MODE] 
  [find_options].  
```

[`pattern`](abapfind_pattern.md) · [`section_of`](abapfind_section_of.md) · [`find_options`](abapfind_options.md)

### Addition

[1. `... {FIRST OCCURRENCE}|{ALL OCCURRENCES} OF`](abapfind.md#addition-1)

[2. `... [IN {CHARACTER|BYTE} MODE]`](abapfind.md#addition-2)

## Overview

### Description

The operand `dobj` is searched for the character or byte sequence determined by a search pattern [`pattern`](abapfind_pattern.md).

The additions `FIRST OCCURRENCE` and `ALL OCCURRENCES` determine whether all occurrences or only the first one is searched. The addition [`section_of`](abapfind_section_of.md) can be used to restrict the search range. The search is terminated if the search pattern is found for the first time, all search patterns in the entire search range have been found, or if the end of the search range was reached. The search result is communicated by setting `sy-subrc`. The addition `MODE` determines whether a character or byte string is processed, and the addition [`find_options`](abapfind_options.md) provides additional options for controlling and evaluating the statement.

When a character string is processed, `dobj` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) and the blanks are respected for `dobj` operands of a fixed length.

### System Fields

| **`sy-subrc`** | **Meaning**                                                     |
|----------------|-----------------------------------------------------------------|
| 0              | The search pattern was found at least once in the search range. |
| 4              | The search pattern was not found in the search range.           |

### Hints

- The statement [`FIND IN TABLE`](abapfind_itab.md) is available for searching in internal tables.

- [Search functions](abensearch_functions.md) can be used to search in a string in an operand position. They cover some of the functions of the statement `FIND`.

- The statement `FIND` and the search functions can be quicker than the comparison operator [`CS`](../abap-program-flow-logic/abenlogexp_strings.md) by some magnitude.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The simplest form of the statement `FIND`.

``` abap
FIND 'bcd' in 'abcde'. 
ASSERT sy-subrc = 0.
```

## Addition 1

`... {FIRST OCCURRENCE}|{ALL OCCURRENCES} OF`

### Description

The optional addition `{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF` specifies whether all or only the first occurrence of the search pattern is searched. If the addition `FIRST OCCURRENCE` or none of the additions is specified, only the first occurrence is searched for. Otherwise, all occurrences are searched for.

If `substring` is an empty string in [`pattern`](abapfind_pattern.md) or is of type `c`, `n`, `d`, or `t` and only contains blanks, the place in front of the first character or byte of the search range is found when searching for the first occurrence. In searches for all occurrences, the exception `CX_SY_FIND_INFINITE_LOOP` is raised in this case.

If `regex` in [pattern](abenregex_syntax.md) contains a [`regular expression`](abapfind_pattern.md) that matches the empty character string, the search for the first occurrence also finds the place in front of the first character. When searching for all occurrences in this case, the search finds the place in front of the first character, all interim places that are not within a match, and the place after the last character.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

All three occurrences of the letter *a* are searched for and found.

``` abap
FIND ALL OCCURRENCES OF 'a' in 'ababa' MATCH COUNT FINAL(mcnt). 
ASSERT mcnt = 3.
```

## Addition 2

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is performed. Depending on the processing type, `dobj` and `substring` in [`pattern`](abapfind_pattern.md) must be character-like or byte-like. If [regular expressions](abenregex_syntax.md) are used in `pattern`, only character string processing is allowed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Search for the first byte that represents a blank space in the code page UTF-8.

``` abap
FINAL(xstr) = 
  cl_abap_conv_codepage=>create_out( )->convert( `a b c` ). 
FINAL(xspc) = 
  cl_abap_conv_codepage=>create_out( )->convert( ` ` ). 
FIND xspc IN xstr IN BYTE MODE MATCH OFFSET FINAL(moff). 
ASSERT moff = 1.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_FIND_INFINITE_LOOP`

- *Cause:* Substring of length **0** creates an endless loop when searching for all occurrences.

  *Runtime error:* `FIND_INFINITE_LOOP`

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in the addition `SECTION OF`.

  *Runtime error:* `REFI_WRONG_SECTION`

`CX_SY_INVALID_REGEX`

- *Cause:* Invalid expression after the addition `PCRE|REGEX`.

  *Runtime error:* `INVALID_REGEX`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* More information: [Exceptions in Regular Expressions](abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

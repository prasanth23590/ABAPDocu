---
title: "FIND, options"
source_file: abapfind_options.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > FIND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND, options

## Syntax

``` abap
...  [{RESPECTING|IGNORING} CASE] 
     [MATCH COUNT  mcnt] 
     { {[MATCH OFFSET moff] 
        [MATCH LENGTH mlen]} 
     | [RESULTS result_tab|result_wa] } 
     [SUBMATCHES s1 s2 ...] ...  
```

### Addition

[1. `... {RESPECTING|IGNORING} CASE`](abapfind_options.md#addition-1)

[2. `... MATCH COUNT mcnt`](abapfind_options.md#addition-2)

[3. `... MATCH OFFSET moff`](abapfind_options.md#addition-3)

[4. `... MATCH LENGTH mlen`](abapfind_options.md#addition-4)

[5. `... RESULTS result_tab|result_wa`](abapfind_options.md#addition-5)

[6. `... SUBMATCHES s1 s2 ...`](abapfind_options.md#addition-6)

## Overview

### Description

These additions control the [`FIND`](abapfind.md) statement and provide advanced evaluation options. The addition `CASE` can be used to specify whether the search is case-sensitive. The additions `MATCH`, `SUBMATCHES`, and `RESULTS` can be used to determine the number, position, and length of the sequences found.

## Addition 1

`... {RESPECTING|IGNORING} CASE`

### Description

This addition is only allowed for character string processing. It specifies whether the search in `pattern` and `dobj` is case-sensitive. If `RESPECTING CASE` is specified, the search is case-sensitive and if `IGNORING CASE` is used, it is not. If neither of these additions is specified, `RESPECTING CASE` is used implicitly. If a regular expression is passed as an object of class `CL_ABAP_REGEX` for [`pattern`](abapfind_pattern.md), this addition is not allowed. Instead, the properties of the object are respected by the search.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first search finds the letter *a*, the second finds the letter *A*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIND 'A' in `aA` IGNORING   CASE MATCH OFFSET FINAL(moff1). 
FIND 'A' in `aA` RESPECTING CASE MATCH OFFSET FINAL(moff2). 
out->write( |{ moff1 }, { moff2 }| ). 
 
out->display( ).
```

## Addition 2

`... MATCH COUNT mcnt`

### Description

If the search pattern `pattern` is found in the search range, the `MATCH COUNT` addition saves the number of occurrences in `mcnt`. The following can be specified for `mcnt`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If `FIRST OCCURRENCE` is used, the value after a successful search is always 1. If the search is not successful, `mcnt` is set to 0.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Check whether the numbers of opening and closing tags in an HTML file match.

``` abap
DATA html TYPE string. 
 
... 
 
FIND ALL OCCURRENCES OF '<div'  IN html IGNORING CASE 
                                MATCH COUNT FINAL(divo). 
FIND ALL OCCURRENCES OF '</div' IN html IGNORING CASE 
                                MATCH COUNT FINAL(divc). 
ASSERT divo = divc.
```

## Addition 3

`... MATCH OFFSET moff`

### Description

If the search pattern `pattern` is found in the search range, the `MATCH OFFSET` addition saves the [offset](../../abap-glossary/abenoffset_glosry.md) of the last occurrence with reference to the `dobj` operand in `moff`. The following can be specified for `moff`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If `FIRST OCCURRENCE` is used, the result is the offset of the first occurrence. If the search is not successful, `moff` retains its previous value or remains initial.

### Hint

The system field `sy-fdpos` is not filled by `FIND`.

## Addition 4

`... MATCH LENGTH mlen`

### Description

If the search pattern `pattern` is found in the search range, the `MATCH LENGTH` addition saves the length of the last substring found in `mlen`. The following can be specified for `mlen`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If `FIRST OCCURRENCE` is used, the result is the length of the first occurrence. If the search is not successful, `mlen` retains its previous value or remains initial.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the first string of digits within a string and its output.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIND PCRE '\d+' IN 'abc123def' 
     MATCH OFFSET FINAL(moff) 
     MATCH LENGTH FINAL(mlen). 
 
out->write( substring( val = 'abc123def' 
                       off = moff 
                       len = mlen ) ). 
 
out->display( ).
```

## Addition 5

`... RESULTS result_tab|result_wa`

### Description

If the search pattern `pattern` is found in the search range, the `RESULTS` addition saves the offsets of the occurrences, the lengths of the substrings found, and information about the subgroup registers of regular expressions either in an internal table `result_tab` or in a structure `result_wa`. The internal table or structure can be specified as follows:

- An existing internal table with the table type `MATCH_RESULT_TAB` with the line type `MATCH_RESULT` from the ABAP Dictionary is specified for `result_tab`. A structure of the type `MATCH_RESULT` from the ABAP Dictionary is specified for `result_wa`

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) is specified after `RESULTS`. If `ALL OCCURRENCES` is used, an internal table of the type `MATCH_RESULT_TAB` is declared. If `FIRST OCCURRENCE` is used, a structure of the type `MATCH_RESULT` is declared.

When an internal table is used, it is initialized before the search starts and a line is inserted into the internal table for each match found. If a structure is used, it is assigned the values of the last occurrence. If `FIRST OCCURRENCE` is used and an internal table is specified, exactly one line is inserted into this table if the search is successful.

The line type or structure type `MATCH_RESULT` has the following components:

- `OFFSET` of type `INT4` for storing the offset of the substring

- `LENGTH` of type `INT4` for storing the length of the substring

- `SUBMATCHES` of table type `SUBMATCH_RESULT_TAB` with the line type `SUBMATCH_RESULT` for storing the offset and length of the substring of the current occurrence, which are stored in the [subgroup registers](../abap-obsolete-language-elements/abenregex_posix_syntax_operators.md) of a regular expression

The lines from `result_tab` are sorted according to the `OFFSET` and `LENGTH` columns. An additional component `LINE` is only relevant for the [`FIND IN TABLE`](abapfind_itab.md) variant.

After an unsuccessful search, the content of the internal table `result_tab` is empty, whereas the structure `result_wa` preserves its content.

### Hint

The `RESULTS` addition is particularly useful when used with the `ALL OCCURRENCES` addition if an internal table is specified, and with the `FIRST OCCURRENCE` addition if a structure is specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following search for a regular expression finds the two substrings *ab* and *ba* at offset 0 and 2 and fills the internal table `result_tab` accordingly with two lines. Since the regular expression contains three subgroups, the `submatches` component contains three lines. The first line of `submatches` relates to the outer parenthesis, the second line relates to the first inner parenthesis, and the third line relates to the second inner parenthesis. The first and second lines contain the offset and length of the first occurrence, and the third line remains undefined. The first and third lines contain the offset and length of the second occurrence, and the second line remains undefined.

``` abap
FIND ALL OCCURRENCES OF pcre `((ab)|(ba))` 
     IN 'abba' 
     RESULTS FINAL(result_tab).
```

## Addition 6

`... SUBMATCHES s1 s2 ...`

### Description

This addition can be used only if a [regular expression](abenregex_syntax.md) is used in [`pattern`](abapfind_pattern.md). The current content of the [subgroup register](../abap-obsolete-language-elements/abenregex_posix_syntax_operators.md) of the regular expression is written to `s1`, `s2`, ... for the current occurrence. The operands can be specified as follows:

- As existing variables that expect a character-like type.

- As an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of type `string` is declared.

When `ALL OCCURRENCES` is used, the last occurrence is evaluated. If more operands `s1`, `s2`, ... than subgroups are listed, the surplus variables of fixed length are filled with blanks and strings are initialized. If fewer operands `s1`, `s2`, ... than subgroups are listed, the surplus subgroups are ignored.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The regular expression after `PCRE` has two subgroups. The search finds the substring at offset 0 with length 14. The content of the subgroup registers is *Hey* and *my*.

``` abap
DATA text TYPE string. 
 
text = `Hey hey, my my, Rock and roll can never die`. 
 
FIND PCRE `(\w+)\W+\1\W+(\w+)\W+\2` 
     IN text 
     IGNORING CASE 
     MATCH OFFSET FINAL(moff) 
     MATCH LENGTH FINAL(mlen) 
     SUBMATCHES FINAL(s1) FINAL(s2).
```

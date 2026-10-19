---
title: "FIND, pattern"
source_file: abapfind_pattern.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > FIND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND, pattern

## Syntax

``` abap
...  {[SUBSTRING] substring} | {PCRE pcre}|{REGEX regex_ref} ... .  
```

[`pcre`](abenregex_pcre_syntax.md)

### Variant

[1. `... [SUBSTRING] substring.`](abapfind_pattern.md#variant-1)

[2. `... {PCRE pcre}|{REGEX regex_ref}`](abapfind_pattern.md#variant-2)

## Overview

### Description

Definition of a search pattern for the statements [`FIND`](abapfind.md) and [`FIND IN TABLE`](abapfind_itab.md). The system can either search for exactly one substring `substring` or for a substring that matches a regular expression behind `PCRE` or `REGEX`.

### Hint

The statements [`REPLACE`](abapreplace.md) and [`REPLACE IN TABLE`](abapreplace_itab.md) use the same search pattern.

## Variant 1

`... [SUBSTRING] substring.`

### Description

In this variant, a search is performed for the exact occurrence of a substring specified in a character-like or byte-like operand `substring`. `substring` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). The optional word `SUBSTRING` can be specified for emphasis.

If `substring` is either an empty string or is of type `c`, `n`, `d`, or `t` and only contains blanks, a search is performed for an empty substring. This is only possible when searching for the first occurrence, and the empty substring is always found before the first character or byte. In character string processing, the trailing blanks are ignored for `substring` data objects of fixed length.

### Hint

If trailing blanks are not to be ignored in the substring, `substring` must have the data type `string`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Search for all occurrences of the string *now* in a text string literal. The offsets 11 and 24 of both occurrences are shown in the output.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIND ALL OCCURRENCES OF `now` IN 
     `Everybody knows this is nowhere` 
     RESULTS FINAL(result_tab). 
 
LOOP AT result_tab ASSIGNING FIELD-SYMBOL(<match>). 
  out->write( |{ <match>-offset } { 
                 <match>-length }| ). 
ENDLOOP. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Search for all occurrences of the string *now* in a text string literal using a `WHILE` loop. After every successful search, the search range is redefined to start after the occurrence. In this way, all occurrences of the search pattern could be found even before the addition `ALL OCCURRENCES` was introduced.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(off) = 0. 
WHILE sy-subrc = 0. 
  FIND `now` IN SECTION OFFSET off OF 
       `Everybody knows this is nowhere` 
       MATCH OFFSET FINAL(moff) 
       MATCH LENGTH FINAL(mlen). 
  IF sy-subrc = 0. 
    out->write_data( moff ). 
    off = moff + mlen. 
  ENDIF. 
ENDWHILE. 
 
out->display( ).
```

## Variant 2

`... {PCRE pcre}|{REGEX regex_ref}`

### Description

In this variant, a search is performed for a substring that matches a [regular expression](abenregular_expressions.md) specified in `pcre` or `regex_ref`.

- If the addition `PCRE` is used, a character-like operand can be specified for `pcre` that contains a valid [PCRE regular expression](abenregex_pcre_syntax.md). The PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched off with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

- If the addition `REGEX` is used, an object reference variable `regex_ref` can be specified that points to an instance of the [system class](abenregex_system_classes.md) `CL_ABAP_REGEX` that in turn represents a regular expression in any allowed [syntax for regular expressions](abenregex_syntax.md) supported by ABAP.

`pcre` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md).

In searches using a regular expression, special search patterns can be specified that allow further conditions including forecast conditions.

An empty string in `pcre` is not a valid regular expression and raises an exception. A character string is empty if `pcre` is either an empty string or is of type `c`, `n`, `d`, or `t` and only contains blanks.

### Hints

- Instances of `CL_ABAP_REGEX` for all kinds of regular expressions, PCRE, XPath, XSD and POSIX (obsolete) can be used with the addition `REGEX`. This circumvents the restriction that regular expressions of XPath and XSD syntax cannot be specified directly as character strings.

- When using `CL_ABAP_REGEX`, the extended mode can be switched by a parameter for PCRE and XPath regular expressions.

- Some regular expressions that are not empty, such as `a*`, are used to search for empty character strings. This is possible when searching for the first occurrence or all occurrences. The corresponding empty substrings are found before the first character, between all characters, and after the last character of the search range. A search of this type is always successful.

- A regular expression can have correct syntax but be too complex for the execution of the statement `FIND`, which raises a catchable exception of the class `CX_SY_REGEX_TOO_COMPLEX`. See [Exceptions in Regular Expressions](abenregex_exceptions.md).

- Behind `REGEX`, a character-like operand that contains a valid [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) [`posix`](../abap-obsolete-language-elements/abapfind_replace_regex_obs.md) can also be specified. This variant is obsolete.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The search uses PCRE regular expression syntax and finds the `'ab'` from offset 3.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(text) = `oooababboo`. 
 
FIND PCRE 'a.|[ab]+|b.*' IN text 
     MATCH OFFSET FINAL(moff) 
     MATCH LENGTH FINAL(mlen). 
IF sy-subrc = 0. 
  out->write( substring( val = text off = moff 
                                    len = mlen ) ). 
ENDIF. 
 
out->display( ).
```

## Executable Examples

- [Find a PCRE regular expression](abenpcre_abexa.md)

- [Search for a regular expression](abenregex_abexa.md)

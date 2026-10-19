---
title: "cstring_func - count, count_..."
source_file: abencount_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Description Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - count, count\_...

## Syntax

``` abap
1. ... count( val = text {sub = substring}|{pcre = regex} [case = case] 
             [off = off] [len = len] ) ...  

2. ... count_any_of( val = text  sub = substring 
                    [off = off] [len = len] ) ...  

3. ... count_any_not_of( val = text  sub = substring 
                        [off = off] [len = len] ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) search functions `count` and `count_...` search [`text`](abenstring_functions_val.md) in the same way as the corresponding search functions [`find`](abensearch_functions.md) and [`find_...`](abensearch_functions.md), either in the entire string [`text`](abenstring_functions_val.md) or in a subarea defined using [`off`](abenstring_functions_off_len.md) and [`len`](abenstring_functions_off_len.md) for characters specified in [`substring`](abenstring_functions_sub.md) or for a match with a [regular expression](abenregex_syntax.md) specified in [`regex`](abenstring_functions_regex.md). Instead of an offset, they return the number of all occurrences.

If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md). A regular expression in PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` in a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

The return value has the type `i`.

## Hint

Besides `pcre`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is 1, 3, and 6.

``` abap
FINAL(result1) = count(            val = `xxx123yyy` pcre = `\d+` ). 
FINAL(result2) = count_any_of(     val = `xxx123yyy` sub  = `123` ). 
FINAL(result3) = count_any_not_of( val = `xxx123yyy` sub  = `x`   ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the first counting is 2 because the [PCRE regular expression](abenregex_pcre_syntax.md) handles the [surrogate pair](../../abap-glossary/abensurrogate_pair_glosry.md) in the character string as two characters by default. When counting with a regular expression that is introduced with `(*UTF)`, the result is 1, because the surrogate pair is interpreted as one [UTF-16](../../abap-glossary/abenutf16_glosry.md) character.

``` abap
FINAL(surrogate_pair) = cl_abap_codepage=>convert_from( 
  codepage = 'UTF-8' 
  source    = CONV xstring( 'F09F91BD' ) ). 
                            "U+1F47D, EXTRATERRESTRIAL ALIEN 
 
cl_demo_output=>write_text( surrogate_pair ). 
 
cl_demo_output=>write( |{ 
  count( val = surrogate_pair pcre = `.` ) } { 
  count( val = surrogate_pair pcre = `(*UTF).` ) }| ). 
 
cl_demo_output=>display( ).
```

## Executable Example

[String Functions, `count`, `find` and `match`](abenstring_function_find_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in `off` and `len`.

  *Runtime error:* `STRING_OFFSET_TOO_LARGE`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* More information: [Exceptions in Regular Expressions](abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_STRG_PAR_VAL`

- *Cause:* Substring in `sub` or regular expression in `regex` is empty or occurrence in `occ` is 0.

  *Runtime error:* `STRG_ILLEGAL_PAR`

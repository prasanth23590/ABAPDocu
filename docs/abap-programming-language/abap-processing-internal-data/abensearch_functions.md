---
title: "cstring_func - find, find_..."
source_file: abensearch_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Description Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - find, find\_...

## Syntax

``` abap
1. ... find( val = text {sub = substring}|{pcre = regex} [case = case] 
           [off = off] [len = len] [occ = occ] ) ...  

2. ... find_end( val = text {sub = substring}|{pcre = regex} [case = case] 
               [off = off] [len = len] [occ = occ] ) ...  

3. ... find_any_of( val = text sub = substring 
                  [off = off] [len = len] [occ = occ] ) ...  

4. ... find_any_not_of( val = text  sub = substring 
                      [off = off] [len = len] [occ = occ] ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`occ = occ`](abenstring_functions_occ.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`occ = occ`](abenstring_functions_occ.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`occ = occ`](abenstring_functions_occ.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`occ = occ`](abenstring_functions_occ.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) search functions `find` and `find_...` search [`text`](abenstring_functions_val.md) for the characters specified in [`substring`](abenstring_functions_sub.md) or for a match with a [regular expression](abenregex_syntax.md) specified in [`regex`](abenstring_functions_regex.md), where the optional parameters [`off`](abenstring_functions_off_len.md) and [`len`](abenstring_functions_off_len.md) determine the subarea to be searched and the occurrence of the match can be specified in the optional parameter [`occ`](abenstring_functions_occ.md).

If the parameter `pcre` is used, `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md). A regular expression in PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

The return value has the type `i` and is filled as follows:

- The function `find` searches for the exact substring specified in [`substring`](abenstring_functions_sub.md) or for a match with the regular expression [`regex`](abenstring_functions_regex.md) and returns the offset of the occurrence with respect to the entire length of `text`. The search is case-sensitive by default, but this can be overridden using the parameter [`case`](abenstring_functions_case.md). If `substring` is empty, an exception from the class `CX_SY_STRG_PAR_VAL` is raised.

- The function `find_end` searches like `find`, but it returns the sum of the offset of the occurrence and the length of the found match with the regular expression.

- The function `find_any_of` returns the offset of the occurrence of any character contained in [`substring`](abenstring_functions_sub.md), and is always case-sensitive. If `substring` is empty, the value -1 is returned.

- The function `find_any_not_of` returns the offset of the found occurrence of any character not in [`substring`](abenstring_functions_sub.md), and is always case-sensitive. If `substring` is empty, the value -1 is returned.

If a search is not successful, all functions return the value -1.

The optional parameters [`off`](abenstring_functions_off_len.md), [`len`](abenstring_functions_off_len.md), and [`occ`](abenstring_functions_occ.md) have the following meaning when combined:

- If `occ` is positive, the subarea defined by `off` and `len` is searched from left to right.

- If `occ` is negative, the subarea defined by `off` and `len` is searched from right to left.

The occurrence of the match specified by `occ` refers to the search range defined by `off` and `len`.

## Hints

- Using the related search functions [`count`](abencount_functions.md) and [`count_...`](abencount_functions.md), it is possible to determine the total number of occurrences instead of an offset.

- Like the statement [`FIND`](abapfind.md), the search functions can be faster than the comparison operator [`CS`](../abap-program-flow-logic/abenlogexp_strings.md) by some magnitude.

- Besides `pcre`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is 3, 6, 3, and 3.

``` abap
FINAL(result1) = find(            val = `xxx123yyy` pcre = `\d+` ). 
FINAL(result2) = find_end(        val = `xxx123yyy` pcre = `\d+` ). 
FINAL(result3) = find_any_of(     val = `xxx123yyy` sub  = `123` ). 
FINAL(result4) = find_any_not_of( val = `xxx123yyy` sub  = `x`   ).
```

## Executable Example

[String Functions, `find` and `substring`](abenstring_function_find_abexa.md)

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

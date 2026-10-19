---
title: "cstring_func - substring, substring_..."
source_file: abensubstring_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - substring, substring\_...

## Syntax

``` abap
1. ... substring( val = text [off = off] [len = len] ) ...  

2. ... substring_from( val = text {sub = substring}|{pcre = regex} 
                     [case = case] [occ = occ] [len = len]  ) ...  

3. ... substring_after( val = text {sub = substring}|{pcre = regex} 
                      [case = case] [occ = occ] [len = len]  ) ...  

4. ... substring_before( val = text {sub = substring}|{pcre = regex} 
                       [case = case] [occ = occ] [len = len]  ) ...  

5. ... substring_to( val = text {sub = substring}|{pcre = regex} 
                   [case = case] [occ = occ] [len = len]  ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md) · [`len = len`](abenstring_functions_off_len.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) substring functions determine a substring in the argument [`text`](abenstring_functions_val.md) and return it.

The substring is determined as follows:

- The function `substring` uses the offset [`off`](abenstring_functions_off_len.md) and the length [`len`](abenstring_functions_off_len.md) to return a certain substring. At least one of the parameters `off` or `len` must be specified.

- The function `substring_from` searches `text` for the match specified in [`occ`](abenstring_functions_occ.md) with the character string specified in [`substring`](abenstring_functions_sub.md) or with the [regular expression](abenregex_syntax.md) specified in [`regex`](abenstring_functions_regex.md) and returns the subarea of the length [`len`](abenstring_functions_off_len.md) from the offset of the occurrence.

  If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md). A regular expression in PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression. If `len` is not specified, the substring is returned to the end of the character string. If `substring` is empty, an exception of the class `CX_SY_STRG_PAR_VAL` is raised. The search is case-sensitive by default, but this can be overridden using the parameter `case`. If no substring is found, the return value is empty.

- The function `substring_after` works in the same way as `substring_from`, but the subarea plus the length of the substring found is returned, from the offset of the occurrence.

- The function `substring_before` works in the same way as `substring_from`, but the subarea of the length [`len`](abenstring_functions_off_len.md) is returned before the offset of the occurrence. If `len` is not specified, the subarea is formed from the start of the character string.

- The function `substring_to` works in the same way as `substring_before`, but the subarea before the offset of the occurrence plus the length of the substring found is returned.

The return value has the type `string` accordingly.

## Hints

- The performance of the substring functions is not as good as a direct [substring access](../abap-operands/abenoffset_length.md). They do, however, make it possible to use [expressions](../../abap-glossary/abenexpression_glosry.md) in all operand positions and they allow searches for substrings that match regular expressions.

- Besides `pcre`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The return values of the following function calls are: *CD*, *CDEFGH*, *EFGH*, *AB*, and *ABCD*.

``` abap
DATA result TYPE string. 
... 
result = substring( val = 'ABCDEFGH' off = 2 len = 2 ). 
... 
result = substring_from( val = 'ABCDEFGH' sub = 'CD' ). 
... 
result = substring_after( val = 'ABCDEFGH' sub = 'CD' ). 
... 
result = substring_before( val = 'ABCDEFGH' sub = 'CD' ). 
... 
result = substring_to( val = 'ABCDEFGH' sub = 'CD' ). 
...
```

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

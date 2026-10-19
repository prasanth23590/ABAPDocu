---
title: "cstring_func - match"
source_file: abenmatch_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - match

The match function returns a substring of a character-like argument that matches a regular expression.

## Syntax

``` abap
... match( val = text pcre|xpath = regex [case = case] [occ = occ] ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`pcre|xpath = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md)

## Description

The [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) `match` searches [`text`](abenstring_functions_val.md) for the match specified in [`occ`](abenstring_functions_occ.md) with the [regular expression](abenregex_syntax.md) specified in [`regex`](abenstring_functions_regex.md) and returns the substring found. The search is case-sensitive by default, but this can be overridden using the parameter [`case`](abenstring_functions_case.md).

- If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md).

- If the parameter `xpath` is supplied, `regex` must contain a [XPath regular expression](abenregex_xpath_syntax.md).

A regular expression in PCRE or XPath syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to specify whitespace and `#` characters in a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

The return value has the type `string`.

## Hint

Besides `pcre` and `xpath`, the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can also be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following match function returns `x2`.

``` abap
cl_demo_output=>display( 
  match( val = 'x1 x2 x3' pcre = 'x.' occ = 2 ) ).
```

## Executable Example

[String Functions, `count`, `find` and `match`](abenstring_function_find_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* See [Exceptions in Regular Expressions](abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_STRG_PAR_VAL`

- *Cause:* Regular expression in `regex` is empty or there are 0 occurrences in `occ`.

  *Runtime error:* `STRG_ILLEGAL_PAR`

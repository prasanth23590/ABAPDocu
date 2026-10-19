---
title: "cstring_func - pcre, xpath"
source_file: abenstring_functions_regex.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - pcre, xpath

## Syntax

``` abap
... ( ... pcre|xpath = regex ...  ) ...  
```

[`pcre`](abenregex_pcre_syntax.md) · [`xpath`](abenregex_xpath_syntax.md)

## Description

`pcre|xpath$` is used to pass a [regular expression](abenregex_syntax.md) to be searched for or compared to. `regex` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) that must contain a correct regular expression. Only arguments with elementary data types can be specified.

- If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md).

- If the parameter `xpath` is supplied, `regex` must contain a [XPath regular expression](abenregex_xpath_syntax.md).

If a character-like data object with a fixed length is specified, any trailing blanks are ignored. If `regex` is empty, an exception from the class `CX_SY_STRG_PAR_VAL` is raised.

The regular expression is compiled an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

## Hints

- The regular expression in `regex` may have correct syntax but be too complex for the execution of the function, which can raise a catchable exception of the class `CX_SY_REGEX_TOO_COMPLEX`. See [Exceptions in Regular Expressions](abenregex_exceptions.md).

- Besides `pcre` and `xpath`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function call is `<tag>def</tag>`. By placing a question mark (`?`) behind `+`, the greedy behavior of the PCRE regular expression is switched off for that quantifier.

``` abap
cl_demo_output=>display( 
  replace( val   = `<tag>abc</tag>` 
           pcre  = `(<tag>).+?(</tag>)` 
           with  = `$1def$2` ) ).
```

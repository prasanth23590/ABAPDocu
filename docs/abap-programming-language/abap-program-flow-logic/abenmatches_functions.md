---
title: "rel_exp - matches"
source_file: abenmatches_functions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Functions > rel_exp - Predicate Functions for Character-Like Arguments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - matches

## Syntax

``` abap
... matches( val = text pcre|xpath = regex [case = case] 
             [off = off] [len = len] ) ...  
```

[`val = text`](../abap-processing-internal-data/abenstring_functions_val.md) · [`pcre|xpath = regex`](../abap-processing-internal-data/abenstring_functions_regex.md) · [`case = case`](../abap-processing-internal-data/abenstring_functions_case.md) · [`[off = off`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`[len = len`](../abap-processing-internal-data/abenstring_functions_off_len.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) [predicate function](../../abap-glossary/abenpredicate_function_glosry.md) `matches` compares a search range of the argument [`text`](../abap-processing-internal-data/abenstring_functions_off_len.md), defined using [`off`](../abap-processing-internal-data/abenstring_functions_off_len.md) and [`len`](../abap-processing-internal-data/abenstring_functions_val.md), with the [regular expression](../abap-processing-internal-data/abenregex_syntax.md) specified in [`regex`](../abap-processing-internal-data/abenstring_functions_regex.md).

- If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](../abap-processing-internal-data/abenregex_pcre_syntax.md).

- If the parameter `xpath` is supplied, `regex` must contain a [XPath regular expression](../abap-processing-internal-data/abenregex_xpath_syntax.md).

A regular expression in PCRE or XPath syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to specify whitespace and `#` in a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](../abap-processing-internal-data/abenregex_pcre_syntax_specials.md) in the regular expression.

The function returns a [truth value](../../abap-glossary/abentruth_value_glosry.md).

- The return value is true when the whole search range matches the regular expression.

- It is false else.

The comparison is case-sensitive by default, but this can be overridden using the parameter [`case`](../abap-processing-internal-data/abenstring_functions_case.md).

## Hints

- The match function [`match`](../abap-processing-internal-data/abenmatch_functions.md) can be used to return a substring that matches a regular expression.

- Besides `pcre` and `xpath`, the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can also be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first predicate function returns the value *true* because the argument `val` only contains letters. The second predicate function returns the value *false* because the argument `val` also contains numbers.

``` abap
ASSERT     matches( val = 'abcde' pcre = '[[:alpha:]]*' ). 
ASSERT NOT matches( val = 'a123e' pcre = '[[:alpha:]]*' ).
```

## Executable Example

[Predicate Function, `matches`](abenpred_function_matches_abexa.md)

**[Exceptions](abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in `off` and `len`.

  *Runtime error:* `STRING_OFFSET_TOO_LARGE`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* See [Exceptions in Regular Expressions](../abap-processing-internal-data/abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_STRG_PAR_VAL`

- *Cause:* Regular expression in `regex` is empty.

  *Runtime error:* `STRG_ILLEGAL_PAR`

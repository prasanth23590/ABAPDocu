---
title: "rel_exp - contains, contains_..."
source_file: abencontains_functions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Functions > rel_exp - Predicate Functions for Character-Like Arguments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - contains, contains\_...

## Syntax

``` abap
1. ... contains( val = text sub|start|end = substring [case = case] 
                [off = off] [len = len] [occ = occ] ) ...  

2. ... contains( val = text pcre|xpath = regex [case = case] 
                [off = off] [len = len] [occ = occ] ) ...  

3. ... contains_any_of( val = text sub|start|end = substring 
                       [off = off] [len = len] [occ = occ] ) ...  

4. ... contains_any_not_of( val = text sub|start|end = substring 
                           [off = off] [len = len] [occ = occ] ) ...  
```

[`val = text`](../abap-processing-internal-data/abenstring_functions_val.md) · [`sub|start|end = substring`](../abap-processing-internal-data/abenstring_functions_sub.md) · [`case = case`](../abap-processing-internal-data/abenstring_functions_case.md) · [`off = off`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`len = len`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`val = text`](../abap-processing-internal-data/abenstring_functions_val.md) · [`pcre|xpath = regex`](../abap-processing-internal-data/abenstring_functions_regex.md) · [`case = case`](../abap-processing-internal-data/abenstring_functions_case.md) · [`off = off`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`len = len`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`val = text`](../abap-processing-internal-data/abenstring_functions_val.md) · [`sub|start|end = substring`](../abap-processing-internal-data/abenstring_functions_sub.md) · [`off = off`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`len = len`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`val = text`](../abap-processing-internal-data/abenstring_functions_val.md) · [`sub|start|end = substring`](../abap-processing-internal-data/abenstring_functions_sub.md) · [`off = off`](../abap-processing-internal-data/abenstring_functions_off_len.md) · [`len = len`](../abap-processing-internal-data/abenstring_functions_off_len.md)

## Description

These [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) [predicate functions](../../abap-glossary/abenpredicate_function_glosry.md) return a [truth value](../../abap-glossary/abentruth_value_glosry.md) resulting from a condition for the argument [`text`](../abap-processing-internal-data/abenstring_functions_val.md).

- The variants of the function `contains` with the parameters `sub`, `start`, or `end` scan a search range defined by [`off`](../abap-processing-internal-data/abenstring_functions_off_len.md) and [`len`](../abap-processing-internal-data/abenstring_functions_off_len.md) in `text` for matches with the string specified in [`substring`](../abap-processing-internal-data/abenstring_functions_sub.md). The return value is true if at least the number of matches specified in `occ` is found. The search is case-sensitive by default, but this can be overridden using the parameter [`case`](../abap-processing-internal-data/abenstring_functions_case.md). If `substring` is passed to `start` or `end`, the matches must occur directly one after another either at the start or at the end of the search range. `sub`, on the other hand, allows the matches to occur anywhere in the search range. If `substring` is empty, an exception of the class `CX_SY_STRG_PAR_VAL` is raised.

- The variants of the function `contains` with the parameter [`pcre`](../abap-processing-internal-data/abenstring_functions_regex.md) or [`xpath`](../abap-processing-internal-data/abenstring_functions_regex.md) scan a search range defined by [`off`](../abap-processing-internal-data/abenstring_functions_off_len.md) and [`len`](../abap-processing-internal-data/abenstring_functions_off_len.md) in `text` for matches with the [regular expression](../abap-processing-internal-data/abenregex_syntax.md) specified in [`regex`](../abap-processing-internal-data/abenstring_functions_regex.md).

  - If the parameter `pcre` is supplied, `regex` must contain a [PCRE regular expression](../abap-processing-internal-data/abenregex_pcre_syntax.md).

  - If the parameter `xpath` is supplied, `regex` must contain a [XPath regular expression](../abap-processing-internal-data/abenregex_xpath_syntax.md).

    A regular expression in PCRE or XPath syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` in a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](../abap-processing-internal-data/abenregex_pcre_syntax_specials.md) in the regular expression. The return value is true if at least the number of matches specified in `occ` is found. The search is case-sensitive by default, but this can be overridden using the parameter [`case`](../abap-processing-internal-data/abenstring_functions_case.md).

- The function `contains_any_of` has the same effect as `contains`, but does not check for the occurrences of the entire string in [`substring`](../abap-processing-internal-data/abenstring_functions_sub.md). Instead, it checks for the individual characters in `substring`, which is always case-sensitive. The return value is true if `text` contains at least the set of characters specified in `occ`. If `start` or `end` are specified, the characters must be at the start or at the end of the search range in any order, whereas in `sub` they can be anywhere.

- The function `contains_any_not_of` has the same effect as `contains_any_of` but does not require the characters from [`substring`](../abap-processing-internal-data/abenstring_functions_sub.md). Instead, it requires any characters that are not in `substring`.

`occ` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of type `i` and its default value is 1. Specifying a value less than or equal to 0 raises an exception of the class `CX_SY_STRG_PAR_VAL`.

## Hints

- The parameter `occ` has a different meaning here than in other functions used for searches.

- Besides `pcre` and `xpath`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `IF` block is reached in the following code section, since neither the first nor the last character in `html` occur in the system field `sy-abcde`.

``` abap
DATA html TYPE string. 
 
html = '<body>Text</body>'. 
FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
IF contains_any_not_of( val = to_upper( html ) start = abcde ) AND 
   contains_any_not_of( val = to_upper( html ) end   = abcde ). 
  ... 
ENDIF.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following function call checks whether a type `c` field contains any non-digit character.

``` abap
DATA postal_code TYPE c LENGTH 5. 
cl_demo_input=>request( CHANGING field = postal_code ). 
 
IF contains( val  = postal_code 
             pcre = `\D` ). 
  cl_demo_output=>display( `Invalid postal code.` ). 
  RETURN. 
ENDIF.
```

**[Exceptions](abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in `off` and `len`.

  *Runtime error:* `STRING_OFFSET_TOO_LARGE`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* See [Exceptions in Regular Expressions](../abap-processing-internal-data/abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_STRG_PAR_VAL`

- *Cause:* A substring in `substring` or regular expression in `regex` is empty or the number of occurrences in `occ` is less than or equal to 0.

  *Runtime error:* `STRG_ILLEGAL_PAR`

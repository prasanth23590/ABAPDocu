---
title: "regex - Searching, Replacing, Matching"
source_file: abenregex_mtch.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Searching, Replacing, Matching

Regular expressions can be used to find and replace substrings of character strings or to check if a complete character string matches its pattern. If a regular expression is applied to a character string as a search pattern, a search for matches of the regular expression with substrings of the character string is intended. In this case, special characters in the regular expression do not match characters, but match positions, thus affecting the type and number of occurrences. If a regular expression is applied to a character string as a match pattern, it is checked whether the character string matches a pattern.

- [Searching](abenregex_mtch.md#searching)

- [Replacing](abenregex_mtch.md#replacing)

- [Matching](abenregex_mtch.md#matching)

## Hint

A regular expression in PCRE or XPath syntax can be compiled in a normal or extended mode. In the extended mode, most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In ABAP statements and built-in functions, the extended mode is switched on by default. It can be switched of with the special character [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression. When using `CL_ABAP_REGEX`, it can be switched by the parameter `EXTENDED` of method `CREATE_PCRE`.

## Searching

In order to search for substrings that match a pattern described by a regular expression you can use the following:

- Statement [`FIND`](abapfind.md) with the addition [`PCRE|REGEX`](abapfind_pattern.md).

- Built-in functions with the parameter [`pcre|xpath`](abenstring_functions_regex.md) and with [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) (obsolete):

  - [`find`, `find_...`](abensearch_functions.md)

  - [`count`, `count_...`](abencount_functions.md)

  - [`match`](abenmatch_functions.md)

  - [`substring`, `substring_...`](abensubstring_functions.md)

  - [`contains...`](../abap-program-flow-logic/abencontains_functions.md)

- Methods of [system class](abenregex_system_classes.md) `CL_ABAP_MATCHER`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of different possibilities for searching substrings that match a regular expression.

``` abap
FINAL(text)  = `aaa-bbb-ccc`. 
FINAL(regex) = `\W`. 
 
IF contains( val = text pcre = regex ). 
 
  FIND ALL OCCURRENCES OF PCRE regex IN text MATCH COUNT  FINAL(cnt) 
                                             MATCH LENGTH FINAL(len). 
 
  FINAL(off) = find( val = text pcre = regex occ = cnt ). 
 
  ASSERT count( val = text pcre = regex ) = cnt. 
 
  FINAL(sub) = substring_from( val = text pcre = regex len = len  ). 
 
  cl_demo_output=>display( 
    |{ cnt } occurrences found.\n| && 
    |The offset of the last occurrence is { off }.\n| && 
    |The first substring that matches is { sub }.| ). 
 
ENDIF.
```

## Replacing

In order to replace substrings that match a pattern described by a regular expression, the following can be used:

- Statement [`REPLACE`](abapreplace.md) with the addition [`PCRE|REGEX`](abapreplace_pattern.md).

- Built-in function [`replace`](abenreplace_functions.md) with the parameter [`pcre`](abenstring_functions_regex.md) or [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) (obsolete).

- Methods of the [system class](abenregex_system_classes.md) `CL_ABAP_MATCHER`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of different possibilities for replacing substrings that match a regular expression.

``` abap
DATA(text)  = `aaa-bbb-ccc`. 
FINAL(regex) = `\W`. 
 
REPLACE FIRST OCCURRENCE OF PCRE regex IN text WITH '_'. 
 
cl_demo_output=>display( 
  replace( val = text pcre = regex with = `~` ) ).
```

## Matching

In order to check if a complete character string matches a regular expression, the following can be used:

- Built-in function [`matches`](../abap-program-flow-logic/abenmatches_functions.md) with the parameter [`pcre|xpath`](abenstring_functions_regex.md) or [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) (obsolete).

- Methods of [system class](abenregex_system_classes.md) `CL_ABAP_MATCHER`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of different possibilities for matching strings with a regular expression.

``` abap
FINAL(text)  = `aaa-bbb-ccc`. 
FINAL(regex) = `\w+\W\w+\W\w+`. 
 
IF cl_abap_regex=>create_pcre( pattern = regex 
     )->create_matcher( text = text )->match( ). 
  ASSERT matches( val = text pcre = regex ). 
  cl_demo_output=>display( 'match' ). 
ENDIF.
```

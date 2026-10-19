---
title: "REPLACE, pattern"
source_file: abapreplace_pattern.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > REPLACE > REPLACE pattern IN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE, pattern

## Syntax

``` abap
... {[SUBSTRING] substring} 
  | {PCRE pcre}|{REGEX regex_ref} ... .  
```

[`pcre`](abenregex_pcre_syntax.md)

## Description

Defines a search pattern for the statements [`REPLACE`](abapreplace.md) and [`REPLACE IN TABLE`](abapreplace_itab.md).

- If `substring` is specified, the exact substring specified in `substring` is searched for. The optional addition `SUBSTRING` can be specified in front of `substring` for emphasis.

- If `PCRE` or `REGEX` is specified, the substring that matches a [regular expression](abenregular_expressions.md) specified in `pcre` or `regex_ref` is searched for.

  - `PCRE` denotes a [PCRE regular expression](abenregex_pcre_syntax.md) in a character string `pcre`. The PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

  - `REGEX` denotes a any regular expression supported by ABAP represented by an instance of the [system class](abenregex_system_classes.md) `CL_ABAP_REGEX` referenced by a reference variable `regex_ref`.

`substring` and `pcre` are [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). The syntax and semantics are the same as in the definition of a search pattern for the statement [`FIND`](abapfind_pattern.md). The statement [`REPLACE`](abapreplace.md) replaces the found substring in accordance with the specification after [`WITH`](abapreplace_in_pattern.md).

## Hints

- Instances of `CL_ABAP_REGEX` for all kinds of regular expressions, PCRE, POSIX, XPath and XSD can be used with the addition `REGEX`. This circumvents the restriction that regular expressions of XPath and XSD syntax cannot be specified directly as character strings.

- When using `CL_ABAP_REGEX`, the extended mode option can be switched by a parameter.

- A regular expression can have correct syntax, but be too complex for the execution of the statement `REPLACE`, which raises a catchable exception of the class `CX_SY_REGEX_TOO_COMPLEX`. See [Exceptions in Regular Expressions](abenregex_exceptions.md).

- Behind `REGEX`, also a character-like operand [`posix`](../abap-obsolete-language-elements/abapfind_replace_regex_obs.md) can be specified, that contains a valid [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md). This variant is obsolete.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement of the substring `all` with `er`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `Hallo`. 
REPLACE SUBSTRING `all` IN str WITH `er`. 
out->write( str ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacement with regular expression `\D` removes all non-digits from a string.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `4 Apples + 2 Oranges`. 
REPLACE ALL OCCURRENCES OF PCRE `\D` IN str WITH ``. 
out->write( str ). 
 
out->display( ).
```

---
title: "regex - XPath Syntax"
source_file: abenregex_xpath_syntax.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - XPath Syntax

Regular expressions with XPath syntax can be specified behind the parameter [`xpath`](abenstring_functions_regex.md) of built-in functions for strings. Objects for XPath regular expressions can be created with the factory method `CREATE_XPATH2` of the system class [`CL_ABAP_REGEX`](abenregex_system_classes.md) to be used in statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) or with the system class [`CL_ABAP_MATCHER`](abenregex_system_classes.md).

Currently, there is no detailed description of the XPath syntax for regular expressions in the ABAP keyword documentation.

- For a short syntax overview, see

  [Special Characters in XPath Regular Expressions](abenregex_xpath_syntax_specials.md)

- For the complete documentation, refer to

  [XQuery 1.0 and XPath 2.0 Functions and Operators](https://www.w3.org/TR/xquery-operators/#regex-syntax).

A regular expression in XPath syntax can be compiled in a normal and extended mode. In the extended mode, most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In ABAP built-in functions, the extended mode is switched on by default and can be switched off with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression. When using `CL_ABAP_REGEX`, it can be switched by the parameter `EXTENDED` of method `CREATE_XPATH2`.

## Hints

- A regular expression with XPath syntax cannot be specified directly as a character string in the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md), but you can use objects of `CL_ABAP_REGEX` that are created with method `CREATE_XPATH2` with the addition [`REGEX`](abapfind_pattern.md) instead.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A special feature of XPath regular expressions is the subtraction of character sets. In the following example, the letters `a` to `c` are subtracted from character set `BasicLatin` and the first match is `d` at offset 3.

``` abap
FIND REGEX 
  cl_abap_regex=>create_xpath2( pattern = '[\p{IsBasicLatin}-[a-c]]' ) 
  IN 'abcd' MATCH OFFSET FINAL(moff).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Compared to PCRE, XPath regular expressions allow the escape character `\` not only in front of special characters. The `match` function with parameter `xpath` finds `x` while the `match` function with parameter `pcre` does not. Accordingly the first `FIND` statement returns in `sy-subrc` the value 0 while the second `FIND` statement returns 4.

``` abap
FINAL(x) = match( val = `abxcd` xpath = `\x`  occ = 1  ). 
FINAL(y) = match( val = `abxcd` pcre =  `\x`  occ = 1  ). 
 
FIND REGEX cl_abap_regex=>create_xpath2( pattern = '\x' ) IN 'abxcd'. 
FIND REGEX cl_abap_regex=>create_pcre(   pattern = '\x' ) IN 'abxcd'.
```

## Executable Example

[XPath regular expression](abenxpath_regex_abexa.md)

---
title: "regex - PCRE Syntax"
source_file: abenregex_pcre_syntax.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - PCRE Syntax

Regular expressions with PCRE syntax can be specified after the addition [`PCRE`](abapfind_pattern.md) of the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) and the parameter [`pcre`](abenstring_functions_regex.md) of built-in functions for strings. Objects for PCRE regular expressions can be created with the factory method `CREATE_PCRE` of the system class [`CL_ABAP_REGEX`](abenregex_system_classes.md) to be used in statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) or with the system class [`CL_ABAP_MATCHER`](abenregex_system_classes.md).

Currently, there is no detailed description of the PCRE syntax for regular expressions in the ABAP keyword documentation.

- For a short syntax overview, see

  [Special Characters in PCRE Regular Expressions](abenregex_pcre_syntax_specials.md)

- For the complete documentation, refer to:

  [Perl documentation **perlre**](https://perldoc.perl.org/perlre.html)

A regular expression in PCRE syntax can be compiled in a normal or extended mode. In the extended mode, most unescaped whitespace characters (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In ABAP statements and built-in functions, the extended mode is switched on by default and can be switched off with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression. When using `CL_ABAP_REGEX`, it can be switched by the parameter `EXTENDED` of method `CREATE_PCRE`.

For regular expressions in PCRE syntax, it can be defined whether valid [UTF-16](../../abap-glossary/abenutf16_glosry.md) character strings are expected or not. In ABAP statements and built-in functions, a PCRE regular expression can be introduced with [`(*UTF)`](abenregex_pcre_syntax_specials.md) in order to check for valid [UTF-16](../../abap-glossary/abenutf16_glosry.md) strings. When using `CL_ABAP_REGEX`, the parameter `UNICODE_HANDLING` of method `CREATE_PCRE` can be used. When the strict mode for working with UTF-16 strings is switched on, a [surrogate pair](../../abap-glossary/abensurrogate_pair_glosry.md) is handled as a single character (see example for [counting](abencount_functions.md)).

## Hints

- Currently supported version: PCRE2, version 10.44.

- The PCRE syntax is more powerful than the obsolete [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md). Furthermore, PCRE regular expressions generally perform better than the POSIX regular expressions supported by ABAP. Therefore, it is recommended that [POSIX regular expressions are migrated to PCRE](abenregex_migrating_posix.md).

- The PCRE syntax supports callouts that call ABAP methods during matching an regular expression with [`CL_ABAP_MATCHER`](abenregex_system_classes.md).

- [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) also support the PCRE syntax with the built-in functions [`REPLACE_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md), [`LIKE_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md), and [`OCCURRENCES_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md). These functions access the PCRE1 library implemented in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Searching for a PCRE regular expression in a character string. See also the class `CL_DEMO_FIND_REGEX`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(regex)    = `(\b.at\b)`. 
FINAL(text)     = `Cathy's cat with the hat sat on Matt's mat.`. 
 
FIND PCRE regex IN text SUBMATCHES FINAL(subm). 
 
IF sy-subrc = 0. 
  out->write( subm ). 
ENDIF. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

PCRE regular expressions support non-greedy behavior by placing a question mark (`?`) behind quantifiers as for example the character asterisk (`*`). In the following example, the asterisk quantifier in the first regular expression is greedy and finds everything between the first `<i>` and the last `</i>`. In the second regular expression, the asterisk quantifier is marked as non-greedy and only the substring between the first `<i>` and the following `</i>` is found. Non-greedy behavior is not supported in the obsolete [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) and other workarounds as for example `[^<]*` have to be used. For more information, see [New features in PCRE compared to POSIX](abenregex_posix_pcre_improve.md).

``` abap
FINAL(text)  = `<i>abc</i>def<i>ghi</i>`. 
 
FIND PCRE `<i>(.*)</i>` IN text SUBMATCHES FINAL(subm1). 
IF sy-subrc = 0. 
  cl_demo_output=>write( |Greedy: { subm1 }| ). 
ENDIF. 
 
FIND PCRE `<i>(.*?)</i>` IN text SUBMATCHES FINAL(subm2). 
IF sy-subrc = 0. 
  cl_demo_output=>write( |Non-greedy: { subm2 }| ). 
ENDIF. 
 
cl_demo_output=>display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows the effect of the extended mode, that is switched on by default and might lead to unexpected results. All replacements yield the same result `a-b` except the one in `r5`, where the line break character is not found but instead all empty spaces are replaced by the replacement character `-`. The reason is that the pattern `|\n|` consists of nothing but the line break character and this is ignored in the extended mode. Therefore, the pattern is in fact an empty string and yields the same result as specifying an empty string directly. By switching off the extended mode with `(?-x)`, the linebreak character is not ignored and yields the same result as the special PCRE character `\n`, which is expressed in different ways here.

``` abap
FINAL(text) =  `a` && |\n| && `b`. 
 
FINAL(r0) = replace( val = text sub  = |\n|        with = '-' occ = 0 ). 
 
FINAL(r1) = replace( val = text pcre = `\n`        with = '-' occ = 0 ). 
FINAL(r2) = replace( val = text pcre = `(?-x)\n`   with = '-' occ = 0 ). 
FINAL(r3) = replace( val = text pcre = |\\n|       with = '-' occ = 0 ). 
FINAL(r4) = replace( val = text pcre = |(?-x)\\n|  with = '-' occ = 0 ). 
FINAL(r5) = replace( val = text pcre = |\n|        with = '-' occ = 0 ). 
FINAL(r6) = replace( val = text pcre = |(?-x)\n|   with = '-' occ = 0 ). 
 
FINAL(re) = replace( val = text pcre = ``          with = '-' occ = 0 ). 
 
ASSERT r0 = r1. 
ASSERT r0 = r2. 
ASSERT r0 = r3. 
ASSERT r0 = r4. 
ASSERT r0 = r6. 
 
ASSERT re = r5. 
 
cl_demo_output=>new( 
  )->write( r0 
  )->write( r5 )->display( ).
```

## Executable Examples

- [PCRE Regular Expression with Callouts](abenpcre_callout_abexa.md)

- [Parsing with PCRE Regular Expression](abenpcre_parsing_abexa.md)

**Copyright Note**

This software uses the [PCRE2](https://www.pcre.org/) library under the [PCRE2 LICENCE](https://github.com/rurban/pcre/blob/master/LICENCE).

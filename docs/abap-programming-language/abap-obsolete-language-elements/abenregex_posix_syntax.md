---
title: "regex - POSIX Syntax (obsolete)"
source_file: abenregex_posix_syntax.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - POSIX Syntax (obsolete)

Regular expressions with POSIX syntax can be specified after the addition `REGEX` in obsolete variants of the statements [`FIND` and `REPLACE`](abapfind_replace_regex_obs.md) and the obsolete parameter [`regex`](abenstring_functions_regex_obs.md) of built-in functions for strings. Objects for POSIX regular expressions can be created with the obsolete factory method `CREATE_POSIX` of the system class [`CL_ABAP_REGEX`](../abap-processing-internal-data/abenregex_system_classes.md) to be used in statements [`FIND`](../abap-processing-internal-data/abapfind.md) and [`REPLACE`](../abap-processing-internal-data/abapreplace.md) or with the system class [`CL_ABAP_MATCHER`](../abap-processing-internal-data/abenregex_system_classes.md).

The POSIX syntax of regular expressions distinguishes the following cases:

- [Single character patterns](abenregex_posix_syntax_signs.md)

- [Character string patterns](abenregex_posix_syntax_operators.md)

- [Search patterns](abenregex_posix_search.md)

- [Replace patterns](abenregex_posix_replace.md)

- [Simplified regular expressions](abenregex_posix_simple.md)

Using the POSIX syntax for single characters and character strings, regular expressions can be created that match entire character strings or substrings of character strings. The POSIX syntax for find and replace offers some additional elements that support the finding and replacement of substrings in character strings.

The special characters that are valid in regular expressions according to POSIX are summarized in:

- [Special Characters in Regular Expressions](abenregex_posix_syntax_specials.md)

Regular expressions in POSIX syntax are obsolete. Using regular expressions in POSIX syntax leads to a warning from the syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that regular expressions are [migrated](../abap-processing-internal-data/abenregex_migrating_posix.md) from POSIX to [PCRE](../abap-processing-internal-data/abenregex_pcre_syntax.md) or another regular expression syntax supported by ABAP.

## Hints

- The PCRE syntax is more powerful than the POSIX syntax. Furthermore, PCRE regular expressions generally perform better than the POSIX regular expressions supported by ABAP.

- Creating objects of class `CL_ABAP_REGEX` with the operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) also creates instances for POSIX regular expressions.

**Copyright Note**

This software uses [Version 1.31](http://www.boost.org/doc/libs/1_31_0/libs/regex/doc/index.html) of the Boost.Regex Library. Copyright (c) 1998-2003 Dr. John Maddock. Attributes of the standard not yet support in this version are [listed here](http://www.boost.org/doc/libs/1_31_0/libs/regex/doc/standards.html).

The syntax and semantics described here may differ from other regular expression implementations based on the POSIX standard, or even the Boost 1.31 regular expression library in a different configuration.

---
title: "Regular Expressions (regex)"
source_file: abenregular_expressions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Regular Expressions (regex)

A regular expression `r` is made up of literal characters and special characters in accordance with the [syntax of regular expressions](abenregex_syntax.md) and represents a set of character strings. If `text` is one of the character strings represented by `r`, it means that `r` matches `text` or that `r` fits `text`. Two different regular expressions are the same if they match the same set of character strings.

ABAP supports the following kinds of extended [regular expressions](../../abap-glossary/abenregular_expression_glosry.md):

- [Perl Compatible Regular Expressions (PCRE)](../../abap-glossary/abenpcre_glosry.md) in [PCRE syntax](abenregex_pcre_syntax.md)

- [XPath regular expressions](../../abap-glossary/abenxpath_regex_glosry.md) in [XPath syntax](abenregex_xpath_syntax.md)

- [XSD regular expressions](../../abap-glossary/abenxsd_regex_glosry.md) in [XSD syntax](abenregex_xsd_syntax.md)

- [POSIX regular expressions](../../abap-glossary/abenposix_regex_glosry.md) in [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) (obsolete)

For Perl and POSIX regular expressions, respective libraries are implemented in [ABAP Kernel](../../abap-glossary/abenkernel_glosry.md):

- The [PCRE2 library](https://www.pcre.org/) is implemented for PCRE regular expressions.

- [Version 1.31 of the Boost.Regex Library](http://www.boost.org/doc/libs/1_31_0/libs/regex/doc/index.html) is implemented for POSIX regular expressions (obsolete).

XPath and XSD regular expressions are internally converted into Perl syntax by the ABAP runtime framework.

Regular expressions can be used for [searching, replacing and matching](abenregex_mtch.md) character strings. To do so, regular expressions can be specified in statements and built-in functions for character string processing:

- For all kinds of regular expressions, objects of system class [`CL_ABAP_REGEX`](abenregex_system_classes.md) can be created. Those objects can be used with the addition [`REGEX`](abapfind_pattern.md) of the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) and with the system class [`CL_ABAP_MATCHER`](abenregex_system_classes.md).

- The following language elements address specific regular expressions:

  - For PCRE regular expressions, the addition [`PCRE`](abapfind_pattern.md) can be used in the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md). The parameter [`pcre`](abenstring_functions_regex.md) can be used in built-in functions for strings.

  - For XPath regular expressions, the parameter [`xpath`](abenstring_functions_regex.md) can be used in some built-in functions for strings.

  - For POSIX regular expressions, the addition `REGEX` can be used in obsolete variants of the statements [`FIND` and `REPLACE`](../abap-obsolete-language-elements/abapfind_replace_regex_obs.md) and the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used in built-in functions for strings.

Regular expressions in [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that [regular expressions are migrated from POSIX to PCRE](abenregex_migrating_posix.md) or another regular expression syntax supported by ABAP.

## Hints

- A regular expression can have correct syntax but be too complex for to be executed, which raises a catchable exception of the class `CX_SY_REGEX_TOO_COMPLEX`. See [Exceptions in Regular Expressions](abenregex_exceptions.md).

- [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) also support regular expressions with the built-in functions [`REPLACE_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md), [`LIKE_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md), and [`OCCURRENCES_REGEXPR`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_string.md). These functions access the PCRE1 library implemented in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

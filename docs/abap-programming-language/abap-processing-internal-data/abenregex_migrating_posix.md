---
title: "regex - Migrating from POSIX to PCRE"
source_file: abenregex_migrating_posix.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Migrating from POSIX to PCRE

The ABAP Kernel of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) implements two libraries for regular expressions:

- The [PCRE2 library](https://www.pcre.org/) for [PCRE regular expressions](../../abap-glossary/abenpcre_regex_glosry.md).

- [Version 1.31 of the Boost.Regex Library](http://www.boost.org/doc/libs/1_31_0/libs/regex/doc/index.html) for [POSIX regular expressions](../../abap-glossary/abenposix_regex_glosry.md) (obsolete).

Regular expressions in [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. Therefore, it is recommended that regular expressions are migrated from POSIX to [PCRE syntax](abenregex_pcre_syntax.md) or another regular expression syntax supported by ABAP.

The following table provides a general troubleshooting for migrating from POSIX to PCRE:

| **Symptom**                                                                                    | **Possible Solutions**                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The PCRE library rejects the pattern (e.g. by giving a compiler error or raising an exception) | Make sure to not use any features that are supported by POSIX but not by PCRE. Also pay close attention to the error message, which often contains useful information.                                           |
| The pattern does not match what it should after migrating to PCRE                              | Make sure that you have taken PCRE's extended mode into account by either explicitly encoding whitespaces or by disabling extended mode. Ensure that you have set the correct Unicode handling for your context. |

The following topics provide detailed assistance for the migration from POSIX to PCRE.

- [Incompatibilities between POSIX and PCRE](abenregex_posix_pcre_incompat.md)

- [New features in PCRE compared to POSIX](abenregex_posix_pcre_improve.md)

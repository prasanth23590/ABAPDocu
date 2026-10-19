---
title: "Obsolete Regular Expression Syntax"
source_file: abenregular_expressions_obsolete.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Obsolete Regular Expression Syntax

ABAP supports several [syntax flavors](../abap-processing-internal-data/abenregex_syntax.md) for [regular expressions](../../abap-glossary/abenregular_expression_glosry.md). Because of these, the [POSIX syntax](abenregex_posix_syntax.md) is obsolete.

Using regular expressions in POSIX syntax leads to a warning from the syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that regular expressions are [migrated](../abap-processing-internal-data/abenregex_migrating_posix.md) from POSIX to [PCRE](../abap-processing-internal-data/abenregex_pcre_syntax.md) or another regular expression syntax supported by ABAP.

The PCRE syntax is more powerful than the obsolete POSIX syntax. Furthermore, PCRE regular expressions generally perform better than the POSIX regular expressions supported by ABAP.

- [POSIX regular expression](abenregex_posix_syntax.md).

- [`FIND, REPLACE REGEX posix`](abapfind_replace_regex_obs.md)

- [`string_func - regex`](abenstring_functions_regex_obs.md)

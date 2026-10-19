---
title: "regex - Syntax"
source_file: abenregex_syntax.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Syntax

A [regular expression](https://en.wikipedia.org/wiki/Regular_expression) is a pattern of literal and special characters that describes a set of character strings. The syntax of regular expressions is widely standardized but there are differences between common standards as [Perl](https://www.perl.org/) or [POSIX](https://en.wikipedia.org/wiki/POSIX) and different syntax flavors as [XPath](https://www.w3.org/TR/xquery-operators/#regex-syntax) or [XSD](https://www.w3.org/XML/2008/03/xsdl-regex/re.xml) regular expressions.

The following topics describe the syntax of regular expressions that can be used in ABAP behind additions `PCRE|REGEX` in statements, for parameters `pcre|regex|xpath` of built-in functions and with the [system classes for regular expressions](abenregex_system_classes.md).

- [PCRE syntax](abenregex_pcre_syntax.md)

- [XPath syntax](abenregex_xpath_syntax.md)

- [XSD syntax](abenregex_xsd_syntax.md)

- [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) (obsolete)

ABAP specific restrictions or modifications to the standard syntax might apply.

## Hints

- Regular expressions in [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that [regular expressions are migrated from POSIX to PCRE](abenregex_migrating_posix.md) or another regular expression syntax supported by ABAP.

- The PCRE syntax is more powerful than the POSIX syntax. Furthermore, PCRE regular expressions generally perform better than the POSIX regular expressions supported by ABAP.

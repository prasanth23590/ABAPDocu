---
title: "regex - XSD Syntax"
source_file: abenregex_xsd_syntax.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - XSD Syntax

Objects for XSD regular expressions can be created with the factory method `CREATE_XSD` of the system class [`CL_ABAP_REGEX`](abenregex_system_classes.md) to be used in statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) or with the system class [`CL_ABAP_MATCHER`](abenregex_system_classes.md).

Currently, there is no detailed description of the XSD syntax for regular expressions in the ABAP keyword documentation.

- For a short syntax overview, see

  [Special Characters in XSD Regular Expressions](abenregex_xsd_syntax_specials.md)

- For the complete documentation, refer to

  [Regular expressions in XSD 1.0 and 1.1](https://www.w3.org/XML/2008/03/xsdl-regex/re.xml).

## Hints

- A regular expression with XSD syntax cannot be specified directly as a character string in the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md), but you can use objects of `CL_ABAP_REGEX` that are created with method `CREATE_XSD` with the addition [`REGEX`](abapfind_pattern.md) instead.

- XSD Syntax is a subset of [XPath syntax](abenregex_xpath_syntax.md). There are mainly the following differences:

  - In a XSD regular expression, `^` and `$` are not special characters for start and end of a line.

  - There is no XSD syntax for non-greedy behavior.

  - There is no XSD syntax for subgroups without registration

  - There is no XSD syntax for back references

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example uses XSD syntax that is invalid for [PCRE](abenregex_pcre_syntax.md) and does not find any matches for [POSIX](../abap-obsolete-language-elements/abenregex_posix_syntax.md). It would work also for [XPath](abenregex_xpath_syntax.md). The regular expression contains special characters `\i` and `\c` that match any character that can be the first character of an XML name or any character that can occur after the first character of an XML name. The result of the replacement is `<ns:tag1><ns:tag2>...</ns:tag2></ns:tag1>`.

``` abap
DATA(xml) = `<tag1><tag2>...</tag2></tag1>`. 
 
REPLACE ALL OCCURRENCES OF 
        REGEX cl_abap_regex=>create_xsd( pattern = `\i\c*` ) 
        IN xml WITH `ns:$0`.
```

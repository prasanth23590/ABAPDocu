---
title: "regex - System Classes"
source_file: abenregex_system_classes.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - System Classes

The system classes for regular expressions are `CL_ABAP_REGEX` and `CL_ABAP_MATCHER`. Both are documented in the class library.

- [`CL_ABAP_REGEX`](abenregex_system_classes.md#cl_abap_regex)

- [`CL_ABAP_MATCHER`](abenregex_system_classes.md#cl_abap_matcher)

## `CL_ABAP_REGEX`

Factory methods of class `CL_ABAP_REGEX` create an object-oriented representation of a regular expression passed in a character-like field:

- `CREATE_PCRE` creates instances for regular expressions with [PCRE syntax](abenregex_pcre_syntax.md).

- `CREATE_XPATH2` creates instances for regular expressions with [XPath syntax](abenregex_xpath_syntax.md).

- `CREATE_XSD` creates instances for regular expressions with [XSD syntax](abenregex_xsd_syntax.md).

- `CREATE_POSIX` creates instances for regular expressions with [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) (obsolete).

Optional parameters allow further specifications for handling the regular expression:

- The Parameter `EXTENDED` for `CREATE_PCRE` and `CREATE_XPATH2` switches the extended mode for compiling PCRE and XPath expressions. The default value is `ABAP_TRUE`. In the extended mode, most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped The extended mode can also be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression.

- The Parameter `UNICODE_HANDLING` for `CREATE_PCRE` and `CREATE_XPATH2` defines how characters from the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md) are handled.

Instances of `CL_ABAP_REGEX` can be used with the class `CL_ABAP_MATCHER` and with the addition `REGEX` of the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md).

### Hints

- The class `CL_ABAP_REGEX` can also be instantiated with the operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md), but this is deprecated. Such a direct instantiation of `CL_ABAP_REGEX` creates instances for regular expressions with [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md). Instead of direct instantiation, the above factory methods `CREATE_PCRE`, `CREATE_POSIX`, `CREATE_XPATH2` or `CREATE_XSD` should be used.

- Instances of `CL_ABAP_REGEX` for all kinds of regular expressions, PCRE, XPath, XSD and POSIX (obsolete) can be used with the addition `REGEX` of the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md). This circumvents the restriction that regular expressions of XPath and XSD syntax cannot be specified directly as character strings.

- Instances of `CL_ABAP_REGEX` cannot be used with the addition `PCRE` of the statements `FIND` and `REPLACE`.

- Regular expressions in [POSIX syntax](../abap-obsolete-language-elements/abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that [regular expressions are migrated from POSIX to PCRE](abenregex_migrating_posix.md) or another regular expression syntax supported by ABAP.

### Executable Example

[Search for a regular expression](abenregex_abexa.md)

## `CL_ABAP_MATCHER`

The class `CL_ABAP_MATCHER` applies regular expressions to either a character string or an internal table. Its methods allow finding, replacing or matching regular expressions. Instances of `CL_ABAP_MATCHER` can be created either with factory methods of the class itself or with the method `CREATE_MATCHER` of the class `CL_ABAP_REGEX`. The latter allows the use of the same regular expression multiple times for different texts.

The class `CL_ABAP_MATCHER` stores the current state of text processing. The current processing state can be queried using different `GET_...` methods.

For [PCRE syntax](abenregex_pcre_syntax.md), the class `CL_ABAP_MATCHER` supports callouts. With the method `SET_CALLOUT` a handler class can be registered that implements the interface `IF_ABAP_MATCHER_CALLOUT`. The [special characters](abenregex_pcre_syntax_specials.md) `(?C...)` of a PCRE regular expression then call the interface method `CALLOUT` when the method `MATCH` is executed.

### Hint

If a regular expression has to be used several times, it is preferable to work with objects of `CL_ABAP_MATCHER` created with `CL_ABAP_REGEX`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An object of `CL_ABAP_MATCHER` is created with the method `CREATE_MATCHER` of an instance of the class `CL_ABAP_REGEX` that represents a regular expression with PCRE syntax. Depending on a successful match, the registered subgroups of submatches are received and displayed.

``` abap
FINAL(matcher) = 
  cl_abap_regex=>create_pcre( pattern = '(\d\d\d)(\D\D\D)(\d\d\d)' 
                              ignore_case = 'X' 
              )->create_matcher( text = '123abc456' ). 
 
IF matcher->match( ). 
  DO. 
    TRY. 
        cl_demo_output=>write( matcher->get_submatch( sy-index ) ). 
      CATCH cx_sy_invalid_submatch. 
        EXIT. 
    ENDTRY. 
  ENDDO. 
ENDIF. 
 
cl_demo_output=>display( ).
```

## Executable Examples

- [PCRE Regular Expression with Callouts](abenpcre_callout_abexa.md)

- [Parsing with PCRE Regular Expression](abenpcre_parsing_abexa.md)

- [XPath Regular Expression](abenxpath_regex_abexa.md)

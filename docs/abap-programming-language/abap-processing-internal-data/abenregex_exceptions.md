---
title: "regex - Exceptions"
source_file: abenregex_exceptions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Exceptions

Invalid regular expressions that are known statically lead to syntax errors. Errors that are recognized during processing lead to catchable exceptions of classes `CX_SY_REGEX_...` or `CX_SY_..._REGEX...`. Such exceptions can occur due to invalid syntax or invalid operations.

A special exception can occur for a regular expression that has correct syntax but is too complex. Then, it cannot be executed by the libraries that are integrated in the ABAP Kernel and an exception of the class `CX_SY_REGEX_TOO_COMPLEX` is raised.

A regular expression is too complex if the number of transitions exceeds a certain limit. This is usually the case for regular expressions that have been programmed disadvantageously or are inadequate because they would lead to extensive backtracking for certain texts.

## Hints

- The occurrence of the `CX_SY_REGEX_TOO_COMPLEX` exception depends on both the regular expression and the text to be matched. A regular expression that works for one text may raise an exception for another text.

- As a rule, [POSIX regular expressions](../../abap-glossary/abenposix_regex_glosry.md) (obsolete) are more vulnerable to this error situation than [PCRE regular expressions](../../abap-glossary/abenpcre_regex_glosry.md). Therefore, it is recommended that [POSIX regular expressions are migrated to PCRE](abenregex_migrating_posix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code section demonstrates that a rather simple regular expression `.*X.*` leads to an exception in the POSIX library if the text is several hundred characters or longer. This is a result of the [leftmost-longest rule](../abap-obsolete-language-elements/abenregex_posix_search.md) and the greedy behavior of the [chaining operator](../abap-obsolete-language-elements/abenregex_posix_syntax_operators.md) `*` where all occurrences of substrings that match the first part of the regular expression (`.*`) are saved internally until the last *X* has been found. In POSIX regular expressions, a chaining like `.*`, which matches any number of substrings, should therefore be avoided at the beginning of a regular expression. In the PCRE library, the same combination of regular expression and text does not lead to an exception. Nevertheless, the last part of the example shows that unfavorable combinations can also lead to an exception in the PCRE library.

``` abap
FINAL(text) = repeat( val = `a` occ = `500` ). 
 
TRY. 
    FIND REGEX `.*X.*` IN text MATCH OFFSET DATA(moff) ##regex_posix. 
    IF sy-subrc = 0. 
      cl_demo_output=>write( |POSIX, offset: { moff }| ). 
    ELSE. 
      cl_demo_output=>write( |POSIX, nothing found| ). 
    ENDIF. 
  CATCH cx_sy_regex_too_complex INTO DATA(exc). 
    cl_demo_output=>write( |POSIX: { exc->get_text( ) }| ). 
ENDTRY. 
 
TRY. 
    FIND PCRE `.*X.*` IN text MATCH OFFSET moff. 
    IF sy-subrc = 0. 
      cl_demo_output=>write( |PCRE, offset: { moff }| ). 
    ELSE. 
      cl_demo_output=>write( |PCRE, nothing found| ). 
    ENDIF. 
  CATCH cx_sy_regex_too_complex INTO exc. 
    cl_demo_output=>write( |PCRE: { exc->get_text( ) }| ). 
ENDTRY. 
 
TRY. 
    FIND PCRE 
      `(*LIMIT_DEPTH=1)(*LIMIT_MATCH=1)(*NO_START_OPT)(a+a+a+a+a+)+b` 
      IN text MATCH OFFSET moff. 
    IF sy-subrc = 0. 
      cl_demo_output=>write( |PCRE, offset: { moff }| ). 
    ELSE. 
      cl_demo_output=>write( |PCRE, nothing found| ). 
    ENDIF. 
  CATCH cx_sy_regex_too_complex INTO exc. 
    cl_demo_output=>write( |PCRE: { exc->get_text( ) }| ). 
ENDTRY. 
 
 
cl_demo_output=>display( ).
```

In the case of `.*X.*`, a search is successful for every character string that contains at least one *X* and any number of other characters. For such a search, the use of a regular expression is not necessary at all and can be replaced by

``` abap
FIND SUBSTRING 'X' IN text. 
IF sy-subrc = 0. 
  ... 
ENDIF.
```

or by

``` abap
IF text CS 'X'. 
  ... 
ENDIF.
```

---
title: "cstring_func - regex (Obsolete)"
source_file: abenstring_functions_regex_obs.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - regex (Obsolete)

## Syntax

``` abap
... ( ... regex = posix ...  ) ...  
```

## Description

In [string functions](../abap-processing-internal-data/abenstring_functions.md), where the parameters [`pcre`](../abap-processing-internal-data/abenstring_functions_regex.md) or [`xpath`](../abap-processing-internal-data/abenstring_functions_regex.md) can be used, the parameter `regex` is also possible. `posix` is then a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) that must contain a [POSIX regular expression](abenregex_posix_syntax.md).

## Hint

Regular expressions in [POSIX syntax](abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that [regular expressions are migrated from POSIX to PCRE](../abap-processing-internal-data/abenregex_migrating_posix.md) or another regular expression syntax supported by ABAP.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function call is `<tag>def</tag>`. The POSIX regular expression is greedy and special care must be taken to find the desired substring between the tags.

``` abap
cl_demo_output=>display( 
  replace( val   = `<tag>abc</tag>` 
           regex = `(<tag>)[^<]+(</tag>)` ##regex_posix 
           with  = `$1def$2` ) ).
```

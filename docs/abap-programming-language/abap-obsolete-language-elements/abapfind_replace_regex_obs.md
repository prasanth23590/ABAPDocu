---
title: "FIND, REPLACE REGEX posix (obsolete)"
source_file: abapfind_replace_regex_obs.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND, REPLACE REGEX posix (obsolete)

## Syntax

``` abap
FIND|REPLACE REGEX posix ... .  
```

## Description

In this variant for specifying a [pattern](../abap-processing-internal-data/abapfind_pattern.md) in the statements [`FIND`](../abap-processing-internal-data/abapfind.md) and [`REPLACE`](../abap-processing-internal-data/abapreplace.md), a character string `posix` is specified behind `REGEX` instead of a reference variable [`regex_ref`](../abap-processing-internal-data/abapfind_pattern.md).

`posix` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) that can contain a valid [POSIX regular expression](abenregex_posix_syntax.md).

The occurrences are determined according to the *leftmost-longest* rule. Of all possible matches between the regular expression and the character string to be searched, the substring that starts at the furthest position to the left is selected. If there are multiple matches at this position, the longest of these substrings is selected.

## Hint

Regular expressions in [POSIX syntax](abenregex_posix_syntax.md) are obsolete. Using regular expressions in POSIX syntax leads to a warning from syntax check that can be hidden by the pragma `##regex_posix`. It is recommended that [regular expressions are migrated from POSIX to PCRE](../abap-processing-internal-data/abenregex_migrating_posix.md) or another regular expression syntax supported by ABAP.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The search uses obsolete POSIX regular expression syntax and finds the substring `'ababb'` from offset 3. The substring `'babboo'` from offset 4, which also matches, is not found because of the leftmost-longest rule of POSIX regular expressions.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(text) = `oooababboo`. 
 
FIND REGEX 'a.|[ab]+|b.*' IN text ##regex_posix 
     MATCH OFFSET FINAL(moff) 
     MATCH LENGTH FINAL(mlen). 
IF sy-subrc = 0. 
  out->write( substring( val = text off = moff 
                                    len = mlen ) ). 
ENDIF. 
 
out->display( ).
```

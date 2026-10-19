---
title: "cstring_func - replace"
source_file: abenreplace_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - replace

## Syntax

``` abap
1. ... replace( val = text [off = off] [len = len] 
               with = new ) ...  

2. ... replace( val = text {sub = substring}|{pcre = regex} 
               with = new [case = case] [occ = occ] ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`off = off`](abenstring_functions_off_len.md) · [`len = len`](abenstring_functions_off_len.md) · [`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`pcre = regex`](abenstring_functions_regex.md) · [`case = case`](abenstring_functions_case.md) · [`occ = occ`](abenstring_functions_occ.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) replaces a substring of [`text`](abenstring_functions_val.md) with the character string specified in `new` and returns the changed text.

The substring is determined as follows:

- The variant with the parameters [`off`](abenstring_functions_off_len.md) and [`len`](abenstring_functions_off_len.md) replaces the substring determined by the offset `off` and the length `len`. At least one of these additions must be defined.

- The variant with the parameters `sub` or [`pcre`](abenstring_functions_regex.md) searches the `text` for the occurrence specified in [`occ`](abenstring_functions_occ.md) for a match with the substring specified in [`substring`](abenstring_functions_sub.md) or with a [regular expression](abenregex_syntax.md) specified in [`regex`](abenstring_functions_regex.md) and replaces the occurrence.

  `regex` must contain a [PCRE regular expression](abenregex_pcre_syntax.md). A regular expression in PCRE syntax is compiled in an extended mode: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes and comments can be placed behind `#`. In order to include whitespace and `#` into a pattern, they must be escaped or the extended mode must be switched of with [`(?-x)`](abenregex_pcre_syntax_specials.md) in the regular expression. If `occ` contains the value 0, all occurrences are replaced. If `substring` is empty, an exception of the class `CX_SY_STRG_PAR_VAL` is raised. Note that a character string in `substring` of a fixed length containing only blanks is handled like an empty string. This also applies to the predefined constant `space`. For more information, refer to [Trailing Blanks in Character String Processing](abenstring_processing_trail_blanks.md). The search is case-sensitive by default, but this can be overridden using the parameter `case`. If no substring is found, the unchanged content of `text` is returned.

`new` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). If this has a fixed length, trailing blanks are ignored.

The return value has the type `string`.

## Hints

- Borderline cases for the variants with the parameters `off` and `len`:

  - If only `off` is specified or if the value 0 is specified for `len`, `replace` works like the [`insert`](abeninsert_functions.md) function.

  - If only `len` is specified or if `off` has the value 0, the first segment of the length `len` is replaced.

  - If the value of `off` is equal to the length of `text`, the value of `len` must be equal to 0 or `len` is not specified. The character string `new` is then appended to the end of `text`.

- If a regular expression is used with [`regex`](abenstring_functions_regex.md), special [replacement patterns](../abap-obsolete-language-elements/abenregex_posix_replace.md) that allow references to the respective occurrences can be specified in `new`. It should be noted that in regular replacement texts, the associated special characters `$`, `&`, \`\`\`, and `&#x00B4;` as well as the escape character `\` must be transformed to literal characters using the prefix `\`.

- Besides `pcre`, also the obsolete parameter [`regex`](../abap-obsolete-language-elements/abenstring_functions_regex_obs.md) can be used. Then an obsolete [POSIX regular expression](../abap-obsolete-language-elements/abenregex_posix_syntax.md) must be passed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following replacement is

aa_XX_cc

The substring *bb* starting at offset 3 having a length of 2 is replaced with *XX*.

``` abap
DATA(text) = `aa-bb-cc`. 
cl_demo_output=>write( text ). 
 
text = replace( val = text off = 3 len = 2 with = `XX` ). 
cl_demo_output=>write( text ). 
 
cl_demo_output=>display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following replacements are

aa_bb_cc

and

aabbcc

First, all occurrences (`occ = 0`) of substring *-* are replaced with *\_*, then these are replaced by an empty string, hence removed.

``` abap
DATA(text) = `aa-bb-cc`. 
cl_demo_output=>write( text ). 
 
text = replace( val = text sub = `-` with = `_`  occ = 0 ). 
cl_demo_output=>write( text ). 
 
text = replace( val = text sub = `_` with = ``  occ = 0 ). 
cl_demo_output=>write( text ). 
 
cl_demo_output=>display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following replacement is

``` abap
<title>Th<b>i</b>s <b>i</b>s the <i>T<b>i</b>tle</i></title>\.
```

In an HTML line, a particular letter is surrounded by format tags if it is not within a tag itself.

``` abap
DATA(html) = `<title>This is the <i>Title</i></title>`. 
FINAL(repl)   = `i`. 
 
html = replace( val  = html 
                pcre = repl && `(?![^<>]*>)` 
                with = `<b>$0</b>` 
                occ  =   0 ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Illegal offset or length specified in `off` and `len`.

  *Runtime error:* `STRING_OFFSET_TOO_LARGE`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* More information: [Exceptions in Regular Expressions](abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_STRG_PAR_VAL`

- *Cause:* Substring in `sub` or regular expression in `regex` is empty.

  *Runtime error:* `STRG_ILLEGAL_PAR`

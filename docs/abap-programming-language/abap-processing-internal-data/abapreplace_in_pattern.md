---
title: "REPLACE pattern IN"
source_file: abapreplace_in_pattern.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > REPLACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE pattern IN

## Syntax

``` abap
REPLACE [{FIRST OCCURRENCE}| {ALL OCCURRENCES} OF] pattern   
        IN [section_of] dobj WITH new   
        [IN {CHARACTER|BYTE} MODE]   
        [replace_options].  
```

[`pattern`](abapreplace_pattern.md) · [`section_of`](abapfind_section_of.md) · [`replace_options`](abapreplace_options.md)

### Addition

[1. `... {FIRST OCCURRENCE}|{ALL OCCURRENCES} OF`](abapreplace_in_pattern.md#addition-1)

[2. `... IN {CHARACTER|BYTE} MODE`](abapreplace_in_pattern.md#addition-2)

## Overview

### Description

In pattern-based replacements, the data object `dobj` is searched for the character or byte strings specified in [`pattern`](abapreplace_pattern.md) and the occurrences are replaced by the content of the operand `new`. `new` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

If a regular expression is used in `pattern`, special [replacement patterns](../abap-obsolete-language-elements/abenregex_posix_replace.md) can be specified in `new` that allow a reference to the respective occurrence. It should be noted that, in regular replacement texts, the associated special characters `$`, `&`, \`\`\`, and `&#x00B4;` as well as the escape character `\` must be transformed to literal characters using the prefix `\`.

The syntax and effect of the addition [`section_of`](abapfind_section_of.md) are the same as searching a data object for a substring using the statement [`FIND`](abapfind.md), and the same catchable exception can be raised. The addition `MODE` defines whether a character or byte string is processed, and the addition [`replace_options`](abapreplace_options.md) provides additional options for controlling and evaluating the statement.

### Hint

The statement [`REPLACE IN TABLE`](abapreplace_itab.md) can be used to make replacements in internal tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the replacement is *\$bcd\$*. While `$1` in the replacement pattern represents the parenthesized subgroup `bcd` of the regular expression `a(bcd)e`, the two `\$` stand for the literal character *\$*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `abcde`. 
REPLACE PCRE `a(bcd)e` IN str WITH `\$$1\$`. 
out->write( str ). 
 
out->display( ).
```

## Addition 1

`... {FIRST OCCURRENCE}|{ALL OCCURRENCES} OF`

### Description

The optional addition `{FIRST OCCURRENCE}|{ALL OCCURRENCES} OF` specifies whether only the first occurrence or all occurrences of the search pattern are replaced by the content of `new`. If the addition `FIRST OCCURRENCE` or none of the additions are specified, the first occurrence is replaced. If `ALL OCCURRENCES` is used, all non-overlapping occurrences are replaced.

If `substring` is an empty string in [`pattern`](abapreplace_pattern.md) or is of the type `c`, `n`, `d`, or `t` and only contains blanks, the place in front of the first character or byte of the search range is found when searching for the first occurrence, and the content of `new` is inserted in front of the first character or byte. When searching for all occurrences, the exception `CX_SY_REPLACE_INFINITE_LOOP` is raised in this case.

If `regex` contains a [regular expression](abenregex_syntax.md) in [`pattern`](abapreplace_pattern.md) that matches the empty character string, the content of `new` is also inserted in front of the first character when searching for the first occurrence. When searching for all occurrences, the content of `new` is inserted in front of the first character in all spaces that are not in front of or inside a match, and after the last character.

### Hint

If the addition `ALL OCCURRENCES` is used, no recursive processing takes place. This means that, if the statement finds further occurrences of the search pattern, they are not replaced automatically, since this could create endless loops.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the replacement, `text` contains the value *x-xx-x*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA text TYPE string VALUE '-uu-'. 
 
REPLACE ALL OCCURRENCES OF PCRE 'u*' IN text WITH 'x'. 
 
out->write( text ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the replacement, `text` still contains the substring *abcde* once.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA text TYPE string VALUE 'xxababcdcdxx'. 
 
REPLACE ALL OCCURRENCES OF 'abcd' IN text WITH ``. 
 
out->write( text ). 
 
out->display( ).
```

## Addition 2

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is performed. Depending on the processing type, `dobj`, `new`, and `substring` in [`pattern`](abapreplace_pattern.md) must be character-like or byte-like. If [regular expressions](abenregex_syntax.md) are used in `pattern`, only character string processing is allowed.

### Hint

For replacements with character-like content that contains trailing blanks, `new` must have the data type `string`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement of all bytes that represent a hyphen in code page UTF-8 with bytes for an underscore.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(xstr) = cl_abap_conv_codepage=>create_out(  )->convert( `a-b-c` ). 
REPLACE ALL OCCURRENCES OF CONV xstring( `2D` ) IN xstr 
                      WITH CONV xstring( `5F` ) IN BYTE MODE. 
out->write( 
  cl_abap_conv_codepage=>create_in( )->convert( xstr ) ). 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_REPLACE_INFINITE_LOOP`

- *Cause:* Substring of length **0** creates an endless loop when searching for all occurrences.

  *Runtime error:* `REPLACE_INFINITE_LOOP`

`CX_SY_INVALID_REGEX`

- *Cause:* Invalid expression after the addition `PCRE|REGEX`.

  *Runtime error:* `INVALID_REGEX`

`CX_SY_REGEX_TOO_COMPLEX`

- *Cause:* See [Exceptions in Regular Expressions](abenregex_exceptions.md).

  *Runtime error:* `REGEX_TOO_COMPLEX`

`CX_SY_INVALID_REGEX_FORMAT`

- *Cause:* Invalid [replacement pattern](../abap-obsolete-language-elements/abenregex_posix_replace.md) after the addition `WITH`.

  *Runtime error:* `INVALID_FORMAT`

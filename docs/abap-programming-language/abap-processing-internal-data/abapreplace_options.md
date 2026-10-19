---
title: "REPLACE, options"
source_file: abapreplace_options.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > REPLACE > REPLACE pattern IN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE, options

## Syntax

``` abap
... [VERBATIM]   
    [RESPECTING|IGNORING CASE]   
    [REPLACEMENT COUNT rcnt]   
    { {[REPLACEMENT OFFSET roff]   
       [REPLACEMENT LENGTH rlen]}   
    | [RESULTS result_tab|result_wa] } ...  
```

### Addition

[1. `... VERBATIM`](abapreplace_options.md#addition-1)

[2. `... RESPECTING|IGNORING CASE`](abapreplace_options.md#addition-2)

[3. `... REPLACEMENT COUNT rcnt`](abapreplace_options.md#addition-3)

[4. `... REPLACEMENT OFFSET roff`](abapreplace_options.md#addition-4)

[5. `... REPLACEMENT LENGTH rlen`](abapreplace_options.md#addition-5)

[6. `... RESULTS result_tab|result_wa`](abapreplace_options.md#addition-6)

## Overview

### Description

These additions control the statement [`REPLACE pattern IN`](abapreplace_in_pattern.md) and provide extended evaluation options. The addition `CASE` can be used to determine whether the search is case-sensitive. The additions `REPLACEMENT` and `RESULTS` can be used to determine the number, position, and length of the strings replaced.

## Addition 1

`... VERBATIM`

### Description

The addition `VERBATIM` can only be used together with [`PCRE|REGEX`](abapreplace_pattern.md). It causes all characters in the operand `new` to be used literally. Special characters for replacement patterns have no effect.

### Hint

A `REPLACE` statement with addition `VERBATIM` is always faster than one without.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

While in the first `REPLACE` statement the `$` characters have a special meaning as operators for addressing subgroups, this is not the case when the addition `VERBATIM` is used in the second `REPLACE` statement. In the third `REPLACE` statement, the special characters are escaped using `\`. While the effect of escaping is the same as for the addition, the addition `VERBATIM` is faster.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(text1) = `123XXX456`. 
DATA(text2) = text1. 
DATA(text3) = text1. 
 
FINAL(regex) =  `(\d*)(\D*)(\d*)`. 
 
REPLACE PCRE regex IN text1 WITH `$1___$3`. 
REPLACE PCRE regex IN text2 WITH `$1___$3` VERBATIM. 
REPLACE PCRE regex IN text3 WITH `\$1___\$3`. 
 
out->write( |{ text1 }\n{ text2 }\n{ text3 }| ). 
 
out->display( ).
```

## Addition 2

`... {RESPECTING|IGNORING} CASE`

### Description

This addition is only allowed in character string processing. It has the same syntax and effect as the corresponding [addition](abapfind_options.md) for searching for a substring in a data object using the [`FIND`](abapfind.md) statement. This addition is not allowed when using an instance of class `CL_ABAP_REGEX`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacement of all uppercase characters in a string with a backquote. If `IGNORING CASE` were specified, all characters would be replaced.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `Hello`. 
REPLACE ALL OCCURRENCES OF PCRE `[A-Z]` IN str WITH '`' 
        RESPECTING CASE. 
out->write( str ). 
 
 
TYPES: 
  BEGIN OF result, 
    line   TYPE i, 
    offset TYPE i, 
    length TYPE i, 
  END OF result, 
  result_tab TYPE TABLE OF result WITH EMPTY KEY. 
 
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 5, 
    col2 TYPE c LENGTH 5, 
  END OF line, 
  itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
DATA(itab) = VALUE itab( FOR i = 1 UNTIL i > 5 
                       ( col1 = 'abcde' col2 = 'abcde' ) ). 
 
REPLACE ALL OCCURRENCES OF `cd` 
        IN TABLE itab 
        FROM 2 OFFSET 5 
        TO   4 OFFSET 5 
        WITH 'XX' 
        RESULTS FINAL(results). 
 
out->write( CORRESPONDING result_tab( results ) ). 
 
out->display( ).
```

## Addition 3

`... REPLACEMENT COUNT rcnt`

### Description

This addition saves the number of replacements made in data object `dobj` to `rcnt`. The following can be specified for `rcnt`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If no replacements are made, `rcnt` is set to 0.

### Hint

In data objects with a fixed length, the number of replacements made in data object `dobj` can be less than the number of occurrences.

## Addition 4

`... REPLACEMENT OFFSET roff`

### Description

This addition saves the [offset](../../abap-glossary/abenoffset_glosry.md) related to the data object `dobj` at which the last replacement was made to `roff`. The following can be specified for `roff`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If no replacement is made, `roff` retains its previous value or stays initial.

### Hints

- When `ALL OCCURRENCES` is used, `REPLACEMENT OFFSET` generally returns a different value than [`MATCH OFFSET`](abapfind_options.md) for the [`FIND`](abapfind.md) statement because the position of the last found location can be shifted by previous replacements.

- In data objects of fixed length, the value in `roff` refers to the last replacement within the data object. Occurrences that are shifted by previous replacements in the data object are no longer relevant.

## Addition 5

`... REPLACEMENT LENGTH rlen`

### Description

This addition saves the length of the last substring inserted into `dobj` to `rlen`. The following can be specified for `rlen`:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The declared variable has the data type `i`.

If no replacement is made, `rlen` retains its previous value or stays initial.

### Hint

In data objects with a fixed length, the length of the last inserted string can be shorter than the length of `new` if the interim result is truncated.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Pattern-based replacement of all occurrences of the substring *know* in the data objects `text1` and `text2` with *should know that*. After the first `REPLACE` statement, `text1` contains the complete content *I should know that you know* and `sy-subrc` contains 0. The data objects `cnt`, `off`, and `len` have the values 2, 23, and 16. After the second `REPLACE` statement, `text2` contains the truncated content *I should know that* and `sy-subrc` contains 2. The data objects `cnt`, `off`, and `len` have the values 1, 2, and 16.

``` abap
DATA: text1 TYPE string, 
      text2 TYPE c LENGTH 18. 
 
text1 = text2 = 'I know you know'. 
 
REPLACE ALL OCCURRENCES OF 'know' IN 
        text1 WITH 'should know that' 
              REPLACEMENT COUNT  DATA(cnt) 
              REPLACEMENT OFFSET DATA(off) 
              REPLACEMENT LENGTH DATA(len). 
 
REPLACE ALL OCCURRENCES OF 'know' IN 
        text2 WITH 'should know that' 
              REPLACEMENT COUNT  cnt 
              REPLACEMENT OFFSET off 
              REPLACEMENT LENGTH len.
```

## Addition 6

`... RESULTS result_tab|result_wa`

### Description

If at least one replacement is made, the `RESULTS` addition saves the offsets of the positions at which replacements were made and the lengths of the inserted substrings either in an internal table `result_tab` or in a structure `result_wa`. The syntax and meaning of the addition are otherwise the same as those for the identically named [addition](abapfind_options.md) for the [`FIND`](abapfind.md) statement, with the difference that the data types for `result_tab` and `result_wa` must be `REPL_RESULT_TAB` and `REPL_RESULT`, for which there is no `SUBMATCHES` component. As in `FIND`, an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) can be specified after `RESULTS`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A result table `results` is declared inline and supplied with the properties of the seven replaced characters.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(str) = `Diddeldummdideldei`. 
REPLACE ALL OCCURRENCES OF `d` IN str WITH 't' 
        IGNORING CASE 
        RESULTS FINAL(results). 
out->write( results ). 
 
out->display( ).
```

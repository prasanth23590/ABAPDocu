---
title: "CONCATENATE"
source_file: abapconcatenate.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONCATENATE

## Syntax

``` abap
CONCATENATE {dobj1 dobj2 ...}|{LINES OF itab}   
            INTO result   
            [IN {CHARACTER|BYTE} MODE]   
            [SEPARATED BY sep]   
            [RESPECTING BLANKS].  
```

### Addition

[1. `... IN {CHARACTER|BYTE} MODE`](abapconcatenate.md#addition-1)

[2. `... SEPARATED BY sep`](abapconcatenate.md#addition-2)

[3. `... RESPECTING BLANKS`](abapconcatenate.md#addition-3)

## Overview

### Description

Concatenates either the content of the data objects `dobj1, dobj2, ...` or the lines of the internal table `itab` in accordance with their order and assigns them to the target field `result`. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The following can be specified for the target field `result`:

- An existing character-like or byte-like variable to which the result of the concatenation can be converted.

- An inline declaration with [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). If `IN CHARACTER MODE` is used, the declared variable is of the type `string`; if `IN BYTE MODE` is used, it is of the type `xstring`.

If the target field `result` has a fixed length and this is greater than the required length, it is padded on the right with blanks or hexadecimal 0. If the target field is too short, the concatenation is truncated on the right. If the target field is a string, its length is adjusted accordingly.

In character string processing, trailing blanks are usually ignored by default for data objects `dobj1, dobj2 ...` or lines in the internal table `itab` of fixed length.

### System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| 0              | The content of all data objects `dobj1, dobj2 ...` or `itab` lines was passed to the target field `result`.                     |
| 4              | The content of the data objects `dobj1, dobj2 ...` or `itab` lines could not be passed completely, since `result` is too short. |

### Hints

- Instead of `CONCATENATE`, [string expressions](abapcompute_string.md) can usually also be used for elementary fields, where concatenations are possible using either [concatenation operators](../../abap-glossary/abenconcatenation_operator_glosry.md) `&&` or [embedded expressions](abenstring_templates_expressions.md) in [string templates](abenstring_templates.md). The built-in function [`concat_lines_of`](abenconcatenation_functions.md) can be used to concatenate lines of an internal table.

- The ABAP runtime framework performs an internal optimization to reduce the number of reassignments if new fragments are appended to an existing [string](../../abap-glossary/abenstring_glosry.md) on the right within a loop. If the string or parts of the string itself are appended, no optimization takes place, which causes a squared increase in runtime in loops. This can be prevented by using helper variables. See also the [Performance Note](abenstring_expr_perfo.md) for string expressions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows that a concatenation with `CONCATENATE` has the same result as a concatenation with the [concatenation operator](../../abap-glossary/abenconcatenation_operator_glosry.md) [`&&`](abenstring_operators.md) or via [embedded expressions](abenstring_templates_expressions.md).

``` abap
CONCATENATE 'a' 'b' 'c' INTO FINAL(str). 
ASSERT str = 'a' && 'b' && 'c'. 
ASSERT str = |{ 'a' }{ 'b' }{ 'c' }|.
```

## Addition 1

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is performed. Depending on the processing type, the data objects `dobj1, dobj2 ...`, the lines of the internal table `itab`, and the separator `sep` must be [character-like](../../abap-glossary/abencharlike_data_object_glosry.md) or [byte-like](../../abap-glossary/abenbyte_like_data_object_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Concatenation of individual bytes from an internal table in a byte string.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES hex TYPE x LENGTH 1. 
DATA itab TYPE TABLE OF hex WITH EMPTY KEY. 
 
itab = VALUE #( 
  ( CONV hex( '48' ) ) 
  ( CONV hex( '65' ) ) 
  ( CONV hex( '6C' ) ) 
  ( CONV hex( '6C' ) ) 
  ( CONV hex( '6F' ) ) ). 
 
CONCATENATE LINES OF itab INTO FINAL(xstr) IN BYTE MODE. 
 
out->write( 
  cl_abap_conv_codepage=>create_in( )->convert( xstr ) ). 
 
out->display( ).
```

## Addition 2

`... SEPARATED BY sep`

### Description

The addition `SEPARATED BY` is used to insert the content of data object `sep` between the content of the consecutive data objects `dobj1, dobj2 ...`. In character string processing, trailing blanks are respected for separators `sep` of fixed length.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the first `CONCATENATE` statement, `result` contains *Wehaveallthetimeintheworld*, and after the second it contains *We have all the time in the world*.

``` abap
DATA: t1 TYPE c LENGTH 10 VALUE 'We', 
      t2 TYPE c LENGTH 10 VALUE 'have', 
      t3 TYPE c LENGTH 10 VALUE 'all', 
      t4 TYPE c LENGTH 10 VALUE 'the', 
      t5 TYPE c LENGTH 10 VALUE 'time', 
      t6 TYPE c LENGTH 10 VALUE 'in', 
      t7 TYPE c LENGTH 10 VALUE 'the', 
      t8 TYPE c LENGTH 10 VALUE 'world'. 
 
CONCATENATE t1 t2 t3 t4 t5 t6 t7 t8 
            INTO DATA(result). 
... 
CONCATENATE t1 t2 t3 t4 t5 t6 t7 t8 
            INTO result SEPARATED BY space.
```

## Addition 3

`... RESPECTING BLANKS`

### Description

The addition `RESPECTING BLANKS` is only allowed in character string processing and respects the trailing blanks for data objects `dobj1, dobj2 ...` or lines of the internal table `itab`. If this addition is not used, the blanks are respected for data type `string` only.

### Hint

The addition `RESPECTING BLANKS` of the statement `CONCATENATE` can be used to assign any character strings `text` to target fields `str` of type `string` while respecting trailing blanks: `CLEAR str.` `CONCATENATE str text INTO str RESPECTING BLANKS.`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the first `CONCATENATE` statement, `result` contains *When_the_music_is_over*, and after the second it contains *When\_\_\_\_\_\_the\_\_\_\_\_\_\_music\_\_\_\_\_is\_\_\_\_\_\_\_\_ over\_\_\_\_\_\_*. The underscores here represent blanks.

``` abap
TYPES text   TYPE c LENGTH 10. 
DATA  itab   TYPE TABLE OF text. 
 
APPEND 'When'  TO itab. 
APPEND 'the'   TO itab. 
APPEND 'music' TO itab. 
APPEND 'is'    TO itab. 
APPEND 'over'  TO itab. 
 
CONCATENATE LINES OF itab INTO DATA(result) SEPARATED BY space. 
... 
CONCATENATE LINES OF itab INTO result RESPECTING BLANKS.
```

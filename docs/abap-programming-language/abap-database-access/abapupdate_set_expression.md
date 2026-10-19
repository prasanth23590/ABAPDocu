---
title: "UPDATE writable_obj, set_expression"
source_file: abapupdate_set_expression.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > UPDATE writable_obj > UPDATE writable_obj, source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE writable_obj, set_expression

## Syntax

``` abap
... {col = f} 
  | {col = col + f} 
  | {col = col - f} 
  | (expr_syntax) ...  
```

[`col`](abenabap_sql_columns.md) · [`col`](abenabap_sql_columns.md) · [`col`](abenabap_sql_columns.md) · [`col`](abenabap_sql_columns.md) · [`col`](abenabap_sql_columns.md)

### Variant

[1. `... col = f`](abapupdate_set_expression.md#variant-1)

[2. `... col = col + f`](abapupdate_set_expression.md#variant-2)

[3. `... col = col - f`](abapupdate_set_expression.md#variant-3)

[4. `... (expr_syntax)`](abapupdate_set_expression.md#variant-4)

## Overview

### Description

[Set expressions](../../abap-glossary/abenset_expression_glosry.md) for the addition `SET` of the statement `UPDATE`. These set expressions can be combined in the comma-separated list in any way required after [`SET`](abapupdate_source.md).

### Hint

A column `col` can occur in a single set expression only.

## Variant 1

`... col = f`

### Description

Assignment of a value. Columns of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) `writable_obj` specified in [`target`](abapiumd_target.md) can be specified for [`col`](abenabap_sql_columns.md). For `f`, a [literal](abenabap_sql_literals.md), a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), a built-in [SQL function](abenabap_sql_builtin_functions.md), a [cast expression](abensql_cast.md), or a column name [`writable_obj~comp`](abenabap_sql_columns.md) of a different column in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) can be used. A column can only occur in a single set expression after `SET`.

The statement `UPDATE` assigns the content of `f` to the columns `col` in all the rows defined by the `WHERE` condition. If the column has one of the data types `DECFLOAT34` or `DECFLOAT16`, the data object has a numeric data type. If the column has the data type `UTCLONG`, the data object must have the data type `utclong`. If the data types are not [compatible](../../abap-glossary/abencompatible_glosry.md), they are converted as follows:

- When assigning a data object that is not a reference variable for a [LOB handle](../../abap-glossary/abenlob_handle_glosry.md), the content is converted, if required, to the [ABAP data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that corresponds to the data type of the column in accordance with the [conversion rules](../abap-processing-internal-data/abenconversion_elementary.md). Any errors in the conversion raise the corresponding uncatchable exception. The content of `f` must match the data type of the column in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md). This can raise an exception.

- When assigning a data object that is a reference variable for a [LOB handle](../../abap-glossary/abenlob_handle_glosry.md), the column `col` must be a [LOB](../../abap-glossary/abenlob_glosry.md) with a suitable type. If the reference has a writer stream type, a writer stream is created. If it is a type for a locator, this locator must exist and is used as a source. For details, see [LOB handles](abenium_lob.md).

- When assigning a different column, the content is converted in the database system, if necessary. The option of a conversion and the conversion rules are specific to the database system. Any errors in the conversion raise the catchable exception `CX_SY_OPEN_SQL_DB`.

In the assignment, the assigned value must fit in the value range of the column. Otherwise, the catchable exception `CX_SY_OPEN_SQL_DB` is raised. This applies in particular for:

- Assignments to numeric columns.

- Assignments to columns of the type `SSTRING`, `STRING`, or `RAWSTRING`. The assigned content must not be longer than the maximum length of the columns in the database structure. This length can be determined using the built-in function [`dbmaxlen`](../abap-processing-internal-data/abenlength_functions.md).

If a column is specified for `f`, changes to this column that are made in the same `UPDATE` statement are ignored during the assignment.

### Hints

- No [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) can be specified for `f`.

- Currently, only built-in [SQL functions](abenabap_sql_builtin_functions.md) and [cast expressions](abensql_cast.md) can be specified for `f`. No other [SQL expressions](abapsql_expr.md) are possible. In particular, [arithmetic expressions](abensql_arith.md) are not supported. Variant 2 and variant 3 below are not arithmetic expressions, but special syntax.

- When specifying an [SQL function](abenabap_sql_builtin_functions.md) for `f`, there currently is a limitation concerning the data type: the result of the SQL function can have any data type, except `STRING` and `RAWSTRING`. The syntax check verifies this.

- As explained above, `f` cannot be an [arithmetic expression](abensql_arith.md). However, it is possible to use arithmetic expressions as operand of a [cast expression](abensql_cast.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `UPDATE` statement sets the specified columns to the specified values in every row of the CDS table entity.

``` abap
DELETE FROM demo_update. 
INSERT demo_cds_update_te FROM TABLE @( VALUE #( ( id = 'X' ) 
                                                 ( id = 'Y' ) 
                                                 ( id = 'Z' ) ) ). 
 
FINAL(num) = 300. 
 
UPDATE demo_cds_update_te SET col1 = 100, 
                              col2 = demo_cds_update_te~col1, 
                              col3 = @num, 
                              col4 = @( num + 100 ).
```

## Variant 2

`... col = col + f`

### Description

Addition of a value. The same applies to [`col`](abenabap_sql_columns.md) and `f` as to the assignment of a value, where `col` must have a numeric data type. `col` must be specified either with or without the prefix `writable_obj~` on both sides. The data types `DF16_RAW` and `DF34_RAW` and the obsolete types `DF16_SCL` and `DF34_SCL` are not allowed.

The statement `UPDATE` adds the value of `f` to the content of the column `col` in all the rows defined by the `WHERE` condition. Otherwise, the same rules apply as to the assignment of a value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `UPDATE` statement adds the specified values to the values in the specified columns in every row of the CDS table entity.

``` abap
DELETE FROM demo_cds_update_te. 
INSERT demo_cds_update_te FROM TABLE @( 
  VALUE #( ( id = 'X' col1 =  1 col2 =  2 col3 =  3 col4 =  4 ) 
           ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 col4 = 14 ) 
           ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 col4 = 24 ) ) ). 
 
FINAL(num) = 300. 
 
UPDATE demo_cds_update_te SET col1 = col1 + 100, 
                              col2 = col2 + demo_cds_update_te~col1, 
                              col3 = col3 + @num, 
                              col4 = col4 + @( num + 100 ).
```

## Variant 3

`... col = col - f`

### Description

Subtraction of a value. The same applies to [`col`](abenabap_sql_columns.md) and `f` as to the assignment of a value. Here, `col` must have a numeric data type. `col` must be specified either with or without the prefix `writable_obj~` on both sides. The data types `DF16_RAW` and `DF34_RAW` and the obsolete types `DF16_SCL` and `DF34_SCL` are not allowed.

The statement `UPDATE` subtracts the value of `f` from the content of the column `col`, in all rows defined by the `WHERE` condition. Otherwise, the same rules apply as to the assignment of a value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `UPDATE` statement subtracts the specified values from the values in the specified columns in every row of the database table.

``` abap
DELETE FROM demo_update. 
INSERT demo_update FROM TABLE @( 
  VALUE #( ( id = 'X' col1 =  1 col2 =  2 col3 =  3 col4 =  4 ) 
           ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 col4 = 14 ) 
           ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 col4 = 24 ) ) ). 
 
FINAL(num) = 300. 
 
UPDATE demo_update SET col1 = col1 - 100, 
                       col2 = col2 - demo_update~col1, 
                       col3 = col3 - @num, 
                       col4 = col4 - @( num + 100 ).
```

## Variant 4

`... (expr_syntax)`

### Description

Dynamic specification of set expressions. A set expression can be specified as a parenthesized data object `expr_syntax` that, when the statement is executed, either contains the syntax of one or more static set expressions (with the exception of host expressions) or is initial. The data object `expr_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) without [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) and with a character-like data object. The syntax in `expr_syntax` is not case-sensitive. When an internal table is specified, the syntax can be distributed across multiple rows.

If `expr_syntax` is `initial` when the statement is executed, the set expression is ignored. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hint

If `expr_syntax` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), the [table body](../../abap-glossary/abentable_body_glosry.md) is evaluated and not the header line.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `UPDATE` statement changes the columns specified in a dynamic token to the specified values in every row of the database table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_update. 
INSERT demo_update FROM TABLE @( 
  VALUE #( ( id = 'X' col1 =  1 col2 =  2 col3 =  3 ) 
           ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 ) 
           ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 ) ) ). 
 
FINAL(num) = 100. 
 
FINAL(expr_syntax) = `col1 = @num, ` && 
                    `col2 = col2 + demo_update~col1, ` && 
                    `col3 = col3 - @num`. 
 
TRY. 
    UPDATE demo_update SET (expr_syntax). 
  CATCH cx_sy_dynamic_osql_error INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

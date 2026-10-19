---
title: "sql_exp - sql_arith"
source_file: abensql_arith.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_arith

## Syntax

``` abap
... [-] sql_exp1 +|-|*|/ [-] sql_exp2 [+|-|*|/ [-] sql_exp3 ... ] ...  
```

## Description

Arithmetic expression in ABAP SQL. The operators perform arithmetic calculations between two adjacent operands `sql_exp1`, `sql_exp2`, ... The possible operators are:

- `+` for adding the operands

- `-` for subtracting the right operand from the left operand

- `*` for multiplying the operands

- `/` for dividing the left operand by the right operand

The operators `*` and `/` have a higher priority than the operators `+` and `-`. Within a [parenthesis level](abensql_exp_parentheses.md), operations with a higher priority are performed before those with a lower priority. Operations with identical priorities are performed from left to right. A minus sign `-` can be placed in front of an operand that does not directly follow an operator `+`, `-`, `*`, or `/`.

The arithmetic expressions in ABAP SQL are distinguished depending on the data type of the operands as follows:

- Integer expressions

  Integer expressions use only integer operands, regardless of the parenthesis level. These have the dictionary type `INT1`, `INT2`, `INT4`, and `INT8` or the ABAP type `b`, `s`, `i`, and `int8` plus packed numbers of the types `DEC`, `CURR`, and `QUAN` or `p` without decimal places. The operator `/` is not allowed in integer expressions. An overflow occurs and an exception of the class `CX_SY_OPEN_SQL_DB` is raised when

  - the value range of the type `INT4` or `i` is exceeded in operations between two integer numbers where neither of the numbers has the type `INT8`,

  - the value range of the type `INT8` or `int8` is exceeded in operations between two integer numbers where one of the numbers has the type `INT8`,

  - the value range of a packed number with length 31 without decimal places is exceeded in operations using packed numbers.

    Depending on the types of the operands and whether packed numbers are involved, the result has the type `INT4`, `INT8` or is a packed number with length 31 and no decimal places. Using the associated [assignment rule](abenselect_into_conversion.md), it can be assigned to all [numeric ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) whose value range is large enough, except for decimal floating point numbers.

- Decimal expressions

  Decimal expression have at least one operand with the type `DEC`, `CURR`, or `QUAN` or `p` with decimal places besides any integer operands (see above).. The operator `/` is not allowed in decimal expressions. The result has the type `DEC` with the length 31 and a maximum of 14 decimal places. Using the associated [assignment rule](abenselect_into_conversion.md), it can be assigned to all [numeric ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) whose value range is large enough, except for decimal floating point numbers. If a decimal expression is specified statically, the syntax check checks that the result of each operation is in the value range of the type `DEC` with length 31 and a maximum of 14 decimal places. If any operands are specified that could produce other values, a syntax error occurs. If the expression is specified dynamically, an exception of the class `CX_SY_DYNAMIC_OSQL_SEMANTICS` is raised in this case.

- Decimal floating point expressions

  Decimal floating point expressions have at least one operand of the type `DECFLOAT16` or `DECFLOAT34` besides any integer operands (see above) and operands of the DDIC types `DEC`, `CURR`, `QUAN`, `DF16_DEC`, `DF16_DEC`, `FLTP` and of the ABAP types `p`, `f`. Decimal floating point expressions that contain only operands of types `DECFLOAT16` or `DECFLOAT34` allow divisions using the operator `/`. Depending on the types of the operands, the result has the type `DECFLOAT16` or `DECFLOAT34`. Using the associated [assignment rule](abenselect_into_conversion.md), it can be assigned to the ABAP types `decfloat16` or `decfloat34`. If the value range of the result type is exceeded or division by 0 takes place, an overflow occurs and an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

- Binary floating point expressions

  Binary floating point expressions have at least one operand of the dictionary type `FLTP` or with the ABAP type `f` besides operands with the DDIC integer type `INT1`, `INT2`, `INT4`, and `INT8` or the ABAP type `b`, `s`, `i`, and `int8`. Binary floating point expressions that contain only operands of types `FLTP` or `f` allow division with the operator `/`. If the value range of the type `FLTP` is exceeded or division by 0 takes place, an overflow occurs and an exception of the class `CX_SY_OPEN_SQL_DB` is raised. The result has the type `FLTP` and can only be assigned to a field with the ABAP type `f` in accordance with the associated [assignment rule](abenselect_into_conversion.md).

No other combinations of operand are allowed. The operands can all be SQL expressions of the specified data types.

If the operand of an arithmetic expression has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the entire arithmetic expression is the null value.

## Hints

- Specifying an arithmetic expression always means specifying an [SQL expression](abapsql_expr.md). Arithmetic expressions can only be specified for operand positions for which SQL expressions are possible.

- The arithmetic expressions are divided into the four categories integer expressions, decimal expressions, decimal floating point expressions and binary floating point expressions to achieve the same behavior in all supported database systems.

- Only operands of the DDIC types `DECFLOAT16` and `DECFLOAT34` lead to a decimal floating point expression. The decimal floating point types `DF34_RAW`, `DF16_RAW` and the obsolete types `DF34_SCL`, `DF16_SCL` are not allowed in arithmetic expression in ABAP SQL.

- The decimal floating types `DF34_DEC`, `DF16_DEC` are handled as packed numbers of type `DEC` in decimal floating point expressions. They cannot be used in other arithmetic expressions. As an exception to the rules shown here, the result of an expression that contains operands of type `DF16_DEC` only is `DF16_DEC`.

- Host variables of the ABAP types `decfloat16` or `decfloat34` are mapped to the DDIC types `DF16_RAW` and `DF34_RAW` and cannot be used in arithmetic expression.

- To use operators that do not have the type `FLTP` in a binary floating point expression, they can be transformed to an operator with the type `FLTP` using a [`CAST` expression](abensql_cast.md).

- A plus sign `+` cannot be specified in front of an operand of an arithmetic expression. If a minus sign `-` is to be specified after an operator `+`, `-`, `*`, or `/`, the sign and the operand must be placed in parentheses.

- Arithmetic expressions can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and internal tables with [`FROM @itab`](abapselect_itab.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Arithmetic expression as an argument of the built-in function [`DIVISION`](abensql_arith_func.md) in a [`SELECT` list](abapselect_list.md). To use the operator `/` instead of `DIVISION`, its operands would have to be [cast](abensql_cast.md) to `DECFLOAT16`, `DECFLOAT34`, or `FLTP` and the result would also have the corresponding type.

``` abap
SELECT FROM   sflight 
       FIELDS fldate, DIVISION( ( seatsmax - seatsocc ) * 100, 
              seatsmax, 2 ) AS availability 
       WHERE carrid = 'LH' AND 
             connid = 400 
       ORDER BY fldate 
       INTO TABLE @FINAL(result).
```

## Executable Example

[SQL Expressions, Arithmetic Calculations](abensql_expr_arith_abexa.md)

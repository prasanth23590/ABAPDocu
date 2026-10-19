---
title: "sql_exp - sql_elem"
source_file: abensql_elem.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_elem

## Syntax

``` abap
... col 
  | literal | @dobj | @( expr ) ...  
```

[`col`](abenabap_sql_columns.md) · [`literal`](abenabap_sql_literals.md) · [`@dobj`](abenabap_sql_host_variables.md) · [`@( expr )`](abenabap_sql_host_expressions.md)

## Description

Elementary expression in ABAP SQL. An elementary SQL expression represents one of the following values:

- Value from the database

  - Column [`col`](abenabap_sql_columns.md) of a [data source](abapselect_data_source.md)

    The column [`col`](abenabap_sql_columns.md) can be of any elementary data type from the ABAP Dictionary, unless otherwise documented for an operand position.

- Values of the ABAP program passed to the database system

  - [Literal](abenabap_sql_literals.md) `literal`

  - [Host variable](abenabap_sql_host_variables.md) `@dobj`

  - [Host expression](abenabap_sql_host_expressions.md) `@( expr )`

    The ABAP objects can have any non-generic elementary ABAP data type and the name of a host variable must be tagged with the escape character `@`. [Typed literals](abenabap_sql_typed_literals.md) are handled strictly according to their type. [Untyped literals](abenabap_sql_untyped_literals.md) are restricted to the types `c` and `i`. Untyped [text field literals](../../abap-glossary/abentext_field_literal_glosry.md) are allowed. String literals are not allowed, neither typed nor untyped. Furthermore, no empty text field literal can be specified. An empty typed literal of type `CHAR` can be specified.

The result of an elementary SQL expression is the value of the specified object or the result of the specified expression. If a value from the database is specified, the data type is its dictionary type. When an ABAP object is specified, the ABAP type is mapped to a dictionary type as follows:

| **Numeric ABAP Type**                        | **Dictionary Type**                              |
|----------------------------------------------|--------------------------------------------------|
| `b`, `s`, `i`, `int8`                        | `INT1`, `INT2`, `INT4`, `INT8`                   |
| `p`                                          | `DEC` with appropriate length and decimal places |
| `decfloat16`, `decfloat34`                   | `DF16_RAW`, `DF34_RAW`                           |
| `f`                                          | `FLTP`                                           |
| **Character-Like ABAP Type**                 | **Dictionary Type**                              |
| `c`                                          | `CHAR` with appropriate length                   |
| `n`                                          | `NUMC` with appropriate length                   |
| `string`                                     | `STRING` with appropriate length                 |
| **Byte-Like ABAP Type**                      | **Dictionary Type**                              |
| `x`                                          | `RAW` with appropriate length                    |
| `xstring`                                    | `RAWSTRING` with appropriate length              |
| **ABAP Type for Date, Time, and Time Stamp** | **Dictionary Type**                              |
| `d`                                          | `DATS`                                           |
| `t`                                          | `TIMS`                                           |
| `utclong`                                    | `UTCLONG`                                        |

Untyped [text field literals](../../abap-glossary/abentext_field_literal_glosry.md) are handled as fields with the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) of the corresponding length where trailing blanks are respected. Like the [untyped numeric literals](../abap-declarations/abenuntyped_number_literals.md) of a general ABAP, untyped numeric literals are handled either as a field with the type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or the type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), depending on their value.

On the database, the value of an ABAP object as an elementary expression is handled according to the rules of the database in accordance with the mapped type. This is different from other operand positions of ABAP objects in ABAP SQL, where they are not handled as elementary expressions. In these operand positions, the content is converted to the target type in accordance with the [rules for lossless assignments](../abap-processing-internal-data/abapmove_exact.md).

## Hints

- Columns, literals, host variables, and host expressions can also occur as elementary [SQL operands](abensql_operands.md) in operand positions in which no general SQL expressions are possible. Columns, literals, hosts variables, and host expressions can only be handled as SQL expressions in positions where SQL expressions are possible. Only there can they be specified inside [parentheses](abensql_exp_parentheses.md). Then, the statement can only have lists separated by commas and host variables must be indicated by the escape character `@`.

- If an elementary SQL expression consists of a host variable in the form of a field symbol or formal parameter, this expression must be completely typed.

- Untyped literals, host variables, and host expressions as operands of other SQL expressions are evaluated before the ABAP SQL statement is sent to the database system. Specifying a host variable from a `SELECT` list after `INTO` in a `SELECT` loop does not mean that a different value is used in each loop pass.

- The fact that literals, host variables, and host expressions are mapped to specific dictionary types as operands of SQL expressions, whereas other operand positions allow conversions to different target types, is particularly significant for [relational expressions](abenabap_sql_expr_logexp.md) in which the [comparability](abenwhere_logexp_compare_types.md) of dictionary types is important.

- An elementary expression can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table with [`FROM @itab`](abapselect_itab.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [`SELECT` list](abapselect_list.md) of the second [`SELECT`](abapselect.md) statement contains all possible elementary SQL expressions.

``` abap
DATA carrid TYPE scarr-carrid VALUE 'LH'. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
SELECT FROM   scarr 
       FIELDS carrid, carrname 
       INTO TABLE @FINAL(carriers). 
 
SELECT SINGLE 
       FROM   spfli 
       FIELDS '*' AS mark, 
              @carrid AS id, 
              @( carriers[ carrid = carrid ]-carrname ) AS carrier, 
              connid 
       WHERE carrid = @carrid 
       INTO @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[Constant in the `SELECT` List](abensql_expr_literal_abexa.md)

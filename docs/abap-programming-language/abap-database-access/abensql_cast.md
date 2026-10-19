---
title: "sql_exp - sql_cast"
source_file: abensql_cast.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_cast

## Syntax

``` abap
... CAST( sql_exp AS dtype ) ...  
```

## Description

Type adjustment in ABAP SQL. A cast expression [converts](abensql_cast_rules.md) the value of the operand `sql_exp` to the dictionary type specified by `dtype`. SQL expressions, which have a type that matches `dtype` as shown below, can be used as an operand `sql_exp`. The result is a representation of the source value in type `dtype`.

[Built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in the ABAP Dictionary with the following syntax can be specified for `dtype`:

- Numeric types

  - `INT1`

  - `INT2`

  - `INT4`

  - `INT8`

  - `DEC[( len[, decimals] )]`

  - `D16N` for `DECFLOAT16`

  - `D34N` for `DECFLOAT34`

  - `FLTP`

- Character-like types

  - `CHAR[( len )]`

  - `SSTRING[( len )]`

- Byte-like types

  - `RAW [( len )]`

- Date types/time types

  - `DATS`

  - `TIMS`

  - `DATN`

  - `TIMN`

  - `UTCL` for `UTCLONG`

- Character-like types with special semantics

  - `NUMC[( len )]`

  - `CLNT`

  - `LANG`

- Currency fields and quantity fields

  - `CURR[( len[, decimals] )]`

  - `CUKY`

  - `QUAN[( len[, decimals] )]`

  - `UNIT( 2|3 )`

`len` and `decimals` can be used to specify lengths and decimal places for those dictionary types that have variable lengths and decimal places. [Literals](abenabap_sql_literals.md) or [host constants](abenabap_sql_host_variables.md) of the [ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) `b`, `s`, `i`, or `int8` can be specified for `len` and `decimals`. If no lengths or decimal places are specified for these types, these values are taken from the result of the specified SQL expression `sql_exp`. In both cases, the lengths and decimal places must meet the requirements of the following table. If the operand `NULL` is cast, the length of dictionary types that have a variable length must be specified.

The following table shows which combinations of built-in data types in the ABAP Dictionary can currently be cast to each other and the corresponding prerequisites. There is a special list of [conversion rules](abensql_cast_rules.md) for every combination.

| **from/to**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`CLNT`** | **`LANG`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`CURR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`QUAN`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DF16_DEC`**   | x          | x          | x          | x          | \-        | \-         | \-         | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DF34_DEC`**   | x          | x          | x          | x          | \-        | \-         | \-         | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`FLTP`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | z          | z             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`CHAR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | x          | x             | y          | y          | y          | \-         | \-         | \-            | y          | y          | c          | y          | \-        |
| **`SSTRING`**    | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | x          | x             | y          | y          | y          | \-         | \-         | \-            | y          | y          | c          | y          | \-        |
| **`NUMC`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | y          | y          | y          | \-         | \-         | \-            | y          | \-         | \-         | \-         | \-        |
| **`DATS`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | x          | x             | y          | x          | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`TIMS`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | x          | x             | y          | \-         | x          | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-        |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | x          | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-        |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | x          | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-        |
| **`UTCLONG`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | x             | \-         | \-         | \-         | \-         | \-        |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | y          | \-         | \-         | \-         | \-         | \-            | x          | \-         | \-         | \-         | \-        |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | x          | \-         | \-         | \-        |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | x          | \-         | \-        |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | x          | \-        |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | c         |

There are no further restrictions for combinations using `x`. The following prerequisites apply to the other combinations:

- For combinations with `y`, the initial length cannot be less than the target length.

- For combinations with `z`, the target length must be sufficient to represent the value in the source.

- For combinations with `c`, the initial length and target length must be equal.

These prerequisites are checked by the ABAP SQL parser.

In the case of incompatible types, the content of the operand is [converted](abensql_cast_rules.md) to the target type. Exceptions can be raised if values are not suitable. If the operand of the expression has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the expression is also the null value.

When casting to a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md), the operand of the cast expression must be compatible with the [base type](../../abap-glossary/abenbase_type_glosry.md) of the CDS enumerated type. The cast matrix and the conversion rules for casting apply with respect to the base type.

## Hints

- Specifying a cast expression always means specifying an [SQL expression](abapsql_expr.md). Cast expressions can only be specified for operand positions in which SQL expressions are possible.

- Type modifications can be used in operand positions of ABAP SQL statements to convert operands without a suitable type to an operand with a suitable type.

- `CAST` expressions are platform-independent with one exception: For conversions from the type `FLTP` to other numeric types the result is platform-dependent.

- For conversions from the type `FLTP` to other types, rounding errors might occur. For conversions to character types depending on the value either the [mathematical](../../abap-glossary/abenmathematical_notation_glosry.md) or [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) is generated and the case of the exponent character is not fixed. Converting back such a character representation to a floating data type always produces the original value.

- For the missing combinations of type modifications that cannot be covered by a `CAST` expression, construction operators such as `CONV` can be used in [host expressions](abenabap_sql_host_expressions.md), at least for literals and host variables. There are also built-in [conversion functions](abenabap_sql_conversion_functions.md) for special conversions:

  - [`BINTOHEX`](abensql_type_conv_func.md) and [`HEXTOBIN`](abensql_type_conv_func.md) for conversions of byte strings to character strings and vice versa.

- A cast expression cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The [table buffer](../../abap-glossary/abentable_buffer_glosry.md) is bypassed and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [`SELECT` list](abapselect_list.md) splits an UTC [time stamp in a packed number](../abap-processing-internal-data/abentime_stamps_packed.md) into its date part and its time part. This requires multiple `CAST` expressions to create a suitable type in every operand position.

``` abap
FINAL(timestamp) = 
  cl_abap_tstmp=>utclong2tstmp_short( utclong_current( ) ). 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( 
  VALUE #( id = 'X' timestamp1 = timestamp ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS CAST( CAST( div( timestamp1, 1000000 ) 
                      AS CHAR ) 
                AS DATS ) AS date, 
              CAST( substring( CAST( timestamp1 
                                 AS CHAR ), 9, 6 ) 
                AS TIMS ) AS time 
       INTO @FINAL(wa). 
 
cl_demo_output=>display( wa ).
```

## Executable Example

[SQL Expressions, Cast Expression](abensql_expr_cast_abexa.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [`SELECT` list](abapselect_list.md) casts a CDS [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) to the data type `INT1`. The [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) 2 is returned.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM TABLE @( VALUE #( 
 ( id = 1 ) 
 ( id = 2 ) ) ). 
 
SELECT FROM demo_cds_enum_type_usage_1 
       FIELDS Id, 
           CAST( @demo_cds_enum_weekday-wed AS INT1 ) AS CastEnum 
       INTO TABLE @FINAL(result). 
cl_demo_output=>display( result ).
```

---
title: "sql_exp - sql_string"
source_file: abensql_string.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_string

## Syntax

``` abap
... sql_elem1 && sql_elem2  [&& sql_elem3 ... ] ...  
```

## Description

String expression in ABAP SQL. The operator `&&` concatenates the character strings in two adjacent operands into a single character string. [Elementary SQL expressions](abensql_elem.md) can be specified as the operands `sql_elem1`, `sql_elem2` with the following restrictions:

- A literal must be a non-empty [text field literal](../../abap-glossary/abentext_field_literal_glosry.md) of type `c`.

- Host variables and host expressions must be of ABAP type `c`.

- Columns of [data sources](abapselect_data_source.md) must have one of the dictionary types [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the concatenation must be no longer than 255 characters. Trailing blanks are handled as follows:

- Precisely one blank is respected in host variables declared using `CONSTANTS` and in text field literals consisting only of blanks.

- In all other cases, trailing blanks are cut off on the right.

The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in the resulting length and can be assigned to the ABAP types `c` and `string` in accordance with the associated [assignment rule](abenselect_into_conversion.md).

If the operand of a string expression has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the full string expression is the null value.

## Hints

- Specifying a string expression always means specifying an [SQL expression](abapsql_expr.md). String expressions can only be specified for operand positions for which SQL expressions are possible.

- Strings can also be concatenated using the SQL function [`CONCAT`](abensql_string_func.md). The function `CONCAT` is restricted to concatenating two operands but has the following benefits when compared to the operator `&&`:

  - It allows any SQL expressions as operands.

  - It allows more data types.

  - It does not apply any special handling to constants and text field literals that contain only blanks.

  - It allows results to be longer than 255 characters.

- A string expression cannot be evaluated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) and always causes [table buffer](../../abap-glossary/abentable_buffer_glosry.md) to be bypassed and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The two columns in a result set are created using a concatenation of character-like columns of the data source and of literals.

``` abap
SELECT FROM spfli 
         INNER JOIN scarr 
           ON spfli~carrid = scarr~carrid 
       FIELDS spfli~carrid && ' ' && '(' && scarr~carrname && ')' 
              AS carrier, 
              cityfrom && ' ' && '-' && ' ' && cityto 
              AS connection 
       ORDER BY spfli~carrid, connid 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[SQL Expressions, Concatenations](abensql_expr_string_abexa.md)

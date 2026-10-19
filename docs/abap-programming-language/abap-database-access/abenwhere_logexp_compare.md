---
title: "sql_cond - Comparison Operators"
source_file: abenwhere_logexp_compare.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - Comparison Operators

## Syntax

``` abap
... operand1 operator operand2 
                    | {[ALL|ANY|SOME] ( SELECT subquery_clauses )} ...  
```

[`[ALL|ANY|SOME]`](abenwhere_logexp_all_any_some.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md)

## Description

This relational expression compares the content of the operand `operand1` according to the comparison operator `operator` with the content of the operand `operand2` or with the result of a [scalar subquery](abenwhere_logexp_all_any_some.md).

- The following can be specified for `operand1` on the left side:

  - Any [SQL expressions](abapsql_expr.md) except [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md).

  - [Aggregate expressions](abapselect_aggregate.md) in a [`HAVING`](abaphaving_clause.md) clause.

- The following can be specified for `operand2` on the right side:

  - Any elementary [SQL operands](abensql_operands.md).

    Here, a column [`col`](abenabap_sql_columns.md) must be specified as [`data_source`](abapselect_data_source.md)~comp, or `tabalias~comp` using the [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) and it must be possible to [compare](abenwhere_logexp_compare_types.md) the data types of the left side and right side.

The content of an ABAP object, that is, an [untyped literal](abenabap_sql_untyped_literals.md), a [host variable](abenabap_sql_host_variables.md), or a [host expression](abenabap_sql_host_expressions.md) must match the data type of `operand1` in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md). - Built-in [SQL functions](abenabap_sql_builtin_functions.md) and [cast expressions](abensql_cast.md).

\- [Aggregate expressions](abapselect_aggregate.md) in a [`HAVING`](abaphaving_clause.md) clause.

The following table shows the possible comparison operators:

| **`operator`** | **Meaning**                                                                              |
|----------------|------------------------------------------------------------------------------------------|
| `=`, `EQ`      | True if the content of `operand1` is equal to the content of `operand2`.                 |
| `<>`, `NE`     | True if the content of `operand1` is not equal to the content of `operand2`.             |
| `<`, `LT`      | True if the content of `operand1` is less than the content of `operand2`.                |
| `>`, `GT`      | True if the content of `operand1` is greater than the content of `operand2`.             |
| `<=`, `LE`     | True if the content of `operand1` is less than or equal to the content of `operand2`.    |
| `>=`, `GE`     | True if the content of `operand1` is greater than or equal to the content of `operand2`. |

The following should be noted when using these operators:

- If `operand2` is an [untyped literal](abenabap_sql_untyped_literals.md), a [host variable](abenabap_sql_host_variables.md), or a [host expression](abenabap_sql_host_expressions.md), the value is converted, if necessary, to the data type that matches the type of the operand `operand1` in accordance with the [ABAP conversion rules](../abap-processing-internal-data/abenconversion_rules.md) and the [tables of built-in types in the ABAP Dictionary](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) before the statement is passed to the database.

- Comparisons between columns or between SQL expressions (including [typed literals](abenabap_sql_typed_literals.md) and aggregate expressions) and columns are performed completely on the database. No type conversions are made in ABAP beforehand. If the data types or lengths on the left and right side do not match, the resulting behavior depends entirely on the conversion rules of the database, where fewer conversions are generally possible here than in ABAP. The platform-dependent behavior can produce different results or even SQL errors on individual platforms. For details on the conversion rules of SAP HANA Platform, see the [SAP HANA SQL Reference Guide](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- The decimal places are respected in comparisons between numeric types.

- In greater than or less than comparisons with character-like types, the result can depend on the [code page](../../abap-glossary/abencodepage_glosry.md) used by the database system. This applies in particular to the non-printable characters.

- Trailing blanks are usually ignored in comparisons between character-like types.

- In the case of columns that contain nothing but a blank character, it depends on the platform how this blank is saved:

  - In the SAP HANA database and in MaxDB, a single blank is saved as an empty string and not as the value from the respective code page.

  - In all other databases and in the [table buffer](../../abap-glossary/abentable_buffering_glosry.md), a single blank is saved in accordance with the code page.

    This means that the behavior produced when a value of this type is selected using size comparisons depends on the platform and buffering. More specifically, a single blank in the SAP HANA database and in MaxDB is not found in the interval of all possible characters.

## Hints

- Size comparisons for character-like operands should be avoided to prevent platform-dependent behavior. An exception here are simple cases, such as operands that contain only digits.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads flights with a seat occupancy that is less than the entered value.

``` abap
DATA seatsocc TYPE sflight-seatsocc. 
cl_demo_input=>request( CHANGING field = seatsocc ). 
 
SELECT carrid, connid, fldate 
       FROM sflight 
       WHERE seatsocc < @seatsocc 
       INTO TABLE @FINAL(sflight_tab).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads overbooked flights.

``` abap
SELECT carrid, connid, fldate 
       FROM sflight 
       WHERE seatsocc > sflight~seatsmax 
       INTO TABLE @FINAL(sflight_tab).
```

---
title: "ABAP SQL In-Memory Engine, Supported SQL Expressions"
source_file: abensql_engine_expr.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - ABAP SQL In-Memory Engine"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL In-Memory Engine, Supported SQL Expressions

The evaluation of [SQL expressions](abapsql_expr.md) as well as the execution of [built-in functions](abenabap_sql_builtin_functions.md) as operands of such expressions is not fully supported by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) and must be processed partly on the database. The following expressions and functions can be processed by the ABAP SQL in-memory engine. Their use in read accesses (even nested) does not lead to the bypassing of table buffering and does not cause the transport of an internal table accessed with [`FROM @itab`](abapselect_itab.md) to the database:

- [Elementary SQL expression](abensql_elem.md)

- [Built-in SQL function](abensql_builtin_func.md)

  - [Numeric functions](abensql_arith_func.md) `ABS`, `CEIL`, `DIV`, `FLOOR`, and `MOD`

  - [String functions](abensql_string_func.md) `CONCAT`, `CONCAT_WITH_SPACE`, `LEFT`, `LENGTH`, `LOWER`, `RIGHT`, `UPPER` and `SUBSTRING`

  - [Null value function](abensql_coalesce.md) `COALESCE` (in the [`SELECT`](abapselect_list.md) list only)

- [Arithmetic expressions](abensql_arith.md)

- [Case distinctions](abensql_case.md) (in the [`SELECT`](abapselect_list.md) list only)

- [Aggregate functions](abensql_agg_func.md) `MAX`, `MIN`, and `SUM` (in the [`SELECT`](abapselect_list.md) list only)

- A standalone [aggregate function](abensql_agg_func.md) `COUNT( * )` (in the [`SELECT`](abapselect_list.md) list only).

The expressions and functions can be used in both [`SELECT`](abapselect_list.md) lists and in [`WHERE`](abapwhere.md) clauses.

If a catchable exception is raised when an SQL expression is processed by the ABAP SQL in-memory engine, it is wrapped by the class `CX_SY_OPEN_SQL_DB` and can be handled using this class. The attribute `PREVIOUS` of the associated exception object is then given the name of the original exception class.

## Hints

- When an SQL expression is processed by the ABAP SQL in-memory engine, the same results are produced as on the database and not as in the corresponding ABAP evaluation. The following are some examples:

  - Evaluations of the functions [`DIV`](abensql_arith_func.md) and [`MOD`](abensql_arith_func.md) that are not the same as calculations with the identically named [ABAP operators](../abap-processing-internal-data/abenarith_operators.md).

  - Operands of the type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that do not have trailing blanks on the database, unlike in ABAP.

  - Any [null values](../../abap-glossary/abennull_value_glosry.md) produced as results of nested expressions, for example in the [`COALESCE`](abensql_coalesce.md) function or in [comparisons](abenabap_sql_expr_logexp.md), are handled as null values.

  - The result of a [relational expression](abenabap_sql_stmt_logexp.md) with columns that contain [null values](../../abap-glossary/abennull_value_glosry.md) is unknown, except in the case of the expression [`IS [NOT] NULL`](abenwhere_logexp_null.md).

  - Calculations for built-in type [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are done with the respective arithmetic. The ABAP [calculation type](../abap-processing-internal-data/abenarith_type.md) for [`decfloat16`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) is [`decfloat34`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) in contrast.

- When calculating with the built-in types [`DF16_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), the ABAP SQL in-memory engine uses the respective decimal floating point arithmetic, while the database uses packed number arithmetic. This can lead to different results.

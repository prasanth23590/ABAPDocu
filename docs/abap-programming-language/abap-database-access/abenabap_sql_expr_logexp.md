---
title: "sql_cond - rel_exp for Expressions"
source_file: abenabap_sql_expr_logexp.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - rel_exp for Expressions

## Syntax

``` abap
 ... { {operand1 {=|EQ|<>|NE|>|GT|<|LT|>=|GE|<=|LE} operand2} 
    | {operand  [NOT] BETWEEN operand1 AND operand2} 
    | {operand1 [NOT] LIKE operand2 [ESCAPE esc]} 
    | {operand  IS [NOT] NULL} 
    | {operand  IS [NOT] INITIAL} } ...  
```

## Description

Relational expression in a condition of an expression in an ABAP SQL statement. From the relational expressions shown here, logical expressions `sql_cond` can be formed for the following conditions:

- [`ON` condition](abapwith_associations_defining.md) in the definition of a [CTE association](../../abap-glossary/abencte_association_glosry.md).

- [Filter condition](abenabap_sql_path_filter.md) of a [path expression](abenabap_sql_path.md).

- [`WHEN` condition](abensql_searched_case.md) of a complex [case distinction](abensql_case.md).

- Start condition of the table function [`HIERARCHY`](abenselect_hierarchy_generator.md).

- [`WHERE`](abenselect_hierarchy_agg_navis.md), [`ON`](abenselect_hierarchy_desc_agg.md), and [`START WHERE`](abenselect_hierarchy_ancs_agg.md) condition in a [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md).

The relational expressions that can be used in expressions are a subset of the [relational expressions for statements](abenabap_sql_stmt_logexp.md), but also allow [SQL expressions](abapsql_expr.md) as operands on the right side. SQL expressions on the right side must be enclosed in parentheses with a blank after the opening parenthesis and in front of the closing parenthesis.

- `operand1 =|<>|>|<|>=|<= operand2`

  Comparison of the operand `operand1` on the left side with the operand `operand2` on the right side. The same applies to comparison operators as in a [condition for statements](abenwhere_logexp_compare.md). Here, the operands of size comparisons can have the following data types:

  - Numeric data types: All except for the [replacement types for decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md).

  - Character-like data types: `CHAR`, `CLNT`, `LANG`, `CUKY`, `UNIT`, and `NUMC`.

  - Date types, time types, and time stamp types: `DATN`, `DATS`, `TIMN`, `TIMS`, and `UTCLONG`.

    The operand `operand2` on the right-hand side can be any [SQL expression](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md). If an operand of the comparison has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of this comparison is unknown.

- `operand [NOT] BETWEEN operand1 AND operand2`

  Checks the assignment to an interval. The relational expression has the same effect as the corresponding [condition for statements](abenwhere_logexp_interval.md). The operands can have the same data types as for size comparisons. For `operand1` and `operand2`, any [SQL expressions](abapsql_expr.md) except [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified. If one of the operands has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the check is unknown.

- `operand1 [NOT] LIKE operand2 [ESCAPE esc]`

  Pattern comparison. The relational expression has the same effect as the corresponding [condition for statements](abenwhere_logexp_like.md). The same applies to the operands as in the [condition for statements](abenwhere_logexp_like.md). The operands must be character-like and only [literals](abenabap_sql_literals.md) and [host variables](abenabap_sql_host_variables.md) can be specified on the right-hand side.

- `operand IS [NOT] NULL`

  Checks for the [null value](../../abap-glossary/abennull_value_glosry.md). The relational expression has the same effect as the corresponding [condition for statements](abenwhere_logexp_null.md).

- `operand IS [NOT] INITIAL`

  Checks for the initial value of the assigned elementary ABAP type. The relational expression has the same effect as the corresponding [condition for statements](abenwhere_logexp_initial.md).

The operands on the left side can be any SQL expressions except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md). All columns and expressions, except for `LIKE`, can have any dictionary type except for `ACCP`, `LCHR`, `LRAW`, `PREC`, `RAWSTRING`, `STRING`, and `GEOM_EWKB`. Individually specified literals, host variables, and host expressions are handled as [elementary SQL expressions](abensql_elem.md) and can be of any ABAP type.

It must be possible to [compare](abenwhere_logexp_compare_types.md) the data types of the operands of a relational expression. If this is not the case, a statically specified type raises a syntax error and a dynamically specified type raises an exception of the class `CX_SY_DYNAMIC_OSQL_SEMANTICS`. Unlike in [conditions for statements](abenabap_sql_stmt_logexp.md), operands of the types `DATS` and `TIMS` are handled like regular flat character-like operands.

If an expression is used for a selection, the [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source of a query or the target of a write statement in an SQL condition of this expression cannot be used as an operand due to [implicit client handling](abenabap_sql_client_handling.md).

## Hints

- Because an expression is passed to the database essentially unchanged, the possible relational expressions and their operands represent only a subset of the [relational expressions for statements](abenabap_sql_stmt_logexp.md). In some constructs, however, a `WHERE`, `HAVING`, or `ON` condition of a statement is processed by the ABAP runtime framework before the pass, to achieve platform-independent behavior.

- When specifying [literals](abenabap_sql_literals.md), [host variables](abenabap_sql_host_variables.md), and [host expressions](abenabap_sql_host_expressions.md), it should be noted that these are used as elementary SQL expressions in expressions and that their ABAP type is mapped to a dictionary type according to the corresponding [tables](abensql_elem.md). This type must fulfill the [comparability](abenwhere_logexp_compare_types.md) rules. This differs from [relational expressions for statements](abenabap_sql_stmt_logexp.md), for which the ABAP type is generally converted to the appropriate dictionary type.

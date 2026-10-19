---
title: "sql_cond - rel_exp for Statements"
source_file: abenabap_sql_stmt_logexp.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - rel_exp for Statements

## Syntax

``` abap
... { {operand1 {=|EQ|<>|NE|>|GT|<|LT|>=|GE|<=|LE} 
                  {  operand2 
                  | {[ALL|ANY|SOME] ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )} }} 
    | {operand [NOT] BETWEEN operand1 AND operand2} 
    | {operand1 [NOT] LIKE operand2 [ESCAPE esc]} 
    | {operand IS [NOT] NULL} 
    | {operand IS [NOT] INITIAL} 
    | {EXISTS ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )} 
    | {operand [NOT] IN (operand1, operand2 ...)} 
    | {operand [NOT] IN ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )} 
    | {( operand1, operand2, ... ) IN ( ( operand11, operand21 ... ), 
                                        ( operand12, operand22 ... ), ... )} 
    | {operand [NOT] IN @range_tab} 
    | {(cond_syntax)} } ...  
```

[`=|EQ|<>|NE|>|GT|<|LT|>=|GE|<=|LE`](abenwhere_logexp_compare.md) · [`operand2`](abenwhere_logexp_compare.md) · [`[ALL|ANY|SOME]`](abenwhere_logexp_all_any_some.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`operand [NOT] BETWEEN operand1 AND operand2`](abenwhere_logexp_interval.md) · [`operand1 [NOT] LIKE operand2 [ESCAPE esc]`](abenwhere_logexp_like.md) · [`operand IS [NOT] NULL`](abenwhere_logexp_null.md) · [`operand IS [NOT] INITIAL`](abenwhere_logexp_initial.md) · [`EXISTS`](abenwhere_logexp_exists.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`operand [NOT] IN (operand1, operand2 ...)`](abenwhere_logexp_operand_in.md) · [`operand [NOT] IN`](abenwhere_logexp_operand_in.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`( operand1, operand2, ... ) IN ( ( operand11, operand21 ... ),`](abenwhere_logexp_list_in.md) · [`( operand12, operand22 ... ), ... )`](abenwhere_logexp_list_in.md) · [`operand [NOT] IN @range_tab`](abenwhere_logexp_seltab.md) · [`(cond_syntax)`](abenwhere_logexp_dynamic.md)

## Description

Relational expression in a condition of an ABAP SQL statement. Logical expressions `sql_cond` can be formed from the relational expressions shown here for the following conditions:

- Read accesses

  - [`WHERE` clause](abapwhere.md) of a [query](../../abap-glossary/abenasql_query_glosry.md)

  - [`HAVING` clause](abaphaving_clause.md) of a [query](../../abap-glossary/abenasql_query_glosry.md)

  - [`ON` condition](abapselect_join.md) of a [join expression](../../abap-glossary/abenjoin_expression_glosry.md)

- Modifying accesses

  - [`WHERE` condition](abapupdate_source.md) of the statement [`UPDATE`](abapupdate.md)

  - [`WHERE` condition](abapdelete_where.md) of the statement [`DELETE`](abapdelete_dbtab.md)

Possible operands of a relational expression are elementary [SQL operands](abensql_operands.md) and [SQL expressions](abapsql_expr.md). The kind of expression and where it is used determine which operands can be used and where. The following principles apply:

- On the right side of relational expressions, [elementary SQL expressions](abensql_elem.md), [cast expressions](abensql_cast.md), and built-in [SQL functions](abensql_builtin_func.md) can be used. No other [SQL expressions](abapsql_expr.md) are possible. [Typed literals](abenabap_sql_typed_literals.md) are handled as elementary SQL expressions, while [untyped literals](abenabap_sql_untyped_literals.md) are handled like [host variables](abenabap_sql_host_variables.md).

- [Aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can only be used as operands in the [`HAVING`](abaphaving_clause.md) clause of a [query](../../abap-glossary/abenasql_query_glosry.md), but also on the right side.

- [Window expressions](../../abap-glossary/abenwindow_expression_glosry.md) cannot be used.

- Operands of the type `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, or `GEOM_EWKB` cannot be used. One exception is the expression [`IS [NOT] NULL`](abenwhere_logexp_null.md), which can also evaluate [LOBs](../../abap-glossary/abenlob_glosry.md) and [geodata types](../../abap-glossary/abengeo_data_type_glosry.md).

A relational expression `rel_exp` is either

- true

- false, or

- unknown.

The expression is unknown if one of the operands involved contains the [null value](../../abap-glossary/abennull_value_glosry.md) and is evaluated with a comparison other than [`IS NULL`](abenwhere_logexp_null.md). The result of joins of relational expressions with unknown results is described under [`AND, OR, NOT`](abenwhere_logexp_andornot.md).

In an SQL condition of a statement, the [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source of a query or of the target of a write statement cannot be used as an operand due to [implicit client handling](abenabap_sql_client_handling.md).

## Hints

- In comparisons between values determined on the database, it is essential that only operands of the same type and the same length are used. This avoids platform-dependent conversions from taking place.

- The following elements of relational expressions cannot be handled by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md):

  - [SQL Expressions](abapsql_expr.md) except those listed under [ABAP SQL In-Memory Engine, Supported SQL Expressions](abensql_engine_expr.md).

  - Comparisons between different types except the following cases: Both operands have numeric types except `DF16_DEC` or `DF34_DEC`; both operands are character-like; both operands have the type `RAW` with the same length.

    Statements that use relational expressions that cannot be handled by the ABAP SQL in-memory engine bypass the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- The ABAP SQL statement bypasses [table buffering](../../abap-glossary/abentable_buffering_glosry.md) if items other than [host variables](../../abap-glossary/abenhost_variable_glosry.md) or [host expressions](../../abap-glossary/abenhost_expression_glosry.md) are specified on the right side of a relational expression or are used to identify a single record or a generically buffered area.

- A client column can be used as an operand only if [implicit client handling](abenabap_sql_client_handling.md) is disabled using the obsolete addition `CLIENT SPECIFIED` for the query or the write statement.

- That the result of a check is unknown if one of the operands has the [null value](../../abap-glossary/abennull_value_glosry.md), is especially true for the [null expression `NULL`](abensql_null.md) that contains the null value by definition.

- Single relational expressions that are unknown can be handled similarly to expressions that are false in the sense that they are not true. Caution is needed when using [`AND, OR, NOT`](abenwhere_logexp_andornot.md). For example, an unknown expression cannot be made true by using `NOT`.

- The rule that the result of an relational expression is unknown if an operand contains the [null value](../../abap-glossary/abennull_value_glosry.md) is overridden by an initial ranges table in the expression [`IN range_tab`](abenwhere_logexp_seltab.md). It also has no effect if an empty internal table is used for [`FOR ALL ENTRIES`](abenwhere_all_entries.md) because then the entire `WHERE` condition is ignored.

---
title: "sql_cond - subquery_clauses"
source_file: abenwhere_logexp_subquery.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - subquery_clauses

## Syntax

``` abap
... { FROM source 
      FIELDS select_clause } 
  | { select_clause 
      FROM source } 
      [WHERE sql_cond] 
      [GROUP BY group] [HAVING group_cond] 
      [ORDER BY [UP TO n ROWS [OFFSET o]]] 
      [db_hints]  ...  
```

[`FROM`](abapfrom_clause.md) · [`FIELDS`](abapfields_clause.md) · [`select_clause`](abapselect_clause.md) · [`select_clause`](abapselect_clause.md) · [`FROM`](abapfrom_clause.md) · [`WHERE`](abapwhere.md) · [`sql_cond`](abenabap_sql_stmt_logexp.md) · [`GROUP BY`](abapgroupby_clause.md) · [`HAVING`](abaphaving_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`[UP TO n ROWS [OFFSET o]]`](abapselect_up_to_offset.html) · [`db_hints`](abenabap_sql_db_hints.md)

## Description

Possible [clauses and additions](abenselect_clauses.md) of a [subquery](../../abap-glossary/abensubquery_glosry.md) in a condition [`sql_cond`](abenabap_sql_stmt_logexp.md) in ABAP SQL.

In the [`FROM`](abapfrom_clause.md) clause, the addition `USING` cannot specified to affect [client handling](../../abap-glossary/abenclient_handling_glosry.md). Client handling of the subquery depends on the client handling of the outer statement. An addition `USING` of the outer statement also affects the subquery.

A subquery can be used within the following relational expressions `sql_cond` for a subquery:

- [`operand operator [ALL|ANY|SOME] subquery`](abenwhere_logexp_all_any_some.md)

- [`[NOT] EXISTS subquery`](abenwhere_logexp_exists.md)

- [`[NOT] IN subquery`](abenwhere_logexp_operand_in.md) ([scalar subquery](../../abap-glossary/abenscalar_subquery_glosry.md))

- [`IN subquery with value tuples`](abenwhere_logexp_list_in.md)

Conditions of a subquery can themselves contain subqueries. In nested subqueries, the columns specified in the SQL conditions are searched inside out and the columns of inner subqueries hide columns with the same name in outer subqueries.

Only a limited number of `SELECT` statements can be used as subqueries in an ABAP SQL statement. The maximum number is defined so that the ABAP SQL statement can be executed on all supported database systems. If known statically, more than 50 `SELECT` statements currently produce a syntax error and otherwise a runtime error. This restriction is independent of whether the subqueries are nested or occur in different relational expressions of the SQL condition.

The addition [`UP TO n ROWS`](abapselect_up_to_offset.md) can only be used after [`ORDER BY`](abaporderby_clause.md) and the addition [`OFFSET`](abapselect_up_to_offset.md) can only be used after [`UP TO n ROWS`](abapselect_up_to_offset.md). An `ORDER BY` clause in a subquery is not supported by all databases. If this is detected at runtime on a database that does not support the pragma, a catchable exception of the class `CX_SY_SQL_UNSUPPORTED_FEATURE` is raised.

## Hints

- In a correlated subquery, a DDIC projection view cannot be accessed in the surrounding `SELECT` statement.

- If a subquery is used in a condition, the ABAP SQL statement cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). It bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- If a [query](../../abap-glossary/abenasql_query_glosry.md) accesses a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) that is linked with a [CDS role](../../abap-glossary/abencds_role_glosry.md) and for which [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is not disabled using the value *\#NOT_ALLOWED* for the annotation [`@AccessControl.authorizationCheck`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) or using the addition [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md) in the [`FROM`](abapfrom_clause.md) clause or [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) for the complete `SELECT` statement, only that data is read that meets the [access condition](../../abap-glossary/abenaccess_condition_glosry.md) defined in the CDS role. If data cannot be read, ABAP programs cannot distinguish whether this is due to the conditions of the `SELECT` statement, the conditions of the CDS entity, or an associated CDS role. If the [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is accessed, no access control takes place.

- In subqueries that are used in the `WHERE` condition of a [`DELETE`](abapdelete_where.md) or [`UPDATE`](abapupdate_source.md) statement, the DDIC database table to be changed cannot be accessed.

## Executable Example

[Subquery in `WHERE` Condition](abenselect_subquery_abexa.md)

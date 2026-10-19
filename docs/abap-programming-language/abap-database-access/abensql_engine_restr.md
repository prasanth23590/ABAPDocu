---
title: "ABAP SQL In-Memory Engine, Restrictions"
source_file: abensql_engine_restr.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - ABAP SQL In-Memory Engine"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL In-Memory Engine, Restrictions

The following language elements of ABAP SQL can be processed on the database but not yet by the ABAP SQL in-memory engine:

- Currently, reads that use one of the following cannot be processed by the ABAP SQL in-memory engine:

  - Use of [subqueries](../../abap-glossary/abensubquery_glosry.md) except those used as [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) in the statement [`WITH`](abapwith.md).

  - The statement [`WITH`](abapwith.md) if access to database tables is involved. The ABAP SQL in-memory engine can process the statement `WITH` if only internal tables are accessed with [`FROM @itab`](abapselect_itab.md) within the complete statement.

  - Use of the ABAP SQL language element [`GROUPING SETS`](abapgrouping_sets_clause.md).

  - Use of the ABAP SQL [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md).

  - Access to a table or view for which a replacement object is defined.

  - Use of a secondary connection specified explicitly using the addition [`CONNECTION`](abapselect_connection.md). If specified, a [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) or a [service connection](../../abap-glossary/abenservice_connection_glosry.md) can be processed by the ABAP SQL in-memory engine.

  - Access to a [CDS table function](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_table_functions.md) or a [CDS scalar function](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_scalar_functions.md).

- Currently, the following elements of a [main query](../../abap-glossary/abenmainquery_glosry.md) cannot be processed by the ABAP SQL in-memory engine:

  - [`JOIN`](abapselect_join.md) expressions if access to database tables is involved. The ABAP SQL in-memory engine can process joins where only internal tables are accessed with [`FROM @itab`](abapselect_itab.md).

  - [SQL Expressions](abapsql_expr.md) except those listed under [ABAP SQL In-Memory Engine, Supported SQL Expressions](abensql_engine_expr.md).

  - [Hierarchy data](abenselect_hierarchy_data.md): [CDS hierarchies](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_hierarchies.md) and [hierarchy functions](../../abap-glossary/abenhierarchy_function_glosry.md) [`SELECT FROM HIERARCHY`](abenselect_hierarchy_generator.md) and [`SELECT FROM hierarchy_navigator`](abenselect_hierarchy_navigators.md).

  - Additions [`DISTINCT`](abapselect_clause.md) and [`FOR UPDATE`](abapselect_single.md).

  - The [`GROUP BY`](abapgroupby_clause.md) clause and therefore the [`HAVING`](abaphaving_clause.md) clause too.

- Currently, the following elements of [SQL conditions](abenasql_cond.md) in the `WHERE` clause cannot be processed by the ABAP SQL in-memory engine:

  - [SQL Expressions](abapsql_expr.md) except those listed under [ABAP SQL In-Memory Engine, Supported SQL Expressions](abensql_engine_expr.md).

  - Comparisons between different types except the following cases: Both operands have numeric types except `DF16_DEC` or `DF34_DEC`; both operands are character-like; both operands have the type `RAW` with the same length.

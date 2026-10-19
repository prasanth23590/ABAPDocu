---
title: "ABAP SQL - Null Values"
source_file: abenabap_sql_null_values.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Null Values

A null value is a special value returned by a [database](../../abap-glossary/abendatabase_glosry.md) in order to indicate an undefined value or result. Null values do not correspond to any content of [data objects](../../abap-glossary/abendata_object_glosry.md) in ABAP. Especially, a null value is not the same as a type-dependent initial value.

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), null values can be handled using one of the following:

- The condition [`IS NULL`](abenwhere_logexp_null.md)

- The special expression [`sql_null`](abensql_null.md)

- A [null indicator](../../abap-glossary/abennull_indicator_glosry.md)

- The function [`coalesce`](abensql_coalesce.md)

- The parameter `on_null` in [date/time conversion functions](abensql_date_time_conversions.md)

ABAP SQL statements for [write access](abenabap_sql_writing.md) generally do not create null values, except when processing [views](../../abap-glossary/abenview_glosry.md) that do not cover all columns of a database table.

As values of database fields, null values might occur in the following situations:

- Depending on the [database system](../../abap-glossary/abendatabase_system_glosry.md), empty [strings](../../abap-glossary/abenstring_glosry.md) can also be represented by null values.

- Null values can be produced in DDIC database tables if new columns are appended to filled tables.

In read accesses with the ABAP SQL statement [`SELECT`](abapselect.md), null values can be produced by

- [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md),

- outer [joins](../../abap-glossary/abenjoin_glosry.md),

- [SQL expressions](../../abap-glossary/abensql_expression_glosry.md),

- when [CDS entities](../../abap-glossary/abencds_entity_glosry.md) containing such constructs are accessed.

When they are passed to data objects, they are transformed to type-dependent [initial values](../../abap-glossary/abeninitial_value_glosry.md). However, in the additions [`GROUP BY`](abapgroupby_clause.md) and [`ORDER BY`](abaporderby_clause.md), in the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) or internal tables as [data sources](abapselect_itab.md), null values are handled as null values. A [null indicator](../../abap-glossary/abennull_indicator_glosry.md) of a structured target area of a query can show which columns of the result set contain null values and which do not.

## Hints

- When [subqueries](../../abap-glossary/abensubquery_glosry.md) are inserted using [`INSERT`](abapinsert_dbtab.md) or [`MODIFY`](abapmodify_dbtab.md), null values are also transformed to type-dependent initial values or raise an exception after an attempt to set a key field to the null value.

- It is, by principle, not possible to insert null values in key fields of DDIC database tables. If an attempt is made, this raises an exception on the database.

- In the ABAP Dictionary, a [flag for initial values](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_init.md) can be set when inserting new columns in existing DDIC database tables to preserve the type-dependent initial value instead of the null value.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, the condition `IS NULL` is true because the [`CASE`](abensql_case.md) expression on the left side does not find a true `WHEN` condition and does not have an `ELSE` branch.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( id = 'X' ) ). 
 
SELECT SINGLE '_' AS id 
       FROM demo_expressions 
       WHERE CASE WHEN id = 'Y' THEN 'Z' END IS NULL 
       INTO @FINAL(wa).
```

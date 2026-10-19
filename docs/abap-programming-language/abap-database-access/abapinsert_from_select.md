---
title: "INSERT, MODIFY writable_obj, subquery_clauses"
source_file: abapinsert_from_select.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, MODIFY writable_obj, subquery_clauses

## Syntax

``` abap
... { FROM source 
      FIELDS select_clause } 
  | { select_clause 
      FROM source } 
      [WHERE sql_cond] 
      [GROUP BY group] [HAVING group_cond] 
      [ORDER BY [UP TO n ROWS [OFFSET o]]] 
      [db_hints] 
      [OPTIONS] 
        [PRIVILEGED ACCESS] ...  
```

[`FROM`](abapfrom_clause.md) · [`FIELDS`](abapfields_clause.md) · [`select_clause`](abapselect_clause.md) · [`select_clause`](abapselect_clause.md) · [`FROM`](abapfrom_clause.md) · [`WHERE`](abapwhere.md) · [`sql_cond`](abenabap_sql_stmt_logexp.md) · [`GROUP BY`](abapgroupby_clause.md) · [`HAVING`](abaphaving_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`[UP TO n ROWS [OFFSET o]]`](abapselect_up_to_offset.html) · [`db_hints`](abenabap_sql_db_hints.md) · [`OPTIONS`](abapselect_options.md) · [`PRIVILEGED ACCESS`](abapselect_privileged_access.md)

## Description

Possible [clauses and additions](abenselect_clauses.md) of a [subquery](../../abap-glossary/abensubquery_glosry.md) after the addition `FROM` of the statements [`INSERT`](abapinsert_dbtab.md) and [`MODIFY`](abapmodify_dbtab.md). These clauses define a result set, which is used as a data source of the `INSERT` or `MODIFY` statement.

Apart from the client column, the result set of the subquery must have at least as many columns as the primary key of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) that is filled using the `INSERT` statement or modified using the `MODIFY` statement. It cannot, however, have more columns than the target [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md).

The following special rules apply:

- `FROM` clause

  - If the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) processed using the `INSERT` or `MODIFY` statement is [client-dependent](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_client.md), at least one data source of the subquery must be client-dependent.

- `SELECT` clause

  - Any [`SELECT` lists](abapselect_list.md) of the subquery specified as comma-separated lists must define one column of the result set for at least every column of the primary key of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled.

  - In a [`SELECT` list](abapselect_list.md) of the subquery specified using `*`, the result set produced for at least every column of the primary key of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled must contain a column.

    If the subquery uses default client handling, the client column of the result set is ignored.

- `ORDER BY` clause

  - The addition [`UP TO n ROWS`](abapselect_up_to_offset.md) can only be used after [`ORDER BY`](abaporderby_clause.md).

  - The addition [`OFFSET`](abapselect_up_to_offset.md) can only be used after [`UP TO n ROWS`](abapselect_up_to_offset.md).

  - For the variant `ORDER BY n` that specifies the position of a column, [special rules](abapinsert_from_select_order_by_n.md) apply.

  - An `ORDER BY` clause in a subquery is not supported by all databases. If this is detected at runtime on a database that does not support the pragma, a catchable exception of the class `CX_SY_SQL_UNSUPPORTED_FEATURE` is raised.

- `OPTIONS`

  - Behind [`OPTIONS`](abapselect_options.md), the addition [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) can be placed.

A further subquery within the subquery cannot access the table processed using the `INSERT` or `MODIFY` statement.

## Hints

- If a subquery is used, the ABAP SQL statement cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- If a [query](../../abap-glossary/abenasql_query_glosry.md) accesses a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) that is linked with a [CDS role](../../abap-glossary/abencds_role_glosry.md) and for which [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is not disabled using the value *\#NOT_ALLOWED* for the annotation [`@AccessControl.authorizationCheck`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) or using the addition [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md) in the [`FROM`](abapfrom_clause.md) clause or [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) for the complete `SELECT` statement, only that data is read that meets the [access condition](../../abap-glossary/abenaccess_condition_glosry.md) defined in the CDS role. If data cannot be read, ABAP programs cannot distinguish whether this is due to the conditions of the `SELECT` statement, the conditions of the CDS entity, or an associated CDS role. If the [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is accessed, no access control takes place.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of columns of a result set formed by an inner join in a table entity.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_cds_join1_te. 
INSERT demo_cds_join1_te 
  FROM TABLE @( VALUE #( ( a = 'a1' b = 'b1' d = 'd1' ) 
                         ( a = 'a2' b = 'b2' d = 'd2' ) 
                         ( a = 'a3' b = 'b3' d = 'd3' ) ) ). 
DELETE FROM demo_cds_join2_te. 
INSERT demo_cds_join2_te 
  FROM TABLE @( VALUE #( ( d = 'd1' e = 'e1' f = 'f1' ) 
                         ( d = 'd2' e = 'e2' f = 'f2' ) 
                         ( d = 'd3' e = 'e3' f = 'f3' ) ) ). 
 
DELETE FROM demo_cds_join3_te. 
INSERT demo_cds_join3_te  FROM ( SELECT FROM demo_cds_join1_te AS d1 
                                   INNER JOIN demo_cds_join2_te AS d2 
                                     ON d1~d = d2~d 
                                 FIELDS d1~a, d1~b, d2~e, d2~f ). 
 
SELECT * 
       FROM demo_cds_join3_te 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

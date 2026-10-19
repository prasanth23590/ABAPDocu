---
title: "WITH, subquery_clauses"
source_file: abapwith_subquery.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, subquery_clauses

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

Possible [clauses and additions](abenselect_clauses.md) of [subqueries](../../abap-glossary/abensubquery_glosry.md) of a [`WITH`](abapwith.md) statement. These clauses define the result set of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md).

The result set can be used as a temporary table in subsequent subqueries and in the main query of the current `WITH` statement as a data source [`data_source`](abapselect_data_source.md).

The names of the columns of the result set are defined by the [`SELECT`](abapselect_list.md) of the subquery by default. However, they can be overwritten in the `WITH` statement. If a union set, an intersection set, or a difference set is created in the subquery using [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md) the column names are determined by the `SELECT` list of the first `SELECT` statement.

If the clauses of the subquery contain dynamic tokens, the common table expression can only be used in other dynamic tokens of the `WITH` statement.

The addition [`UP TO n ROWS`](abapselect_up_to_offset.md) can only be used after [`ORDER BY`](abaporderby_clause.md) and the addition [`OFFSET`](abapselect_up_to_offset.md) can only be used after [`UP TO n ROWS`](abapselect_up_to_offset.md). An `ORDER BY` clause in a subquery is not supported by all databases. If this is detected at runtime on a database that does not support the pragma, a catchable exception of the class `CX_SY_SQL_UNSUPPORTED_FEATURE` is raised.

## Hints

- If a [query](../../abap-glossary/abenasql_query_glosry.md) accesses a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) that is linked with a [CDS role](../../abap-glossary/abencds_role_glosry.md) and for which [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) is not disabled using the value *\#NOT_ALLOWED* for the annotation [`@AccessControl.authorizationCheck`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) or using the addition [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md) in the [`FROM`](abapfrom_clause.md) clause or [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) for the complete `SELECT` statement, only that data is read that meets the [access condition](../../abap-glossary/abenaccess_condition_glosry.md) defined in the CDS role. If data cannot be read, ABAP programs cannot distinguish whether this is due to the conditions of the `SELECT` statement, the conditions of the CDS entity, or an associated CDS role. If the [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is accessed, no access control takes place.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Subquery of a common table expression `+flights` with almost all possible clauses. Since the [`ORDER BY`](abaporderby_clause.md) clause followed by the addition [`UP TO`](abapselect_up_to_offset.md) is not supported by all databases, a syntax warning from the extended program check is raised that can be hidden here using the pragma `##db_feature_mode[limit_in_subselect_or_cte]`.

``` abap
DATA carrids TYPE RANGE OF sflight-carrid. 
 
... 
 
WITH 
  +flights AS ( SELECT FROM sflight 
                       FIELDS carrid, 
                              connid, 
                              AVG( seatsocc AS DEC( 16,2 ) ) AS avg 
                       WHERE carrid IN @carrids 
                       GROUP BY carrid, connid 
                       ORDER BY carrid, connid UP TO 1 ROWS ) 
                       ##db_feature_mode[limit_in_subselect_or_cte] 
  SELECT FROM +flights AS f 
           INNER JOIN scarr AS s 
             ON f~carrid = s~carrid 
         FIELDS s~carrname, f~connid, f~avg 
         ORDER BY s~carrname, f~connid 
         INTO TABLE @FINAL(itab).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a common table expression in which all clauses of the subquery and the main query are specified as dynamic tokens. In the [`INTO`](abapinto_clause.md) clause, the addition [`NEW`](abapselect_into_target.md) and the declaration operator [`@FINAL(...)`](abapselect_into_target.md) are used to declare a generic data reference variable that points to the result in an anonymous data object.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA carrid TYPE spfli-carrid VALUE 'LH'. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
DATA: 
  sel_sub1 TYPE string VALUE `cityfrom AS city`, 
  sel_sub2 TYPE string VALUE `cityto AS city`, 
  frm_sub  TYPE string VALUE `spfli`, 
  whr_sub  TYPE string VALUE `carrid = @carrid`, 
  sel_main TYPE string VALUE `*`, 
  frm_main TYPE string VALUE `sgeocity`, 
  whr_main TYPE string VALUE `city IN ( SELECT city FROM +cities )`. 
 
WITH 
  +cities AS ( 
    SELECT (sel_sub1) 
           FROM (frm_sub) 
           WHERE (whr_sub) 
    UNION DISTINCT 
    SELECT (sel_sub1) 
           FROM (frm_sub) 
           WHERE (whr_sub) ) 
  SELECT (sel_main) 
         FROM (frm_main) 
         WHERE (whr_main) 
         INTO TABLE NEW @FINAL(result). 
 
out->write( result->* ). 
 
out->display( ).
```

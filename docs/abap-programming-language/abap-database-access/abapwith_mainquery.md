---
title: "WITH, mainquery_clauses"
source_file: abapwith_mainquery.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, mainquery_clauses

## Syntax

``` abap
... [SINGLE [FOR UPDATE]] 
    { FROM source 
      FIELDS select_clause } 
  | { select_clause 
      FROM source } 
    [WHERE sql_cond] 
    [GROUP BY group] [HAVING group_cond] 
    [ORDER BY sort_key] 
    [db_hints] ...  
```

[`SINGLE [FOR UPDATE]`](abapselect_single.md) · [`FROM`](abapfrom_clause.md) · [`FIELDS`](abapfields_clause.md) · [`select_clause`](abapselect_clause.md) · [`select_clause`](abapselect_clause.md) · [`FROM`](abapfrom_clause.md) · [`WHERE`](abapwhere.md) · [`GROUP BY`](abapgroupby_clause.md) · [`HAVING`](abaphaving_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`db_hints`](abenabap_sql_db_hints.md)

## Description

Possible [clauses and additions](abenselect_clauses.md) of the main query of a [`WITH`](abapwith.md) statement. All clauses are possible as in a standalone [`SELECT`](abapselect.md) statement except for [`FOR ALL ENTRIES`](abenwhere_all_entries.md), and they have the same effect. In particular, a `SELECT` loop is opened under the same circumstances as in the standalone [`SELECT`](abapselect.md) statement. In this case, this loop must be closed with [`ENDWITH`](abapendwith.md).

The result set of a common table expression does not have a client column, which means that the [`FROM`](abapfrom_clause.md) clause of the main query cannot contain the addition `USING` for switching for disabling [implicit client handling](abenabap_sql_client_handling.md).

If an internal table [`@itab`](abapselect_data_source.md) with elementary row type is accessed in the [`FROM`](abapfrom_clause.md) clause of a common table expression, the [`SELECT` list](abapselect_list.md) cannot be `*` or contain `data_source~*`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows a `WITH` statement whose main query creates a tabular result set. Since the example writes to an internal table `itab`, no `SELECT` loop is opened.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
WITH 
  +carriers AS ( SELECT FROM scarr 
                        FIELDS carrid, carrname ) 
  SELECT FROM spfli AS s 
           INNER JOIN +carriers AS c 
             ON s~carrid = c~carrid 
         FIELDS c~carrname, s~connid 
         WHERE s~carrid = 'UA' 
         INTO TABLE @FINAL(itab) 
         UP TO 10 ROWS. 
 
out->write( itab ). 
 
out->display( ).
```

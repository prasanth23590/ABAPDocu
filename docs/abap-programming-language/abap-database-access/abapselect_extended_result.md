---
title: "SELECT, extended_result"
source_file: abapselect_extended_result.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, extended_result

## Syntax

``` abap
... EXTENDED RESULT @oref ...  
```

## Description

The `EXTENDED RESULT` addition of the [`INTO`](abapinto_clause.md) clause can be used to provide an extended result of the current [main query](../../abap-glossary/abenmainquery_glosry.md) in a result object. After `EXTENDED RESULT`, an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) `oref` of static type for the documented class `CL_OSQL_EXTENDED_RESULT` must be specified as a [host variable](abenabap_sql_host_variables.md), which points to an object of the class. The reference variable must be prefixed with the escape character `@`.

The following applies to the use of `EXTENDED RESULT`:

- The reference variable must not be initial and the object must be created before the ABAP SQL statement is executed. Parameters that specify which values the extended result should include must be passed to the instance constructor of class `CL_OSQL_EXTENDED_RESULT`.

- If possible, the result object is filled with the requested values during the first database access.

  - If a loop is opened using the statements [`SELECT`](abapselect.md) or [`WITH`](abapwith.md), the result object is filled once when the loop is entered.

  - If the [`INTO`](abapinto_clause.md) clause after `FETCH` is used for the result set of a database cursor opened using `OPEN CURSOR`, the result object is filled once in the first `FETCH` statement.

- After the ABAP SQL statement is closed, the required values can be read using the instance methods of the class. If the result object then contains no results or no valid results, an exception of the class `CX_OSQL_EXTENDED_RESULT` is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Excerpt from the executable example SAP HANA, Cached Views.

``` abap
FINAL(extended_result) = 
  NEW cl_osql_extended_result( iv_cached_view = abap_true ). 
SELECT carrid, 
       MAX( fldate )   AS max_fldate, 
       MIN( price )    AS min_price, 
       SUM( seatsocc ) AS sum_seatsocc 
       FROM demo_cds_cached_view 
       GROUP BY carrid 
       %_HINTS HDB 'RESULT_CACHE' 
       INTO TABLE @FINAL(result) 
       EXTENDED RESULT @extended_result.
```

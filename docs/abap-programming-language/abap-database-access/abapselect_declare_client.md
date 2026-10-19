---
title: "SELECT, FROM data_source, declare_client"
source_file: abapselect_declare_client.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM data_source, declare_client

## Syntax

``` abap
... DECLARE CLIENT clnt_col  
```

## Description

The optional addition `DECLARE CLIENT` declares the data source as client-dependent for the current read access and the column specified by the operand `clnt_col` as its [client column](../../abap-glossary/abenclient_column_glosry.md). ABAP SQL's [implicit client handling](abenabap_sql_client_handling.md) takes place for that data source as it does for any [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data source.

The addition `DECLARE CLIENT` can be specified for all [client-independent](../../abap-glossary/abenclient_independent_glosry.md) data sources [`data_source`](abapselect_data_source.md) that have a column with a name specified by the operand `clnt_col`. The column must have type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) of length 3.

## Hints

- The addition `DECLARE CLIENT` can be used in any positions where data sources can be specified, as for example in join expressions and for all kinds of data sources including [SQL hierarchies](abenselect_hierarchy.md). The column `clnt_col` should be specified in a way to produce meaningful results.

- Examples for [client-independent](../../abap-glossary/abenclient_independent_glosry.md) data sources are:

  - [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) without [client column](../../abap-glossary/abenclient_column_glosry.md) as the first key field.

  - [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) that are implicitly or declared as client independent.

  - Any [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) (CTEs).

  - Any internal table specified with [`FROM @itab`](abapselect_itab.md)

- The addition `DECLARE CLIENT` enables client handling for data sources that otherwise are never client-dependent (CTEs, internal tables).

- The column specified by `client_col` can have any position in the data source. It is not required to be in the first position.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statements read data for the current client from an internal table. In the first `SELECT` statement, the column `col2` is declared as the client column and implicit client handling takes place. `SELECT` statement uses an explicit `WHERE` condition.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struc, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE c LENGTH 3, 
    col3 TYPE i, 
  END OF struc, 
  itab TYPE STANDARD TABLE OF struc WITH EMPTY KEY. 
 
DATA(itab) = VALUE itab( 
  ( col1 = 'A' col2 = '000' col3 = 1 ) 
  ( col1 = 'B' col2 = '100' col3 = 2 ) 
  ( col1 = 'C' col2 = '200' col3 = 3 ) 
  ( col1 = 'D' col2 = '400' col3 = 4 ) 
   ). 
 
SELECT * 
       FROM @itab AS itab DECLARE CLIENT col2 
       INTO TABLE @FINAL(result_current). 
 
out->write( result_current ). 
 
SELECT * 
       FROM @itab AS itab 
       WHERE col2 = @sy-mandt 
       INTO TABLE @FINAL(result_sy_mandt). 
 
ASSERT result_sy_mandt = result_current. 
 
out->display( ).
```

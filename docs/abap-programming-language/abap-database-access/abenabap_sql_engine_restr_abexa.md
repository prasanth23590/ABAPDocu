---
title: "ABAP SQL In-Memory Engine, Restrictions"
source_file: abenabap_sql_engine_restr_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - ABAP SQL In-Memory Engine > ABAP SQL In-Memory Engine, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL In-Memory Engine, Restrictions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the access to internal tables in the statement [`WITH`](abapwith.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_abap_sql_with_itab DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_sql_with_itab IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      from_id TYPE spfli-carrid VALUE 'AA', 
      to_id   TYPE spfli-carrid VALUE 'UA'. 
 
    SELECT * FROM spfli   INTO TABLE @FINAL(spfli_tab). 
    SELECT * FROM scarr   INTO TABLE @FINAL(scarr_tab). 
    SELECT * FROM sflight INTO TABLE @FINAL(sflight_tab). 
 
    "Access to database tables 
    WITH 
      +connections AS ( 
        SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
               FROM spfli 
               INNER JOIN scarr 
                 ON scarr~carrid = spfli~carrid 
               WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
      +sum_seats AS ( 
        SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
               FROM sflight 
               WHERE carrid BETWEEN @from_id AND @to_id 
               GROUP BY carrid, connid ), 
      +result( name, connection, departure, arrival, occupied ) AS ( 
        SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
               FROM +connections AS c 
                 INNER JOIN +sum_seats AS s 
                   ON c~carrid = s~carrid AND 
                      c~connid = s~connid ) 
      SELECT * 
             FROM +result 
             ORDER BY name, connection 
             INTO TABLE @FINAL(result1). 
 
    "The following accesses must be processed on the database 
    "because of subqueries and aggregate function SUM. 
    "Only one internal table can be accessed and transported to the DB. 
 
    WITH 
      +connections AS ( 
        SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
               FROM @spfli_tab AS spfli  "<--- internal table 
               INNER JOIN scarr 
                 ON scarr~carrid = spfli~carrid 
               WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
      +sum_seats AS ( 
        SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
               FROM sflight 
               WHERE carrid BETWEEN @from_id AND @to_id 
               GROUP BY carrid, connid ), 
      +result( name, connection, departure, arrival, occupied ) AS ( 
        SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
               FROM +connections AS c 
                 INNER JOIN +sum_seats AS s 
                   ON c~carrid = s~carrid AND 
                      c~connid = s~connid ) 
      SELECT * 
             FROM +result 
             ORDER BY name, connection 
             INTO TABLE @FINAL(result2). 
 
    ASSERT result2 = result1. 
 
    WITH 
      +connections AS ( 
        SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
               FROM spfli 
               INNER JOIN @scarr_tab AS scarr "<--- internal table 
                 ON scarr~carrid = spfli~carrid 
               WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
      +sum_seats AS ( 
        SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
               FROM sflight 
               WHERE carrid BETWEEN @from_id AND @to_id 
               GROUP BY carrid, connid ), 
      +result( name, connection, departure, arrival, occupied ) AS ( 
        SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
               FROM +connections AS c 
                 INNER JOIN +sum_seats AS s 
                   ON c~carrid = s~carrid AND 
                      c~connid = s~connid ) 
      SELECT * 
             FROM +result 
             ORDER BY name, connection 
             INTO TABLE @FINAL(result3). 
 
    ASSERT result3 = result1. 
 
    WITH 
      +connections AS ( 
        SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
               FROM spfli 
               INNER JOIN scarr 
                 ON scarr~carrid = spfli~carrid 
               WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
      +sum_seats AS ( 
        SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
               FROM @sflight_tab AS sflight "<--- internal table 
               WHERE carrid BETWEEN @from_id AND @to_id 
               GROUP BY carrid, connid ), 
      +result( name, connection, departure, arrival, occupied ) AS ( 
        SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
               FROM +connections AS c 
                 INNER JOIN +sum_seats AS s 
                   ON c~carrid = s~carrid AND 
                      c~connid = s~connid ) 
      SELECT * 
             FROM +result 
             ORDER BY name, connection 
             INTO TABLE @FINAL(result4). 
 
    ASSERT result4 = result1. 
 
*    Not possible, since multiple tables cannot be transported to DB 
*    WITH 
*      +connections AS ( 
*        SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
*               FROM @spfli_tab as spfli 
*               INNER JOIN @scarr_tab as scarr 
*                 ON scarr~carrid = spfli~carrid 
*               WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
*      +sum_seats AS ( 
*        SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
*               FROM @sflight_tab AS sflight 
*               WHERE carrid BETWEEN @from_id AND @to_id 
*               GROUP BY carrid, connid ), 
*      +result( name, connection, departure, arrival, occupied ) AS ( 
*        SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
*               FROM +connections AS c 
*                 INNER JOIN +sum_seats AS s 
*                   ON c~carrid = s~carrid AND 
*                      c~connid = s~connid ) 
*      SELECT * 
*             FROM +result 
*             ORDER BY name, connection 
*             INTO TABLE @FINAL(result5). 
* 
*    ASSERT result5 = result1. 
 
    out->write(  'Success' ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Behind [`WITH`](abapwith.md), [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) are defined, each accessing a different data source. Since the aggregate function `SUM` cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md), the `WITH` statement must be processed on the database. Since only one internal table can be transported to the database for each ABAP SQL statement, access to only one internal table is possible in each `WITH` statement. The last `WITH` statement accessing three internal tables is not allowed.

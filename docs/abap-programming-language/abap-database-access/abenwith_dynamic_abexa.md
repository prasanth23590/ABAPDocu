---
title: "WITH, Dynamic Form"
source_file: abenwith_dynamic_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Dynamic Form

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the dynamic form of statement [`WITH`](abapwith.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Templat for executable demo of ABAP Docu</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_dynamic_with DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_dynamic_with IMPLEMENTATION. 
  METHOD main. 
 
    DATA from_id TYPE spfli-carrid VALUE 'AA'. 
    DATA to_id TYPE spfli-carrid VALUE 'UA'. 
 
    "Static form of WITH statement 
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
             INTO TABLE @FINAL(result). 
 
    DATA dyn_result LIKE result. 
 
    "Fill token table with same syntax as static form 
    DATA token_tab TYPE TABLE OF string WITH EMPTY KEY. 
    token_tab = VALUE #( 
      ( `+connections AS (` ) 
      ( `  SELECT spfli~carrid, carrname, connid, cityfrom, cityto` ) 
      ( `         FROM spfli` ) 
      ( `         INNER JOIN scarr` ) 
      ( `           ON scarr~carrid = spfli~carrid` ) 
      ( `         WHERE spfli~carrid BETWEEN @from_id AND @to_id ),` ) 
      ( `+sum_seats AS (` ) 
      ( `  SELECT carrid, connid, SUM( seatsocc ) AS sum_seats` ) 
      ( `         FROM sflight` ) 
      ( `         WHERE carrid BETWEEN @from_id AND @to_id` ) 
      ( `        GROUP BY carrid, connid ),` ) 
      ( `+result( name, connection, departure, arrival, occupied )` ) 
      ( `  AS (` ) 
      ( `  SELECT carrname, c~connid, cityfrom, cityto, sum_seats` ) 
      ( `         FROM +connections AS c` ) 
      ( `           INNER JOIN +sum_seats AS s` ) 
      ( `             ON c~carrid = s~carrid AND` ) 
      ( `                c~connid = s~connid )` ) 
      ( `SELECT *` ) 
      ( `       FROM +result` ) 
      ( `       ORDER BY name, connection` ) 
    ). 
 
    "Dynamic form of WITH statement with token table 
    WITH (token_tab) 
             INTO TABLE @dyn_result. 
    ASSERT result = dyn_result. 
 
    "Dynamic form of WITH statement with token string 
    DATA token_string TYPE string. 
    CONCATENATE LINES OF token_tab INTO token_string SEPARATED BY ` `. 
    WITH (token_string) 
             INTO TABLE @dyn_result. 
    ASSERT result = dyn_result. 
 
    DATA dyn_wa LIKE LINE OF dyn_result. 
 
    "Dynamic form of WITH loop with token string 
    CLEAR dyn_result. 
    WITH (token_string) 
       INTO @dyn_wa. 
      APPEND dyn_wa TO dyn_result. 
    ENDWITH. 
    ASSERT result = dyn_result. 
 
    "Put WITH also into the token table 
    DATA with_tab LIKE token_tab. 
    with_tab = VALUE #( 
      ( `WITH` ) 
      ( LINES OF token_tab ) 
      ). 
 
    out->write( dyn_result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

First, a static form of [`WITH`](abapwith.md) is executed, then dynamic tokens for the dynamic form are constructed that contain the same syntax as the static form.

- The first dynamic form uses an internal table `token_tab` that contains the syntax.

- The next dynamic form uses a text string `token_string` that contains the syntax.

- The next dynamic form demonstrates a dynamic `WITH` loop terminated with `ENDWITH`.

All ABAP SQL queries yield the same result.

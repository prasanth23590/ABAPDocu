---
title: "ABAP SQL In-Memory Engine, Restriction to One Internal Table"
source_file: abenabap_sql_engine_itab_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - ABAP SQL In-Memory Engine > ABAP SQL In-Memory Engine, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL In-Memory Engine, Restriction to One Internal Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the access to one internal table in the statement [`WITH`](abapwith.md).

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
CLASS cl_demo_abap_sql_with_one_itab DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_sql_with_one_itab IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE spfli-carrid VALUE 'LH'. 
 
    SELECT * FROM spfli INTO TABLE @FINAL(spfli_tab). 
 
    WITH 
      +cities AS ( 
        SELECT cityfrom AS city 
               FROM spfli 
               WHERE carrid = @carrid 
        UNION DISTINCT 
        SELECT cityto AS city 
               FROM spfli 
               WHERE carrid = @carrid ) 
      SELECT * 
             FROM sgeocity 
             WHERE city IN ( SELECT city 
                                    FROM +cities ) 
             INTO TABLE @FINAL(result1). 
 
    "Error: Even the same internal table cam be accessed only once 
*    WITH 
*      +cities AS ( 
*        SELECT cityfrom AS city 
*               FROM @spfli_tab AS spfli  "<-- internal table 
*               WHERE carrid = @carrid 
*        UNION DISTINCT 
*        SELECT cityto AS city 
*               FROM @spfli_tab AS spfli  "<-- internal table 
*               WHERE carrid = @carrid ) 
*      SELECT * 
*             FROM sgeocity 
*             WHERE city IN ( SELECT city 
*                                    FROM +cities ) 
*             INTO TABLE @FINAL(result2). 
* 
*    ASSERT result2 = result1. 
 
    "Workaround: Only one access to internal table in additional CTE 
    WITH 
     +spfli_gtt AS ( SELECT carrid, cityfrom, cityto 
                            FROM @spfli_tab AS spfli "<-- internal table 
                            WHERE carrid = @carrid ), 
      +cities AS ( 
        SELECT cityfrom AS city 
               FROM +spfli_gtt AS spfli 
        UNION DISTINCT 
        SELECT cityto AS city 
               FROM +spfli_gtt AS spfli ) 
      SELECT * 
             FROM sgeocity 
             WHERE city IN ( SELECT city 
                                    FROM +cities ) 
             INTO TABLE @FINAL(result2). 
 
    ASSERT result2 = result1. 
 
    out->write(  'Success' ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Because of the usage of `UNION`, the ABAP SQL statement [`WITH`](abapwith.md) can be processed on the database only and it is not possible to address more than one internal table within the statement, even if it is the same statement: The second `WITH` statement produces a syntax error. As a workaround, the internal table is addressed only once in an additional [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) which is then used twice in the following CTE.

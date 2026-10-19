---
title: "INSERT, FROM SELECT"
source_file: abeninsert_from_select_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > INSERT writable_obj > INSERT writable_obj, source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, FROM SELECT

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the statement [`INSERT`](abapinsert_dbtab.md) with the addition [`FROM SELECT`](abapinsert_source.md).

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
CLASS cl_demo_insert_from_select DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_insert_from_select IMPLEMENTATION. 
  METHOD main. 
    "INSERT FROM TABLE 
    SELECT 
      FROM scarr AS s 
           INNER JOIN spfli AS p ON s~carrid = p~carrid 
      FIELDS s~mandt, 
             s~carrname, 
             p~distid, 
             SUM( p~distance ) AS sum_distance 
      GROUP BY s~mandt, s~carrname, p~distid 
      INTO TABLE @FINAL(temp). 
    INSERT demo_sumdist_agg FROM TABLE @temp. 
 
    SELECT * FROM demo_sumdist_agg 
      ORDER BY carrname, distid, sum_distance 
      INTO TABLE @FINAL(insert_from_table). 
 
    DELETE FROM demo_sumdist_agg. 
 
    "INSERT FROM SELECT 
    INSERT demo_sumdist_agg FROM 
      ( SELECT 
          FROM scarr AS s 
            INNER JOIN spfli AS p ON s~carrid = p~carrid 
          FIELDS s~carrname, 
                 p~distid, 
                 SUM( p~distance ) AS sum_distance 
          GROUP BY s~mandt, s~carrname, p~distid ). 
 
    SELECT * FROM demo_sumdist_agg 
      ORDER BY carrname, distid, sum_distance 
      INTO TABLE @FINAL(insert_from_select). 
 
    DELETE FROM demo_sumdist_agg. "GTT 
 
    IF insert_from_select = insert_from_table. 
      out->write( 
        `Same data inserted by FROM TABLE and FROM SELECT:` 
       )->write( insert_from_select ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The DDIC database table `DEMO_SUMDIST_AGG` is filled with aggregated data from the tables `SCARR` and `SPFLI`.

- First, a standalone `SELECT` statement is used to read the aggregated data into an internal table and then the statement `INSERT` is used to write it to the DDIC database table. This requires two database reads and the transport of the data between the database server and the AS ABAP.

- The same `SELECT` statement is then used directly as a subquery in the `INSERT` statement. Only a single database read and no transport of data between the database server and the AS ABAP is then required.

The result of both `INSERT` statements is the same. `DEMO_SUMDIST_AGG` is a [global temporary table (GTT)](../../abap-glossary/abenglobal_temporary_table_glosry.md), which means that its content must be deleted before the results are produced, since this creates an implicit database commit.

---
title: "ABAP SQL - Connection Objects"
source_file: abenif_abap_sql_connection_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - System Interfaces and Classes > IF_ABAP_SQL_CONNECTION, ABAP SQL Connection Object"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Connection Objects

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) can be created and used.

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
CLASS cl_demo_abap_sql_conn_object DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_sql_conn_object IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( 'ABAP SQL Connection Objects' 
      )->begin_section( 'Create Connection Object' 
      )->begin_code( `conn` ). 
 
    FINAL(conn) = 
      cl_abap_sql_connection_builder=>service( 
        `R/3*service_conn` )->create( ). 
 
    out->end_code( `conn` 
      )->write( conn->describe( ) 
      )->next_section( 'DML Statements' 
      )->begin_code( `DML` ). 
 
    DELETE FROM scarr WHERE carrid = 'XX' 
           OPTIONS 
             CONNECTION @conn. 
    INSERT scarr 
           FROM @( VALUE #( carrid = 'XX' 
                            carrname = 'Jefferson Airplane' ) ) 
           OPTIONS 
             CONNECTION @conn. 
 
    out->end_code( `DML` 
      )->write( COND string( 
                  WHEN conn->has_uncommited_changes( ) = 'X' 
                    THEN 'Uncommitted changes' 
                    ELSE 'No uncommited changes' ) 
      )->next_section( 'Commit' 
      )->begin_code( `commit` ). 
 
    "Both do the same 
    conn->commit( ). 
    COMMIT CONNECTION @conn. 
 
    out->end_code( `commit` 
      )->write( COND string( 
                  WHEN conn->has_uncommited_changes( ) = 'X' 
                    THEN 'Uncommitted changes' 
                    ELSE 'No uncommited changes' ) 
      )->next_section( 'DQL Statement' 
      )->begin_code( `DQL` ). 
 
    SELECT SINGLE 
           FROM scarr 
           FIELDS carrid, carrname 
           WHERE carrid = 'XX' 
           INTO @DATA(result) 
           OPTIONS 
             CONNECTION @conn. 
 
    out->end_code( `DQL` 
      )->write( result 
      )->next_section( 'Close Connection' 
      )->begin_code( `close` ). 
 
    conn->close( ). 
 
    out->end_code( `close` ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `SERVICE` of class `CL_ABAP_SQL_CONNECTION_BUILDER` is used to create a [service connection](../../abap-glossary/abenservice_connection_glosry.md). The connection object is used behind the `CONNECTION` addition of DML statements, `COMMIT` and a DQL statement.

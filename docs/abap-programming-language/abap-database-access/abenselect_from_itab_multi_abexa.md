---
title: "SELECT, Multiple Internal Tables as Data Sources of a Query"
source_file: abenselect_from_itab_multi_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM @itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Multiple Internal Tables as Data Sources of a Query

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a multiple join of internal tables.

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
CLASS cl_demo_select_from_multi_itab DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_from_multi_itab IMPLEMENTATION. 
  METHOD main. 
 
    DATA: 
      demo_join1 TYPE HASHED TABLE OF demo_join1 WITH UNIQUE KEY a, 
      demo_join2 TYPE HASHED TABLE OF demo_join2 WITH UNIQUE KEY d, 
      demo_join3 TYPE HASHED TABLE OF demo_join3 WITH UNIQUE KEY i, 
      demo_join4 TYPE HASHED TABLE OF demo_join4 WITH UNIQUE KEY l. 
 
    demo_join1 = VALUE #( 
           ( a = 'a1' b = 'b1' c = 'c1' d = 'uu' ) 
           ( a = 'a2' b = 'b2' c = 'c2' d = 'uu' ) 
           ( a = 'a3' b = 'b3' c = 'c3' d = 'vv' ) 
           ( a = 'a4' b = 'b4' c = 'c4' d = 'ww' ) ). 
    demo_join2 = VALUE #( 
           ( d = 'uu' e = 'e1' f = 'f1' g = 'g1'  h = 'h1' ) 
           ( d = 'ww' e = 'e2' f = 'f2' g = 'g2'  h = 'h2' ) 
           ( d = 'xx' e = 'e3' f = 'f3' g = 'g3'  h = 'h3' ) ). 
    demo_join3 = VALUE #( 
           ( i = 'i1' j = 'j1' k = 'k1' l = 'vv' ) 
           ( i = 'i2' j = 'j2' k = 'k2' l = 'vv' ) 
           ( i = 'i3' j = 'j3' k = 'k3' l = 'ww' ) ). 
    demo_join4 = VALUE #( 
           ( l = 'uu' m = 'm1' n = 'n1' ) 
           ( l = 'vv' m = 'm2' n = 'n2' ) 
           ( l = 'ww' m = 'm3' n = 'n3' ) ). 
 
    SELECT FROM 
             ( ( @demo_join1 AS t1 
                   INNER JOIN 
                     @demo_join2 AS t2 ON t2~d = t1~d ) 
                       LEFT OUTER JOIN 
                         @demo_join3 AS t3 ON t3~l = t2~d ) 
                           INNER JOIN 
                             @demo_join4 AS t4 ON t4~l = t3~l 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2, 
                  t3~i AS i3, 
                  t3~j AS j3, 
                  t3~k AS k3, 
                  t3~l AS l3, 
                  t4~l AS l4, 
                  t4~m AS m4, 
                  t4~n AS n4 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The `SELECT` statement joins four internal tables. The result is the same as for the respective statement from [`SELECT`, Multiple Joins](abenjoin_joins_abexa.md), where database tables of the same structure and content are joined.

The `SELECT` statements can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md), since only internal tables and no database tables are involved.

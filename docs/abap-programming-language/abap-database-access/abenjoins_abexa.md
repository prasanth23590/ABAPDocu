---
title: "SELECT, Inner, Outer, and Cross Joins"
source_file: abenjoins_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM JOIN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Inner, Outer, and Cross Joins

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates inner and outer [joins](abapselect_join.md) as well as [cross joins](abapselect_join.md) in the `SELECT` statement.

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
CLASS cl_demo_joins DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES wa1 TYPE demo_join1 . 
    TYPES wa2 TYPE demo_join2 . 
    TYPES: 
      BEGIN OF wa. 
        INCLUDE TYPE wa1 AS wa1 RENAMING WITH SUFFIX 1. 
        INCLUDE TYPE wa2 AS wa2 RENAMING WITH SUFFIX 2. 
  TYPES END OF wa . 
    METHODS fill_tables . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_joins IMPLEMENTATION. 
  METHOD main. 
    DATA: itab  TYPE TABLE OF wa, 
          itabi LIKE itab, 
          itab1 LIKE itab, 
          itab2 LIKE itab, 
          itab3 LIKE itab. 
 
    fill_tables( ). 
 
    out->begin_section( `Inner Joins` 
      )->begin_section( `demo1 INNER JOIN demo2` ). 
    SELECT FROM demo_join1 AS t1 
             INNER JOIN demo_join2 AS t2 ON t2~d = t1~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    itabi = itab. 
    out->write( itab 
      )->next_section( `demo2 INNER JOIN demo1` ). 
    SELECT FROM demo_join2 AS t2 
             INNER JOIN demo_join1 AS t1 ON t1~d = t2~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab 
      )->end_section( 
      )->next_section( `Outer Joins` 
      )->begin_section( `demo1 LEFT OUTER JOIN demo2` ). 
    SELECT FROM demo_join1 AS t1 
             LEFT OUTER JOIN demo_join2 AS t2 ON t2~d = t1~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab 
      )->next_section( `demo2 LEFT OUTER JOIN demo1` ). 
    SELECT FROM demo_join2 AS t2 
             LEFT OUTER JOIN demo_join1 AS t1 ON t1~d = t2~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab 
      )->end_section( 
      )->begin_section( `demo1 RIGHT OUTER JOIN demo2` ). 
    SELECT FROM demo_join1 AS t1 
             RIGHT OUTER JOIN demo_join2 AS t2 ON t2~d = t1~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
          ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab 
      )->next_section( `demo2 RIGHT OUTER JOIN demo1` ). 
    SELECT FROM demo_join2 AS t2 
             RIGHT OUTER JOIN demo_join1 AS t1 ON t1~d = t2~d 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab 
      )->end_section( 
      )->next_section( `Cross Joins` 
      )->begin_section( `demo2 CROSS JOIN demo1` ). 
    SELECT FROM demo_join2 AS t2 
             INNER JOIN demo_join1 AS t1 ON 1 = 1 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~a, 
                    t1~b, 
                    t1~c, 
                    t1~d, 
                    t2~d, 
                    t2~e, 
                    t2~f, 
                    t2~g, 
                    t2~h 
           INTO CORRESPONDING FIELDS OF TABLE @itab1. 
    SELECT FROM demo_join2 AS t2 
             LEFT OUTER JOIN demo_join1 AS t1 ON 1 = 1 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~a, 
                    t1~b, 
                    t1~c, 
                    t1~d, 
                    t2~d, 
                    t2~e, 
                    t2~f, 
                    t2~g, 
                    t2~h 
           INTO CORRESPONDING FIELDS OF TABLE @itab2. 
    SELECT FROM demo_join2 AS t2 
             RIGHT OUTER JOIN demo_join1 AS t1 ON 1 = 1 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~a, 
                    t1~b, 
                    t1~c, 
                    t1~d, 
                    t2~d, 
                    t2~e, 
                    t2~f, 
                    t2~g, 
                    t2~h 
           INTO CORRESPONDING FIELDS OF TABLE @itab3. 
    SELECT FROM demo_join2 AS t2 
             CROSS JOIN demo_join1 AS t1 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~a, 
                    t1~b, 
                    t1~c, 
                    t1~d, 
                    t2~d, 
                    t2~e, 
                    t2~f, 
                    t2~g, 
                    t2~h 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    ASSERT itab = itab1. 
    ASSERT itab = itab2. 
    ASSERT itab = itab3. 
    out->write( itab 
      )->next_section( `demo1 CROSS JOIN demo2` ). 
    SELECT FROM demo_join1 AS t1 
             CROSS JOIN demo_join2 AS t2 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           ORDER BY t1~a, 
                    t1~b, 
                    t1~c, 
                    t1~d, 
                    t2~d, 
                    t2~e, 
                    t2~f, 
                    t2~g, 
                    t2~h 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    ASSERT itab = itab1. 
    ASSERT itab = itab2. 
    ASSERT itab = itab3. 
    out->write( itab 
      )->next_section( `demo1 CROSS JOIN demo2 WHERE ...` ). 
    SELECT FROM demo_join1 AS t1 
             CROSS JOIN demo_join2 AS t2 
           FIELDS t1~a AS a1, 
                  t1~b AS b1, 
                  t1~c AS c1, 
                  t1~d AS d1, 
                  t2~d AS d2, 
                  t2~e AS e2, 
                  t2~f AS f2, 
                  t2~g AS g2, 
                  t2~h AS h2 
           WHERE t2~d = t1~d 
           ORDER BY t1~d 
           INTO CORRESPONDING FIELDS OF TABLE @itab. 
    ASSERT itab = itabi. 
    out->write( itab ). 
  ENDMETHOD. 
  METHOD fill_tables. 
    out->begin_section( `Database Tables` ). 
    DELETE FROM demo_join1.                             "#EC CI_NOWHERE 
    INSERT demo_join1 FROM TABLE @( VALUE #( 
      ( a = 'a1' b = 'b1' c = 'c1'  d = 'uu' ) 
      ( a = 'a2' b = 'b2' c = 'c2'  d = 'uu' ) 
      ( a = 'a3' b = 'b3' c = 'c3'  d = 'vv' ) 
      ( a = 'a4' b = 'b4' c = 'c4'  d = 'ww' ) ) ). 
    SELECT * FROM demo_join1 INTO TABLE @FINAL(itab1). 
    DELETE FROM demo_join2.                             "#EC CI_NOWHERE 
    INSERT demo_join2 FROM TABLE @( VALUE #( 
      ( d = 'uu' e = 'e1' f = 'f1'  g = 'g1'  h = 'h1' ) 
      ( d = 'ww' e = 'e2' f = 'f2'  g = 'g2'  h = 'h2' ) 
      ( d = 'xx' e = 'e3' f = 'f3'  g = 'g3'  h = 'h3' ) ) ). 
    SELECT * FROM demo_join2 INTO TABLE @FINAL(itab2). 
    out->begin_section( `demo1` 
      )->write( itab1 
      )->next_section( `demo2` 
      )->write( itab2 
      )->end_section( 
      )->end_section( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Inner and outer joins between two tables `DEMO_JOIN1` and `DEMO_JOIN2`, for which the last column of `DEMO_JOIN1` matches the first column of `DEMO_JOIN2` in the join conditions.

- Both inner joins between the tables produce the same result set, regardless of how they are arranged on the left or the right. Three row combinations meet the join condition.

- The result sets of the two left joins depends on the arrangement of the tables on the left and right side. Apart from the three rows already produced by the inner join, an empty row (actually null values) is created on the right for each surplus row on the left. The fact that the empty row is displayed on the left in the final result is due to the structure of the internal table in the `INTO` clause. Here, the columns of `DEMO_JOIN1` are always read from the left and those of `DEMO_JOIN2` are always read from the right. If `*` was specified in the `SELECT` list, and `CORRESPONDING FIELDS` was not used in the `INTO` clause, the result would be arranged differently.

- The result sets of both right outer joins exactly correspond to the result sets of both previous left outer joins with the DDIC database tables specified in reverse order.

- The result sets of both cross joins without a `WHERE` condition are identical to the result sets of the corresponding inner and outer joins whose `ON` condition is always true. It makes no difference which side the data sources are specified on in the cross join. The number of rows is determined by `4 x 3 = 12`.

- The result set of the cross join with a `WHERE` condition is identical to the result set of an inner join with a corresponding `ON` condition. It should be noted that in a cross join, all rows are read first and then selected, whereas the inner join only reads the rows that meet the conditions.

See also the executable example [SQL Expressions, Coalesce Function](abensql_expr_coalesce_abexa.md), in which the default initial values set for the null values in the outer join are replaced by a different value.

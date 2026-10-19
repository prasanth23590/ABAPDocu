---
title: "SELECT, Intersection of Multiple Tables"
source_file: abenselect_intersect_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT > INTERSECT, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Intersection of Multiple Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an intersection is created across multiple tables.

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
CLASS cl_demo_select_intrsct DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_intrsct IMPLEMENTATION. 
  METHOD main. 
 
    SELECT a AS c1, b AS c2, c AS c3, d AS c4 
           FROM demo_join1 
    INTERSECT 
    SELECT d AS c1, e AS c2, f AS c3, g AS c4 
          FROM demo_join2 
    INTERSECT DISTINCT 
    SELECT i AS c1, j AS c2, k AS c3, l AS c4 
           FROM demo_join3 
           INTO TABLE @FINAL(result). 
    out->write( result ). 
 
    SELECT a AS c1, b AS c2, c AS c3, d AS c4 
           FROM demo_join1 
    INTERSECT 
    SELECT d AS c1, e AS c2, f AS c3, g AS c4 
          FROM demo_join2 
    UNION 
    SELECT i AS c1, j AS c2, k AS c3, l AS c4 
           FROM demo_join3 
           INTO TABLE @FINAL(result_with_union). 
    out->write( result_with_union ). 
 
    SELECT a AS c1, b AS c2, c AS c3, d AS c4 
           FROM demo_join1 
    INTERSECT 
    ( SELECT d AS c1, e AS c2, f AS c3, g AS c4 
            FROM demo_join2 
      UNION 
      SELECT i AS c1, j AS c2, k AS c3, l AS c4 
            FROM demo_join3 ) 
            INTO TABLE @FINAL(result_with_union2). 
    out->write( result_with_union2 ). 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_join1.                             "#EC CI_NOWHERE 
    DELETE FROM demo_join2.                             "#EC CI_NOWHERE 
    DELETE FROM demo_join3.                             "#EC CI_NOWHERE 
    INSERT demo_join1 FROM TABLE @( VALUE #( 
      ( a = 'a1' b = 'b1' c = 'c1' d = 'd1' ) 
      ( a = 'a2' b = 'b2' c = 'c2' d = 'd2' ) 
      ( a = 'a3' b = 'b3' c = 'c3' d = 'd3' ) ) ). 
    INSERT demo_join2 FROM TABLE @( VALUE #( 
      ( d = 'a1' e = 'b1' f = 'c1' g = 'd1' ) 
      ( d = 'a2' e = 'b2' f = 'c2' g = 'd2' ) 
      ( d = 'a3' e = 'b3' f = 'c3' g = 'd3' ) ) ). 
    INSERT demo_join3 FROM TABLE @( VALUE #( 
      ( i = 'a1' j = 'b1' k = 'c1' l = 'd1' ) 
      ( i = 'i1' j = 'j1' k = 'k1' l = 'l1' ) 
      ( i = 'i2' j = 'j2' k = 'k2' l = 'l2' ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Four columns of the same type from result sets from three database tables `DEMO_JOIN1`, `DEMO_JOIN2` and `DEMO_JOIN3` are combined to different `SELECT` statements using [`INTERSECT`](abapunion.md). The DDIC database tables are filled in the static constructor.

- The first statement shows the default behavior with addition `DISTINCT` in the second `INTERSECT` and without addition `DISTINCT` in the first `INTERSECT`. No rows are inserted from DDIC database table `DEMO_JOIN2` and no rows are inserted from DDIC database table `DEMO_JOIN3` because these rows either already exist or do not match the first result set. The non-matching rows between the first result set and `DEMO_JOIN3` are removed from `DEMO_JOIN1`.

- The second statement shows the behavior of `INTERSECT` together with `UNION`. `INTERSECT` inserts no rows from DDIC database table `DEMO_JOIN2` and `UNION` inserts two rows from DDIC database table `DEMO_JOIN3`. The result is the same as using only `UNION DISTINCT`.

- The third statement is the same as the second, except that parentheses have been inserted here. First, the parentheses are evaluated. `UNION` inserts two rows from DDIC database table `DEMO_JOIN3`. Afterwards, the result set of the parentheses is completely inserted into the result set of `DEMO_JOIN1` and removes the two rows that were inserted before.

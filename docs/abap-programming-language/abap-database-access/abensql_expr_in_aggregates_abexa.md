---
title: "sql_agg - Use in Aggregate Expressions"
source_file: abensql_expr_in_aggregates_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg > sql_agg - Examples of Aggregate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - Use in Aggregate Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [SQL expressions](abapsql_expr.md) as an argument of [aggregate functions](abapselect_aggregate.md).

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
CLASS cl_demo_sql_expr_in_aggregates DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_in_aggregates IMPLEMENTATION. 
  METHOD main. 
 
    SELECT char1, char2, num1, num2, num1 + num2 AS sum, 
                                     num1 * num2 AS product 
           FROM demo_expressions 
           ORDER BY char1, char2 
           INTO TABLE @FINAL(ungrouped). 
    out->write( ungrouped ). 
 
    SELECT char1 && '_' && char2 AS group, 
           MAX( num1 + num2 ) AS max, 
           MIN( num1 + num2 ) AS min, 
           MIN( num1 * num2 ) AS min_product, 
           MEDIAN( num1 * num2 ) AS median_product 
           FROM demo_expressions 
           GROUP BY char1, char2 
           ORDER BY group 
           INTO TABLE @FINAL(grouped). 
    out->write( grouped ). 
 
    SELECT char1 && '_' && char2 AS group, 
           MAX( num1 + num2 ) AS max, 
           MEDIAN( num1 + num2 ) AS median 
           FROM demo_expressions 
           GROUP BY char1, char2 
           HAVING MIN( num1 * num2 ) > 25 
           ORDER BY group 
           INTO TABLE @FINAL(grouped_having). 
    out->write( grouped_having ). 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    TYPES tab_type TYPE STANDARD TABLE OF 
                   demo_expressions WITH EMPTY KEY. 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( REDUCE tab_type( 
      LET r1 = cl_abap_random_int=>create( 
                 seed = CONV i( 
                  cl_demo_date_time=>get_user_time( ) ) 
                  min = 1 max = 10 ) 
          r2 = cl_abap_random_int=>create( 
                 seed = CONV i( r1->get_next( ) ) min = 0 max = 1 ) 
          c = `AB` IN 
      INIT t TYPE tab_type 
      FOR i = 0 THEN i + 1 UNTIL i > 25 
      NEXT t = VALUE #( 
                 BASE t ( id    = abcde+i(1) 
                          num1  = r1->get_next( ) 
                          num2  = r1->get_next( ) 
                          char1 = substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) && 
                                  substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) 
                          char2 = substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) && 
                                  substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) ) ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The DDIC database table `DEMO_EXPRESSIONS` is filled with random values in the static constructor.

- The first `SELECT` statement reads the filled columns individually. Here, the total and the product of the numeric columns `NUM1` and `NUM2` are calculated using [arithmetic statements](abensql_arith.md) in the `SELECT` list.

- The second `SELECT` statement performs a grouping by the columns `CHAR1` and `CHAR2`. For each group, aggregate functions are used to determine aggregated values whose arguments are [arithmetic expressions](abensql_arith.md)

- The third `SELECT` statement performs the same grouping as the second `SELECT` statement, but restricts the selected groups using a [`HAVING` clause](abaphaving_clause.md) in which a condition is set on an aggregate expression that has an [arithmetic expression](abensql_arith.md) as an argument.

See also the executable example for [using aggregate expressions in SQL expressions](abensql_expr_aggr_in_expr_abexa.md). Here, the roles of the expressions are switched, and different results are produced.

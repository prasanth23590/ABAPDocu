---
title: "sql_exp - Complex CASE"
source_file: abensql_expr_searched_case_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_case > sql_exp - sql_searched_case"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Complex CASE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates complex case distinctions in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_expr_searched_case DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_searched_case IMPLEMENTATION. 
  METHOD main. 
    CONSTANTS: both_l  TYPE c LENGTH 20 VALUE 'Both < 50', 
               both_gt TYPE c LENGTH 20 VALUE 'Both >= 50', 
               others  TYPE c LENGTH 20 VALUE 'Others'. 
 
    FINAL(rnd) = cl_abap_random_int=>create( 
      seed = CONV i( 
        cl_demo_date_time=>get_user_time( ) ) 
        min = 1 max = 100 ). 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      FOR i = 0 UNTIL i > 9 
      ( id = i 
        num1 = rnd->get_next( ) 
        num2 = rnd->get_next( ) ) ) ). 
 
    SELECT num1, num2, 
           CASE WHEN num1 <  50 AND num2 <  50 THEN @both_l 
                WHEN num1 >= 50 AND num2 >= 50 THEN @both_gt 
                ELSE @others 
           END AS group 
           FROM demo_expressions 
           ORDER BY group 
           INTO TABLE @FINAL(results). 
 
    out->write( results ). 
 
    LOOP AT results ASSIGNING FIELD-SYMBOL(<wa>) 
                    GROUP BY ( key = <wa>-group size = GROUP SIZE ) 
                    INTO FINAL(group). 
      out->write( group ). 
    ENDLOOP. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a list of columns specified after `SELECT`, [`CASE`](abensql_simple_case.md) is used to make a complex case distinction for the content of two columns. The result is a string taken from a [host variable](abenabap_sql_host_variables.md). Using the alias name defined after `AS`, the result is assigned to the identically named column in an internal table declared inline, `results`. [`GROUP BY`](../abap-processing-internal-data/abaploop_at_itab_group_by.md) is used to group this table by the results column.

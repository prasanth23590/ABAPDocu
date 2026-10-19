---
title: "sql_func - String Functions"
source_file: abensql_string_func_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - String Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - String Functions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [string functions](abensql_string_func.md) in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_function_string DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_function_string IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      ( id = 'X' 
        char1 = ' 0123' 
        char2 = 'aAaA' ) ) ). 
 
    SELECT SINGLE 
     char1 AS text1, 
     char2 AS text2, 
     concat(               char1,char2 )     AS concat, 
     concat_with_space(    char1,char2, 1 )  AS concat_with_space, 
     initcap(              char2 )           AS initcap, 
     instr(                char1,'12' )      AS instr, 
     left(                 char1,3 )         AS left, 
     length(               char1 )           AS length, 
     like_regexpr(         pcre = '\CA', 
                           value = char2 )   AS like_regex, 
     locate(               char2,'A',-1,2 )  AS locate, 
     locate_regexpr(       pcre = 'A(?=a)', 
                           value = char2 )   AS locate_regexpr, 
     locate_regexpr_after( pcre = 'A(?!a)', 
                           value = char2 )   AS locate_regexpr_after, 
     lower(                char2 )           AS lower, 
     lpad(                 char1,10,'x' )    AS lpad, 
     ltrim(                char1,' ' )       AS ltrim, 
     occurrences_regexpr(  pcre = '\CA', 
                           value = char2 )   AS occ_regex, 
     replace(              char1,'12','__' ) AS replace, 
     replace_regexpr(      pcre = '\CA', 
                           value = char2, 
                           with = 'bb' )     AS replace_regex, 
     right(                char1,3 )         AS right, 
     rpad(                 char1,10,'x' )    AS rpad, 
     rtrim(                char1,'3' )       AS rtrim, 
     substring(            char1,3,3 )       AS substring, 
     substring_regexpr(    pcre = 'A(a|b)', 
                           value = char2 )   AS substring_regexpr, 
     upper(                char2 )           AS upper 
     FROM demo_expressions 
     INTO @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Uses the string functions supported by ABAP SQL as elements of a `SELECT` list.

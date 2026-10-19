---
title: "sql_agg - Aggregate Function string_agg"
source_file: abensql_expr_string_agg_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg > sql_agg - Examples of Aggregate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - Aggregate Function string_agg

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [aggregate function](abensql_agg_func.md) `string_agg`.

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
CLASS cl_demo_str_agg DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_agg IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      ( id = '5' char1 = 'nowhere' ) 
      ( id = '3' char1 = 'this' ) 
      ( id = '1' char1 = 'everybody' ) 
      ( id = '4' char1 = 'is' ) 
      ( id = '2' char1 = 'knows' ) ) ). 
 
    SELECT STRING_AGG( char1,' ' ) 
           FROM demo_expressions 
           INTO TABLE @FINAL(unordered). 
    out->write( unordered ). 
 
    SELECT STRING_AGG( char1,' ' ORDER BY id ASCENDING ) 
           FROM demo_expressions 
           INTO TABLE @FINAL(ordered_ascending). 
    out->write( ordered_ascending ). 
 
    SELECT STRING_AGG( char1,' ' ORDER BY id DESCENDING ) 
           FROM demo_expressions 
           INTO TABLE @FINAL(ordered_descending). 
    out->write( ordered_descending ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Use of the [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md) [`STRING_AGG`](abensql_agg_func.md) as an [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) in the [`SELECT` list](abapselect_list.md) with different sorts.

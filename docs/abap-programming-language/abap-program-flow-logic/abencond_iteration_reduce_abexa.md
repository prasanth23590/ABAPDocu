---
title: "Creating Values with FOR and REDUCE"
source_file: abencond_iteration_reduce_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > FOR, Iteration Expressions > Examples of Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Values with FOR and REDUCE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [conditional iterations](abenfor_conditional.md) with the operator [`REDUCE`](abenconstructor_expression_reduce.md).

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
CLASS cl_demo_reduce_cond_iteration DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_cond_iteration IMPLEMENTATION. 
  METHOD main. 
    out->next_section( 'Summation' 
      )->write( REDUCE i( INIT sum = 0 
                          FOR n = 1 UNTIL n > 10 
                          NEXT sum = sum + n ) 
      )->next_section( 'Concatenation without THEN' 
      )->write( REDUCE string( INIT text = `Count up:` 
                               FOR n = 1 UNTIL n > 10 
                               NEXT text &&= | { n }| ) 
      )->next_section( 'Concatenation with THEN' 
      )->write( REDUCE string( INIT text = `Count down:` 
                               FOR n = 10 THEN n - 1 WHILE n > 0 
                               NEXT text &&= | { n }| ) 
      )->next_section( 'Non arithmetic expression' 
      )->write( REDUCE string( INIT text = `` 
                               FOR t = `x` THEN t && `y` 
                                           UNTIL strlen( t ) > 10 
                               NEXT text &&= |{ t } | ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the following simple iterations, which can be used to construct elementary data objects and directly display them in a constructor expression using the reduction operator [`REDUCE`](abenconstructor_expression_reduce.md):

- The first expression constructs a value of the type `i` for which the total of the iteration variable `n` is calculated. `n` is numeric, which means that `THEN` does not have to be specified. Each iteration step increases the value of `n` by 1.

- The second expression uses the same iteration as the first, but constructs a text string to which each iteration step appends the character representation of `n`.

- Like the second expression, the third expression constructs a text string, but uses the addition `THEN` explicitly to decrement the iteration variable instead of incrementing it.

- Finally, the fourth expression shows that the iteration variable does not have to be numeric. In this case, `THEN` must be specified explicitly with a suitable expression. Here, a text string is made longer until it has reached a specific size.

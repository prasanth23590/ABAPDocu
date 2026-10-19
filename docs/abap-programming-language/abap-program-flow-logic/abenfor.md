---
title: "FOR, Iteration Expressions"
source_file: abenfor.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR, Iteration Expressions

## Syntax

``` abap
... REDUCE|NEW|VALUE type( ... FOR ... UNTIL|WHILE ... 
                                 | ... IN ... ...) ...  
```

[`REDUCE`](abenconstructor_expression_reduce.md) · [`NEW`](../abap-creating-objects-and-values/abennew_constructor_params_itab.md) · [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) · [`... UNTIL|WHILE ...`](abenfor_conditional.md) · [`... IN ...`](../abap-processing-internal-data/abenfor_itab.md)

## Description

The language element `FOR` introduces an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) as a subexpression in [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) with the reduction operator [`REDUCE`](abenconstructor_expression_reduce.md) and in the variants of the instance operator [`NEW`](../abap-creating-objects-and-values/abennew_constructor_params_itab.md) and the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) for creating internal tables.

There are two main variants of iteration expressions:

- Iteration expressions with [`UNTIL`](abenfor_conditional.md) or [`WHILE`](abenfor_conditional.md) for conditional iterations. These expressions are used to iteratively create the results of any data types using `REDUCE` or to create lines of internal tables using `NEW` or `VALUE`. The iteration steps can be defined as required.

- Iteration expressions with [`IN`](../abap-processing-internal-data/abenfor_itab.md) for [table iterations](../../abap-glossary/abentable_iteration_glosry.md). These expressions are used for [table reductions](../../abap-glossary/abentable_reduction_glosry.md) using `REDUCE` or [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) using `NEW` or `VALUE`. The iteration steps here evaluate an existing internal table.

## Hints

- Any `FOR` variants can be used in any way in a constructor expression and produce nested iterations.

- The reduction operator [`REDUCE`](abenconstructor_expression_reduce.md) must contain at least one iteration expression. The variants of the instance operator [`NEW`](../abap-creating-objects-and-values/abennew_constructor_params_itab.md) and the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) for creating internal tables can contain iteration expressions.

- The conditional iterations using [`UNTIL`](abenfor_conditional.md) or [`WHILE`](abenfor_conditional.md) provide an expression-oriented alternative to the loop statements [`DO`](abapdo.md) and [`WHILE`](abapwhile.md). The same applies to the table iterations using [`IN`](../abap-processing-internal-data/abenfor_itab.md) and the statement [`LOOP`](../abap-processing-internal-data/abaploop_at_itab_variants.md). The direct use of operand positions on the expression-oriented variants helps to avoid helper variables. Furthermore, they also enable certain tasks, such as creating values iteratively, to be expressed more concisely and more elegantly.

- In [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md), local helper variables such as the helper variable `wa` in `... VALUE #( FOR wa IN itab ... ) ...` (or those defined in `LET` expressions), can only be used within the iteration expression itself. This includes additional subexpressions or constructing the result, as well as subsequent iteration expressions that use variables with the same name and type. Local helper variables cannot be used outside of iteration expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Two `FOR` loops are constructing an internal table `conn_tab` from an existing internal table `connections` using [grouping](../abap-processing-internal-data/abenfor_groups_of.md). The first [l`LET`](../abap-declarations/abaplet.md) expression is executed once per group of lines, the second [l`LET`](../abap-declarations/abaplet.md) expression is executed for each group member.

``` abap
SELECT s~carrname, p~carrid, p~connid, p~cityfrom, p~cityto 
       FROM scarr AS s 
         INNER JOIN spfli AS p ON s~carrid = p~carrid 
      ORDER BY p~carrid 
      INTO TABLE @FINAL(connections) 
      UP TO 100 ROWS. 
 
TYPES: 
  BEGIN OF conn, 
    carrier    TYPE string, 
    connection TYPE string, 
    cities     TYPE string, 
  END OF conn, 
  conn_tab TYPE TABLE OF conn WITH EMPTY KEY. 
 
FINAL(conn_tab) = VALUE conn_tab( 
   FOR GROUPS group OF flight IN connections 
     GROUP BY ( carrname = flight-carrname carrid  = flight-carrid ) 
     LET _carrier = group-carrname && ` (` && group-carrid && `)` IN 
     FOR member IN GROUP group 
     LET _cities = member-cityfrom && ` - ` && member-cityto IN 
     ( carrier     = _carrier 
       connection  = member-connid 
       cities      = _cities ) ). 
 
cl_demo_output=>display( conn_tab ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example illustrates that local helper variables declared in iteration expressions and their names cannot be used outside of the expressions.

``` abap
DATA it1 TYPE string_table. 
DATA it2 TYPE string_table. 
 
"Using the variable wa in a FOR loop. 
it2 = VALUE #( FOR wa IN it1 ( wa ) ). 
 
"It is not possible to specify an inline declaration and use 
"the name of a local variable already declared in an iteration 
"expression. 
*LOOP AT it1 INTO DATA(wa). 
*  APPEND wa TO it2. 
*ENDLOOP. 
 
"The local variable of the iteration expression cannot be used 
"outside iteration expressions. 
*LOOP AT it1 INTO wa. 
*  APPEND wa TO it2. 
*ENDLOOP. 
 
"Reusing local variables is possible in subsequent iteration 
"expressions, provided they share the same type. 
it2 = VALUE #( FOR wa IN it1 ( wa ) ). 
 
"The following iteration expression is not possible due to 
"type incompatibility. 
DATA it3 TYPE TABLE OF i WITH EMPTY KEY. 
*it3 = VALUE #( FOR wa IN it1 ( wa ) ).
```

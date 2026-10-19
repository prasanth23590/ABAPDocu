---
title: "rel_exp - Predicative Method Calls, Data Objects as Relational Expressions"
source_file: abenpredicative_method_calls.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicative Method Calls, Data Objects as Relational Expressions

## Syntax Forms

**Predicative Method Call**

``` abap
 ... meth( ... ) ...
```

**Data Objects as Relational Expressions**

``` abap
 ... dobj ...
```

### Alternative

[1. ` ... meth( ... ) ...`](abenpredicative_method_calls.md#alternative-1)

[2. ` ... dobj ...`](abenpredicative_method_calls.md#alternative-2)

## Overview

### Description

Both predicative method calls and individual data objects can represent relational expressions. These expressions may consist of either a functional method call or the data object itself, returning a truth value.

## Alternative 1

` ... meth( ... ) ...`

### Description

A predicative method call is a relational expression whose only operand is a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) `meth( ... )`. The result of the relational expression is true if the result of the functional method call is not initial and false if the result of the functional method call is initial. The data type of the result of the functional method call, that is, the return value of the called function method, is arbitrary. A check is made for the type-dependent initial value.

A predicative method call, like any relational expression, can be a full [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) or part of one. This means it can be specified as a condition in [control statements](../../abap-glossary/abencontrol_statement_glosry.md) and other statements, as an argument in [Boolean functions](../../abap-glossary/abenboole_function_glosry.md) or [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md), or in combinations with [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md).

### Hints

- A predicative method call is a short form of the predicate expression:

  [`... meth( ... ) IS NOT INITIAL ...`](abenlogexp_initial.md)

- [Predicate methods](../../abap-glossary/abenpredicate_method_glosry.md) whose return value has the type `abap_bool` are particularly suitable for predicative method calls. Calling a predicate method in a predicative method call simulates the call of a method whose return value has the real Boolean data type that does not exist in ABAP.

- As usual, the functional method call `meth( ... )` can be specified as an [individual method](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) or as a [method chaining](../abap-calling-and-exiting-program-units/abapcall_method_static_chain.md). If the first method called is an instance method, the functional method call can be introduced as usual using the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or the casting operator [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md).

- In addition to the dedicated [predicate functions](abenpredicate_functions.md), predicative method calls are the only way of creating a relational expression using a single operand.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Here the predicative method call `equals(...)` is equivalent to `num1 = num2`.

``` abap
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
    CLASS-METHODS equals 
      IMPORTING num1       TYPE i 
                num2       TYPE i 
      RETURNING VALUE(out) TYPE string. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD equals. 
    IF num1 = num2. 
      out = abap_true. 
    ELSE. 
      out = abap_false. 
    ENDIF. 
  ENDMETHOD. 
 
  METHOD main. 
    DATA: num1 TYPE i, 
          num2 TYPE i. 
    cl_demo_input=>add_field( CHANGING field = num1 ). 
    cl_demo_input=>add_field( CHANGING field = num2 ). 
    cl_demo_input=>request( ). 
 
    IF equals( num1 = num1 num2 = num2 ). 
      cl_demo_output=>display( num1 && ` equals ` && num2 ). 
    ELSE. 
      cl_demo_output=>display( num1 && ` does not equal ` && num2 ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Predicative Method Calls](abenpredicative_method_call_abexa.md)

## Alternative 2

` ... dobj ...`

### Description

An individual data object `dobj` can function as a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md). The expression evaluates to true if the operand's content is not initial. It evaluates to false if it is initial. The concrete type of the operand is arbitrary, as the type-specific initial value is checked.

Like any relational expression, an individual data object can serve as a complete [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) or as part of one. This allows it to function as a condition in [control statements](../../abap-glossary/abencontrol_statement_glosry.md), be used as an argument in [Boolean functions](../../abap-glossary/abenboole_function_glosry.md) or [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md), or be combined with [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifying only the data object is a short form of the predicate expression: [`... operand IS NOT INITIAL ...`](abenlogexp_initial.md)

``` abap
DATA(flag) = 'X'. 
DATA note TYPE string. 
 
IF flag. 
  note = `not initial`. 
ELSE. 
  note = `initial`. 
ENDIF. 
 
IF flag IS NOT INITIAL. 
  note = `not initial`. 
ELSE. 
  note = `initial`. 
ENDIF.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet demonstrates various statements using individual data objects functioning as relational expressions. This includes arguments in Boolean functions, combinations with Boolean operators, conditional expressions, and `WHERE` conditions in internal table processing statements.

``` abap
  "Elementary data objects 
  DATA num TYPE i VALUE 1. 
  DATA single_char TYPE c LENGTH 1 VALUE 'Z'. 
  DATA text TYPE string. 
 
  "Structure 
  DATA: BEGIN OF struct, 
          comp1 TYPE i VALUE 0, 
          comp2 TYPE c LENGTH 4 VALUE 'ABAP', 
        END OF struct. 
 
  "Internal table 
  DATA(string_table) = VALUE string_table( 
    ( `A` ) ( `` ) ( `` ) ( `B` ) ( `` ) ( `A` ) ( `P` ) ( `` ) ). 
 
  "Data reference variable 
  DATA(dref) = NEW i( 1 ). 
 
  "Various contexts 
  DATA(flag1) = xsdbool( num ). 
  ASSERT flag1. 
  ASSERT num. 
 
  DATA(flag2) = xsdbool( single_char ). 
  DATA(flag3) = xsdbool( text ). 
 
  IF flag2 OR flag3. 
    text = `either one or both are not initial`. 
  ELSE. 
    text = `both are initial`. 
  ENDIF. 
  CLEAR text. 
 
  DATA(flag4) = xsdbool( struct ). 
  DATA(flag5) = xsdbool( string_table ). 
  DATA(flag6) = xsdbool( dref ). 
  ASSERT: flag4, flag5, flag6. 
  ASSERT struct AND string_table AND dref. 
 
  CLEAR num. 
  DATA(flag7) = xsdbool( num ). 
  ASSERT NOT flag7. 
  ASSERT NOT num. 
 
  IF string_table[ 2 ]. 
    text = `not initial`. 
  ELSE. 
    text = `initial`. 
  ENDIF. 
  CLEAR text. 
 
  text = COND #( WHEN struct-comp1 THEN `not initial` ELSE `initial` ). 
  CLEAR text. 
 
  LOOP AT string_table INTO DATA(wa) WHERE table_line. 
    text &&= wa. 
  ENDLOOP. 
 
  CHECK text AND text = `ABAP`. 
 
  FIND `A` IN text. 
  IF NOT sy-subrc. 
    text = `found`. 
  ELSE. 
    text = `not found`. 
  ENDIF. 
 
  READ TABLE string_table INTO wa WHERE table_line. 
  ASSERT wa AND sy-tabix = 1. 
 
  DELETE string_table WHERE NOT table_line. 
 
  CLEAR text. 
  LOOP AT string_table INTO wa. 
    text &&= wa. 
  ENDLOOP. 
 
  ASSERT text AND text = `ABAP`.
```

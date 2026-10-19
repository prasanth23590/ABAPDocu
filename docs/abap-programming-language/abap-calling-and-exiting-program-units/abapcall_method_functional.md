---
title: "meth( ... ), Functional Method Call"
source_file: abapcall_method_functional.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# meth( ... ), Functional Method Call

## Syntax

``` abap
... { meth( )   
    | meth( a )   
    | meth( p1 = a1 p2 = a2 ... )   
    | meth( [EXPORTING p1 = a1 p2 = a2 ...]   
            [IMPORTING p1 =a1 p2 = a2 ...]   
            [CHANGING  p1 =a1 p2 = a2 ...] ) } ...  
```

[`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`EXPORTING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md) · [`IMPORTING p1 =a1 p2 = a2 ...`](abapcall_method_parameters.md) · [`CHANGING p1 =a1 p2 = a2 ...`](abapcall_method_parameters.md)

## Description

Functional call of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) [`meth`](abapcall_method_meth_ident_stat.md) in a suitable [read position for expressions](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md). The return value of the method declared using [`RETURNING`](../abap-declarations/abapmethods_functional.md) is used as an operand and its complete typing determines the data type of the operand. The actual parameters bound to [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md) and [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md) are handled in the same way as in [standalone method calls](abapcall_method_static_short.md).

The semantics of the syntax used in parameter passing are the same as in standalone method calls. Functional method calls differ from standalone method calls in the following ways:

- The return value in functional method calls cannot be assigned to an actual parameter explicitly using [`RECEIVING`](abapcall_method_parameters.md).

- [Inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) are not possible for actual parameters.

- Non-class-based exceptions cannot be handled using [`EXCEPTIONS`](abapcall_method_parameters.md).

If the return value of the method has a structured data type, a functional method call can, like a structure, be listed in front of the [structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md) `-` and used to access a component of the structure.

If a functional method has the same name as a [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md), the functional method is always called.

If an exception is raised when the functional method call is used as an operand, it cannot always be handled, but can cause a runtime error, depending on the position of the operand.

## System Fields

Each method call sets the system field `sy-subrc` to 0 in the moment the method is called.

## Hints

- In functional method calls, class-based exceptions that are propagated from the method can be handled as usual in a [`TRY`](../abap-program-flow-logic/abaptry.md) control structure or propagated further. The [non-class-based](../abap-program-flow-logic/abenexceptions_non_class.md) exceptions of a functional method, however, always produce a runtime error.

- The same applies to [resumable exceptions](../../abap-glossary/abenresumable_exception_glosry.md) in functional method calls as to all other methods. If processing can be resumed successfully, the execution of the statement called in the method is completed.

- [Method chaining](../../abap-glossary/abenmethod_chaining_glosry.md) is possible in the operand positions where functional methods can be specified.

- A functional method call whose first method is an instance method can be introduced using the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or the casting operator [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md).

- A single functional method call can be used as a [predicative method call](../../abap-glossary/abenpredicative_method_call_glosry.md) and as a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md).

- In functional calls of a functional method, an implicit temporary actual parameter is always assigned to the return value and this parameter is used as the operand of the current operand position. This means that the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`IS SUPPLIED`](../abap-program-flow-logic/abenlogexp_supplied.md) is always true for the return value within a functionally called method.

- Since functional method calls can be nested in any way, inline declarations for actual parameters could lead to confusing effects and are therefore not allowed.

- Since each successful method call sets the system field `sy-subrc` to 0, all statements with functional method calls can change the value of this field.

- When used as operands of [arithmetic expressions](../abap-processing-internal-data/abapcompute_arith.md), the results of functional calls of a functional methods are calculated before evaluating the arithmetic expression and their result is buffered for usage in the respective operand position. This might lead to unexpected results, especially if the method call has side-effects. See the example under [Arithmetic Expressions](../abap-processing-internal-data/abapcompute_arith.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Functional call of a method. Unlike in the example for [standalone method calls](abapcall_method_static_short.md), the return value is assigned to the result. The inline declarations made here, however, are not possible.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS do_something IMPORTING p1       TYPE i 
                                         p2       TYPE i 
                               EXPORTING p3       TYPE i 
                                         p4       TYPE i 
                               RETURNING VALUE(r) TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: a1 TYPE i, 
          a2 TYPE i. 
    FINAL(result) = 
      demo=>do_something( EXPORTING p1 = 333 
                                  p2 = 444 
                        IMPORTING p3 = a1 
                                  p4 = a2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [functional method](../../abap-glossary/abenfunctional_method_glosry.md) `factorial` in this example has the return value `fact` of type `int8`, used on the right side of an assignment in an expression.

``` abap
CLASS math DEFINITION. 
  PUBLIC SECTION. 
    METHODS factorial 
      IMPORTING n           TYPE i 
      RETURNING VALUE(fact) TYPE int8. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS math IMPLEMENTATION. 
  METHOD factorial. 
    fact = COND int8( WHEN n < 0 THEN 0 
                                 ELSE REDUCE int8( 
                                   INIT f = CONV int8( 1 ) 
                                   FOR  i = 1 UNTIL i > n 
                                   NEXT f *= i  ) ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(result) = 100 + NEW math( )->factorial( 4 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [functional method](../../abap-glossary/abenfunctional_method_glosry.md) `get` in this example has a structured return value whose component `carrname` is accessed.

``` abap
CLASS carriers DEFINITION. 
  PUBLIC SECTION. 
    METHODS get 
      IMPORTING carrid   TYPE scarr-carrid 
      RETURNING VALUE(r) TYPE scarr. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS carriers IMPLEMENTATION. 
  METHOD get. 
    SELECT SINGLE * 
           FROM scarr 
           WHERE carrid = @carrid 
           INTO @r. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write( NEW carriers( )->get( 'LH' )-carrname ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

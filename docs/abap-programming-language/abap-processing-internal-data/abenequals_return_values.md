---
title: "=, Assign Return Values and Results"
source_file: abenequals_return_values.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > =, Assignment Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, Assign Return Values and Results

## Syntax

``` abap
destination = meth( ) | func( ) | constr_expr | table_expr.  
```

[`meth( )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) · [`func( )`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) · [`constr_expr`](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) · [`table_expr`](abentable_expressions.md)

## Description

If one of the following calls or expressions is specified on the right side of the [assignment operator `=`](abenequals_operator.md), their return value or result is determined and assigned to the left side, `destination`. If necessary, type-dependent conversions are performed in accordance with the [conversion rules](abenconversion_rules.md). The following items are possible on the right side:

- A [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) [`meth( )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) including [method chainings](../abap-calling-and-exiting-program-units/abapcall_method_static_chain.md). The return value of a function method or an attribute addressed using a method chaining always has a complete type that must match the type of the left side.

- A [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) [`func( )`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md). The type of the return value, which can depend on the data type of the argument in some numeric functions, must match the type of the left side.

- A [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) [`constr_expr`](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md). The type of the result is determined by the `type` specified for the constructor expression and must match the type of the left side.

- A [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_expr`](abentable_expressions.md). The type of the result must match the type on the left side.

The following can be specified for `destination`:

- A [variable](../../abap-glossary/abenvariable_glosry.md) that is compatible with the return value or result, or in whose type the return value or result can be converted.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The data type of the declared variable `var` is the statically known type of the return value or result. If an [offset/length specification](../abap-operands/abenoffset_length.md) is applied to the result of a chaining where a constructor expression or a table expression is involved, the data type of the declared variable is the data type of the result in its full length and not in the length of the substring.

## Hint

If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified as an argument for one of the overloaded [numeric functions](abenmathematical_functions.md), the function itself works like an arithmetic expression and its assignment is one of the [assignments of arithmetic expressions](abenequals_arith_expr.md), which can cause a different order of conversions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of the return value of a method to an internal table declared inline.

``` abap
METHOD m1. 
  DATA(itab) = m2( ). 
  ... 
ENDMETHOD.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows different results when assigning offset/length specifications to inline declarations. The first offset/length specification is directly applied to a data object and the resulting data object has type `n` of length 2. The second offset/length specification is applied to the result of a constructor expression and the resulting data object has type `n` of length 8. The last output shows that the data type of the substring is used at runtime when passed to a method.

``` abap
TYPES text TYPE n LENGTH 8. 
DATA  text TYPE text VALUE '12345678'. 
 
FINAL(test1) = text+2(2). 
FINAL(test2) = CAST text( REF text( text ) )->*+2(2). 
 
cl_demo_output=>new( 
  )->write( test1 
  )->write( test2 
  )->write( CAST text( REF text( text ) )->*+2(2) 
  )->display( ).
```

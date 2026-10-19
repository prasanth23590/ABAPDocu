---
title: "Expressions as Actual Parameters"
source_file: abentyping_arith_expr.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > Checking Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Expressions as Actual Parameters

[Expressions](../abap-operands/abenoperands_expressions.md) can be specified as actual parameters in the following formal parameters:

- Write Positions

  - [Output parameters](../../abap-glossary/abenoutput_parameter_glosry.md), [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md), and [return values](../../abap-glossary/abenreturn_value_glosry.md) in [method calls](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md).

- Read Positions

  - [Input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of [methods](../../abap-glossary/abenmethod_glosry.md) in [method calls](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md), when [objects are created](../abap-creating-objects-and-values/abapcreate_object_parameters.md), or when exceptions are raised using [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) or [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional exception](../abap-program-flow-logic/abenconditional_expressions.md)

  - [Input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of [function modules](../../abap-glossary/abenfunction_module_glosry.md) for all variants of the statement [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md).

The parameters are evaluated from left to right (and from inside to outside) and the procedure is executed. A parameter cannot be affected by the method itself but by the evaluation of a preceding expression. This applies in particular to [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) in [result positions](../../abap-glossary/abenresult_position_glosry.md).

Special rules apply to typing checks, identifying the calculation type, and parameter passes.

- [Checking Typing](abentyping_arith_expr.md#checking-typing)

- [Calculation Type and Calculation Length](abentyping_arith_expr.md#calculation-type-and-calculation-length)

- [Passing Parameters](abentyping_arith_expr.md#passing-parameters)

  - [Complete Typing](abentyping_arith_expr.md#complete-typing)

  - [Generic Typing](abentyping_arith_expr.md#generic-typing)

## Hints

- In the case of [dynamic method calls](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md), the same rules apply as to static method calls. However, handling at runtime is time-consuming. Therefore, helper variables should be used in a dynamic call instead of expressions if possible. Function module calls are always dynamic and, compared to method calls, fewer rules apply.

## Checking Typing

- A [numeric function](../../abap-glossary/abenmathematical_funktion_glosry.md), a [description function](../../abap-glossary/abendescription_function_glosry.md), or an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) can

  - be bound to any numeric or any input parameter typed using the type `any` in a method call.

  - be bound to any appropriately typed input parameter in a function module call.

- A [bit function](../../abap-glossary/abenbit_function_glosry.md) or a [bit expression](../../abap-glossary/abenbit_expression_glosry.md) can

  - be bound to any byte-like or general typed input parameter in a method call.

  - be passed to input parameters of type `x` or a generic type including `x` in function module calls.

- A [character string function](../../abap-glossary/abencstring_function_glosry.md) or a [string expression](../../abap-glossary/abenstring_expression_glosry.md) can

  - be bound to any character-like or general typed input parameter in a method call.

  - be passed to input parameters of type `string` or a generic type including `string` in function module calls.

- A [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) can

  - be passed to every input parameter that matches the specified type [`type`](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) of the constructor expression in method calls. In this case, with the exception of conversion operator [`CONV`](../abap-processing-internal-data/abenconv_constructor_inference.md) in the constructor expression, the `#` character can only be specified for `type` if the input parameter is typed completely and this type is used.

  - be passed to every input parameter that matches the specified type [`type`](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) of the constructor expression in function module calls. The character `#` cannot be specified for `type` in the constructor expression since no static derivations of types are possible in function module calls.

- A [table expression](../../abap-glossary/abentable_expression_glosry.md) can

  - be passed in method or function calls to every input parameter that matches the type of the result.

### Hints

- In function module calls, the typing is not checked until runtime.

- No arithmetic expressions, description functions, or numeric functions can be passed to formal parameters with the generic type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). This restriction can be bypassed using the [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) on the actual parameter. This restriction does not apply to the generic type `any`.

## Calculation Type and Calculation Length

If calculation expressions are specified as actual parameters, the calculation type and calculation length are determined as follows:

- The [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of an arithmetic expression is determined

  - in method calls from the operands of the expression and the typing of the input parameter, if this parameter is completely typed. If the input parameter is typed generically, only the operands of the expression are evaluated.

  - in function module calls from the operands of the expression. The typing of the input parameter is ignored.

- The [calculation length](../../abap-glossary/abencalculation_length_glosry.md) of a bit expression is the length of the largest operand of the expression.

## Passing Parameters

When binding a function, a calculation expression, a constructor expression, or a table expression, the parameters are always [passed by value](../../abap-glossary/abenpass_by_value_glosry.md), even if the formal parameter is defined as to be [passed by reference](../../abap-glossary/abenpass_by_reference_glosry.md).

### Complete Typing

The return value of a function or the result of a calculation expression, a constructor expression, or a table expression is [converted](../abap-processing-internal-data/abenconversion_rules.md), if necessary, to the type of the input parameter and passed.

### Generic Typing

- In a function, a constructor expression, or a table expression, the formal parameter inherits the type of the return value or result. Only bit functions are handled like bit expressions (see below).

- With an arithmetic expression, the formal parameter inherits the calculation type determined by the operand. If the calculation type is `p`, the length is always 16. The number of decimal places is determined by the accuracy required for the calculation and therefore depends on the values of the operands.

- In a bit expression or a bit function, the formal parameter is set to type `x` in the calculation length determined by the operands.

- In a string expression, the formal parameter is set to the type `string` for completely generic typing or the generic types `csquence` `clike`. In the case of the types `c` and `n` with generic length, the length is set to the length of the result of the string expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The functional method `m1` is called twice for each assignment to `result`. The first call is executed in an arithmetic expression, which is passed as an actual parameter in the second call. In the first call of each assignment, the formal parameter `p1` has type `p` of length 16. The number of decimal places is 0 in the first assignment, 14 in the second, and 1 in the third assignment. In the second call, the formal parameter `p1` has the type `decfloat34` in each assignment, because the calculation type of the arithmetic expression is determined by the return value of `m1`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS m1 IMPORTING p1         TYPE numeric 
                     RETURNING VALUE(ret) TYPE decfloat34. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    ret = p1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA num1   TYPE p DECIMALS 2 VALUE '2.00'. 
    DATA num2   TYPE p DECIMALS 2 VALUE '1.00'. 
    DATA result TYPE decfloat34. 
 
    result = c1=>m1( sqrt( 4 ) +  c1=>m1( num1 / 2 )  ). 
    result = c1=>m1( sqrt( 4 ) +  c1=>m1( num1 / 3 )  ). 
    result = c1=>m1( sqrt( 4 ) +  c1=>m1( num2 / 2 )  ). 
  ENDMETHOD. 
ENDCLASS.
```

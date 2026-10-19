---
title: "Arithmetic Expressions (arith_exp)"
source_file: abapcompute_arith.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Arithmetic Expressions (arith_exp)

## Syntax

``` abap
... [+|-] operand1 
    [{+|-|*|/|DIV|MOD|**} [+|-] operand2 
    [{+|-|*|/|DIV|MOD|**} [+|-] operand3 
    ... ]] ...  
```

[`+|-|*|/|DIV|MOD|**`](abenarith_operators.md) · [`+|-|*|/|DIV|MOD|**`](abenarith_operators.md)

## Description

An arithmetic expression expresses a calculation. The result of an arithmetic expression is a numeric value that exists in the [calculation type](abenarith_type.md) that is assigned to the arithmetic expression. In an arithmetic expression `arith_exp`, the [arithmetic operators](abenarith_operators.md) `+`, `-`, `*`, `/`, `DIV`, `MOD`, or `**` can be used to combine an operand `operand1` with one or more operands `operand2`, `operand3` ... [Brackets](abenarith_brackets.md) are also possible. The calculation is based on [calculation rules](abenarith_type.md) that depend on the respective calculation type.

Arithmetic expressions can occur in the read positions of [certain statements](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md), in particular on the right side of an [assignment](abenequals_arith_expr.md) with the [assignment operator `=`](abenequals_operator.md). When used as the operand of the lossless operator `EXACT`, an arithmetic expression can be checked for a [lossless calculation](abenlossless_calculation.md).

The operand positions `operand` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), that is, numeric data objects, [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md), [functional methods](../abap-declarations/abapmethods_functional.md), or compound arithmetic expressions can be specified. The arithmetic operators `+`, `-`, `*`, `/`, `DIV`, `MOD`, and `**` combine two adjacent operands. When the expression is evaluated, a numeric value is calculated and combined with the next adjacent operand. The priority of this combination depends on the [operators](abenarith_operators.md) used.

Each operand can be preceded by the signs `+` or `-`, in any order and separated by one or more blanks. The effect of a plus/minus sign is the same as specifying the expression `+1 *` or `-1 *` in its place, which means that a sign has the same priority as a multiplication.

If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) or [character-like expressions](../../abap-glossary/abencharlike_expression_glosry.md) are specified as operands, they are executed from left to right and from inside to outside before the remainder of the expression is evaluated. The return values are buffered for use in the corresponding operand positions. Here, [character-like processing functions](abenprocess_functions.md) and [string expressions](abapcompute_string.md) are only possible as arguments for [description functions](abendescriptive_functions.md).

## Hints

- It should be ensured that the value of a data object that is also used as an operand is changed in a specified functional method. Even if such an operand is to the left of the functional method, its value will always be changed by the method before it is evaluated.

- Arithmetic expressions, [string expressions](../../abap-glossary/abenstring_expression_glosry.md), and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md) cannot be combined. To built-in functions that are used as operands for arithmetic expressions can, however, string expressions or bit expressions be passed as arguments.

- If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified as an argument for one of the overloaded [numeric functions](abenmathematical_functions.md), the entire function works like an arithmetic expression.

- A simple arithmetic expression `+|- literal`, which is comprised of an operator `+|-`, a blank, and an unsigned [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md) `literal`, has the same value as the corresponding numeric literal `+|-literal` prefixed directly with a plus/minus sign. However, since the expression is handled like an expression and always evaluated at runtime, the numeric literal should always be used in these cases for performance reasons.

- The above rule specifying how [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) or [character-like expressions](../../abap-glossary/abencharlike_expression_glosry.md) are evaluated might lead to unexpected results.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program section calculates the hyperbolic sine with the Eulerian formula in the explicit calculation type `decfloat34` and with the [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) `sinh` in the implicit calculation type `f` and displays the difference.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    x       TYPE string, 
    result1 TYPE string, 
    result2 TYPE string, 
    diff    TYPE string, 
  END OF  line. 
DATA 
  output TYPE TABLE OF line WITH EMPTY KEY. 
 
DO 2001 TIMES. 
  TRY. 
      FINAL(x) = sy-index - 1001. 
      FINAL(result1) = CONV decfloat34( 
                             ( exp( x ) - exp( -1 * x ) ) / 2 ). 
      FINAL(result2) =  sinh( x ). 
      FINAL(diff)    =  abs( result1 - result2 ). 
      IF diff <> 0. 
        APPEND VALUE #( 
          x       = |{ x }| 
          result1 = |{ result1 STYLE = SCIENTIFIC }| 
          result2 = |{ result2 STYLE = SCIENTIFIC }| 
          diff    = |{ diff    STYLE = SCIENTIFIC }| ) TO output. 
      ENDIF. 
    CATCH cx_sy_conversion_overflow cx_sy_arithmetic_overflow. 
  ENDTRY. 
ENDDO. 
out->write( output ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program demonstrates the rule specifying how [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are evaluated in arithmetic expressions. The first calculation sets the variable `changing` to 6 and returns the expected result of 9. The result of the second calculation is 15 and not 10 as might be expected. The functional method is called first and its result 9 is added to the changed value 6 of variable `changing` and not to its initial value 1.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth 
      IMPORTING i_par        TYPE i 
      CHANGING  c_par        TYPE i OPTIONAL 
      RETURNING VALUE(r_par) TYPE i. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    c_par = i_par + c_par. 
    r_par = i_par + 4. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA changing TYPE  i. 
    changing = 1. 
    FINAL(result1) = demo=>meth( EXPORTING i_par = 5 
                                 CHANGING  c_par = changing ). 
    out->write( |changing: { changing }\n| & 
                           |result1:  { result1 }| ). 
    changing = 1. 
    FINAL(result2) = changing + demo=>meth( EXPORTING i_par = 5 
                                           CHANGING  c_par = changing ). 
    out->write( |changing: { changing }\n| & 
                           |result2:  { result2 }| ). 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ARG_OUT_OF_DOMAIN`

- *Cause:* Illegal argument in powers

  *Runtime error:* `COMPUTE_POW_DOMAIN`

`CX_SY_ARITHMETIC_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (type `p`)

  *Runtime error:* `BCD_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (all operands type `p`)

  *Runtime error:* `COMPUTE_BCD_OVERFLOW`

- *Cause:* Overflow in `cosh`

  *Runtime error:* `COMPUTE_COSH_OVERFLOW`

- *Cause:* Overflow or underflow in `exp`

  *Runtime error:* `COMPUTE_EXP_RANGE`

- *Cause:* Overflow in addition (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_ADD_OVERFLOW`

- *Cause:* Overflow in subtraction (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_SUB_OVERFLOW`

- *Cause:* Overflow in multiplication (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_MUL_OVERFLOW`

- *Cause:* Overflow in division (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_DIV_OVERFLOW`

- *Cause:* Overflow in division (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_DIV_OVERFLOW`

- *Cause:* Overflow in division (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_DIV_OVERFLOW`

- *Cause:* Overflow in subtraction (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_MINUS_OVERFLOW`

- *Cause:* Overflow in addition (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_PLUS_OVERFLOW`

- *Cause:* Overflow in multiplication (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_TIMES_OVERFLOW`

- *Cause:* Overflow in \|-2147483648\|

  *Runtime error:* `COMPUTE_INT_ABS_OVERFLOW`

- *Cause:* Integer overflow in division

  *Runtime error:* `COMPUTE_INT_DIV_OVERFLOW`

- *Cause:* Integer overflow after subtraction

  *Runtime error:* `COMPUTE_INT_MINUS_OVERFLOW`

- *Cause:* Integer overflow while adding

  *Runtime error:* `COMPUTE_INT_PLUS_OVERFLOW`

- *Cause:* Integer overflow in multiplication

  *Runtime error:* `COMPUTE_INT_TIMES_OVERFLOW`

- *Cause:* Invalid call of `log10`

  *Runtime error:* `COMPUTE_LOG10_ERROR`

- *Cause:* Invalid call of `log`

  *Runtime error:* `COMPUTE_LOG_ERROR`

- *Cause:* Overflow or underflow in powers

  *Runtime error:* `COMPUTE_POW_RANGE`

- *Cause:* Overflow in `sinh`

  *Runtime error:* `COMPUTE_SINH_OVERFLOW`

- *Cause:* Overflow in function `round` or `rescale`

  *Runtime error:* `COMPUTE_ROUND_RESCALE_OVERFLOW`

`CX_SY_CONVERSION_NO_NUMBER`

- *Cause:* Operand cannot be interpreted as a number

  *Runtime error:* `CONVT_NO_NUMBER`

`CX_SY_CONVERSION_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (type `p`, with specified length)

  *Runtime error:* `BCD_FIELD_OVERFLOW`

- *Cause:* Operand too big or (interim) result too big

  *Runtime error:* `CONVT_OVERFLOW`

`CX_SY_PRECISION_LOSS`

- *Cause:* Result of `cos` not exact

  *Runtime error:* `COMPUTE_COS_LOSS`

- *Cause:* Result of `sin` not exact

  *Runtime error:* `COMPUTE_SIN_LOSS`

- *Cause:* Result of `tan` not exact

  *Runtime error:* `COMPUTE_TAN_LOSS`

`CX_SY_UNSUPPORTED_FUNCTION`

- *Cause:* Invalid function for calculation type `decfloat34`

  *Runtime error:* `COMPUTE_UNSUPPORTED_DECF_FUNC`

`CX_SY_ZERODIVIDE`

- *Cause:* Division by 0 (type `p`)

  *Runtime error:* `BCD_ZERODIVIDE`

- *Cause:* Division by 0 (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_ZERODIVIDE`

- *Cause:* Division by 0 (types (`b`, `s`), `i`, `int8`)

  *Runtime error:* `COMPUTE_INT_ZERODIVIDE`

- *Cause:* Division by 0 (type `decfloat`)

  *Runtime error:* `COMPUTE_DECFLOAT_ZERODIVIDE`

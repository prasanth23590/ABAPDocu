---
title: "arith_exp - Arithmetic Operators"
source_file: abenarith_operators.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - Arithmetic Operators

The table shows the possible arithmetic operators for [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md), their priority, and the order in which the calculation is performed. Within a [parenthesis level](abenarith_brackets.md), calculations with operators of higher priority are performed before calculations with operators of lower priority. For adjacent operators of the same priority, the calculation is performed in the order specified. In the third column of the table below, 3 indicates the highest priority and 1 the lowest.

The calculation is performed according to the [calculation rule](abenarith_type.md) for the current [calculation type](abenarith_type.md). With the exception of `**`, the operators have no effect on the calculation type. If the operator `**` does not occur in an arithmetic expression, the calculation type is determined only by the data types involved. If `**` is used, the calculation type is either `decfloat34` or `f`. It is `decfloat34` if one of the operands involved is a [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) and `f` in all other cases.

| **Operator** | **Calculation**                                                                                                                                           | **Priority** | **Order**          |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------|
| `+`          | Addition of the operands                                                                                                                                  | 1            | From left to right |
| `-`          | Subtraction of the right operand from the left                                                                                                            | 1            | From left to right |
| `*`          | Multiplication of the operands                                                                                                                            | 2            | From left to right |
| `/`          | Division of the left operand by the right                                                                                                                 | 2            | From left to right |
| `DIV`        | Integer part of the division of the left operand by the right, with positive remainder                                                                    | 2            | From left to right |
| `MOD`        | Positive remainder of the division of the left operand by the right; a remainder other than zero is always between zero and the size of the right operand | 2            | From left to right |
| `**`         | Left operand raised to the power of the right                                                                                                             | 3            | From right to left |

Division by the value 0 is undefined and raises a catchable exception. The only situation where division by 0 does not raise an exception is if the dividend is also 0. Here, the result is set to 0.

## Hints

- Setting the result to 0 in a division by the value 0, where the dividend is 0 can be seen as an internal exception handling that sets the result to a predefined value in that case.

- In ABAP, the result of a division for the [calculation types](abenarith_type.md) `i`, `int8`, `p`, and `decfloat34` is rounded commercially, whereas in most other programming languages any surplus decimal places are cut off.

- The result of `DIV` multiplied by `operand2` plus the result of `MOD` always produces `operand1`. Therefore, the rule that the result of `MOD` is always positive also affects the result of `DIV`. The result of an integer division of two positive numbers with a remainder that is not equal to zero differs from the result of an integer division of two negative numbers with the same amounts. Likewise, for operands with different plus/minus signs, it is important which operand is positive and which is negative.

- If, when raising to a power, the left operand is 0, the right operand must be greater than or equal to 0. If the left operand is negative, the right operand must be an integer. Otherwise, both cases raise a catchable exception.

- To prevent the operator `**` from producing the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `f`, the built-in function [`ipow`](abenpower_function.md) can be used for integer exponents for which the calculation type is determined by the argument.

- The ABAP operators `DIV` and `MOD` behave differently with respect to the signs than the SQL operators [`DIV`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) and [`MOD`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the functions of the three division operators, `DIV`, `MOD`, and `/`. The results are `4.7273`, `4.0000`, and `0.8000`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: pack TYPE p DECIMALS 4, 
      n    TYPE decfloat34 VALUE '+5.2', 
      m    TYPE decfloat34 VALUE '+1.1'. 
 
pack = n / m. 
out->write( |{ n } / { m } = { pack }| ). 
 
pack = n DIV m. 
out->write( |{ n } DIV { m } = { pack }| ). 
 
pack = n MOD m. 
out->write( |{ n } MOD { m } = { pack }| ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following table shows the results of integer divisions and their remainders. See also the example for the SQL operators [`DIV`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md) and [`MOD`](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions_numeric.md).

\|`operand1`\|`operand2`\|`DIV`\|`MOD`\|

\|7\|3\|2\|1\| \|-7\|3\|-3\|2\| \|7\|-3\|-2\|1\| \|-7\|-3\|3\|2\|

## Executable Example

[Arithmetic Calculations](abendivisions_abexa.md)

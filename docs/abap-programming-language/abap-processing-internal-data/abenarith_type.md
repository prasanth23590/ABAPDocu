---
title: "arith_exp - Calculation Type and Calculation Rules"
source_file: abenarith_type.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - Calculation Type and Calculation Rules

An arithmetic expression is assigned a calculation type that defines the calculation rules for the arithmetic expression. The calculation type is determined at program runtime from the data types involved that can be identified. The calculation type only needs to be determined statically if the target field is an [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md), where generically type operands are included using a [standard type](../../abap-glossary/abenstandard_type_glosry.md).

- [Determining the Calculation Type](abenarith_type.md#determining-the-calculation-type)

- [Calculation Rules for Calculation Type](abenarith_type.md#calculation-rules-for-calculation-type)

- [Handling the Result](abenarith_type.md#handling-the-result)

## Determining the Calculation Type

The calculation type corresponds to one of the numeric data types `i`, `int8`, `p`, `f`, or `decfloat34`. It is determined by the following hierarchy, and in the order of decreasing priority:

1.  If one of the data types involved is `decfloat16` or `decfloat34`, the calculation type is `decfloat34`.

2.  If one of the data types involved is `f` or if the operator `**` is used, the calculation type is `f`.

3.  If one of the data types involved is `p`, the calculation type is `p`.

4.  If one of the data types involved is `int8`, the calculation type is `int8`.

5.  If one of the data types involved is `i`, (`b` or `s`), the calculation type is `i`.

The data type that has the largest [value range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) therefore determines the calculation type with the exception that each [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) produces the calculation type `decfloat34`, and that use of the operator `**` is handled like a data type of type `f`.

Involved data types include:

- The right side of an [assignment](abenequals_arith_expr.md) in arithmetic expressions:

  - If it is not an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), the data types of all operands of the entire arithmetic expressions, and the data type of the result field `result`.

  - If `result` is an inline declaration, the calculation type derived from the data types of the arithmetic expression determines the data type of the declared variable. Here, a calculation type `p` always produces the data type `p` with length 8 and no decimal places.

- as the operand of a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) in an arithmetic expression, the data types of all operands of the entire relational expression. The calculation type of each arithmetic expression involved is not created first and the [comparison type](../../abap-glossary/abencomparison_type_glosry.md) then derived. All operands of the relational expression are part of the calculation type, which is also the comparison type, regardless of the arithmetic expressions they belong to.

- in an arithmetic expression after the statement [`CASE`](../abap-program-flow-logic/abapcase.md), the operands of the arithmetic expression, ignoring the operands specified after `WHEN`.

- as [actual parameters](../abap-declarations/abentyping_arith_expr.md) for [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of [methods](../../abap-glossary/abenmethod_glosry.md) in an arithmetic expression, the data types of all operands of the entire arithmetic expression and the [typing](../../abap-glossary/abentyping_glosry.md) of the formal parameter, provided that it is completely typed. If the formal parameter is typed generically, then only the operands of the expression are evaluated.

- as [actual parameters](../abap-declarations/abentyping_arith_expr.md) for [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of [function modules](../../abap-glossary/abenfunction_module_glosry.md), the data types of all operands of the entire arithmetic expression. The typing of the formal parameter is ignored.

- as an argument of a built-in function in an arithmetic expression, the data types of all operands of the entire arithmetic expression and the type of the input parameter, if it is fully determined. An overloaded [numeric function](abenmathematical_functions.md) where an arithmetic expression is used as an argument, on the other hand, acts like an arithmetic operator and is handled in its position like an arithmetic expression.

- as an [embedded expression](../../abap-glossary/abenembedded_expression_glosry.md) in a [string template](../../abap-glossary/abenstring_template_glosry.md) in an arithmetic expression, only the operands of the expression are evaluated.

- as an argument in a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) in an arithmetic expression, the calculation type is determined as in an [assignment](abenequals_arith_expr.md). The left side of the assignment is either the result of the constructor expression with the type [`type`](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) specified in front of the parentheses or a structure component.

For operands with complete numeric data types, this data type is used. Operands with other data types are handled as follows:

- `d` and `t` as `i`

- `c`, `n`, and `string` as `p`

- `x` and `xstring` as `i`

- `utclong` is not allowed

In the case of operands that are not specified as data objects, the type is determined as follows:

- In the case of operands that are specified as non-overloaded [integrated functions](../../abap-glossary/abenbuiltin_function_glosry.md), the data type of the return value applies.

- Operands of overloaded [general numeric functions](abennumerical_functions.md), and of the overloaded power function [`ipow`](abenpower_function.md), are used to determine the calculation type.

- When a [floating point function](abenfloating_point_functions.md) is used, the calculation type is either `decfloat34` or `f`.

- In the case of operands specified as [functional method calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md), the data type of the return value applies.

- In the case of operands specified as [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md), the data type specified by `type` here applies. The arithmetic expression itself, however, does not determine the type of the constructor expression. If constructor expressions are used as operands of arithmetic expressions, the `#` character can only be specified for the data type of the constructor expression if the type can be determined from the constructor expression itself.

- In the case of operands specified as [table expressions](../../abap-glossary/abentable_expression_glosry.md), the data type of the result applies.

- If operands are specified as generically typed field symbols or formal parameters and an existing variable is used as the target field of an [assignment](abenequals_arith_expr.md), these operands contribute to the calculation type assigned to them at runtime with their data type.

- If operands are specified as generically typed field symbols or formal parameters and an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) is used as the target field of an [assignment](abenequals_arith_expr.md), the generic types are part of the statically known calculation type, from which the data type of the declaration is determined as follows:

  - `any`, `data`, `simple`, `numeric`, and `decfloat` as `decfloat34`

  - `csequence`, `clike`, `c`, and `n`, as `p`. If there is no involved type with a higher priority, type `p` with length 8 and without decimal places is used for the declaration.

  - `xsequence` and `x` as `i`

    The calculation type determined at runtime from all operands including the target field always matches the data type of the variable declared inline, because this is always the data type with the greatest value range.

### Hints

- The determination of a calculation type before the calculation is performed and while respecting all operands including the result field (as the right side of an [assignment](abenequals_arith_expr.md) or as an actual parameter in the case of an arithmetic expression) is a special ABAP feature that differs considerably from how other programming languages perform calculations. To avoid unnecessary conversions, all operands and a result field should have the same numeric data type.

- In the case of arithmetic expressions as operands of [relational expressions](../../abap-glossary/abenrelational_expression_glosry.md) in [logical expressions](../../abap-glossary/abenlogical_expression_glosry.md) combined using [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md), the rule above only applies to the relational expression in question. The calculation type is not determined while skipping the Boolean operators `AND`, `OR`, or `EQUIV`.

- If the calculation type is `f`, it should be ensured that the precision is only approximately 15 places and integers are only represented accurately up to an absolute value of 2\*\*53, that is, 9,007,199,254,740,992. Other interim results are rounded. This is especially important when using the operator `**`, which can produce the calculation type `f` if no decimal floating point number is involved.

- To avoid that the operator `**` produces the calculation type `f`, the built-in function [`ipow`](abenpower_function.md) can be used for integer exponents, for which the calculation type is determined by the argument.

- The time stamp type `utclong` cannot be converted implicitly to a numeric type, and therefore cannot be specified directly as an operand of an arithmetic expression.

- The conversion operator [`CONV`](abenconstructor_expression_conv.md) can be used to convert parts of arithmetic expressions to other types and hence modify the calculation type.

- A calculation type `p` in [assignments](abenequals_arith_expr.md) to an inline declaration can produce the data type `p` with length 8 and no decimal places, which can produce unexpected results and raise exceptions. It is best to either avoid inline declarations when using the calculation type `p` or to determine the data type by applying the conversion operator [`CONV`](abenconstructor_expression_conv.md) to the arithmetic expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The calculation type of the following arithmetic expression is `f`. Accordingly, a data object of the type `f` is declared in the inline declaration.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(result) = 2 ** 10. 
 
FINAL(t) = cl_abap_typedescr=>describe_by_data( result )->type_kind. 
out->write( |{ result } of type { t }| ). 
 
out->display( ).
```

## Calculation Rules for Calculation Type

Before the calculation is performed, all operands for which it is necessary are converted to the calculation type, in accordance with the [conversion rules for elementary data types](abenconversion_elementary.md).

The calculation type determines the calculation method and the calculation precision:

- **Calculation types** `i` and `int8`

  The arithmetic expression is calculated using integer arithmetic, in which each interim result that is not an integer (after a division) is rounded commercially to the nearest integer. Each interim result must be in the [value range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) of the data type `i` or `int8`, otherwise the catchable exception `CX_SY_ARITHMETIC_OVERFLOW` is raised.

- **Calculation type** `p`

  Fixed point arithmetic. The arithmetic expression is calculated with an internal precision of 31 [places](../../abap-glossary/abenplace_glosry.md) and a special decimal floating point arithmetic for interim results. During the calculation, the decimal point for numbers of type `p` is not fixed. If an overflow occurs because an interim result is greater than 10<sup>31 - 1, the whole expression is recalculated to an internal precision of 63 places, or a maximum value of 10</sup>63 -1 for interim results. If another overflow occurs, the catchable exception `CX_SY_ARITHMETIC_OVERFLOW` is raised. An overflow always occurs if the level of precision is not sufficient for all integral digits before the decimal separator. Surplus [decimal places](../../abap-glossary/abendecimal_place_glosry.md) do not raise an exception but are rounded commercially to the nearest whole number for each interim result.

- **Calculation type** `f`

  The arithmetic expression is calculated using the binary floating point arithmetic of the current platform. Each interim result must be in [value range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) of the data type `f`, otherwise the catchable exception `CX_SY_ARITHMETIC_OVERFLOW` is raised. Since the decimal places of a floating point number are represented internally using a dual fraction, there is not an exact equivalent for every number that can be represented in the decimal system, which can produce rounding errors in the interim results.

- **Calculation type** `decfloat34`

  The arithmetic expression is calculated with decimal floating point arithmetic according to norm IEEE-754-2008, where division by 0 does not raise an exception if the dividend is 0 as for all calculation types. Each interim result must be in [value range](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) of the data type `decfloat34`, otherwise the catchable exception `CX_SY_ARITHMETIC_OVERFLOW` is raised. Interim results are rounded commercially to the nearest whole number. The [scaling](../../abap-glossary/abenscale_glosry.md) of each interim result is defined so that the smallest possible exponent is selected if the result is not precise, and the following procedure is used to determine the scaling if the result is precise:

  - For addition and subtraction, the exponent of the result is the smaller of the exponents of the two operands.

  - For multiplication, the exponent of the result is the sum of the exponents of the two operands.

  - For division, the exponent of the result is the difference between the exponents of the dividend and of the divisor.

  - If the `sqrt` function is used, the exponent is the integer part of half of the exponent of the operand.

### Hint

Commercial rounding of interim results in the calculation types `i`, `int8`, `p`, and `decfloat34` is a characteristic that distinguishes ABAP greatly from other programming languages where the decimal places are usually cut off rather than rounded. This can produce different results, in particular in divisions with the calculation types `i`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the second arithmetic expression is 0. The calculation type is `i` and the interim results of each division are rounded to 0. The result of the second arithmetic expression is `0.9999999999999999999999999999999999`. The calculation type `decfloat34` and the interim results `0.3333333333333333333333333333333333` are not rounded. The outer conversion operator [`CONV`](abenconstructor_expression_conv.md) creates the integer 1 from this data.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(result1) =  1 / 3 + 1 / 3 + 1 / 3. 
FINAL(result2) =  CONV i( CONV decfloat34( 1 / 3 + 1 / 3 + 1 / 3 ) ). 
 
out->write( |{ result1 }, { result2 }| ). 
 
out->display( ).
```

## Handling the Result

After the calculation is performed, the result of the arithmetic expression is handled as follows:

- In the case of an arithmetic expression as the right side of an [assignment](abenequals_arith_expr.md) to an existing data object, the result is converted to the data type of the result field if the calculation type is different.

- With an arithmetic expression on the right side of an [assignment](abenequals_arith_expr.md) to an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), the statically known calculation type of variable `var`, whereby generically typed field symbols and formal parameters are included with the [standard type](../../abap-glossary/abenstandard_type_glosry.md) described above. In the case of the calculation type `p`, the data type of the declared variable is always `p` with the length 8 without decimal places.

- In the case of an arithmetic expression as an operand of a relational expression, no conversion takes place, since the calculation type and the comparison type are identical.

- In the case of an arithmetic expression as an actual parameter for input values of methods, and if the formal parameter is completely typed, the result is converted into the formal parameter type in the static method call and passed. If the formal parameter is generically typed, it inherits the calculation type, where in the case of calculation type `p`, the number of decimal places is determined based on the precision required in the calculation.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation type `f` of the following arithmetic expression is [converted](abenconversion_type_f.md) to `string`, whereby the value is formatted in [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md). After the assignment, the text string contains the character string `1.0240000000000000E+03`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA result TYPE string. 
 
result = 2 ** 10. 
out->write( result ). 
 
out->display( ).
```

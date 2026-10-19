---
title: "REDUCE, Reduction Operator"
source_file: abenconstructor_expression_reduce.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REDUCE, Reduction Operator

## Syntax

``` abap
... REDUCE type( 
      [let_exp] 
      INIT {x1 = rhs1}|{<x1> = wrexpr1}|{x1|<x1> TYPE dtype1} 
           {x2 = rhs2}|{<x2> = wrexpr2}|{x2|<x2> TYPE dtype2} 
           ... 
      FOR for_exp1 
      FOR for_exp2 
      ... 
      NEXT ... 
           {x1 =|+=|-=|*=|/=|&&= rhs1}|{<x1> =|+=|-=|*=|/=|&&= wrexpr1} 
           {x2 =|+=|-=|*=|/=|&&= rhs2}|{<x2> =|+=|-=|*=|/=|&&= wrexpr2} 
           ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md) · [`FOR for_exp1`](abenfor.md) · [`FOR for_exp2`](abenfor.md)

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the reduction operator `REDUCE` creates a result of a data type specified using `type` from one or more [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md). The following can be specified for `type`:

- A non-generic data type `dtype`.

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md).

  - If the data type required in an operand position is unique and known completely, this type is used.

  - If the operand type is not known completely, the type of the first declaration after `INIT`, which is always known, is used, except when the constructor expression is passed to an actual parameter with a generically typed formal parameter.

  - If the constructor expression is passed to an actual parameter with a generically typed formal parameter, the operand type is derived in accordance with [special rules](abenreduce_constructor_inference.md).

The operands of the constructor expression must be specified as follows:

- First, an optional [`LET` expression](../abap-declarations/abaplet.md) can be specified for defining local helper fields whose value can be used within the expression but can no longer be changed there.

- Then, an addition `INIT` must be specified followed by any number of declarations. The declarations after `INIT` create local variables `x1`, `x2`, ... or field symbols `<x1>`, `<x2>`, ... to which the same applies with respect to namespace and visibility as to the helper fields declared in a [`LET` expression](../abap-declarations/abaplet.md). The syntax of the declaration is either:

  - the same as in a [`LET` expression](../abap-declarations/abaplet.md) and it follows the rules that apply here.

  - initial variables or field symbols of the specified data type `dtype` can be created using `TYPE`.

    At least one variable or field symbol must be specified. The variables or field symbols declared after `INIT` can only be used after `NEXT`. In particular, they cannot be used to declare other variables or field symbols.

  - The first variable `x1` or the first field symbol `<x1>` determines the result of the expression and the data type must be convertible to the result type `type`.

  - All other variables or field symbols declared after `INIT` are optional additional helper fields that can be on the left side of assignments after `NEXT`, unlike those declared after `LET`.

- Then, at least one [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) must be specified using [`FOR`](abenfor.md) but it is also possible to specify multiple expressions.

  - If [conditional iterations](abenfor_conditional.md) are used, the result is created in custom iteration steps.

  - If [table iterations](../abap-processing-internal-data/abenfor_itab.md) are used, the lines of existing internal tables are evaluated. This is referred to as a [table reduction](../../abap-glossary/abentable_reduction_glosry.md), since any values are constructed from the lines of existing internal tables.

- Then, assignments must be specified after `NEXT` that are executed for every iteration of the last `FOR` expression. For the assignments, either the [assignment operator](../../abap-glossary/abenassignment_operator_glosry.md) `=` or the [calculation assignment operators](../../abap-glossary/abencalc_assignment_op_glosry.md) `+=`, `-=`, `*=`, `/=`, or `&&=` can be specified and the assignment is carried out accordingly. A value or memory area must be assigned to all variables and field symbols declared after `INIT`. In the case of structured variables or field symbols, an assignment to one of their components is sufficient.

  - The assignment on the right side `rhs` to variables `x` takes place in accordance with the rules of a regular assignment using the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md) or a [calculation assignment operator `+=`, `+=`, `*=`, `/=`](../abap-processing-internal-data/abencalculation_assignments.md) or [`&&=`](../abap-processing-internal-data/abencalculation_assignment_string.md), which means that any of the possible calls and expressions can be specified for `rhs`.

  - Only the result of a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) `wrexp` can be assigned to a field symbol. The same applies here as to assignments of writable expressions using [`ASSIGN`](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md), which means that only the expressions listed there can be specified.

    The assignments can be listed in any order and they are evaluated from to left to right. Each non-structured variable or field symbol declared after `INIT` can be specified exactly once as the left side. In the case of structured variables or field symbols, either the entire structure or each component once can be specified as the left side. In addition to the data objects of the program, all local variables and field symbols of the expression visible after the last `FOR` expression can be used in the operand positions on the right side:

  - All variables and field symbols declared after `LET`.

  - All variables and field symbols declared after `INIT`.

  - The `wa1`, `wa2`, ... or `<fs1>`, `<fs2>`, .... filled by the `FOR` expressions. This enables the content of the lines of the internal tables to be accessed and the result constructed.

    All helper fields declared after `INIT` can only be specified in read positions on the right side.

After the full evaluation, the content of the first variable `x1` or the memory area pointed to by the first field symbol `<x1>` is assigned to the temporary result of the expression of type `type` in accordance with the [assignment rules](../abap-processing-internal-data/abenconversion_rules.md).

## Hints

- The name of the operator `REDUCE` is explained as follows:

  - [Conditional iterations](abenfor_conditional.md) are generally used to reduce sets of data objects to a single data object.

  - [Table iterations](../abap-processing-internal-data/abenfor_itab.md) for [table reductions](../../abap-glossary/abentable_reduction_glosry.md) are generally used to reduce the content of the internal tables in question to a summary value. Any result type is possible and does not have to be less complex than the involved internal tables, but this should only be used in exceptional cases. When constructing tables from tables, it is best to use [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) instead.

- When a local field symbol `<xi>` is used on the left side of assignments after `NEXT`, it should be noted that the assignments are not made to the value referenced by the field symbol like in `INIT` and `LET`. Instead, the field symbol is set in the same way as in the statement [`ASSIGN`](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md).

- Unlike in [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) with the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md), an assignment of a `REDUCE` expression to a structure or an internal table does not overwrite them completely before the `FOR` expressions are processed and can be used directly anywhere in the entire expression.

- If a variable is declared in the first position after `INIT` and the `VALUE` operator is specified with the character `#` on the right side, the result type `type` of the `REDUCE` expression is used for this character if possible.

- Table reductions are also possible with [`FOR` expressions](../abap-processing-internal-data/abenmesh_for.md) for [mesh paths](../../abap-glossary/abenmesh_path_glosry.md).

- In [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md), local helper variables such as the helper variable `wa` in `... VALUE #( FOR wa IN itab ... ) ...` (or those defined in `LET` expressions), can only be used within the iteration expression itself. This includes additional subexpressions or constructing the result, as well as subsequent iteration expressions that use variables with the same name and type. Local helper variables cannot be used outside of iteration expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation of the total of the numbers from 1 to 10 via `REDUCE`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->write( 
  REDUCE i( INIT s = 0 
            FOR  i = 1 UNTIL i > 10 
            NEXT s += i ) ). 
 
out->display( ).
```

## Executable Examples

- [Creating Values with `FOR` and `REDUCE`](abencond_iteration_reduce_abexa.md)

- [Examples of Table Reductions](../abap-processing-internal-data/abentable_reductions_abexas.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example illustrates that local helper variables declared in iteration expressions and their names cannot be used outside of iteration expressions.

``` abap
DATA(sum1) = REDUCE i( INIT a = 0 
                       FOR  b = 1 UNTIL b > 10 
                       NEXT a += b ). 
 
"It is not possible to use the local variables or their names 
"for new variables outside iteration expressions. 
*DATA(addition1) = 1 + a. 
*DATA(addition2) = 1 + b. 
*DATA(a) = 1 + 1. 
*DATA(b) = 2 + 2. 
 
"Reusing local variables is possible in subsequent iteration 
"expressions, provided they share the same type. 
DATA(sum2) = REDUCE i( INIT b = 0 
                       FOR  a = 1 UNTIL a > 20 
                       NEXT b += a ). 
 
"If the local variables do not have the same type, the reuse 
"is not possible. 
*DATA(counter) = REDUCE string( LET c = 10 IN 
*                               INIT a = `` 
*                               FOR b = c THEN b - 1 WHILE b > 0 
*                               NEXT a &&= |{ b } | ).
```

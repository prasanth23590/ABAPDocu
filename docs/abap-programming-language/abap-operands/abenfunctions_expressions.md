---
title: "Expressions for Operand Positions"
source_file: abenfunctions_expressions.html
section: "ABAP Programming Language > ABAP - Operands > Expressions in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Expressions for Operand Positions

- [Write Positions](abenfunctions_expressions.md#write-positions)

- [Read Positions](abenfunctions_expressions.md#read-positions)

## Write Positions

The following expressions can be specified in [write positions](../../abap-glossary/abenwrite_position_glosry.md):

- [Declaration expressions](../../abap-glossary/abendeclaration_expression_glosry.md)

  - ... [`DATA(...)`](../abap-declarations/abendata_inline.md) ...

  - ... [`FINAL(...)`](../abap-declarations/abenfinal_inline.md) ...

  - ... [`FIELD-SYMBOL(...)`](../abap-declarations/abenfield-symbol_inline.md) ...

- [Writable expressions](../../abap-glossary/abenwritable_expression_glosry.md)

  - The [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) [`NEW class( ... )->attr`](../abap-creating-objects-and-values/abennew_constructor_params_class.md) and [`CAST type( ... )->dobj`](../abap-processing-internal-data/abenconstructor_expression_cast.md)

  - [Table expressions](../../abap-glossary/abentable_expression_glosry.md) [`itab[ ... ]`](../abap-processing-internal-data/abentable_expressions.md) and their [chainings](../abap-processing-internal-data/abentable_exp_chaining.md)

## Read Positions

Functions that can be specified in a read position include the following:

- [Built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md)

  ... [`func( arg )`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) ...

  ... [`... func( val = arg p1 = arg1 p2 = arg2 ... )`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) ...

- [Functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md)

  ... [`meth( )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) ...

  ... [`meth( a )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) ...

  ... [`meth( p1 = a1 p2 = a2 ... )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) ...

  ... [`meth( [EXPORTING p1 = a1 p2 = a2 ...]`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) [`[IMPORTING p1 = a1 p2 = a2 ...]`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) [`[CHANGING p1 = a1 p2 = a2 ...] )`](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) ...

- [Method chaining](../../abap-glossary/abenmethod_chaining_glosry.md)

  - Chained method call:

    ... [`...->meth1( ... )->meth2( ... )->...->meth( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_static_chain.md) ...

  - Chained attribute access:

    ... [`...->meth1( ... )->meth2( ... )->...->attr`](../abap-calling-and-exiting-program-units/abapcall_method_static_chain.md) ...

The following expressions can be specified in read positions:

- [Calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md):

  - [Arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md)

    ... [`arith_exp`](../abap-processing-internal-data/abapcompute_arith.md) ...

  - [Bit expressions](../../abap-glossary/abenarithmetic_expression_glosry.md)

    ... [`bit_exp`](../abap-processing-internal-data/abapcompute_bit.md) ...

  - [String Expressions](../../abap-glossary/abenstring_expression_glosry.md)

    ... [`string_exp`](../abap-processing-internal-data/abapcompute_string.md) ...

- [Constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md):

  - [Instance operator](../../abap-glossary/abeninstance_operator_glosry.md)

    [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md)

  - [Value operator](../../abap-glossary/abenvalue_operator_glosry.md)

    [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md)

  - [Conversion operator](../../abap-glossary/abenconversion_operator_glosry.md)

    [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md)

  - [Component operator](../../abap-glossary/abencorresponding_operator_glosry.md) [`CORRESPONDING`](../abap-processing-internal-data/abenconstructor_expr_corresponding.md)

  - [Casting operator](../../abap-glossary/abeninstance_operator_glosry.md)

    [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md)

  - [Reference operator](../../abap-glossary/abenreference_operator_glosry.md)

    [`REF`](../abap-processing-internal-data/abenconstructor_expression_ref.md)

  - [Lossless operator](../../abap-glossary/abenlossless_operator_glosry.md)

    [`EXACT`](../abap-processing-internal-data/abenconstructor_expression_exact.md)

  - [Reduction operator](../../abap-glossary/abenreduce_operator_glosry.md)

    [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md)

  - [Filter operator](../../abap-glossary/abenfilter_operator_glosry.md)

    [`FILTER`](../abap-processing-internal-data/abenconstructor_expression_filter.md)

  - [Conditional operator](../../abap-glossary/abenconditional_operator_glosry.md)

    [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md), [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md)

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md) [`itab[ ... ]`](../abap-processing-internal-data/abentable_expressions.md) and their [chainings](../abap-processing-internal-data/abentable_exp_chaining.md)

### Hints

- Functions with numeric return values and arithmetic expressions are summarized as [numeric expressions](../../abap-glossary/abennumerical_expression_glosry.md).

- Functions with character-like return values and string expressions are summarized as [character-like expressions](../../abap-glossary/abencharlike_expression_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Numeric expression used for specification of a table index for an internal table.

``` abap
DATA: itab TYPE STANDARD TABLE OF i, 
      n    TYPE i. 
 
... 
 
READ TABLE itab INDEX lines( itab ) - n 
                INTO  FINAL(wa).
```

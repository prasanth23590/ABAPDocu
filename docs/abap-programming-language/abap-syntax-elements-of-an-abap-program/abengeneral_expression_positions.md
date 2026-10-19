---
title: "General Expression Positions"
source_file: abengeneral_expression_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Read Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# General Expression Positions

General expression positions are [read positions](../../abap-glossary/abenread_position_glosry.md) where appropriate [data objects](../../abap-glossary/abendata_object_glosry.md), [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), [table expressions](../../abap-glossary/abentable_expression_glosry.md), [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md), [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md), or [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) can be specified. The following general expression positions are available:

- Right side of an assignment with the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md)

- Operands of [arithmetic expressions](../abap-processing-internal-data/abapcompute_arith.md) and [bit expressions](../abap-processing-internal-data/abapcompute_bit.md)

- [Embedded expressions](../abap-processing-internal-data/abenstring_templates_expressions.md) in [string templates](../abap-processing-internal-data/abenstring_templates.md)

- Operands of [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md) in [logical expressions](../abap-program-flow-logic/abenlogexp.md)

- Operand of the statement [`CASE`](../abap-program-flow-logic/abapcase.md)

- [Actual parameters](../abap-declarations/abentyping_arith_expr.md) for input parameters of methods in [`meth( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md), [`RAISE EVENT`](../abap-calling-and-exiting-program-units/abapraise_event.md), [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md), and [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) or [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../abap-program-flow-logic/abenconditional_expressions.md)

- [Actual parameters](../abap-declarations/abentyping_arith_expr.md) for input parameters of function modules in the case of [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md)

- Arguments of [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) [numeric functions](../abap-processing-internal-data/abenmathematical_functions.md) if these are specified in an arithmetic expression

- Reference variable `oref` of the statement [`RAISE EXCEPTION oref.`](../abap-program-flow-logic/abapraise_exception_class.md)

- The operands after the addition `WITH TABLE KEY` of the statements [`READ TABLE itab`](../abap-processing-internal-data/abapread_table.md) and [`DELETE TABLE itab`](../abap-processing-internal-data/abapdelete_itab_line.md)

- The operands after the addition [`WITH KEY`](../abap-processing-internal-data/abapread_table_free.md) of the statement [`READ TABLE itab`](../abap-processing-internal-data/abapread_table.md)

- Work area `wa` of the following statements:

  - [`APPEND wa TO ...`](../abap-processing-internal-data/abapappend_linespec.md)

  - [`INSERT wa INTO ...`](../abap-processing-internal-data/abapinsert_itab_linespec.md)

  - [`MODIFY ... FROM wa ...`](../abap-processing-internal-data/abapmodify_itab_single.md)

- Expression `exp` for dynamic sorting at:

  - [`SORT itab BY exp`](../abap-processing-internal-data/abapsort_itab.md)

- Source fields of the statements `WRITE` and `WRITE TO`, with the restriction that [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md) cannot be specified directly but can only be specified as content of [embedded expressions](../../abap-glossary/abenembedded_expression_glosry.md) in [string templates](../../abap-glossary/abenstring_template_glosry.md)

The type restrictions determined by the [operand type](abenoperand_type.md) apply in the operand positions. For example, no [numeric functions](../../abap-glossary/abenmathematical_funktion_glosry.md) can be specified in a bit expression.

## Hints

- By specifying [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) as actual parameters of methods, it is possible to nest method calls in an operand position.

- The three types of [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) can be listed as operands of relational expressions, but they cannot be combined in one calculation expression.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of a constructor expressions with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) on the right side of an assignment and of a constructor expression with the reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) as an input parameter for the method `DISPLAY` of the class `CL_DEMO_OUTPUT`.

``` abap
TYPES itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( ( 1 ) ( 2 ) ( 3 ) ). 
 
cl_demo_output=>display( 
  REDUCE string( INIT s = `` 
                 FOR <wa> IN itab 
                 NEXT s &&= <wa> && ` ` ) ).
```
